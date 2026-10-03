"""
Unit tests for Letter Explainer
"""

import sys
import unittest
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(SRC_DIR))

from letter_explainer import analyze_letter


class TestLetterExplainer(unittest.TestCase):
    def test_rental_notice(self):
        sample = "Dear Tenant, your rent of $1,200.00 is due on October 1, 2026. Please remit promptly."
        result = analyze_letter(sample, sender_name="Landlord Management")
        self.assertIn("housing / rental notice", result.summary)
        self.assertIn("$1,200.00", result.amounts_owed)
        self.assertTrue(len(result.deadlines) >= 1)
        self.assertIn("Landlord Management", result.draft_reply)

    def test_insurance_denial(self):
        sample = "Notice of Claim Denial: Your recent medical claim #49281 has been denied under policy section 4B."
        result = analyze_letter(sample)
        self.assertIn("insurance letter", result.summary)
        self.assertIn("appeal", result.action_required)


if __name__ == "__main__":
    unittest.main()
