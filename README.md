# Awesome Codex Doctors 🩺

> Every Codex doctor, mapped and compared.

A curated, evidence-backed directory of diagnostic skills, repair tools, recovery utilities, and observability projects for OpenAI Codex.

[简体中文](README.zh-CN.md) · [Full catalog](CATALOG.md) · [Methodology](METHODOLOGY.md) · [Contributing](CONTRIBUTING.md)

![Growth of the Codex Doctor community](assets/community-growth.svg)

## Why this community matters

Codex now includes an [official `codex doctor` diagnostic command](https://github.com/openai/codex/blob/main/codex-rs/cli/src/doctor.rs), released with [Codex CLI v0.131.0](https://github.com/openai/codex/releases/tag/rust-v0.131.0). The community has continued to build specialized doctors for problems the general command cannot cover deeply: Windows setup, Desktop plugins, sessions, SQLite state, storage, reconnect loops, hooks, MCP, providers, context pressure, and more.

Our 2026-08-27 snapshot found **51 name matches** and retained **42 reviewed projects**: **38 core doctors**, **3 adjacent Doctor workflows**, and **1 unverified candidate**. **12 are packaged as, or explicitly centered on, Codex skills/plugins.** Thirty-four of the 42 appeared after the official command shipped.

That growth is the point of this repository: Codex troubleshooting is becoming a community-maintained layer, not a single command.

## Start here

| Project | Focus | Form | Changes local state? |
|---|---|---|---:|
| [`openai/codex doctor`](https://github.com/openai/codex/blob/main/codex-rs/cli/src/doctor.rs) | Official environment and runtime diagnostics | Built-in CLI | No |
| [`YizeSun/codex-doctor`](https://github.com/YizeSun/codex-doctor) | Runtime storage, caches, and macOS build artifacts | Skill + Shell | Optional cleanup |
| [`hj01857655/codex-doctor`](https://github.com/hj01857655/codex-doctor) | Session index repair and recovery | Rust CLI + GUI | Yes, with backup/dry-run |
| [`Maverick04/codex-doctor`](https://github.com/Maverick04/codex-doctor) | Context pressure, repeated work, and slow tools | Plugin + Node CLI | No |
| [`navi118/codex-desktop-doctor-skill`](https://github.com/navi118/codex-desktop-doctor-skill) | Windows Desktop, Chrome, and Computer Use failures | PowerShell Skill | Yes |

The complete catalog is embedded below and is also available as a standalone **[CATALOG.md](CATALOG.md)**.

## Quick navigation by specialty

<!-- quick-links-en:start -->

- **Desktop Plugin Repair**: [navi118/codex-desktop-doctor-skill](https://github.com/navi118/codex-desktop-doctor-skill), [UPmeme/codex-windows-plugin-doctor](https://github.com/UPmeme/codex-windows-plugin-doctor), [y3078266584/codex-plugin-doctor](https://github.com/y3078266584/codex-plugin-doctor) and more
- **Windows**: [cuijialin8888-code/codex-win-doctor](https://github.com/cuijialin8888-code/codex-win-doctor), [Yaro-Tab/codex-windows-doctor](https://github.com/Yaro-Tab/codex-windows-doctor), [Yurainln1122/codex-windows-doctor](https://github.com/Yurainln1122/codex-windows-doctor) and more
- **Reconnect**: [baixinpan/codex-reconnecting-doctor](https://github.com/baixinpan/codex-reconnecting-doctor), [juzai0924-cloud/codex-reconnect-doctor](https://github.com/juzai0924-cloud/codex-reconnect-doctor) and more
- **Session Repair**: [hj01857655/codex-doctor](https://github.com/hj01857655/codex-doctor), [Nitmi/codex-session-doctor](https://github.com/Nitmi/codex-session-doctor) and more
- **Authentication**: [Qiyuanqiii/codex-401-doctor](https://github.com/Qiyuanqiii/codex-401-doctor) and more
- **Configuration**: [Lumidew/codex-doctor](https://github.com/Lumidew/codex-doctor) and more
- **Context**: [ChenSir886/codex-context-doctor-cn](https://github.com/ChenSir886/codex-context-doctor-cn) and more
- **Context And Tokens**: [ironman429100-rgb/codex-token-doctor](https://github.com/ironman429100-rgb/codex-token-doctor) and more

<!-- quick-links-en:end -->

## Recommended starters

<!-- starters-en:start -->

- [navi118/codex-desktop-doctor-skill](https://github.com/navi118/codex-desktop-doctor-skill) — Desktop Plugin Repair · 32 ⭐ · repair
- [wokao4360-rgb/codex-desktop-doctor](https://github.com/wokao4360-rgb/codex-desktop-doctor) — Desktop Repair · 12 ⭐ · repair
- [2023Anita/codex-speed-doctor](https://github.com/2023Anita/codex-speed-doctor) — Performance · 5 ⭐ · read-only
- [cuijialin8888-code/codex-win-doctor](https://github.com/cuijialin8888-code/codex-win-doctor) — Windows · 3 ⭐ · unknown
- [Esquetta/CodexPluginDoctor](https://github.com/Esquetta/CodexPluginDoctor) — Plugin Validation · 2 ⭐ · unknown

<!-- starters-en:end -->

## Complete catalog

<!-- catalog-en:start -->

| Project | Focus | Specialty | Scope | Skill / plugin | Risk level | Dry-run | Backup | Evidence | Language | License | Created | Stars | Last push |
|---|---|---|---:|:---:|---|---:|---:|---:|---|---|---:|---:|---:|
| [Qiyuanqiii/codex-401-doctor](https://github.com/Qiyuanqiii/codex-401-doctor) | Diagnose and repair common Codex 401 Unauthorized issues on Windows | Authentication | Core | No | repair | unknown | unknown | 1 | PowerShell | Not declared | 2026-07-07 | 2 | 2026-08-06 |
| [Lumidew/codex-doctor](https://github.com/Lumidew/codex-doctor) | Codex-native diagnostics and configuration hygiene with approval-gated fixes. | Configuration | Core | No | unknown | unknown | unknown | 1 | — | Not declared | 2026-07-25 | 0 | 2026-07-25 |
| [ChenSir886/codex-context-doctor-cn](https://github.com/ChenSir886/codex-context-doctor-cn) | 中文 Codex 上下文配置体检工具，检查自动压缩阈值和模型窗口 | Context | Core | No | unknown | unknown | unknown | 1 | Python | MIT | 2026-05-23 | 0 | 2026-05-23 |
| [ironman429100-rgb/codex-token-doctor](https://github.com/ironman429100-rgb/codex-token-doctor) |  | Context And Tokens | Core | No | unknown | unknown | unknown | 1 | Python | Not declared | 2026-05-20 | 0 | 2026-05-25 |
| [navi118/codex-desktop-doctor-skill](https://github.com/navi118/codex-desktop-doctor-skill) | Codex Skill for diagnosing Chrome and Computer Use failures in Codex Desktop on Windows. | Desktop Plugin Repair | Core | Yes | repair | unknown | unknown | 2 | PowerShell | MIT | 2026-06-03 | 32 | 2026-07-21 |
| [UPmeme/codex-windows-plugin-doctor](https://github.com/UPmeme/codex-windows-plugin-doctor) | Fix and diagnose Codex Computer Use, Chrome, and Browser plugin issues on Windows. | Desktop Plugin Repair | Core | Yes | repair | unknown | unknown | 2 | PowerShell | MIT | 2026-06-04 | 0 | 2026-06-04 |
| [y3078266584/codex-plugin-doctor](https://github.com/y3078266584/codex-plugin-doctor) | 🩺 修复 Codex Windows 端 openai-bundled 插件（Browser/Chrome/Computer Use）不可用的 Codex Skill | Desktop Plugin Repair | Core | Yes | repair | unknown | unknown | 1 | PowerShell | Not declared | 2026-08-13 | 0 | 2026-08-13 |
| [wokao4360-rgb/codex-desktop-doctor](https://github.com/wokao4360-rgb/codex-desktop-doctor) | Windows-first repair toolkit for Codex Desktop plugins, MCP OAuth, local API providers, and session visibility | Desktop Repair | Core | No | repair | unknown | unknown | 2 | PowerShell | MIT | 2026-05-03 | 12 | 2026-05-03 |
| [RE-Rays/codex-environment-doctor](https://github.com/RE-Rays/codex-environment-doctor) |  | Environment | Core | No | unknown | unknown | unknown | 1 | Python | MIT | 2026-08-06 | 1 | 2026-08-06 |
| [2395115107-stack/codex-history-doctor](https://github.com/2395115107-stack/codex-history-doctor) |  | History | Core | No | unknown | unknown | unknown | 1 | JavaScript | MIT | 2026-05-27 | 1 | 2026-05-28 |
| [xiangyanghua-22/codex-hooks-doctor](https://github.com/xiangyanghua-22/codex-hooks-doctor) | Find out why your Codex hooks aren't firing | Hooks | Core | No | unknown | unknown | unknown | 1 | TypeScript | MIT | 2026-08-11 | 0 | 2026-08-13 |
| [leiJack-lo/codex-local-doctor-skill](https://github.com/leiJack-lo/codex-local-doctor-skill) | Codex skill to audit and safely mitigate local Codex log, state, and broken Git health issues | Local State | Core | Yes | unknown | unknown | unknown | 1 | Python | Apache-2.0 | 2026-06-26 | 0 | 2026-06-26 |
| [Freyliu0516/Codex-Log-Doctor](https://github.com/Freyliu0516/Codex-Log-Doctor) | Codex Log Doctor is a local, content-blind safety tool for diagnosing and controlling Codex SQLite log churn.  It is an independent community project. It is not affiliated with, endorsed by, or supported by OpenAI. | Logs | Core | No | unknown | unknown | unknown | 1 | Rust | MIT | 2026-07-13 | 1 | 2026-07-14 |
| [shixianli083-eng/codex-doctor](https://github.com/shixianli083-eng/codex-doctor) | Codex Doctor: macOS diagnostics for Codex and AI development environments. | Macos Environment | Core | No | unknown | unknown | unknown | 1 | Python | MIT | 2026-07-05 | 0 | 2026-07-05 |
| [luogangan7-lgtm/codex-mcp-doctor](https://github.com/luogangan7-lgtm/codex-mcp-doctor) | 'npm doctor' for MCP. Diagnose broken servers, Cyrillic homoglyph attacks, and silent rug-pulls - zero deps, 287 tests. Built in Codex with GPT-5.6. | Mcp | Core | No | unknown | unknown | unknown | 1 | Python | MIT | 2026-07-18 | 0 | 2026-07-19 |
| [wildbyteai/codex-provider-doctor](https://github.com/wildbyteai/codex-provider-doctor) | Read-only Codex third-party model provider diagnostics for configuration, authentication, plugins, and history compatibility. | Model Provider | Core | No | read-only | unknown | unknown | 1 | Python | MIT | 2026-08-04 | 0 | 2026-08-06 |
| [DWG7318/codex-network-doctor](https://github.com/DWG7318/codex-network-doctor) | Windows offline network evidence collector and v2rayN TUN repair tool | Network | Core | No | repair | unknown | unknown | 1 | Go | Apache-2.0 | 2026-07-30 | 0 | 2026-08-13 |
| [2023Anita/codex-speed-doctor](https://github.com/2023Anita/codex-speed-doctor) | Local-first, read-only diagnostics for slow Codex Desktop or CLI startup | Performance | Core | No | read-only | unknown | unknown | 1 | Python | MIT | 2026-05-15 | 5 | 2026-07-19 |
| [Esquetta/CodexPluginDoctor](https://github.com/Esquetta/CodexPluginDoctor) | Local CLI validator for Codex plugin packages, skills, and MCP server bundles. | Plugin Validation | Core | Yes | unknown | unknown | unknown | 1 | TypeScript | MIT | 2026-04-22 | 2 | 2026-08-25 |
| [baixinpan/codex-reconnecting-doctor](https://github.com/baixinpan/codex-reconnecting-doctor) | Codex skill and doctor script for diagnosing and repairing Codex Desktop reconnecting loops, proxy drift, and WebSocket transport issues. | Reconnect | Core | Yes | repair | unknown | unknown | 2 | Python | MIT | 2026-06-10 | 0 | 2026-06-10 |
| [juzai0924-cloud/codex-reconnect-doctor](https://github.com/juzai0924-cloud/codex-reconnect-doctor) | A native macOS menu bar tool for diagnosing Codex reconnect and local proxy issues. | Reconnect | Core | No | unknown | unknown | unknown | 1 | Swift | MIT | 2026-07-05 | 0 | 2026-07-06 |
| [YizeSun/codex-doctor](https://github.com/YizeSun/codex-doctor) |  | Runtime Storage | Core | Yes | cleanup | unknown | unknown | 2 | Shell | MIT | 2026-07-07 | 0 | 2026-07-25 |
| [Gmasterzhangxinyang/codex-doctor](https://github.com/Gmasterzhangxinyang/codex-doctor) | A local-first CLI health check for Codex sessions: see visible events, tool activity, network status, and likely reasons when Codex appears stuck. | Session Health | Core | No | unknown | unknown | unknown | 1 | Python | MIT | 2026-07-01 | 1 | 2026-07-22 |
| [configcrate/codex-session-doctor](https://github.com/configcrate/codex-session-doctor) | Read-only health check for oversized and malformed local Codex Desktop sessions. | Session Integrity | Core | No | read-only | unknown | unknown | 1 | Go | MIT | 2026-07-17 | 0 | 2026-07-17 |
| [Maverick04/codex-doctor](https://github.com/Maverick04/codex-doctor) | Codex session diagnostic plugin | Session Observability | Core | Yes | unknown | unknown | unknown | 1 | JavaScript | MIT | 2026-04-24 | 1 | 2026-04-25 |
| [ember056/codex_session_doctor](https://github.com/ember056/codex_session_doctor) | A local recovery and repair tool for Codex Desktop conversations that still exist on disk but disappear from the sidebar. | Session Recovery | Core | No | repair | unknown | unknown | 1 | Python | MIT | 2026-06-12 | 0 | 2026-06-12 |
| [hj01857655/codex-doctor](https://github.com/hj01857655/codex-doctor) | Diagnose and repair local Codex state across CLI and native egui GUI. | Session Repair | Core | No | repair | yes | yes | 3 | Rust | Not declared | 2026-04-06 | 1 | 2026-04-08 |
| [Nitmi/codex-session-doctor](https://github.com/Nitmi/codex-session-doctor) | Windows repair tool for Codex Desktop session render crashes caused by persisted git markers | Session Repair | Core | No | repair | unknown | unknown | 1 | Go | MIT | 2026-05-16 | 0 | 2026-05-16 |
| [warren2008-2020-spec/codex-doctor](https://github.com/warren2008-2020-spec/codex-doctor) | Read-only diagnostics for Codex setup problems across Windows, WSL, GitHub, npm, sandbox, proxy, and CI workflows | Setup | Core | No | read-only | unknown | unknown | 1 | JavaScript | MIT | 2026-07-16 | 0 | 2026-07-16 |
| [warwickmei/codex-skill-doctor](https://github.com/warwickmei/codex-skill-doctor) | Local proof CLI for Codex skill wrapper diagnostics. | Skill Diagnostics | Core | Yes | unknown | unknown | unknown | 1 | Python | NOASSERTION | 2026-03-27 | 0 | 2026-03-27 |
| [junchangzhu42-eng/codex-skill-doctor](https://github.com/junchangzhu42-eng/codex-skill-doctor) | Diagnose and recover Codex Skill installations on Windows | Skill Recovery | Core | Yes | repair | unknown | unknown | 1 | Python | MIT | 2026-07-13 | 0 | 2026-07-13 |
| [BTCElectrician/codex-storage-doctor](https://github.com/BTCElectrician/codex-storage-doctor) | Preservation-first diagnosis and reversible mitigation for Codex SQLite diagnostic-log churn. | Sqlite Storage | Core | No | unknown | unknown | unknown | 1 | Python | Apache-2.0 | 2026-07-24 | 0 | 2026-07-25 |
| [RobertIonutF/codex-budget-doctor](https://github.com/RobertIonutF/codex-budget-doctor) | Local, privacy-first diagnostics for Codex usage amplification and efficient model profiles. | Usage And Budget | Core | No | unknown | unknown | unknown | 1 | TypeScript | MIT | 2026-08-21 | 0 | 2026-08-21 |
| [cuijialin8888-code/codex-win-doctor](https://github.com/cuijialin8888-code/codex-win-doctor) | Unofficial diagnostics and troubleshooting toolkit for OpenAI Codex on Windows. | Windows | Core | No | unknown | unknown | unknown | 1 | PowerShell | MIT | 2026-08-11 | 3 | 2026-08-26 |
| [Yaro-Tab/codex-windows-doctor](https://github.com/Yaro-Tab/codex-windows-doctor) | Privacy-safe, read-only diagnostics for Codex failures on Windows and WSL. | Windows | Core | No | read-only | unknown | unknown | 1 | PowerShell | MIT | 2026-08-09 | 0 | 2026-08-09 |
| [Yurainln1122/codex-windows-doctor](https://github.com/Yurainln1122/codex-windows-doctor) | Safe, read-only diagnostics for Windows-specific Codex failures: PowerShell, PATH, configuration, sandbox, and OS compatibility. | Windows | Core | No | read-only | unknown | unknown | 1 | PowerShell | MIT | 2026-07-31 | 1 | 2026-07-31 |
| [zjp1997720/codex-doctor](https://github.com/zjp1997720/codex-doctor) | Audit Codex health and workspace context with read-only checks for AGENTS.md, Skills, MCP, hooks, config, and Git hygiene. | Workspace Configuration | Core | No | read-only | unknown | unknown | 1 | Python | MIT | 2026-07-14 | 0 | 2026-07-17 |
| [momochoog/codex-workspace-doctor](https://github.com/momochoog/codex-workspace-doctor) | Read-only storage report for local Codex workspaces on macOS. | Workspace Storage | Core | No | read-only | unknown | unknown | 1 | — | Not declared | 2026-08-09 | 0 | 2026-08-09 |
| [daniel-p-green/codex-skill_secret-agents-dot-md-doctor](https://github.com/daniel-p-green/codex-skill_secret-agents-dot-md-doctor) | Codex skill for drafting concise repo-specific AGENTS.md files from repository evidence and current Codex guidance. | Agents Md | Adjacent | Yes | unknown | unknown | unknown | 1 | Python | Not declared | 2026-04-15 | 0 | 2026-04-15 |
| [yezhouyedu/codex-report-doctor](https://github.com/yezhouyedu/codex-report-doctor) | A Codex skill for turning statistical output into defensible research reports. | Report Quality | Adjacent | Yes | unknown | unknown | unknown | 1 | — | MIT | 2026-08-17 | 0 | 2026-08-17 |
| [gtrgear/codex-submission-doctor](https://github.com/gtrgear/codex-submission-doctor) | A local, privacy-conscious preflight checker for hackathon submissions. | Submission Preflight | Adjacent | No | unknown | unknown | unknown | 1 | Python | NOASSERTION | 2026-07-21 | 0 | 2026-07-21 |
| [vik-codex/Doctor](https://github.com/vik-codex/Doctor) |  | Unknown | Unverified | No | unknown | unknown | unknown | 1 | HTML | Not declared | 2026-08-20 | 0 | 2026-08-20 |

<!-- catalog-en:end -->

## Bundled skills

| Skill | Use it for |
|---|---|
| [`$codex-doctor`](skills/codex-doctor/SKILL.md) | Define a Codex problem, search local evidence and this catalog first, then verify official and community sources before recommending a risk-ranked route. |
| [`$update-awesome-codex-doctors`](skills/update-awesome-codex-doctors/SKILL.md) | Discover, verify, classify, render, and audit catalog changes so a contribution is ready to review and merge. |

Install either folder as a normal Codex skill, or use it directly from a checkout that exposes repository skills. The diagnostic skill is read-only by default; the maintenance skill edits only this catalog unless the user explicitly requests Git or GitHub actions.

## What belongs here

A project belongs when it diagnoses, explains, monitors, repairs, or safely mitigates an OpenAI Codex problem. We include built-in commands, CLIs, GUIs, skills, and plugins. Medical apps merely built with Codex, test repositories, and owner-name-only matches are excluded.

Every entry is labeled by specialty and scope. Read-only diagnosis, repair, and cleanup are treated as different risk levels; inclusion is not an endorsement.

## Repository description

**GitHub description:**

> A curated atlas of Codex doctor tools, diagnostic skills, repair utilities, and recovery workflows.

**Suggested topics:**

`awesome-list` · `codex` · `codex-cli` · `codex-doctor` · `openai-codex` · `codex-skills` · `agent-skills` · `plugins` · `diagnostics` · `troubleshooting` · `repair` · `recovery` · `observability` · `developer-tools`

## Data and updates

The current source snapshot lives in [`data/github-snapshot.json`](data/github-snapshot.json). Machine-readable export is written to [`data/catalog.json`](data/catalog.json). Run:

```bash
python scripts/discover.py
python scripts/render.py
python scripts/render.py --check
```

The discovery command refreshes candidate name matches for manual review, `render.py` regenerates catalogs/chart/export, and `--check` is suitable for CI.

## Disclaimer

This is an independent community directory and is not affiliated with or endorsed by OpenAI. Review code and backups before allowing any third-party Doctor to modify `~/.codex` or other local state.

## License

CC0-1.0. Project descriptions and linked source code remain subject to their original licenses.
