# Contributing

Contributions are welcome through pull requests or issues.

For an agent-assisted contribution, invoke [`$update-awesome-codex-doctors`](skills/update-awesome-codex-doctors/SKILL.md). It follows the same evidence rules, regenerates derived files, and runs the catalog audit before handoff.

## Add a Doctor

Please include:

- repository URL;
- the Codex problem it diagnoses or repairs;
- supported platforms;
- delivery form: built-in command, CLI, GUI, skill, or plugin;
- whether it is read-only, repairs state, or performs cleanup;
- files and directories it may touch;
- license and latest verified version;
- evidence: README section, release, source file, or test demonstrating the claim.

## Safety requirements

Tools that modify local state must document backup behavior, dry-run support, confirmation behavior, and the paths they can change. Projects that conceal destructive behavior or encourage unsafe deletion are not accepted.

## Descriptions

Descriptions should be factual and specific. Avoid promotional adjectives, copied marketing text, and unsupported compatibility claims.
