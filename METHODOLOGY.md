# Methodology

## Discovery

The current snapshot was collected from the GitHub Search API on 2026-08-27 with:

```text
codex-doctor in:name
```

The query returned 51 repositories. Each result was reviewed using its name, description, and public repository page.

## Inclusion

A project is included when it does at least one of the following for OpenAI Codex:

- diagnoses configuration, runtime, authentication, network, plugin, MCP, or environment failures;
- explains session, context, token, performance, or storage health;
- repairs or recovers local Codex state;
- provides a Doctor-branded Codex skill or preflight workflow closely related to diagnosis.

We exclude medical applications created with Codex, generic test repositories, repositories matched only because the owner name contains `doctor` or `codex`, and duplicate placeholders.

## Scope labels

- **Core:** directly diagnoses, explains, repairs, or observes Codex.
- **Adjacent:** Doctor-branded Codex workflows for related quality or preflight tasks.
- **Unverified:** potentially relevant, but insufficient public metadata was available.

## Growth chart

The chart uses GitHub repository `created_at`, not the first release, first useful commit, or date the project became public. It is a discovery curve, not an adoption or quality curve.

The skills/plugins series includes repositories explicitly packaged as a Codex skill or plugin, or whose public description clearly centers on skills/plugins. Classification is manually reviewable in `data/github-snapshot.json`.

The official marker uses the publication date of [Codex CLI v0.131.0](https://github.com/openai/codex/releases/tag/rust-v0.131.0), the first release containing the built-in `codex doctor` command.

## Limitations

GitHub search is not exhaustive. Projects may avoid the Doctor name, live inside monorepos, be private, or have incomplete metadata. Stars are volatile and are never used as an inclusion threshold.

