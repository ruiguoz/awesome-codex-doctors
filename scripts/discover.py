#!/usr/bin/env python3
"""Discover candidate repositories from GitHub Search API for manual catalog review."""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT_PATH = ROOT / "data" / "github-snapshot.json"
DEFAULT_OUTPUT = ROOT / "data" / "discovery-candidates.json"
API_BASE = "https://api.github.com/search/repositories"


def fetch_page(*, query: str, per_page: int, page: int, token: str | None) -> dict:
    params = urlencode({"q": query, "sort": "updated", "order": "desc", "per_page": per_page, "page": page})
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "awesome-codex-doctors-discover"}
    if token:
        headers["Authorization"] = "Bearer " + token
    request = Request(f"{API_BASE}?{params}", headers=headers)
    with urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def normalize_repo(item: dict) -> dict:
    license_info = item.get("license") or {}
    return {
        "full_name": item["full_name"],
        "url": item["html_url"],
        "description": item.get("description") or "",
        "created_at": item["created_at"],
        "pushed_at": item["pushed_at"],
        "stars": item.get("stargazers_count", 0),
        "forks": item.get("forks_count", 0),
        "language": item.get("language"),
        "license": license_info.get("spdx_id") if isinstance(license_info, dict) else None,
        "archived": bool(item.get("archived", False)),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", default="codex-doctor in:name")
    parser.add_argument("--per-page", type=int, default=50)
    parser.add_argument("--max-pages", type=int, default=2)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--token", default=os.getenv("GITHUB_TOKEN"))
    args = parser.parse_args()

    snapshot = json.loads(SNAPSHOT_PATH.read_text(encoding="utf-8"))
    existing = {project["full_name"]: project for project in snapshot["projects"]}

    discovered: list[dict] = []
    seen: set[str] = set()
    total_count = None
    for page in range(1, args.max_pages + 1):
        payload = fetch_page(query=args.query, per_page=args.per_page, page=page, token=args.token)
        if total_count is None:
            total_count = payload.get("total_count", 0)
        items = payload.get("items", [])
        if not items:
            break
        for item in items:
            full_name = item["full_name"]
            if full_name in seen:
                continue
            seen.add(full_name)
            candidate = normalize_repo(item)
            reviewed = existing.get(full_name)
            if reviewed:
                candidate["status"] = "already-reviewed"
                candidate["reviewed_fields"] = {
                    "scope": reviewed["scope"],
                    "specialty": reviewed["specialty"],
                    "skill_or_plugin": reviewed["skill_or_plugin"],
                    "state_change_risk": reviewed["state_change_risk"],
                    "dry_run_support": reviewed["dry_run_support"],
                    "backup_support": reviewed["backup_support"],
                    "evidence_count": reviewed["evidence_count"],
                }
            else:
                candidate["status"] = "new-candidate"
                candidate["reviewed_fields"] = {
                    "scope": "unverified",
                    "specialty": "unknown",
                    "skill_or_plugin": False,
                    "state_change_risk": "unknown",
                    "dry_run_support": "unknown",
                    "backup_support": "unknown",
                    "evidence_count": 1,
                }
            discovered.append(candidate)

    output = {
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "source": {
            "provider": "GitHub Search API",
            "query": args.query,
            "total_name_hits": total_count,
            "pages_requested": args.max_pages,
            "per_page": args.per_page,
            "review_note": "Candidates require manual verification before inclusion in data/github-snapshot.json.",
        },
        "counts": {
            "discovered": len(discovered),
            "already_reviewed": sum(item["status"] == "already-reviewed" for item in discovered),
            "new_candidates": sum(item["status"] == "new-candidate" for item in discovered),
        },
        "candidates": discovered,
    }

    args.output.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {args.output.relative_to(ROOT)}")
    print(
        f"discovered {output['counts']['discovered']} repositories "
        f"({output['counts']['already_reviewed']} reviewed, {output['counts']['new_candidates']} new)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
