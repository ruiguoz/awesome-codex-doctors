# Awesome Codex Doctors 🩺

> Every Codex doctor, mapped and compared.

A curated, evidence-backed directory of diagnostic skills, repair tools, recovery utilities, and observability projects for OpenAI Codex.

[简体中文](README.zh-CN.md) · [Full catalog](CATALOG.md) · [Methodology](METHODOLOGY.md) · [Contributing](CONTRIBUTING.md)

![Growth of the Codex Doctor community](assets/community-growth.svg)

## Why this community matters

Codex now includes an [official `codex doctor` diagnostic command](https://github.com/openai/codex/blob/main/codex-rs/cli/src/doctor.rs), released with [Codex CLI v0.131.0](https://github.com/openai/codex/releases/tag/rust-v0.131.0). The community has continued to build specialized doctors for problems the general command cannot cover deeply: Windows setup, Desktop plugins, sessions, SQLite state, storage, reconnect loops, hooks, MCP, providers, context pressure, and more.

Our 2026-08-27 snapshot found **51 name matches** and retained **42 reviewed projects**: **38 core doctors**, **3 adjacent Doctor workflows**, and **1 unverified candidate**. **12 are packaged as, or explicitly centered on, Codex skills/plugins.** Thirty-four of the 42 appeared after the official command shipped.

That growth is the point of this repository: Codex troubleshooting is becoming a community-maintained layer, not a single command.

## Quick navigation by specialty

<!-- quick-links-en:start -->

- **Desktop Plugin Repair**: [navi118/codex-desktop-doctor-skill](https://github.com/navi118/codex-desktop-doctor-skill), [y3078266584/codex-plugin-doctor](https://github.com/y3078266584/codex-plugin-doctor), [UPmeme/codex-windows-plugin-doctor](https://github.com/UPmeme/codex-windows-plugin-doctor) and more
- **Windows**: [cuijialin8888-code/codex-win-doctor](https://github.com/cuijialin8888-code/codex-win-doctor), [Yurainln1122/codex-windows-doctor](https://github.com/Yurainln1122/codex-windows-doctor), [Yaro-Tab/codex-windows-doctor](https://github.com/Yaro-Tab/codex-windows-doctor) and more
- **Reconnect**: [juzai0924-cloud/codex-reconnect-doctor](https://github.com/juzai0924-cloud/codex-reconnect-doctor), [baixinpan/codex-reconnecting-doctor](https://github.com/baixinpan/codex-reconnecting-doctor) and more
- **Session Repair**: [hj01857655/codex-doctor](https://github.com/hj01857655/codex-doctor), [Nitmi/codex-session-doctor](https://github.com/Nitmi/codex-session-doctor) and more
- **Authentication**: [Qiyuanqiii/codex-401-doctor](https://github.com/Qiyuanqiii/codex-401-doctor) and more
- **Configuration**: [Lumidew/codex-doctor](https://github.com/Lumidew/codex-doctor) and more
- **Context**: [ChenSir886/codex-context-doctor-cn](https://github.com/ChenSir886/codex-context-doctor-cn) and more
- **Context And Tokens**: [ironman429100-rgb/codex-token-doctor](https://github.com/ironman429100-rgb/codex-token-doctor) and more

<!-- quick-links-en:end -->

## Complete catalog

Each row says what makes that Doctor distinct. Stars are snapshot counts for discovery, not quality scores. The same table is available as **[CATALOG.md](CATALOG.md)**.

<!-- catalog-en:start -->

| Project | What it does | Stars |
|---|---|---:|
| [navi118/codex-desktop-doctor-skill](https://github.com/navi118/codex-desktop-doctor-skill) | A Windows Skill that diagnoses Codex Desktop Chrome and Computer Use failures across plugin discovery and browser startup. | [⭐ 32](https://github.com/navi118/codex-desktop-doctor-skill/stargazers) |
| [wokao4360-rgb/codex-desktop-doctor](https://github.com/wokao4360-rgb/codex-desktop-doctor) | Windows all-in-one repair toolkit for Codex Desktop plugins, MCP OAuth, local API providers, and session visibility. | [⭐ 12](https://github.com/wokao4360-rgb/codex-desktop-doctor/stargazers) |
| [2023Anita/codex-speed-doctor](https://github.com/2023Anita/codex-speed-doctor) | Profiles slow Codex Desktop or CLI startup with local, read-only checks across configuration, integrations, and runtime timing. | [⭐ 5](https://github.com/2023Anita/codex-speed-doctor/stargazers) |
| [cuijialin8888-code/codex-win-doctor](https://github.com/cuijialin8888-code/codex-win-doctor) | Provides a general Windows troubleshooting toolkit for Codex installation, configuration, and runtime failures. | [⭐ 3](https://github.com/cuijialin8888-code/codex-win-doctor/stargazers) |
| [Esquetta/CodexPluginDoctor](https://github.com/Esquetta/CodexPluginDoctor) | Validates Codex plugin packages, skills, MCP bundles, manifests, and registry metadata before release or installation. | [⭐ 2](https://github.com/Esquetta/CodexPluginDoctor/stargazers) |
| [Qiyuanqiii/codex-401-doctor](https://github.com/Qiyuanqiii/codex-401-doctor) | Diagnoses and repairs common Windows causes of Codex 401 Unauthorized authentication failures. | [⭐ 2](https://github.com/Qiyuanqiii/codex-401-doctor/stargazers) |
| [RE-Rays/codex-environment-doctor](https://github.com/RE-Rays/codex-environment-doctor) | A Windows desktop dashboard for Codex configuration, proxy ports, and reconnect logs, with backed-up reversible optimizations. | [⭐ 1](https://github.com/RE-Rays/codex-environment-doctor/stargazers) |
| [Yurainln1122/codex-windows-doctor](https://github.com/Yurainln1122/codex-windows-doctor) | Checks Windows-specific Codex failures in PowerShell, PATH, configuration, sandboxing, and OS compatibility without modifying state. | [⭐ 1](https://github.com/Yurainln1122/codex-windows-doctor/stargazers) |
| [Gmasterzhangxinyang/codex-doctor](https://github.com/Gmasterzhangxinyang/codex-doctor) | Explains why a Codex session appears stuck by correlating visible events, tool activity, and network status. | [⭐ 1](https://github.com/Gmasterzhangxinyang/codex-doctor/stargazers) |
| [Freyliu0516/Codex-Log-Doctor](https://github.com/Freyliu0516/Codex-Log-Doctor) | Measures and controls Codex SQLite log churn without reading conversation content. | [⭐ 1](https://github.com/Freyliu0516/Codex-Log-Doctor/stargazers) |
| [2395115107-stack/codex-history-doctor](https://github.com/2395115107-stack/codex-history-doctor) | Rebuilds session_index.jsonl and SQLite thread rows from local rollout files, with backups and current-provider realignment. | [⭐ 1](https://github.com/2395115107-stack/codex-history-doctor/stargazers) |
| [Maverick04/codex-doctor](https://github.com/Maverick04/codex-doctor) | Reads session telemetry to expose context pressure, repeated work, tool failures, stalled activity, and token growth. | [⭐ 1](https://github.com/Maverick04/codex-doctor/stargazers) |
| [hj01857655/codex-doctor](https://github.com/hj01857655/codex-doctor) | Repairs invisible sessions caused by drift between rollout files, SQLite indexes, archives, and model providers; includes CLI and GUI backups. | [⭐ 1](https://github.com/hj01857655/codex-doctor/stargazers) |
| [RobertIonutF/codex-budget-doctor](https://github.com/RobertIonutF/codex-budget-doctor) | Finds causes of amplified Codex usage and recommends more efficient model profiles with local, privacy-first analysis. | [⭐ 0](https://github.com/RobertIonutF/codex-budget-doctor/stargazers) |
| [vik-codex/Doctor](https://github.com/vik-codex/Doctor) | Unverified HTML project with no public README or description; its Codex diagnostic purpose is not yet documented. | [⭐ 0](https://github.com/vik-codex/Doctor/stargazers) |
| [yezhouyedu/codex-report-doctor](https://github.com/yezhouyedu/codex-report-doctor) | Turns statistical output into evidence-backed, defensible research reports; an adjacent Codex quality workflow. | [⭐ 0](https://github.com/yezhouyedu/codex-report-doctor/stargazers) |
| [y3078266584/codex-plugin-doctor](https://github.com/y3078266584/codex-plugin-doctor) | Repairs missing or unusable openai-bundled Browser, Chrome, and Computer Use plugin caches on Windows. | [⭐ 0](https://github.com/y3078266584/codex-plugin-doctor/stargazers) |
| [DWG7318/codex-network-doctor](https://github.com/DWG7318/codex-network-doctor) | Collects offline Windows network evidence and repairs v2rayN TUN paths used by Codex connectivity. | [⭐ 0](https://github.com/DWG7318/codex-network-doctor/stargazers) |
| [xiangyanghua-22/codex-hooks-doctor](https://github.com/xiangyanghua-22/codex-hooks-doctor) | Traces why configured Codex hooks are not firing and identifies broken trigger or command wiring. | [⭐ 0](https://github.com/xiangyanghua-22/codex-hooks-doctor/stargazers) |
| [Yaro-Tab/codex-windows-doctor](https://github.com/Yaro-Tab/codex-windows-doctor) | Runs privacy-safe, read-only health checks for Codex installation, configuration, permissions, and networking on Windows and WSL. | [⭐ 0](https://github.com/Yaro-Tab/codex-windows-doctor/stargazers) |
| [momochoog/codex-workspace-doctor](https://github.com/momochoog/codex-workspace-doctor) | Reports how much disk space local Codex workspaces consume on macOS without deleting anything. | [⭐ 0](https://github.com/momochoog/codex-workspace-doctor/stargazers) |
| [wildbyteai/codex-provider-doctor](https://github.com/wildbyteai/codex-provider-doctor) | Diagnoses third-party model providers across configuration, authentication, plugins, and history compatibility without making changes. | [⭐ 0](https://github.com/wildbyteai/codex-provider-doctor/stargazers) |
| [YizeSun/codex-doctor](https://github.com/YizeSun/codex-doctor) | Explains Codex runtime disk usage and offers allowlisted cleanup for sessions, caches, Xcode artifacts, and temporary builds on macOS. | [⭐ 0](https://github.com/YizeSun/codex-doctor/stargazers) |
| [Lumidew/codex-doctor](https://github.com/Lumidew/codex-doctor) | Checks Codex-native configuration hygiene and offers only approval-gated fixes. | [⭐ 0](https://github.com/Lumidew/codex-doctor/stargazers) |
| [BTCElectrician/codex-storage-doctor](https://github.com/BTCElectrician/codex-storage-doctor) | Diagnoses Codex SQLite diagnostic-log growth and applies preservation-first, reversible storage mitigations. | [⭐ 0](https://github.com/BTCElectrician/codex-storage-doctor/stargazers) |
| [gtrgear/codex-submission-doctor](https://github.com/gtrgear/codex-submission-doctor) | Runs a local, privacy-conscious quality and packaging preflight for hackathon submissions; adjacent to Codex diagnostics. | [⭐ 0](https://github.com/gtrgear/codex-submission-doctor/stargazers) |
| [luogangan7-lgtm/codex-mcp-doctor](https://github.com/luogangan7-lgtm/codex-mcp-doctor) | Acts like npm doctor for MCP servers, catching broken setups, Cyrillic homoglyph attacks, and suspicious dependency changes. | [⭐ 0](https://github.com/luogangan7-lgtm/codex-mcp-doctor/stargazers) |
| [configcrate/codex-session-doctor](https://github.com/configcrate/codex-session-doctor) | Detects oversized or malformed local Codex Desktop session files without changing them. | [⭐ 0](https://github.com/configcrate/codex-session-doctor/stargazers) |
| [zjp1997720/codex-doctor](https://github.com/zjp1997720/codex-doctor) | Audits AGENTS.md, Skills, MCP, hooks, configuration, provider history, and Git hygiene with read-only evidence checks. | [⭐ 0](https://github.com/zjp1997720/codex-doctor/stargazers) |
| [warren2008-2020-spec/codex-doctor](https://github.com/warren2008-2020-spec/codex-doctor) | Runs broad read-only setup diagnostics across Windows, WSL, GitHub, npm, sandbox, proxy, and CI workflows. | [⭐ 0](https://github.com/warren2008-2020-spec/codex-doctor/stargazers) |
| [junchangzhu42-eng/codex-skill-doctor](https://github.com/junchangzhu42-eng/codex-skill-doctor) | Diagnoses and recovers missing, broken, or undiscoverable Codex Skill installations on Windows. | [⭐ 0](https://github.com/junchangzhu42-eng/codex-skill-doctor/stargazers) |
| [juzai0924-cloud/codex-reconnect-doctor](https://github.com/juzai0924-cloud/codex-reconnect-doctor) | Monitors Codex reconnect behavior and local proxy health from a native macOS menu-bar app. | [⭐ 0](https://github.com/juzai0924-cloud/codex-reconnect-doctor/stargazers) |
| [shixianli083-eng/codex-doctor](https://github.com/shixianli083-eng/codex-doctor) | Checks Codex and its surrounding AI development environment on macOS for setup and dependency problems. | [⭐ 0](https://github.com/shixianli083-eng/codex-doctor/stargazers) |
| [leiJack-lo/codex-local-doctor-skill](https://github.com/leiJack-lo/codex-local-doctor-skill) | Audits local Codex logs, state, and broken Git health, then offers narrowly scoped mitigations with safety gates. | [⭐ 0](https://github.com/leiJack-lo/codex-local-doctor-skill/stargazers) |
| [ember056/codex_session_doctor](https://github.com/ember056/codex_session_doctor) | Recovers Codex Desktop conversations that remain on disk but have disappeared from the sidebar. | [⭐ 0](https://github.com/ember056/codex_session_doctor/stargazers) |
| [baixinpan/codex-reconnecting-doctor](https://github.com/baixinpan/codex-reconnecting-doctor) | Diagnoses and repairs Codex Desktop reconnect loops caused by proxy drift or WebSocket transport configuration. | [⭐ 0](https://github.com/baixinpan/codex-reconnecting-doctor/stargazers) |
| [UPmeme/codex-windows-plugin-doctor](https://github.com/UPmeme/codex-windows-plugin-doctor) | Checks and repairs Windows installation issues affecting the Computer Use, Chrome, and Browser plugins. | [⭐ 0](https://github.com/UPmeme/codex-windows-plugin-doctor/stargazers) |
| [ironman429100-rgb/codex-token-doctor](https://github.com/ironman429100-rgb/codex-token-doctor) | Analyzes local Codex token events to identify context, caching, output, or long-session drains and rank the highest-impact savings. | [⭐ 0](https://github.com/ironman429100-rgb/codex-token-doctor/stargazers) |
| [ChenSir886/codex-context-doctor-cn](https://github.com/ChenSir886/codex-context-doctor-cn) | Audits Codex context configuration in Chinese, focusing on automatic compaction thresholds and model context windows. | [⭐ 0](https://github.com/ChenSir886/codex-context-doctor-cn/stargazers) |
| [Nitmi/codex-session-doctor](https://github.com/Nitmi/codex-session-doctor) | Repairs Windows Codex Desktop session-render crashes caused by persisted Git markers in stored conversation data. | [⭐ 0](https://github.com/Nitmi/codex-session-doctor/stargazers) |
| [daniel-p-green/codex-skill_secret-agents-dot-md-doctor](https://github.com/daniel-p-green/codex-skill_secret-agents-dot-md-doctor) | Drafts concise, repository-specific AGENTS.md instructions from local evidence and current Codex guidance. | [⭐ 0](https://github.com/daniel-p-green/codex-skill_secret-agents-dot-md-doctor/stargazers) |
| [warwickmei/codex-skill-doctor](https://github.com/warwickmei/codex-skill-doctor) | Checks whether Codex skill wrappers are installed and wired correctly with a local proof CLI. | [⭐ 0](https://github.com/warwickmei/codex-skill-doctor/stargazers) |

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
