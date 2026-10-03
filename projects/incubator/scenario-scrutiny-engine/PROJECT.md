# Project: Scenario Scrutiny Engine (`scenario-scrutiny-engine`)

## Outcome

A deterministic CLI toolchain that parses natural language policy, research, and foresight documents into typed, testable assertion graphs. It extracts claims, causal assumptions, and quantitative bounds, enabling automated scenario scrutiny and preventing epistemic degradation ("Slopolis").

Judgemnetal science, claims dept. fraud detection, evidence - inference -cause and judgement

applicable in the events past , present and future. can be developed and prevent malicious intent of individuals. 

## Users and use cases

- **Innovation & Architecture Teams:** Stress-test vendor claims and technical foresight against verifiable empirical metrics.
- **AI Policy & Treaty Analysts:** Formulate formal dependency graphs for international accords and governance proposals.
- **Applied AI Researchers:** Validate whether model outputs on complex qualitative reasoning tasks adhere to empirical evidence.

## Scope

### In scope
- Extraction of typed claims: Actors, Actions, Assumptions, Enabling Capabilities, Constraints, and Metrics.
- Authorship & provenance labeling (`source-claim`, `ai-inference`, `external-evidence`, `human-decision`).
- Export to structured JSON / JSON-LD schemas.
- Local CLI execution with zero external network dependencies.

### Out of scope
- Web-based multi-user SaaS hosting (deferred to Phase 3).
- Direct proprietary LLM fine-tuning.

## Requirements

- FR-1: Ingest Markdown or plaintext research documents.
- FR-2: Classify assertions into formal schema types with confidence scores.
- FR-3: Generate a dependency graph linking claims to underlying assumptions.
- NFR-1: Execute on CPU in <1 second for standard whitepapers.

## Architecture

- Pure Python with standard dataclasses / JSON schemas.
- `ClaimParser`: Tokenizes and segments prose into addressable paragraphs and claims.
- `ProvenanceTagger`: Attaches source-to-claim metadata.
- `GraphExporter`: Outputs network graph of interrelated assertions.

## Provenance

- Originating Opportunity: `catalog/opportunities/epistemic-scenario-scrutinizer/OPPORTUNITY.md`
- Source Reference: `research/analysis/2026-ai-futures-project-ai-2040-plan-a/04_ALIGNMENT_AND_CONTROL_ROADMAP.md`
