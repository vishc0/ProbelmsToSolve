# Frontier Research Gaps & Unachieved Capabilities

The *AI 2040* foresight framework identifies critical technological, infrastructural, and governance capabilities that currently do **not** exist in an enterprise- or treaty-ready state. Closing these gaps is essential for converting speculative policy into operable engineering.

---

## 1. Unachieved Capability Taxonomy

```text
                  Frontier Unachieved Capabilities
                                  |
    +-----------------------------+-----------------------------+
    |                             |                             |
Hardware & Infrastructure   Surveillance & Intelligence   Alignment & Epistemics
- Packet Recomputation Taps - Thermal Plume Detection     - Untrusted Monitoring
- Hardware Backprop Switches- GMTI Radar Siting Models    - Anti-Alignment Faking
- Maritime MACD Platforms   - Dark Silicon Ledgers        - Scenario Scrutiny Engine
```

---

## 2. Comprehensive Capability Matrix

| Capability ID | Domain | Current State (Baseline) | Target Capability (AI 2040 Req) | Primary Bottleneck |
| :--- | :--- | :--- | :--- | :--- |
| **CAP-001** | **Hardware Verification** | Software-level cluster monitoring (Prometheus, DCGM) easily bypassed with root/firmware access. | In-line hardware packet logging with deterministic replay and 1% sampling verification. | Non-deterministic floating-point math in GPU architectures and proprietary networking IP. |
| **CAP-002** | **Silicon Accounting** | Paper manifests and export licensing declarations; ~30% Chinese compute acquired via smuggling. | Cryptographically signed on-die silicon identity ledger with zero-knowledge ownership proofs. | Resistance from chip fabricators (TSMC, Nvidia) to embed universal attestation root keys. |
| **CAP-003** | **Remote Sensing (Thermal)** | Point-source Landsat/MODIS thermal sensing with 57–100m resolution and high noise. | Automated differential IR satellite pipeline detecting subtle $\Delta T < 0.1^\circ\text{C}$ water discharge plumes. | Atmospheric noise, seasonal diurnal temperature cycles, and turbulent mixing dynamics. |
| **CAP-004** | **AI Control / Sandboxing** | Post-hoc red-teaming and prompt-based guardrails; models frequently deceive or jailbreak. | Isolated untrusted monitor hierarchies with tripwire injection and few-shot catastrophe prevention. | Overhead of redundant inference and risk of covert collusion across worker and monitor models. |
| **CAP-005** | **Epistemic Scrutiny** | LLMs hallucinate plausible citations, create superficial research "slop", and agree with users. | Multi-agent adversarial scenario scrutiny engine verifying empirical claims, assumptions, and math. | Lack of formal verification tools for informal natural language reasoning and policy analysis. |
| **CAP-006** | **Inference-Only Retrofitting** | Software ACLs limit model access, but weights can be extracted or fine-tuned if nodes possess interconnects. | Physical/cryptographic hardware switch that permanently disables distributed backward passes. | Interconnect silicon (NVLink, InfiniBand) designed natively for bidirectional gradient exchange. |
| **CAP-007** | **Mutually Assured Destruction** | Conventional datacenter physical security; no provable, remote, tamper-proof self-destruct. | Verifiable dual-custody cryptographic silicon fuse triggering thermal or electrical destruction. | Risk of accidental detonation, sabotage, or unilateral exploitation during international crises. |

---

## 3. Direct Translation to CloudSetup Portfolio

These unachieved capabilities map directly to the **CloudSetup Opportunity Catalog** and candidate **Incubator Projects**:

1. **CAP-001 ➔ Opportunity:** `verification-packet-auditing` ➔ **Incubator:** `projects/incubator/packet-verification-sim`
2. **CAP-002 ➔ Opportunity:** `silicon-provenance-ledger` ➔ **Incubator:** `projects/incubator/silicon-provenance-engine`
3. **CAP-003 ➔ Opportunity:** `compute-satellite-plume-detection` ➔ **Incubator:** `projects/incubator/thermal-plume-sentinel`
4. **CAP-004 ➔ Opportunity:** `control-untrusted-monitor-sandbox` ➔ **Incubator:** `projects/incubator/untrusted-monitor-runtime`
5. **CAP-005 ➔ Opportunity:** `epistemic-claim-scrutinizer` ➔ **Incubator:** `projects/incubator/scenario-scrutiny-engine`
