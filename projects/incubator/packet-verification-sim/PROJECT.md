# Project: Packet Verification Simulator (`packet-verification-sim`)

## Outcome

A reproducible, deterministic simulation engine that models statistical random recomputation of datacenter compute packets. It proves the detection bounds of unauthorized/fake computational workloads under variable recomputation budgets (0.1% to 5.0%), demonstrating the viability of treaty verification without trust.

## Users and use cases

- **Treaty Verification Architects:** Validate sampling parameters and audit budgets needed to guarantee detection of unauthorized training runs.
- **AI Safety & Security Researchers:** Test evasion strategies and assess backdoor insertion limits in large distributed training runs.
- **Enterprise Auditors:** Implement statistical sampling rather than 100% redundant execution for regulatory compliance.

## Scope

### In scope
- Deterministic simulation of workload pools ($N_{\text{packets}} \in [10^3, 10^7]$).
- Random sampling without replacement vs. Poisson approximation verification.
- Detection probability curves across variable fake packet injection ratios ($F_{\text{fake}}$).
- Automated CLI and unit test suites demonstrating convergence to $P(\text{detected}) = 1 - e^{-C \cdot N_{\text{fake}}}$.

### Out of scope
- Physical hardware interception / network wire tapping.
- Non-deterministic GPU kernel emulation.

## Requirements

- FR-1: Generate synthetic distributed training workload manifests consisting of hashed execution packets.
- FR-2: Inject arbitrary clusters of rogue/fake packets representing unapproved fine-tuning or backdoor injection.
- FR-3: Audit a configurable percentage $C$ of packets and evaluate detection probability over Monte Carlo trials.
- NFR-1: Run on local CPU in <2 seconds for 100,000 packets; zero cloud dependencies.

## Architecture

- Pure Python implementation with NumPy vectorization.
- `PacketWorkload`: Generates and manages the stream of execution packet hashes.
- `VerificationAuditor`: Implements independent sampling and recomputation verification.
- `MonteCarloEvaluator`: Simulates $M$ trials to compute empirical confidence curves against theoretical Poisson bounds.

## Evidence and assumptions

- Grounded in Rinberg et al. (2025) and AI Futures Project *AI 2040 Verification Plan*.
- Assumes packets are reproducible (deterministic inputs map to deterministic outputs).

## Milestones

- M1: Core mathematical model and Monte Carlo simulation harness.
- M2: Unit test suite passing with empirical verification matching theoretical bounds within 1% error.
- M3: Packaging as reusable CLI with SVG/ASCII plot outputs for reports.

## Cost model

- Local laptop execution: 0 USD.
- CPU memory footprint: <50 MB RAM.

## Provenance

- Originating Opportunity: `catalog/opportunities/verification-packet-auditing/OPPORTUNITY.md`
- Source Reference: `research/analysis/2026-ai-futures-project-ai-2040-plan-a/02_VERIFICATION_AND_COMPUTE_GOVERNANCE.md`
