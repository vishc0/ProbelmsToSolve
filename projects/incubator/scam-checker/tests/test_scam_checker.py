"""
Unit tests for Scam Checker
"""

import sys
import unittest
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(SRC_DIR))

from scam_checker import check_message


class TestScamChecker(unittest.TestCase):
    def test_delivery_scam(self):
        sample = "USPS: Your parcel cannot be delivered. Click here within 12 hours: http://usps-track.info"
        report = check_message(sample)
        self.assertEqual(report.risk_level, "High")
        self.assertTrue(any("delivery" in f.lower() for f in report.red_flags))
        self.assertTrue(any("urgency" in f.lower() for f in report.red_flags))

    def test_gift_card_demand(self):
        sample = "Please purchase a $500 Apple gift card and send the code to pay your back taxes."
        report = check_message(sample)
        self.assertEqual(report.risk_level, "High")
        self.assertTrue(any("gift card" in f.lower() for f in report.red_flags))

    def test_benign_message(self):
        sample = "Hey Mom, just letting you know we are having dinner at 6pm tonight. See you soon!"
        report = check_message(sample)
        self.assertEqual(report.risk_level, "Low")
        self.assertEqual(len(report.red_flags), 0)


if __name__ == "__main__":
    unittest.main()
