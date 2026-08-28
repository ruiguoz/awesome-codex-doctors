# Awesome Codex Doctors 🩺

> 收集每一位 Codex Doctor，并把它们放在一起比较。

这是一个经过人工复核、以证据为依据的社区目录，收集 OpenAI Codex 的诊断 Skill、修复工具、恢复工具与可观测性项目。

[English](README.md) · [完整目录](CATALOG.md) · [收录方法](METHODOLOGY.md) · [参与贡献](CONTRIBUTING.md)

![Codex Doctor 社区增长曲线](assets/community-growth.svg)

## 为什么这个社区值得关注

Codex 已经内置了[官方 `codex doctor` 诊断命令](https://github.com/openai/codex/blob/main/codex-rs/cli/src/doctor.rs)，并随 [Codex CLI v0.131.0](https://github.com/openai/codex/releases/tag/rust-v0.131.0) 发布。但社区仍在继续补足通用诊断覆盖不到的专科问题：Windows 环境、Desktop 插件、会话、SQLite 状态、磁盘空间、重连循环、Hooks、MCP、第三方 Provider 和上下文压力等。

截至 2026-08-27，我们从 **51 个名称命中**中人工复核出 **42 个项目**：**38 个核心 Doctor**、**3 个邻近 Doctor 工作流**和 **1 个待核验项目**。其中 **12 个明确采用 Skill 或 Plugin 形态**。42 个项目中有 34 个是在官方命令发布之后出现的。

这条增长曲线说明：Codex 故障诊断正在形成一个社区维护的专业层，而不再只是一个命令。

## 按专科快速导航

<!-- quick-links-zh:start -->

- **Desktop 插件修复**: [navi118/codex-desktop-doctor-skill](https://github.com/navi118/codex-desktop-doctor-skill)、[y3078266584/codex-plugin-doctor](https://github.com/y3078266584/codex-plugin-doctor)、[UPmeme/codex-windows-plugin-doctor](https://github.com/UPmeme/codex-windows-plugin-doctor) 等
- **Windows**: [cuijialin8888-code/codex-win-doctor](https://github.com/cuijialin8888-code/codex-win-doctor)、[Yurainln1122/codex-windows-doctor](https://github.com/Yurainln1122/codex-windows-doctor)、[Yaro-Tab/codex-windows-doctor](https://github.com/Yaro-Tab/codex-windows-doctor) 等
- **重连**: [juzai0924-cloud/codex-reconnect-doctor](https://github.com/juzai0924-cloud/codex-reconnect-doctor)、[baixinpan/codex-reconnecting-doctor](https://github.com/baixinpan/codex-reconnecting-doctor) 等
- **会话修复**: [hj01857655/codex-doctor](https://github.com/hj01857655/codex-doctor)、[Nitmi/codex-session-doctor](https://github.com/Nitmi/codex-session-doctor) 等
- **认证**: [Qiyuanqiii/codex-401-doctor](https://github.com/Qiyuanqiii/codex-401-doctor) 等
- **配置**: [Lumidew/codex-doctor](https://github.com/Lumidew/codex-doctor) 等
- **上下文**: [ChenSir886/codex-context-doctor-cn](https://github.com/ChenSir886/codex-context-doctor-cn) 等
- **上下文与 Token**: [ironman429100-rgb/codex-token-doctor](https://github.com/ironman429100-rgb/codex-token-doctor) 等

<!-- quick-links-zh:end -->

## 完整目录

每一行只说明这位 Doctor 与其他同名项目相比，具体解决什么问题。Stars 是发现线索，不代表质量评分。同一张表也单独保存在 **[CATALOG.md](CATALOG.md)**。

<!-- catalog-zh:start -->

| 项目 | 能做什么 | Stars |
|---|---|---:|
| [navi118/codex-desktop-doctor-skill](https://github.com/navi118/codex-desktop-doctor-skill) | 面向 Windows 的 Skill，诊断 Codex Desktop 中插件发现与浏览器启动链路造成的 Chrome、Computer Use 故障。 | [⭐ 32](https://github.com/navi118/codex-desktop-doctor-skill/stargazers) |
| [wokao4360-rgb/codex-desktop-doctor](https://github.com/wokao4360-rgb/codex-desktop-doctor) | 面向 Windows 的一体化修复工具，覆盖 Desktop 插件、MCP OAuth、本地 API Provider 与会话可见性。 | [⭐ 12](https://github.com/wokao4360-rgb/codex-desktop-doctor/stargazers) |
| [2023Anita/codex-speed-doctor](https://github.com/2023Anita/codex-speed-doctor) | 用本地只读检查分析 Codex Desktop/CLI 启动缓慢，覆盖配置、集成项与运行时耗时。 | [⭐ 5](https://github.com/2023Anita/codex-speed-doctor/stargazers) |
| [cuijialin8888-code/codex-win-doctor](https://github.com/cuijialin8888-code/codex-win-doctor) | 提供面向 Windows 的 Codex 通用排障工具集，覆盖安装、配置与运行时故障。 | [⭐ 3](https://github.com/cuijialin8888-code/codex-win-doctor/stargazers) |
| [Esquetta/CodexPluginDoctor](https://github.com/Esquetta/CodexPluginDoctor) | 在发布或安装前校验 Codex 插件包、Skills、MCP bundle、manifest 与 registry 元数据。 | [⭐ 2](https://github.com/Esquetta/CodexPluginDoctor/stargazers) |
| [Qiyuanqiii/codex-401-doctor](https://github.com/Qiyuanqiii/codex-401-doctor) | 诊断并修复 Windows 上导致 Codex 401 Unauthorized 的常见认证问题。 | [⭐ 2](https://github.com/Qiyuanqiii/codex-401-doctor/stargazers) |
| [RE-Rays/codex-environment-doctor](https://github.com/RE-Rays/codex-environment-doctor) | Windows 桌面仪表盘，检查 Codex 配置、代理端口与重连日志，并提供带备份的可逆优化。 | [⭐ 1](https://github.com/RE-Rays/codex-environment-doctor/stargazers) |
| [Yurainln1122/codex-windows-doctor](https://github.com/Yurainln1122/codex-windows-doctor) | 只读检查 PowerShell、PATH、配置、沙箱与系统兼容性引发的 Windows Codex 故障。 | [⭐ 1](https://github.com/Yurainln1122/codex-windows-doctor/stargazers) |
| [Gmasterzhangxinyang/codex-doctor](https://github.com/Gmasterzhangxinyang/codex-doctor) | 关联可见事件、工具活动与网络状态，解释 Codex 会话为什么看起来卡住。 | [⭐ 1](https://github.com/Gmasterzhangxinyang/codex-doctor/stargazers) |
| [Freyliu0516/Codex-Log-Doctor](https://github.com/Freyliu0516/Codex-Log-Doctor) | 在不读取对话内容的前提下，测量并控制 Codex SQLite 日志持续膨胀。 | [⭐ 1](https://github.com/Freyliu0516/Codex-Log-Doctor/stargazers) |
| [2395115107-stack/codex-history-doctor](https://github.com/2395115107-stack/codex-history-doctor) | 从本地 rollout 文件重建 session_index.jsonl 与 SQLite thread 记录，并先备份、对齐当前 Provider。 | [⭐ 1](https://github.com/2395115107-stack/codex-history-doctor/stargazers) |
| [Maverick04/codex-doctor](https://github.com/Maverick04/codex-doctor) | 读取会话遥测，定位上下文压力、重复工作、工具失败、活动停滞与 Token 增长。 | [⭐ 1](https://github.com/Maverick04/codex-doctor/stargazers) |
| [hj01857655/codex-doctor](https://github.com/hj01857655/codex-doctor) | 修复 rollout 文件、SQLite 索引、归档状态或模型 Provider 漂移导致的会话不可见；提供 CLI、GUI 与备份。 | [⭐ 1](https://github.com/hj01857655/codex-doctor/stargazers) |
| [RobertIonutF/codex-budget-doctor](https://github.com/RobertIonutF/codex-budget-doctor) | 以本地、隐私优先的方式定位 Codex 用量放大原因，并推荐更高效的模型配置档。 | [⭐ 0](https://github.com/RobertIonutF/codex-budget-doctor/stargazers) |
| [vik-codex/Doctor](https://github.com/vik-codex/Doctor) | 待核验的 HTML 项目；没有公开 README 或简介，尚无法确认其 Codex 诊断用途。 | [⭐ 0](https://github.com/vik-codex/Doctor/stargazers) |
| [yezhouyedu/codex-report-doctor](https://github.com/yezhouyedu/codex-report-doctor) | 把统计输出整理为证据充分、可辩护的研究报告；属于 Codex 质量邻近工作流。 | [⭐ 0](https://github.com/yezhouyedu/codex-report-doctor/stargazers) |
| [y3078266584/codex-plugin-doctor](https://github.com/y3078266584/codex-plugin-doctor) | 修复 Windows 上缺失或不可用的 openai-bundled Browser、Chrome 与 Computer Use 插件缓存。 | [⭐ 0](https://github.com/y3078266584/codex-plugin-doctor/stargazers) |
| [DWG7318/codex-network-doctor](https://github.com/DWG7318/codex-network-doctor) | 离线收集 Windows 网络证据，并修复影响 Codex 连接的 v2rayN TUN 链路。 | [⭐ 0](https://github.com/DWG7318/codex-network-doctor/stargazers) |
| [xiangyanghua-22/codex-hooks-doctor](https://github.com/xiangyanghua-22/codex-hooks-doctor) | 追踪 Codex Hooks 未触发的原因，定位触发条件或命令接线错误。 | [⭐ 0](https://github.com/xiangyanghua-22/codex-hooks-doctor/stargazers) |
| [Yaro-Tab/codex-windows-doctor](https://github.com/Yaro-Tab/codex-windows-doctor) | 对 Windows/WSL 的 Codex 安装、配置、权限与网络执行注重隐私的只读健康检查。 | [⭐ 0](https://github.com/Yaro-Tab/codex-windows-doctor/stargazers) |
| [momochoog/codex-workspace-doctor](https://github.com/momochoog/codex-workspace-doctor) | 只读统计 macOS 本地 Codex 工作区的磁盘占用，不执行删除。 | [⭐ 0](https://github.com/momochoog/codex-workspace-doctor/stargazers) |
| [wildbyteai/codex-provider-doctor](https://github.com/wildbyteai/codex-provider-doctor) | 只读诊断第三方模型 Provider 的配置、认证、插件与历史记录兼容性。 | [⭐ 0](https://github.com/wildbyteai/codex-provider-doctor/stargazers) |
| [YizeSun/codex-doctor](https://github.com/YizeSun/codex-doctor) | 解释 Codex 运行时磁盘占用，并为会话、缓存、Xcode 产物与 macOS 临时构建提供白名单清理。 | [⭐ 0](https://github.com/YizeSun/codex-doctor/stargazers) |
| [Lumidew/codex-doctor](https://github.com/Lumidew/codex-doctor) | 检查 Codex 原生配置卫生，并且只在获得批准后执行修复。 | [⭐ 0](https://github.com/Lumidew/codex-doctor/stargazers) |
| [BTCElectrician/codex-storage-doctor](https://github.com/BTCElectrician/codex-storage-doctor) | 诊断 Codex SQLite 诊断日志增长，并提供以保全数据为先、可逆的存储缓解措施。 | [⭐ 0](https://github.com/BTCElectrician/codex-storage-doctor/stargazers) |
| [gtrgear/codex-submission-doctor](https://github.com/gtrgear/codex-submission-doctor) | 为黑客松提交做本地、注重隐私的质量与打包预检；属于 Codex 诊断的邻近工作流。 | [⭐ 0](https://github.com/gtrgear/codex-submission-doctor/stargazers) |
| [luogangan7-lgtm/codex-mcp-doctor](https://github.com/luogangan7-lgtm/codex-mcp-doctor) | 像 npm doctor 一样检查 MCP Server，发现配置损坏、西里尔同形字攻击与可疑依赖变更。 | [⭐ 0](https://github.com/luogangan7-lgtm/codex-mcp-doctor/stargazers) |
| [configcrate/codex-session-doctor](https://github.com/configcrate/codex-session-doctor) | 只读检测体积过大或格式异常的本地 Codex Desktop 会话文件。 | [⭐ 0](https://github.com/configcrate/codex-session-doctor/stargazers) |
| [zjp1997720/codex-doctor](https://github.com/zjp1997720/codex-doctor) | 用只读证据检查审计 AGENTS.md、Skills、MCP、Hooks、配置、Provider 历史与 Git 卫生。 | [⭐ 0](https://github.com/zjp1997720/codex-doctor/stargazers) |
| [warren2008-2020-spec/codex-doctor](https://github.com/warren2008-2020-spec/codex-doctor) | 对 Windows、WSL、GitHub、npm、沙箱、代理与 CI 工作流做广覆盖只读安装诊断。 | [⭐ 0](https://github.com/warren2008-2020-spec/codex-doctor/stargazers) |
| [junchangzhu42-eng/codex-skill-doctor](https://github.com/junchangzhu42-eng/codex-skill-doctor) | 诊断并恢复 Windows 上缺失、损坏或无法被发现的 Codex Skill 安装。 | [⭐ 0](https://github.com/junchangzhu42-eng/codex-skill-doctor/stargazers) |
| [juzai0924-cloud/codex-reconnect-doctor](https://github.com/juzai0924-cloud/codex-reconnect-doctor) | 通过原生 macOS 菜单栏应用监控 Codex 重连行为与本地代理健康。 | [⭐ 0](https://github.com/juzai0924-cloud/codex-reconnect-doctor/stargazers) |
| [shixianli083-eng/codex-doctor](https://github.com/shixianli083-eng/codex-doctor) | 检查 macOS 上 Codex 及其周边 AI 开发环境的安装与依赖问题。 | [⭐ 0](https://github.com/shixianli083-eng/codex-doctor/stargazers) |
| [leiJack-lo/codex-local-doctor-skill](https://github.com/leiJack-lo/codex-local-doctor-skill) | 审计本地 Codex 日志、状态与 Git 健康问题，并在安全门控下提供小范围缓解措施。 | [⭐ 0](https://github.com/leiJack-lo/codex-local-doctor-skill/stargazers) |
| [ember056/codex_session_doctor](https://github.com/ember056/codex_session_doctor) | 恢复仍保存在磁盘上、但已从 Codex Desktop 侧边栏消失的会话。 | [⭐ 0](https://github.com/ember056/codex_session_doctor/stargazers) |
| [baixinpan/codex-reconnecting-doctor](https://github.com/baixinpan/codex-reconnecting-doctor) | 诊断并修复代理漂移或 WebSocket 传输配置导致的 Codex Desktop 反复重连。 | [⭐ 0](https://github.com/baixinpan/codex-reconnecting-doctor/stargazers) |
| [UPmeme/codex-windows-plugin-doctor](https://github.com/UPmeme/codex-windows-plugin-doctor) | 检查并修复 Windows 上影响 Computer Use、Chrome 与 Browser 插件的安装问题。 | [⭐ 0](https://github.com/UPmeme/codex-windows-plugin-doctor/stargazers) |
| [ironman429100-rgb/codex-token-doctor](https://github.com/ironman429100-rgb/codex-token-doctor) | 分析本地 Codex Token 事件，区分上下文、缓存、输出或长会话消耗，并按节省效果排序建议。 | [⭐ 0](https://github.com/ironman429100-rgb/codex-token-doctor/stargazers) |
| [ChenSir886/codex-context-doctor-cn](https://github.com/ChenSir886/codex-context-doctor-cn) | 中文体检 Codex 上下文配置，重点检查自动压缩阈值与模型上下文窗口。 | [⭐ 0](https://github.com/ChenSir886/codex-context-doctor-cn/stargazers) |
| [Nitmi/codex-session-doctor](https://github.com/Nitmi/codex-session-doctor) | 修复 Windows Codex Desktop 因会话数据残留 Git 标记而发生的渲染崩溃。 | [⭐ 0](https://github.com/Nitmi/codex-session-doctor/stargazers) |
| [daniel-p-green/codex-skill_secret-agents-dot-md-doctor](https://github.com/daniel-p-green/codex-skill_secret-agents-dot-md-doctor) | 依据仓库本地证据和当前 Codex 指南，起草精简且针对本项目的 AGENTS.md。 | [⭐ 0](https://github.com/daniel-p-green/codex-skill_secret-agents-dot-md-doctor/stargazers) |
| [warwickmei/codex-skill-doctor](https://github.com/warwickmei/codex-skill-doctor) | 用本地验证 CLI 检查 Codex Skill wrapper 是否安装正确、调用链是否接通。 | [⭐ 0](https://github.com/warwickmei/codex-skill-doctor/stargazers) |

<!-- catalog-zh:end -->

## 仓库自带 Skills

| Skill | 用途 |
|---|---|
| [`$codex-doctor`](skills/codex-doctor/SKILL.md) | 先定义 Codex 问题，优先搜索本地证据和本目录，再核验官方与社区来源，最后按风险给出诊断路线。 |
| [`$update-awesome-codex-doctors`](skills/update-awesome-codex-doctors/SKILL.md) | 发现、核验、分类、生成并审计目录变更，让贡献达到可审查、可合并状态。 |

可以把任一目录作为普通 Codex Skill 安装，也可以在能够发现仓库 Skills 的工作副本中直接使用。诊断 Skill 默认只读；维护 Skill 默认只修改本目录，不会擅自提交、推送或合并。

## 收录范围

项目必须能够诊断、解释、监控、修复或安全缓解 OpenAI Codex 的问题。内置命令、CLI、GUI、Skill 和 Plugin 都可以收录。仅仅使用 Codex 开发的医疗应用、测试仓库，以及只因作者用户名带有 doctor 而命中的项目不收录。

每条记录都会标注专科和范围。只读诊断、修复与清理属于不同风险等级；被收录不代表得到背书。

## 仓库介绍与关键词

**GitHub 简介：**

> 收集、分类并持续验证 Codex 诊断、修复、恢复与可观测性工具。

**建议 Topics：**

`awesome-list` · `codex` · `codex-cli` · `codex-doctor` · `openai-codex` · `codex-skills` · `agent-skills` · `plugins` · `diagnostics` · `troubleshooting` · `repair` · `recovery` · `observability` · `developer-tools`

## 数据与更新

当前数据快照位于 [`data/github-snapshot.json`](data/github-snapshot.json)，机器可读导出位于 [`data/catalog.json`](data/catalog.json)。运行：

```bash
python scripts/discover.py
python scripts/render.py
python scripts/render.py --check
```

`discover.py` 用于拉取待人工复核候选，`render.py` 重新生成目录/曲线/导出，`--check` 供 CI 检查生成文件是否过期。

## 免责声明

这是独立的社区目录，与 OpenAI 无隶属或背书关系。允许任何第三方 Doctor 修改 `~/.codex` 或其他本地状态前，请先阅读代码并确认备份。

## 许可证

CC0-1.0。项目描述和链接指向的源代码仍适用各自原始许可证。
