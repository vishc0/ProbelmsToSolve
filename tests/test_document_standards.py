from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "check_markdown_size", REPOSITORY_ROOT / "tooling" / "check_markdown_size.py"
)
assert SPEC and SPEC.loader
check_markdown_size = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(check_markdown_size)


class DocumentStandardTests(unittest.TestCase):
    def test_markdown_files_stay_within_fixed_limit(self) -> None:
        self.assertEqual(check_markdown_size.oversized_files(REPOSITORY_ROOT), [])


if __name__ == "__main__":
    unittest.main()
