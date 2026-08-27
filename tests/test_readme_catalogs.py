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
            generated_block(ROOT / "README.md", "<!-- catalog-en:start -->", "<!-- catalog-en:end -->"),
            generated_block(ROOT / "README.zh-CN.md", "<!-- catalog-zh:start -->", "<!-- catalog-zh:end -->"),
        ]
        for block in blocks:
            rows = [line for line in block.splitlines() if line.startswith("| [")]
            self.assertEqual(len(rows), len(data["projects"]))
            for project in data["projects"]:
                self.assertIn(f"[{project['full_name']}]({project['url']})", block)


if __name__ == "__main__":
    unittest.main()

