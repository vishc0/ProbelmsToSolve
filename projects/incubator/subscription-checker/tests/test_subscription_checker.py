"""
Unit tests for Subscription Checker
"""

import sys
import unittest
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(SRC_DIR))

from subscription_checker import analyze_statement_csv


class TestSubscriptionChecker(unittest.TestCase):
    def test_recurring_and_hike_detection(self):
        sample_csv = (
            "Date,Description,Amount\n"
            "2026-07-01,Cloud Storage,9.99\n"
            "2026-08-01,Cloud Storage,9.99\n"
            "2026-09-01,Cloud Storage,12.99\n"
            "2026-08-15,One-time Gas,45.00\n"
        )
        items, total = analyze_statement_csv(sample_csv)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].merchant, "Cloud Storage")
        self.assertEqual(items[0].occurrences, 3)
        self.assertTrue(items[0].price_increased)
        self.assertAlmostEqual(items[0].price_change, 3.00)
        self.assertAlmostEqual(total, 12.99)


if __name__ == "__main__":
    unittest.main()
