#!/usr/bin/env python3
"""Render the catalog and community-growth chart from the GitHub snapshot."""

from __future__ import annotations

import argparse
import html
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "github-snapshot.json"
CHART_PATH = ROOT / "assets" / "community-growth.svg"
CATALOG_PATH = ROOT / "CATALOG.md"
DATA_EXPORT_PATH = ROOT / "data" / "catalog.json"
README_PATH = ROOT / "README.md"
README_ZH_PATH = ROOT / "README.zh-CN.md"
OFFICIAL_DOCTOR_RELEASE = datetime(2026, 5, 18, tzinfo=timezone.utc)


SPECIALTY_ZH = {
    "agents-md": "AGENTS.md",
    "authentication": "认证",
    "configuration": "配置",
    "context": "上下文",
    "context-and-tokens": "上下文与 Token",
    "desktop-plugin-repair": "Desktop 插件修复",
    "desktop-repair": "Desktop 修复",
    "environment": "环境",
    "history": "历史记录",
    "hooks": "Hooks",
    "local-state": "本地状态",
    "logs": "日志",
    "macos-environment": "macOS 环境",
    "mcp": "MCP",
    "model-provider": "模型 Provider",
    "network": "网络",
    "performance": "性能",
    "plugin-validation": "插件验证",
    "reconnect": "重连",
    "report-quality": "报告质量",
    "runtime-storage": "运行时存储",
    "session-health": "会话健康",
    "session-integrity": "会话完整性",
    "session-observability": "会话可观测性",
    "session-recovery": "会话恢复",
    "session-repair": "会话修复",
    "setup": "安装与配置",
    "skill-diagnostics": "Skill 诊断",
    "skill-recovery": "Skill 恢复",
    "sqlite-storage": "SQLite 存储",
    "submission-preflight": "提交预检",
    "unknown": "待确认",
    "usage-and-budget": "用量与预算",
    "windows": "Windows",
    "workspace-configuration": "工作区配置",
    "workspace-storage": "工作区存储",
}


def load_data() -> dict:
    return json.loads(DATA_PATH.read_text(encoding="utf-8"))


def parse_date(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def human_specialty(value: str) -> str:
    return value.replace("-", " ").title()


def markdown_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


def has_cjk(value: str) -> bool:
    return any("\u4e00" <= char <= "\u9fff" for char in value)


def render_focus(project: dict, *, chinese: bool = False) -> str:
    focus = markdown_cell(project["description"])
    if not chinese:
        return focus
    if focus and has_cjk(focus):
        return focus
    specialty = SPECIALTY_ZH.get(project["specialty"], project["specialty"])
    action_map = {
        "read-only": "只读诊断",
        "repair": "诊断与修复",
        "cleanup": "诊断与清理",
        "unknown": "诊断",
    }
    action = action_map[project["state_change_risk"]]
    tool_form = "Skill/插件" if project["skill_or_plugin"] else "工具"
    return f"面向{specialty}问题的{action}{tool_form}，用于定位根因并提供处理路径。"


def sorted_projects(data: dict) -> list[dict]:
    return sorted(
        data["projects"],
        key=lambda project: (
            -(project["stars"]),
            -parse_date(project["pushed_at"]).timestamp(),
            project["full_name"].lower(),
        ),
    )


def top_specialties(data: dict, *, limit: int = 8) -> list[str]:
    counts: dict[str, int] = defaultdict(int)
    for project in data["projects"]:
        if project["scope"] == "core":
            counts[project["specialty"]] += 1
    return sorted(counts, key=lambda item: (-counts[item], item))[:limit]


def render_specialty_links(data: dict, *, chinese: bool = False) -> str:
    lines = []
    for specialty in top_specialties(data):
        members = [
            project for project in sorted_projects(data)
            if project["scope"] == "core" and project["specialty"] == specialty
        ][:3]
        label = SPECIALTY_ZH.get(specialty, specialty) if chinese else human_specialty(specialty)
        refs = "、".join(f"[{project['full_name']}]({project['url']})" for project in members) if chinese else ", ".join(
            f"[{project['full_name']}]({project['url']})" for project in members
        )
        suffix = " 等" if chinese else " and more"
        lines.append(f"- **{label}**: {refs}{suffix}")
    return "\n".join(lines)


def export_catalog_data(data: dict) -> dict:
    return {
        "generated_at": data["generated_at"],
        "counts": data["counts"],
        "projects": sorted_projects(data),
    }


def render_catalog_table(data: dict, *, chinese: bool = False) -> str:
    if chinese:
        lines = [
            "| 项目 | 关注点 | 创建日期 | Stars | 最后提交 |",
            "|---|---|---:|---:|---:|",
        ]
    else:
        lines = [
            "| Project | Focus | Created | Stars | Last push |",
            "|---|---|---:|---:|---:|",
        ]

    for project in sorted_projects(data):
        created = parse_date(project["created_at"]).date().isoformat()
        pushed = parse_date(project["pushed_at"]).date().isoformat()
        focus = render_focus(project, chinese=chinese)
        lines.append(
            "| "
            f"[{project['full_name']}]({project['url']}) | {focus} | {created} | {project['stars']} | {pushed} |"
        )
    return "\n".join(lines)


def render_catalog(data: dict) -> str:
    lines = [
        "# Catalog",
        "",
        (
            f"> Snapshot: **{data['generated_at']}** · "
            f"**{data['counts']['core']} core** · "
            f"**{data['counts']['adjacent']} adjacent** · "
            f"**{data['counts']['unverified']} unverified** · "
            f"**{data['counts']['skill_or_plugin']} skills/plugins**"
        ),
        "",
        "Stars and activity dates are discovery signals, not quality endorsements.",
        "",
        render_catalog_table(data),
    ]
    lines.extend(
        [
            "",
            "See [METHODOLOGY.md](METHODOLOGY.md) for inclusion and chart rules.",
            "",
        ]
    )
    return "\n".join(lines)


def render_catalog_json(data: dict) -> str:
    return json.dumps(export_catalog_data(data), ensure_ascii=False, indent=2)


def inject_generated_block(document: str, start: str, end: str, content: str, *, label: str) -> str:
    if document.count(start) != 1 or document.count(end) != 1:
        raise ValueError(f"{label} must contain exactly one {start!r} and {end!r}")
    before, remainder = document.split(start, 1)
    _, after = remainder.split(end, 1)
    return f"{before}{start}\n\n{content.rstrip()}\n\n{end}{after}"


def step_points(projects: list[dict], predicate, start: datetime, end: datetime):
    counts = defaultdict(int)
    for project in projects:
        if predicate(project):
            counts[parse_date(project["created_at"]).date()] += 1
    total = 0
    points = [(start, 0)]
    for day in sorted(counts):
        moment = datetime(day.year, day.month, day.day, tzinfo=timezone.utc)
        points.append((moment, total))
        total += counts[day]
        points.append((moment, total))
    points.append((end, total))
    return points


def render_chart(data: dict) -> str:
    projects = data["projects"]
    start = datetime(2026, 3, 1, tzinfo=timezone.utc)
    end = datetime.fromisoformat(data["generated_at"]).replace(tzinfo=timezone.utc)
    width, height = 960, 500
    left, right, top, bottom = 72, 910, 105, 405
    y_max = 45

    def x(moment: datetime) -> float:
        return left + (moment - start).total_seconds() / (end - start).total_seconds() * (right - left)

    def y(value: int) -> float:
        return bottom - value / y_max * (bottom - top)

    def path(points) -> str:
        return " ".join(
            ("M" if index == 0 else "L") + f" {x(moment):.1f} {y(value):.1f}"
            for index, (moment, value) in enumerate(points)
        )

    all_points = step_points(projects, lambda _: True, start, end)
    skill_points = step_points(projects, lambda project: project["skill_or_plugin"], start, end)
    all_total = all_points[-1][1]
    skill_total = skill_points[-1][1]
    pre_official = sum(parse_date(project["created_at"]) < OFFICIAL_DOCTOR_RELEASE for project in projects)
    after_official = all_total - pre_official

    month_ticks = [
        datetime(2026, month, 1, tzinfo=timezone.utc)
        for month in range(3, 9)
    ]
    y_ticks = [0, 10, 20, 30, 40]
    official_x = x(OFFICIAL_DOCTOR_RELEASE)

    grid = []
    for tick in y_ticks:
        grid.append(
            f'<line class="grid" x1="{left}" y1="{y(tick):.1f}" x2="{right}" y2="{y(tick):.1f}" />'
        )
        grid.append(
            f'<text class="axis" x="{left - 12}" y="{y(tick) + 4:.1f}" text-anchor="end">{tick}</text>'
        )
    for tick in month_ticks:
        grid.append(
            f'<text class="axis" x="{x(tick):.1f}" y="{bottom + 25}" text-anchor="middle">{tick:%b}</text>'
        )

    escaped_snapshot = html.escape(data["generated_at"])
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
  <title id="title">The Codex Doctor community is accelerating</title>
  <desc id="desc">Cumulative public Codex Doctor projects increased from one in March 2026 to {all_total} by {escaped_snapshot}. {skill_total} are skills or plugins. {after_official} projects were created after the official doctor command shipped.</desc>
  <style>
    .bg {{ fill: #f6f8fa; }}
    .frame {{ fill: #ffffff; stroke: #d0d7de; }}
    .title {{ fill: #1f2328; font: 600 23px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }}
    .subtitle, .axis, .note {{ fill: #57606a; font: 13px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }}
    .axis-title {{ fill: #1f2328; font: 14px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }}
    .grid {{ stroke: #d8dee4; stroke-width: 1; }}
    .all {{ fill: none; stroke: #0969da; stroke-width: 4; stroke-linejoin: round; }}
    .skills {{ fill: none; stroke: #1a7f37; stroke-width: 4; stroke-linejoin: round; }}
    .marker {{ stroke: #bf8700; stroke-width: 2; stroke-dasharray: 6 5; }}
    .marker-label {{ fill: #9a6700; font: 600 12px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }}
    .all-label {{ fill: #0969da; font: 600 14px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }}
    .skills-label {{ fill: #1a7f37; font: 600 14px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }}
    @media (prefers-color-scheme: dark) {{
      .bg {{ fill: #0d1117; }} .frame {{ fill: #161b22; stroke: #30363d; }}
      .title, .axis-title {{ fill: #f0f6fc; }} .subtitle, .axis, .note {{ fill: #8b949e; }}
      .grid {{ stroke: #30363d; }} .all {{ stroke: #58a6ff; }} .skills {{ stroke: #3fb950; }}
      .all-label {{ fill: #58a6ff; }} .skills-label {{ fill: #3fb950; }}
      .marker {{ stroke: #d29922; }} .marker-label {{ fill: #e3b341; }}
    }}
  </style>
  <rect class="bg" width="{width}" height="{height}" rx="12" />
  <text class="title" x="32" y="38">The Codex Doctor community is accelerating</text>
  <text class="subtitle" x="32" y="62">{all_total} curated projects · {skill_total} skills/plugins · repository creation dates through {escaped_snapshot}</text>
  <rect class="frame" x="{left}" y="{top}" width="{right-left}" height="{bottom-top}" rx="4" />
  {''.join(grid)}
  <line class="marker" x1="{official_x:.1f}" y1="{top}" x2="{official_x:.1f}" y2="{bottom}" />
  <text class="marker-label" x="{official_x + 8:.1f}" y="{top + 18}">Official codex doctor ships</text>
  <text class="marker-label" x="{official_x + 8:.1f}" y="{top + 34}">CLI v0.131.0 · 18 May</text>
  <path class="all" d="{path(all_points)}" />
  <path class="skills" d="{path(skill_points)}" />
  <circle cx="{x(end):.1f}" cy="{y(all_total):.1f}" r="5" fill="#0969da" />
  <circle cx="{x(end):.1f}" cy="{y(skill_total):.1f}" r="5" fill="#1a7f37" />
  <text class="all-label" x="{right - 10}" y="{y(all_total) - 12:.1f}" text-anchor="end">{all_total} all projects</text>
  <text class="skills-label" x="{right - 10}" y="{y(skill_total) - 12:.1f}" text-anchor="end">{skill_total} skills / plugins</text>
  <text class="axis-title" x="{(left+right)/2:.1f}" y="{bottom+53}" text-anchor="middle">Repository creation date (2026)</text>
  <text class="axis-title" transform="translate(24 {(top+bottom)/2:.1f}) rotate(-90)" text-anchor="middle">Cumulative public projects</text>
  <text class="note" x="{left}" y="{height-18}">{after_official} of {all_total} curated projects appeared after the official command shipped. Source: GitHub Search API + manual review.</text>
</svg>
'''


def write_or_check(path: Path, content: str, check: bool) -> bool:
    normalized = content.rstrip() + "\n"
    if check:
        current = path.read_text(encoding="utf-8") if path.exists() else ""
        if current != normalized:
            print(f"out of date: {path.relative_to(ROOT)}", file=sys.stderr)
            return False
        return True
    path.write_text(normalized, encoding="utf-8", newline="\n")
    print(f"wrote {path.relative_to(ROOT)}")
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if generated files are stale")
    args = parser.parse_args()
    data = load_data()
    ok = write_or_check(CATALOG_PATH, render_catalog(data), args.check)
    ok = write_or_check(DATA_EXPORT_PATH, render_catalog_json(data), args.check) and ok
    ok = write_or_check(CHART_PATH, render_chart(data), args.check) and ok
    readme = README_PATH.read_text(encoding="utf-8")
    readme = inject_generated_block(
        readme,
        "<!-- quick-links-en:start -->",
        "<!-- quick-links-en:end -->",
        render_specialty_links(data),
        label=README_PATH.name,
    )
    readme = inject_generated_block(
        readme,
        "<!-- catalog-en:start -->",
        "<!-- catalog-en:end -->",
        render_catalog_table(data),
        label=README_PATH.name,
    )
    ok = write_or_check(README_PATH, readme, args.check) and ok
    readme_zh = README_ZH_PATH.read_text(encoding="utf-8")
    readme_zh = inject_generated_block(
        readme_zh,
        "<!-- quick-links-zh:start -->",
        "<!-- quick-links-zh:end -->",
        render_specialty_links(data, chinese=True),
        label=README_ZH_PATH.name,
    )
    readme_zh = inject_generated_block(
        readme_zh,
        "<!-- catalog-zh:start -->",
        "<!-- catalog-zh:end -->",
        render_catalog_table(data, chinese=True),
        label=README_ZH_PATH.name,
    )
    ok = write_or_check(README_ZH_PATH, readme_zh, args.check) and ok
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
