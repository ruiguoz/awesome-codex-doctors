# Catalog schema

`data/github-snapshot.json` contains snapshot metadata plus manual review fields.

## Top level

- `generated_at`: snapshot date in `YYYY-MM-DD`.
- `source`: discovery provider, query, raw hit count, and review note.
- `counts`: derived totals for `core`, `adjacent`, `unverified`, and `skill_or_plugin`.
- `projects`: reviewed project records.

## Project fields

- `full_name`: canonical GitHub `owner/name`.
- `url`: `https://github.com/<full_name>`.
- `description`: concise factual public description.
- `scope`: `core`, `adjacent`, or `unverified`.
- `specialty`: lowercase hyphenated taxonomy value; reuse an existing value when it fits.
- `skill_or_plugin`: true only when packaging or public documentation explicitly supports it.
- `created_at`, `pushed_at`: GitHub ISO-8601 timestamps.
- `stars`, `forks`: non-negative GitHub snapshot counts.
- `language`: GitHub primary language or null.
- `license`: SPDX identifier or null; do not infer a license from source headers alone.
- `archived`: GitHub archived state.

## Scope decisions

- `core`: directly diagnoses, explains, monitors, repairs, or safely mitigates Codex.
- `adjacent`: Doctor-branded Codex workflow for a related preflight or quality task.
- `unverified`: likely relevant but insufficient evidence for confident classification.

Forks and mirrors are not automatically distinct entries. Include one only when it has an independently maintained purpose that readers need to compare.

