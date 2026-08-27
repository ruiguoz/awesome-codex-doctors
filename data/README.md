# Data

`github-snapshot.json` is the reviewed source for the generated catalog and growth chart.

Manual fields:

- `scope`
- `specialty`
- `skill_or_plugin`

GitHub snapshot fields:

- repository URL and description
- creation and last-push timestamps
- stars, forks, language, license, and archived state

Run `python scripts/render.py` after updating the snapshot.

