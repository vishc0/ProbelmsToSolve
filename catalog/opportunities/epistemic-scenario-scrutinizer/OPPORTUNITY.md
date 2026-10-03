# Opportunity: Automated Scenario Scrutiny & Claim Verification Engine

## Decision summary

- Status: proposed
- Owner: Chippa Vishweshwar
- Domain: epistemics-and-research-eval
- Horizon: 2026–2028
- Recommendation: Build a deterministic CLI pipeline that extracts assertions, assumptions, and causal predictions from foresight papers and challenges them against empirical datasets to mitigate "Slopolis" in research synthesis.

## Problem and user

- Affected user or organization: Enterprise strategy leaders, venture investors, policy analysts, and applied AI labs.
- Current pain or constraint: AI foresight and policy proposals are rarely subjected to rigorous scenario scrutiny; AI-generated analyses frequently devolve into "Slopolis" (well-formatted, plausible prose containing subtle conceptual flaws and unverifiable assertions).
- Evidence: AI Futures Project emphasizes *Scenario Scrutiny for AI Policy*: when proposals are modeled as explicit state machines and causal dependencies, most fall apart or reveal unstated dependencies.

## Proposed capability

- Outcome: A modular toolchain that parses complex foresight documents, extracts claims into typed schemas (Actors, Triggers, Constraints, Metrics), constructs a dependency graph, and executes automated refutation queries.
- Smallest valuable experiment: Build a local Python CLI (`scenario-scrutinizer`) that ingests Markdown/PDF text, parses out 10 structured claims, and tags them by provenance (`source-claim`, `ai-inference`, `external-evidence`).
- Differentiation or research contribution: Establishes a verifiable standard for turning speculative long-form prose into machine-readable, testable hypothesis graphs.

## Traceability

- Source claims: `source-claim: 2026-ai-futures-project-ai-2040-plan-a#summary`
- External evidence: `external-evidence: blog.aifutures.org/p/scenario-scrutiny-for-ai-policy`
- AI inferences: `ai-inference: Deterministic regex and typed Pydantic models can structure 80% of claims before model-assisted evaluation.`
- Human directions and decisions: `human-direction: Build on local laptop; maintain pristine repository discipline.`

## Assessment

- Expected value: Directly serves CloudSetup's core mission: translating research insight into investable, implementable projects.
- Feasibility: High. Can run locally on CPU using Python + Pydantic.
- Evidence strength: Demonstrated in CloudSetup's own research-to-project pipeline architecture.
- Cost and dependencies: Zero cloud spend.
- Risks and mitigations: Semantic ambiguity in natural language foresight; mitigated by human-in-the-loop steering at decision checkpoints.
- Time-to-learning: 1 day.

## Promotion criteria

- Success metric: Successfully parsing the 5 Plan A supplements into validated JSON claim graphs with zero unverified assertions.
- Approval required: Owner authorization to promote to `projects/incubator/scenario-scrutiny-engine`.
- Next action: Scaffold incubator project and implement Pydantic claim schema.
