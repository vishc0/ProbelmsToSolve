"""
Unit tests for Quick Invoice Generator
"""

import sys
import unittest
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(SRC_DIR))

from quick_invoice import format_invoice_text, parse_job_notes


class TestQuickInvoice(unittest.TestCase):
    def test_invoice_parsing(self):
        sample = "Deck repair for Sarah Jenkins. 3 hours at $60/hr. Replaced boards for $45.00."
        inv = parse_job_notes(sample)
        self.assertEqual(inv.client_name, "Sarah Jenkins")
        # Labor: 3 * 60 = 180. Materials: 45. Total: 225.
        self.assertEqual(inv.subtotal, 225.0)
        self.assertEqual(inv.grand_total, 225.0)
        text = format_invoice_text(inv)
        self.assertIn("TOTAL DUE:", text)
        self.assertIn("Sarah Jenkins", text)


if __name__ == "__main__":
    unittest.main()
