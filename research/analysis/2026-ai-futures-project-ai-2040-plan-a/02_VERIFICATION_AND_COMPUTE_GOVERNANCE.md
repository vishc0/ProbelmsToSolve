# Verification & Compute Governance Framework

In *AI 2040: Plan A*, verification is the load-bearing pillar that enables an international pause and slowdown without relying on trust between geopolitical rivals. This document outlines the technical architecture, mathematical foundations, and hardware governance mechanisms.

---

## 1. The Mathematical Foundation: Packet-Based Random Recomputation

The core verification mechanism operates on reproducible units of computation called **packets** (inputs, instructions, checkpoint diffs, and outputs captured at network taps or hardware interfaces).

### Derivation & Assurance Curve
Let:
- $N_{\text{packets}}$ = Total computational packets in the audited pool.
- $C$ = Recomputation budget fraction (e.g., $1\% = 0.01$).
- $N_{\text{verified}} = C \cdot N_{\text{packets}}$ = Number of packets independently recomputed and audited.
- $N_{\text{fake}}$ = Number of unauthorized or rogue packets inserted by a defector.
- $F_{\text{fake}} = \frac{N_{\text{fake}}}{N_{\text{packets}}}$ = Fraudulent fraction of the total workload.

The probability of an attacker evading detection across independent random samples is:
$$P(\text{undetected}) = (1 - C)^{N_{\text{fake}}}$$:

For small $C$ and moderately large $N_{\text{fake}}$, this converges to a Poisson distribution:
$$P(\text{undetected}) \approx e^{-N_{\text{verified}} \cdot F_{\text{fake}}} = e^{-C \cdot N_{\text{fake}}}$$:

The probability of catching unauthorized computation is:
$$P(\text{detected}) = 1 - e^{-C \cdot N_{\text{fake}}}$$:

### 99% Detection Bound
To achieve 99% confidence of detection ($P(\text{detected}) \ge 0.99$):
$$C \cdot N_{\text{fake}} \ge \ln(100) \approx 4.605$$
$$N_{\text{fake}}^{99\%} = \frac{4.6}{C}$$

Let $p$ be the compute packet size (in H100e-hours). The cumulative rogue work $W_{\text{rogue}}$ an adversary can execute before guaranteed 99% detection is strictly bounded:
$$W_{\text{rogue}}^{99\%} = \frac{4.6 \cdot p}{C}$$

### Operational Scaling Matrix
With a fixed $1\%$ recomputation budget ($C = 0.01$):

| Packet Size ($p$) | Required Fake Packets ($N_{\text{fake}}$) | Maximum Undetected Rogue Work ($W_{\text{rogue}}$) | Equivalent Training Scope |
| :--- | :--- | :--- | :--- |
| **100 H100e-hours** (Per-GPU hour) | 460 packets | **46,000 H100e-hours** | Less than 1/2 of a GPT-3 run (~100K H100e-hrs) |
| **10 H100e-hours** (Sub-batch tap) | 460 packets | **4,600 H100e-hours** | Minor fine-tuning run |
| **1 H100e-hour** (Per-server step) | 460 packets | **460 H100e-hours** | Small experimental ablation |
| **100 H100e-hours (0.1% budget)** | 4,605 packets | **460,000 H100e-hours** | ~4.5x GPT-3 scale |

---

## 2. Hardware Tap Architecture & Evolution (2030–2036)

To prevent tampered execution without relying on software operating systems (which can be jailbroken), physical taps are integrated into datacenter fabrics:

1. **2030 (Server-Level Tap):**
   - Tap granularity: Per rack/chassis (~4,000 H100e per node).
   - Audits distributed data parallelism gradients and checkpoint updates.
2. **2032 (Shelf-Level Tap):**
   - Tap granularity: Optical bus interceptors (~400 H100e per shelf).
   - In-line cryptographically signed gradient verification.
3. **2034 (Per-GPU Hardware Tap):**
   - Tap granularity: Integrated on-die or on-package (~100 H100e per chip).
   - Direct execution trace hashing and secure enclave reporting.

---

## 3. Mutual Chip Declaration & Dark Compute Accounting

Plan A's entry condition in 2029 requires an exhaustive global compute accounting audit:

- **Baseline Global Inventory (Jan 2029 Estimate):**
  - Total World Compute: **~289 Million H100-equivalents (H100e)**.
  - United States: ~224M H100e (~77%).
  - China: ~26M H100e (~9%).
  - Rest of World: ~39M H100e (~14%).
- **Dark Compute Bound:**
  - Strict enforcement of semiconductor supply chain records (TSMC, ASML, packaging facilities).
  - Target ceiling on unaccounted / smuggled chips: **Median 0.51%** (80% CI: 0.11% to 1.4%).
- **Inference-Only Retrofit:**
  - Frontier datacenters (>10,000 H100e) retrofitted with hardware switches disabling multi-node backpropagation networks, allowing economic inference while cryptographically barring frontier pretraining.
- **Edge Compute Caps:**
  - Unverified consumer hardware (mobile phones, consumer GPUs) capped below an aggregate threshold (~30M effective-H100e globally) to eliminate decentralized covert clusters.

---

## 4. Mutually Assured Compute Destruction (MACD)

To eliminate the incentive for either nation to renege on Plan A and seize datacenters for a sprint to ASI:
- **Maritime Floating Datacenters (2035 deployment):** Frontier clusters are relocated to international waters.
- **Vulnerability by Design:** Open-ocean facilities cannot be defended against conventional standoff munitions and lack sovereign territorial defenses.
- **Cryptographic Dead-Man Switches:** Dual-key authorization protocols between international verifiers; tampering or communication severed initiates secure silicon destruction (thermal or high-voltage fusing).