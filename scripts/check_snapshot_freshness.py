#!/usr/bin/env python3
"""Warn when the catalog snapshot is stale."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT_PATH = ROOT / "data" / "github-snapshot.json"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-age-days", type=int, default=30)
    args = parser.parse_args()

    snapshot = json.loads(SNAPSHOT_PATH.read_text(encoding="utf-8"))
    generated_at = datetime.strptime(snapshot["generated_at"], "%Y-%m-%d").replace(tzinfo=timezone.utc)
    age_days = (datetime.now(timezone.utc) - generated_at).days
    if age_days > args.max_age_days:
        print(
            "::warning title=Snapshot freshness::"
            f"data/github-snapshot.json is {age_days} days old (>{args.max_age_days}). "
            "Consider running scripts/discover.py and refreshing reviewed entries."
        )
    else:
        print(f"snapshot age is {age_days} days (threshold {args.max_age_days})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
