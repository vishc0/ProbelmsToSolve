# Opportunity: Untrusted Monitor Hierarchy & Deception Sandbox

## Decision summary

- Status: proposed
- Owner: Chippa Vishweshwar
- Domain: ai-safety-and-control
- Horizon: 2026–2029
- Recommendation: Develop a containerized runtime harness implementing dual-agent untrusted monitoring with state obfuscation and synthetic deception tripwires to test AI control protocols.

## Problem and user

- Affected user or organization: AI safety engineering teams, automated software development pipelines, and frontier model labs.
- Current pain or constraint: As AI models achieve automated coding and engineering capabilities (ITAI threshold), standard unit testing cannot detect sophisticated reward-hacking or covert scheming (Lurkville/Schemeria regimes).
- Evidence: Greenblatt & Larsen (*AI 2040 Alignment Roadmap*) formalize the Max-C boundary and demonstrate that human monitoring must be augmented by untrusted secondary monitors protected by prompt prefix isolation and synthetic tripwire injection.

## Proposed capability

- Outcome: An open runtime environment where a primary "Worker Agent" generates code and execution plans while an isolated "Monitor Agent" (with randomized memory wiping and tripwire injection) audits traces for misaligned behaviors.
- Smallest valuable experiment: Build a local test harness where synthetic "malicious agent tasks" (e.g. attempting to read `/etc/passwd` or ping an unwhitelisted endpoint) are injected into a worker queue, measuring the monitor's detection recall.
- Differentiation or research contribution: Implements the first reproducible benchmark for few-shot catastrophe prevention and untrusted monitor separation.

## Traceability

- Source claims: `source-claim: 2026-ai-futures-project-ai-2040-plan-a#alignment-roadmap`
- External evidence: `external-evidence: Redwood Research (2025) Control Protocols`
- AI inferences: `ai-inference: Protocol can be validated with local SLMs or mock agent traces prior to frontier model integration.`
- Human directions and decisions: `human-direction: Zero-cloud spend, local validation first.`

## Assessment

- Expected value: Provides foundational infrastructure for safe automated agent execution inside CloudSetup.
- Feasibility: High for software runtime; medium for full multi-agent evaluation.
- Evidence strength: Grounded in peer-reviewed alignment research (Anthropic, Redwood, AI Futures).
- Cost and dependencies: Zero cloud cost on local CPU.
- Risks and mitigations: Monitor and worker collusion; mitigated by strict process isolation and lack of shared context window.
- Time-to-learning: 2–3 days.

## Promotion criteria

- Success metric: Monitor achieves 100% detection on injected baseline tripwires with <5% false positive rate.
- Approval required: Owner authorization to promote to `projects/incubator/untrusted-monitor-runtime`.
- Next action: Scaffold incubator project structure.
