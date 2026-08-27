from __future__ import annotations

import importlib.util
import json
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RENDER_PATH = ROOT / "scripts" / "render.py"
SPEC = importlib.util.spec_from_file_location("render", RENDER_PATH)
assert SPEC and SPEC.loader
RENDER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(RENDER)


def generated_block(path: Path, start: str, end: str) -> str:
    text = path.read_text(encoding="utf-8")
    return text.split(start, 1)[1].split(end, 1)[0].strip()


class SemanticConsistencyTests(unittest.TestCase):
    def setUp(self) -> None:
        self.snapshot = json.loads((ROOT / "data" / "github-snapshot.json").read_text(encoding="utf-8"))

    def test_specialty_translation_mapping_covers_snapshot(self) -> None:
        specialties = {project["specialty"] for project in self.snapshot["projects"]}
        missing = specialties - set(RENDER.SPECIALTY_ZH)
        self.assertEqual(missing, set())

    def test_counts_match_grouped_projects(self) -> None:
        derived = Counter(project["scope"] for project in self.snapshot["projects"])
        derived["skill_or_plugin"] = sum(project["skill_or_plugin"] for project in self.snapshot["projects"])
        for key in ("core", "adjacent", "unverified", "skill_or_plugin"):
            self.assertEqual(self.snapshot["counts"][key], derived[key])

    def test_projects_are_chronological(self) -> None:
        created_at = [project["created_at"] for project in self.snapshot["projects"]]
        self.assertEqual(created_at, sorted(created_at))

    def test_catalog_json_matches_render_export(self) -> None:
        expected = RENDER.export_catalog_data(self.snapshot)
        current = json.loads((ROOT / "data" / "catalog.json").read_text(encoding="utf-8"))
        self.assertEqual(current, expected)

    def test_navigation_blocks_not_empty(self) -> None:
        self.assertIn("- **", generated_block(ROOT / "README.md", "<!-- quick-links-en:start -->", "<!-- quick-links-en:end -->"))
        self.assertIn("- **", generated_block(ROOT / "README.zh-CN.md", "<!-- quick-links-zh:start -->", "<!-- quick-links-zh:end -->"))


if __name__ == "__main__":
    unittest.main()
