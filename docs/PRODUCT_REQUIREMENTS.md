# Product Requirements

## Functional requirements

### Source and evidence

- **FR-001 — Source registry:** Record title, authors, publisher, date, URL,
  license/usage notes, version, and retrieval date.
- **FR-002 — Source processing:** Extract structure, claims, assumptions,
  forecasts, recommendations, risks, and cited dependencies.
- **FR-003 — Provenance:** Trace every derived artifact to source excerpts or
  clearly labeled human/AI inference.
- **FR-004 — Corroboration:** Link supporting, contradicting, and uncertainty
  evidence from other credible artifacts.

### Exploration and steering

- **FR-005 — Idea expansion:** Map source material into domains, themes,
  capabilities, constraints, research gaps, and candidate opportunities.
- **FR-006 — Branching:** Let users branch, merge, prune, annotate, and rank
  exploration paths without losing lineage.
- **FR-007 — Decision checkpoints:** Require human approval at promotion,
  architecture, spend, publication, and deployment gates.
- **FR-008 — Decision record:** Store selected option, alternatives, evidence,
  concise rationale, owner, time, and downstream impact.

### Project foundry

- **FR-009 — Opportunity assessment:** Score value, feasibility, evidence,
  differentiation, adoption friction, risk, cost, and time-to-learning.
- **FR-010 — Blueprint generation:** Produce problem framing, personas, use
  cases, requirements, architecture, milestones, risk controls, cost model, and
  validation plan.
- **FR-011 — Boilerplate generation:** Create runnable starter projects with
  documentation, tests, deployment configuration, examples, and extension
  points.
- **FR-012 — Organization adoption:** Produce integration, governance,
  operating-model, skills, migration, and change-management guidance.
- **FR-013 — Startup path:** Produce a wedge, customer hypothesis, defensibility,
  experiments, dependency map, and staged funding/compute needs.
- **FR-014 — Validation:** Track tests, benchmarks, evaluations, assumptions,
  measured cost, and readiness state.

### Publishing and portfolio

- **FR-015 — Review workflow:** Keep generated artifacts private and draft-only
  until approved.
- **FR-016 — Publishing:** Publish approved project pages and downloadable
  starters with attribution and version history.
- **FR-017 — Portfolio:** Filter projects by domain, horizon, maturity, evidence,
  cost, risk, and organization type.
- **FR-018 — Refresh:** Detect source or implementation changes and flag derived
  artifacts for review rather than silently rewriting them.

## Non-functional requirements

- **Traceable:** Claims and artifacts preserve provenance and authorship type.
- **Human-governed:** Consequential actions require explicit approval.
- **Cost-aware:** CPU control plane by default; GPU workers are optional,
  measurable, schedulable, and able to scale to zero.
- **Portable:** Model providers, vector stores, queues, and deployment targets
  remain replaceable behind interfaces.
- **Secure:** Least privilege, tenant isolation, secret management, content
  controls, and audit logs are first-class.
- **Reproducible:** Prompts, schemas, source versions, model configuration, and
  generation outputs are versioned.
- **Uncertainty-aware:** Forecasts, interpretations, and measured facts are
  visibly distinct.
- **Accessible:** Outputs are useful to both technical and business reviewers.

## Initial acceptance milestone

Using one selected AI 2040 source, the system can produce one evidence-backed
opportunity brief and one locally runnable project blueprint through at least two
recorded human decision checkpoints, without provisioning paid infrastructure.
