from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "skills" / "update-awesome-codex-doctors" / "scripts" / "audit_catalog.py"
SPEC = importlib.util.spec_from_file_location("audit_catalog", MODULE_PATH)
assert SPEC and SPEC.loader
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class CatalogAuditTests(unittest.TestCase):
    def test_current_catalog_passes(self) -> None:
        self.assertEqual(AUDIT.audit(ROOT), [])

    def test_duplicate_repository_is_rejected(self) -> None:
        source = json.loads((ROOT / "data" / "github-snapshot.json").read_text(encoding="utf-8"))
        broken = copy.deepcopy(source)
        broken["projects"].append(copy.deepcopy(broken["projects"][-1]))
        errors = AUDIT.audit(ROOT, data_override=broken)
        self.assertTrue(any("duplicate full_name" in error for error in errors), errors)
        self.assertTrue(any("counts.core" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
