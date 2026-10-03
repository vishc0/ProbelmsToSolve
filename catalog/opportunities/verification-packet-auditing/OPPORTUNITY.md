# Opportunity: In-Line Packet Recomputation & Sampling Verification

## Decision summary

- Status: proposed
- Owner: Chippa Vishweshwar
- Domain: verification-and-auditing
- Horizon: 2026–2030
- Recommendation: Prototype an open-source, vendor-agnostic Python/PyTorch harness simulating packet recomputation sampling to prove statistical bounds for rogue workload detection.

## Problem and user

- Affected user or organization: Treaty verification bodies, sovereign regulators, and frontier AI research consortiums.
- Current pain or constraint: Existing datacenter auditing relies on trust or software metrics (Prometheus, NVML) that can be easily spoofed by malicious hosts. Verifying 100% of GPU computation is economically prohibitive (doubles the cost of training).
- Evidence: AI Futures Project *AI 2040 Verification Plan* proves that random sampling of computational packets with a modest 1% recomputation budget catches any rogue training run exceeding 46,000 H100e-hours at 99% statistical confidence ($P = 1 - e^{-C \cdot N_{\text{fake}}}$).

## Proposed capability

- Outcome: A reproducible, deterministic verification simulator and network tap specification that captures training gradient/checkpoint packets and applies Poisson-bounded random auditing.
- Smallest valuable experiment: Build a local Python simulator modeling a 100,000-packet distributed training workload, injecting a 500-packet rogue backdoor, and benchmarking detection rates across recomputation budgets from 0.1% to 5.0%.
- Differentiation or research contribution: Provides the first open-source, empirical validation of the Rinberg/Dean packet-sampling verification equations.

## Traceability

- Source claims: `source-claim: 2026-ai-futures-project-ai-2040-plan-a#verification-plan`
- External evidence: `external-evidence: Rinberg et al. (2025) arXiv:2511.02620`
- AI inferences: `ai-inference: Simulation can run entirely on local CPU without GPU dependency by hashing synthetic tensor gradients.`
- Human directions and decisions: `human-direction: Zero-cloud spend, local validation first.`

## Assessment

- Expected value: Converts an abstract international treaty policy into a testable engineering benchmark.
- Feasibility: High (mathematical simulator runs on local CPU in <1 second; hardware tap requires future silicon partnership).
- Evidence strength: Strong mathematical proof grounded in Poisson sampling theory.
- Cost and dependencies: Zero dollar cost; local Python environment with standard scientific libraries (`numpy`, `pytest`).
- Risks and mitigations: Floating-point non-determinism across disparate GPU architectures can cause false positive verification failures; mitigated by bounded delta tolerance thresholds.
- Time-to-learning: 2–4 hours for initial working simulator.

## Promotion criteria

- Success metric: Python test suite passing with 100% coverage verifying that $P(\text{detected}) \ge 0.99$ holds empirically for injected fake packets $\ge 4.6 / C$.
- Approval required: Owner authorization to promote from Opportunity to Incubator Project (`projects/incubator/packet-verification-sim`).
- Next action: Scaffold incubator project directory and test suite.
