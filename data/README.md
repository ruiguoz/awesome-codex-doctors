# Data

`github-snapshot.json` is the reviewed source for the generated catalog and growth chart.

`catalog.json` is a machine-readable export generated from `github-snapshot.json`.

Manual fields:

- `scope`
- `specialty`
- `skill_or_plugin`
- `state_change_risk`
- `dry_run_support`
- `backup_support`
- `evidence_count`

GitHub snapshot fields:

- repository URL and description
- creation and last-push timestamps
- stars, forks, language, license, and archived state

Run:

```bash
python scripts/discover.py
python scripts/render.py
python scripts/render.py --check
```

`discover.py` creates candidate data for manual review; only reviewed records should be copied into `github-snapshot.json`.
