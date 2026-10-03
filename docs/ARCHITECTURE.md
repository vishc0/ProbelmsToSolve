# Architecture

## System shape

```text
Public catalog + private workbench
              |
          Web application
              |
        API / control plane
       /       |          \
Provenance  Workflow     Artifact
store       engine       registry
       \       |          /
        Model gateway + retrieval
              |
    CPU jobs / optional GPU workers
```

## Logical components

### Web application

- Public project catalog and artifact pages
- Authenticated research workbench
- Source viewer with evidence links
- Expandable idea tree and opportunity board
- Human review, editing, branching, approval, and publication controls
- Run status, cost, model, and provenance visibility

### API and control plane

- Authentication and authorization
- Source, project, decision, run, and artifact APIs
- Approval enforcement
- Workflow scheduling and idempotency
- Budget, quota, and concurrency controls
- Audit events and observability

### Research and generation workers

- Parse and normalize sources
- Extract structured claims and scenarios
- Retrieve corroborating or contradicting evidence
- Generate and evaluate opportunity briefs
- Generate project artifacts from versioned templates
- Run tests, benchmarks, and validation checks in isolated environments

### Model gateway

- Route by privacy, capability, latency, context size, and cost
- Support local models, subscription CLIs for development workflows, and approved
  API providers for hosted execution
- Record provider, model, configuration, token/cost usage, and output lineage
- Prevent local-only data from falling back to cloud models

### Data plane

- Relational store for sources, claims, projects, decisions, workflows, and audit
- Object storage for permitted source snapshots and generated artifacts
- Search/retrieval index derived from approved content
- Queue for asynchronous work
- Git repositories for runnable project boilerplates

## Cost-oriented deployment

- Host the web application and CPU control plane separately from GPU execution.
- Keep routine extraction, metadata, and workflow operations on CPU or local
  models when adequate.
- Start GPU workers only for jobs that require them; apply idle shutdown,
  per-run budgets, and measured utilization.
- Prefer managed primitives only where their reduced operating burden provides
  more value than their recurring cost.
- Do not select or provision a hosting provider until the first local vertical
  slice establishes workload and cost requirements.

## Trust boundaries

- Public content is separate from private drafts and licensed source material.
- User decisions and audit data are not public by default.
- Generated code executes only in isolated, bounded environments.
- Publication, infrastructure spend, access expansion, and destructive actions
  pass explicit approval gates.
