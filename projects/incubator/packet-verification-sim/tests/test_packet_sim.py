"""
Unit tests for Packet Verification Simulator
Verifies mathematical bounds and Monte Carlo convergence.
Compatible with standard unittest and pytest.
"""

import math
import sys
import unittest
from pathlib import Path

# Add src to path
SRC_DIR = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(SRC_DIR))

from packet_sim import (
    exact_detection_probability,
    required_fake_packets_for_confidence,
    run_monte_carlo_audit,
    theoretical_detection_probability,
)


class TestPacketVerification(unittest.TestCase):
    def test_required_packets_99_percent_confidence(self):
        """Verify that a 1% budget requires ~461 fake packets to reach 99% detection."""
        budget = 0.01
        target = 0.99
        required = required_fake_packets_for_confidence(target, budget)
        self.assertEqual(required, 461)
        prob = theoretical_detection_probability(budget, required)
        self.assertGreaterEqual(prob, 0.99)

    def test_zero_budget_and_zero_fakes(self):
        """Verify boundary conditions for zero fake packets or zero budget."""
        self.assertEqual(theoretical_detection_probability(0.0, 100), 0.0)
        self.assertEqual(theoretical_detection_probability(0.01, 0), 0.0)
        self.assertEqual(exact_detection_probability(0.0, 100), 0.0)
        self.assertEqual(exact_detection_probability(0.01, 0), 0.0)

    def test_monte_carlo_convergence(self):
        """
        Test that Monte Carlo simulation matches theoretical bounds within statistical margin.
        Using total_packets=5000, fake_packets=50, budget=0.05.
        Theoretical: 1 - exp(-0.05 * 50) = 1 - exp(-2.5) ~= 0.9179.
        """
        total = 5_000
        fakes = 50
        budget = 0.05
        trials = 300

        metrics = run_monte_carlo_audit(
            total_packets=total,
            fake_packets=fakes,
            recomputation_budget=budget,
            trials=trials,
            seed=123,
        )

        expected_p = theoretical_detection_probability(budget, fakes)
        self.assertTrue(math.isclose(metrics.theoretical_poisson_p, expected_p, rel_tol=1e-5))
        self.assertLess(abs(metrics.empirical_p - expected_p), 0.05)


if __name__ == "__main__":
    unittest.main()
