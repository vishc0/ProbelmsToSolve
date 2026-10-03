"""
Packet Verification Simulator
=============================
Simulates packet-based random recomputation auditing for datacenter compute workloads.
Implements the verification framework and statistical bounds from AI 2040: Plan A.
"""

from __future__ import annotations

import argparse
import math
import random
from typing import NamedTuple


class VerificationMetrics(NamedTuple):
    total_packets: int
    fake_packets: int
    recomputation_budget: float
    theoretical_poisson_p: float
    exact_independent_p: float
    empirical_p: float
    trials: int


def theoretical_detection_probability(recomputation_budget: float, n_fake_packets: int) -> float:
    """Calculate P(detected) using the Poisson approximation: 1 - exp(-C * N_fake)."""
    if recomputation_budget <= 0 or n_fake_packets <= 0:
        return 0.0
    return 1.0 - math.exp(-recomputation_budget * n_fake_packets)


def exact_detection_probability(recomputation_budget: float, n_fake_packets: int) -> float:
    """Calculate P(detected) under independent sampling: 1 - (1 - C)^N_fake."""
    if recomputation_budget <= 0 or n_fake_packets <= 0:
        return 0.0
    if recomputation_budget >= 1.0:
        return 1.0
    return 1.0 - math.pow(1.0 - recomputation_budget, n_fake_packets)


def required_fake_packets_for_confidence(target_confidence: float, recomputation_budget: float) -> int:
    """Calculate minimum N_fake required to achieve target confidence (e.g. 0.99) at budget C."""
    if target_confidence <= 0 or target_confidence >= 1.0:
        raise ValueError("Target confidence must be in (0, 1).")
    if recomputation_budget <= 0 or recomputation_budget > 1.0:
        raise ValueError("Recomputation budget must be in (0, 1].")
    return math.ceil(-math.log(1.0 - target_confidence) / recomputation_budget)


def run_monte_carlo_audit(
    total_packets: int,
    fake_packets: int,
    recomputation_budget: float,
    trials: int = 1000,
    seed: int | None = 42,
) -> VerificationMetrics:
    """
    Run Monte Carlo trials of packet-based verification sampling without replacement.
    """
    if seed is not None:
        random.seed(seed)

    if fake_packets > total_packets:
        raise ValueError("fake_packets cannot exceed total_packets.")

    n_verified = int(total_packets * recomputation_budget)
    n_verified = max(1, min(total_packets, n_verified))

    # Fast hyper-geometric simulation over trials:
    # Instead of shuffling full arrays, sample whether an audited sample hits any fake packet.
    caught_count = 0
    for _ in range(trials):
        # Sample n_verified items from population without replacement
        # Probability of 0 fakes drawn in n_verified draws from total_packets containing fake_packets:
        # P(0 caught) = prod_{i=0}^{n_verified-1} (total_packets - fake_packets - i) / (total_packets - i)
        # Or simulate direct draw indices:
        drawn_fakes = 0
        # If fake_packets is modest, we check if any of the fake packet IDs fall within the audited set
        audited_indices = set(random.sample(range(total_packets), n_verified))
        for fake_idx in range(fake_packets):
            if fake_idx in audited_indices:
                drawn_fakes += 1
                break
        if drawn_fakes > 0:
            caught_count += 1

    empirical_p = caught_count / trials
    poisson_p = theoretical_detection_probability(recomputation_budget, fake_packets)
    exact_p = exact_detection_probability(recomputation_budget, fake_packets)

    return VerificationMetrics(
        total_packets=total_packets,
        fake_packets=fake_packets,
        recomputation_budget=recomputation_budget,
        theoretical_poisson_p=poisson_p,
        exact_independent_p=exact_p,
        empirical_p=empirical_p,
        trials=trials,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Packet Verification Simulator (AI 2040: Plan A)")
    parser.add_argument("--total-packets", type=int, default=100_000, help="Total packets in workload")
    parser.add_argument("--fake-packets", type=int, default=460, help="Rogue/fake packets injected")
    parser.add_argument("--budget", type=float, default=0.01, help="Recomputation budget (0.01 = 1%)")
    parser.add_argument("--trials", type=int, default=1000, help="Monte Carlo trial count")
    args = parser.parse_args()

    metrics = run_monte_carlo_audit(
        total_packets=args.total_packets,
        fake_packets=args.fake_packets,
        recomputation_budget=args.budget,
        trials=args.trials,
    )

    print("=========================================================")
    print("      AI 2040 PACKET VERIFICATION AUDIT SIMULATION      ")
    print("=========================================================")
    print(f"Total Workload Pool (Packets)   : {metrics.total_packets:,}")
    print(f"Injected Rogue Packets          : {metrics.fake_packets:,}")
    print(f"Audit Recomputation Budget (C)  : {metrics.recomputation_budget * 100:.2f}%")
    print(f"Audited Packets per Workload    : {int(metrics.total_packets * metrics.recomputation_budget):,}")
    print(f"Monte Carlo Trials              : {metrics.trials:,}")
    print("---------------------------------------------------------")
    print(f"Theoretical Poisson Bound       : {metrics.theoretical_poisson_p * 100:.4f}%")
    print(f"Exact Independent Draw Bound    : {metrics.exact_independent_p * 100:.4f}%")
    print(f"Empirical Simulation Detection  : {metrics.empirical_p * 100:.4f}%")
    print("=========================================================")


if __name__ == "__main__":
    main()
