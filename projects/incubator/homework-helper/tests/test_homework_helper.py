"""
Unit tests for Homework Helper
"""

import sys
import unittest
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(SRC_DIR))

from homework_helper import get_homework_help


class TestHomeworkHelper(unittest.TestCase):
    def test_negative_numbers(self):
        result = get_homework_help("negative numbers", "-3 - (-7)")
        self.assertEqual(result.topic, "Negative Numbers")
        self.assertIn("two negatives cancel", result.parent_refresher)
        self.assertTrue(len(result.guided_hint) > 10)

    def test_fractions(self):
        result = get_homework_help("fractions", "1/3 + 2/5")
        self.assertEqual(result.topic, "Fractions")
        self.assertIn("denominators", result.parent_refresher)
        self.assertIn("must match", result.parent_refresher)


if __name__ == "__main__":
    unittest.main()
