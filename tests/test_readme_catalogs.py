from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def generated_block(path: Path, start: str, end: str) -> str:
    text = path.read_text(encoding="utf-8")
    return text.split(start, 1)[1].split(end, 1)[0]


class ReadmeCatalogTests(unittest.TestCase):
    def test_both_readmes_embed_every_project(self) -> None:
        data = json.loads((ROOT / "data" / "github-snapshot.json").read_text(encoding="utf-8"))
        blocks = [
            (
                generated_block(ROOT / "README.md", "<!-- catalog-en:start -->", "<!-- catalog-en:end -->"),
                "| Project | What it does | Stars |",
                "description",
            ),
            (
                generated_block(ROOT / "README.zh-CN.md", "<!-- catalog-zh:start -->", "<!-- catalog-zh:end -->"),
                "| 项目 | 能做什么 | Stars |",
                "description_zh",
            ),
        ]
        for block, header, description_field in blocks:
            self.assertIn(header, block)
            rows = [line for line in block.splitlines() if line.startswith("| [")]
            self.assertEqual(len(rows), len(data["projects"]))
            self.assertTrue(all(row.count("|") == 4 for row in rows))
            for project in data["projects"]:
                self.assertIn(f"[{project['full_name']}]({project['url']})", block)
                self.assertIn(project[description_field], block)
                self.assertIn(f"[⭐ {project['stars']}]({project['url']}/stargazers)", block)


if __name__ == "__main__":
    unittest.main()
