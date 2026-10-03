"""
Unit tests for Scenario Scrutiny Engine
"""

import sys
import unittest
from pathlib import Path

# Add src to path
SRC_DIR = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(SRC_DIR))

from scrutinizer import ClaimType, ProvenanceType, ScenarioScrutinizer


class TestScenarioScrutinizer(unittest.TestCase):
    def setUp(self):
        self.scrutinizer = ScenarioScrutinizer(default_source_id="test-source")

    def test_metric_extraction(self):
        text = "A 100 MW datacenter requires circulating 2.4 m3/s of cooling water to maintain safe thermal thresholds."
        claims = self.scrutinizer.parse_document(text, "test-doc")
        self.assertEqual(len(claims), 1)
        self.assertEqual(claims[0].claim_type, ClaimType.METRIC)
        self.assertIn("100 MW", claims[0].extracted_quantities)

    def test_assumption_tagging(self):
        text = "Assuming that global compute stocks grow by 3x annually, the verifier must expand audit throughput."
        claims = self.scrutinizer.parse_document(text, "test-doc")
        self.assertEqual(len(claims), 1)
        self.assertEqual(claims[0].claim_type, ClaimType.ASSUMPTION)

    def test_constraint_tagging(self):
        text = "Frontier model training must be prohibited without an active hardware packet tap."
        claims = self.scrutinizer.parse_document(text, "test-doc")
        self.assertEqual(len(claims), 1)
        self.assertEqual(claims[0].claim_type, ClaimType.CONSTRAINT)

    def test_provenance_defaults(self):
        text = "Plan A delays superintelligence until 2040."
        claims = self.scrutinizer.parse_document(text, "test-doc")
        self.assertEqual(len(claims), 1)
        self.assertEqual(claims[0].provenance, ProvenanceType.SOURCE_CLAIM)
        self.assertTrue(claims[0].claim_id.startswith("test-doc-c"))


if __name__ == "__main__":
    unittest.main()
