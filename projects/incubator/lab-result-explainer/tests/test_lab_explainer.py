"""
Unit tests for Lab Result Explainer
"""

import sys
import unittest
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(SRC_DIR))

from lab_explainer import evaluate_result


class TestLabExplainer(unittest.TestCase):
    def test_glucose_high(self):
        result = evaluate_result("Fasting Glucose", 110.0)
        self.assertEqual(result["status"], "Higher than typical range")
        self.assertIn("energy and sugar levels", result["plain_english"])
        self.assertEqual(len(result["questions_for_doctor"]), 3)

    def test_glucose_normal(self):
        result = evaluate_result("Fasting Glucose", 88.0)
        self.assertEqual(result["status"], "Within standard healthy range")

    def test_unknown_test(self):
        result = evaluate_result("Obscure Enzyme XYZ", 42.0)
        self.assertEqual(result["status"], "Unknown Test")


if __name__ == "__main__":
    unittest.main()
