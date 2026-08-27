#!/usr/bin/env python3
"""Validate the reviewed catalog and its generated files."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse


SCOPES = {"core", "adjacent", "unverified"}
RISK_LEVELS = {"read-only", "repair", "cleanup", "unknown"}
CONFIDENCE_LEVELS = {"yes", "no", "unknown"}
PROJECT_FIELDS = {
    "full_name",
    "url",
    "description",
    "scope",
    "specialty",
    "skill_or_plugin",
    "state_change_risk",
    "dry_run_support",
    "backup_support",
    "evidence_count",
    "created_at",
    "pushed_at",
    "stars",
    "forks",
    "language",
    "license",
    "archived",
}


def parse_timestamp(value: object, field: str, full_name: str, errors: list[str]) -> None:
    if not isinstance(value, str):
        errors.append(f"{full_name}: {field} must be a string")
        return
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        errors.append(f"{full_name}: invalid {field}: {value!r}")


def audit(repo: Path, *, data_override: dict | None = None) -> list[str]:
    errors: list[str] = []
    data_path = repo / "data" / "github-snapshot.json"
    render_path = repo / "scripts" / "render.py"
    if data_override is None:
        if not data_path.is_file():
            return [f"missing {data_path}"]
        if not render_path.is_file():
            return [f"missing {render_path}"]
        try:
            data = json.loads(data_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            return [f"cannot read snapshot: {exc}"]
    else:
        data = data_override

    try:
        datetime.strptime(data["generated_at"], "%Y-%m-%d")
    except (KeyError, TypeError, ValueError):
        errors.append("generated_at must be YYYY-MM-DD")

    projects = data.get("projects")
    if not isinstance(projects, list):
        return errors + ["projects must be a list"]

    names: list[str] = []
    urls: list[str] = []
    derived = Counter()
    last_created = ""
    for index, project in enumerate(projects):
        label = f"projects[{index}]"
        if not isinstance(project, dict):
            errors.append(f"{label}: must be an object")
            continue
        missing = PROJECT_FIELDS - set(project)
        if missing:
            errors.append(f"{label}: missing fields: {', '.join(sorted(missing))}")
        full_name = project.get("full_name")
        if not isinstance(full_name, str) or full_name.count("/") != 1:
            errors.append(f"{label}: invalid full_name")
            full_name = label
        else:
            names.append(full_name.lower())
        url = project.get("url")
        expected_url = f"https://github.com/{full_name}"
        if url != expected_url:
            errors.append(f"{full_name}: url must be {expected_url}")
        if isinstance(url, str):
            urls.append(url.lower().rstrip("/"))
            parsed = urlparse(url)
            if parsed.scheme != "https" or parsed.netloc.lower() != "github.com":
                errors.append(f"{full_name}: URL must use https://github.com")
        scope = project.get("scope")
        if scope not in SCOPES:
            errors.append(f"{full_name}: invalid scope {scope!r}")
        else:
            derived[scope] += 1
        specialty = project.get("specialty")
        if not isinstance(specialty, str) or not specialty or specialty.lower() != specialty or " " in specialty:
            errors.append(f"{full_name}: specialty must be lowercase and hyphenated")
        skill = project.get("skill_or_plugin")
        if not isinstance(skill, bool):
            errors.append(f"{full_name}: skill_or_plugin must be boolean")
        elif skill:
            derived["skill_or_plugin"] += 1
        risk_level = project.get("state_change_risk")
        if risk_level not in RISK_LEVELS:
            errors.append(f"{full_name}: state_change_risk must be one of {sorted(RISK_LEVELS)}")
        for field in ("dry_run_support", "backup_support"):
            value = project.get(field)
            if value not in CONFIDENCE_LEVELS:
                errors.append(f"{full_name}: {field} must be one of {sorted(CONFIDENCE_LEVELS)}")
        evidence_count = project.get("evidence_count")
        if not isinstance(evidence_count, int) or isinstance(evidence_count, bool) or evidence_count < 1:
            errors.append(f"{full_name}: evidence_count must be a positive integer")
        for field in ("stars", "forks"):
            value = project.get(field)
            if not isinstance(value, int) or isinstance(value, bool) or value < 0:
                errors.append(f"{full_name}: {field} must be a non-negative integer")
        for field in ("created_at", "pushed_at"):
            parse_timestamp(project.get(field), field, full_name, errors)
        created_at = project.get("created_at")
        if isinstance(created_at, str):
            if last_created and created_at < last_created:
                errors.append("projects must be ordered chronologically by created_at")
            last_created = created_at

    for kind, values in (("full_name", names), ("url", urls)):
        duplicates = [value for value, count in Counter(values).items() if count > 1]
        if duplicates:
            errors.append(f"duplicate {kind}: {', '.join(sorted(duplicates))}")

    counts = data.get("counts", {})
    for key in ("core", "adjacent", "unverified", "skill_or_plugin"):
        if counts.get(key) != derived[key]:
            errors.append(f"counts.{key} is {counts.get(key)!r}; expected {derived[key]}")

    if not errors and data_override is None:
        result = subprocess.run(
            [sys.executable, str(render_path), "--check"],
            cwd=repo,
            text=True,
            capture_output=True,
            check=False,
        )
        if result.returncode:
            detail = (result.stderr or result.stdout).strip()
            errors.append(f"generated files are stale: {detail}")
    return errors


def main() -> int:
    default_repo = Path(__file__).resolve().parents[3]
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", nargs="?", type=Path, default=default_repo)
    args = parser.parse_args()
    repo = args.repo.resolve()
    errors = audit(repo)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    data = json.loads((repo / "data" / "github-snapshot.json").read_text(encoding="utf-8"))
    print(
        f"Catalog audit passed: {len(data['projects'])} projects, "
        f"{data['counts']['skill_or_plugin']} skills/plugins."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
