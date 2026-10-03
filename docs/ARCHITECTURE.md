# CloudSetup Architecture

## Product proposition

CloudSetup is an **open project foundry**: it converts credible research into
traceable opportunities, adoptable project packages, and maintained open
projects. The differentiator is not generic AI summarization. It is the governed
path from evidence to an accountable team:

`evidence -> opportunity -> validated project package -> adopter -> maintained project`

The founder curates and enriches the portfolio. AI accelerates bounded work.
External teams can discover a project, adopt it, become its steward, and return
improvements through a visible review process.

## Logical planes and responsibilities

### 1. Founder studio — private creation and governance

- Selects sources, priorities, project directions, and publication boundaries.
- Uses paid Codex, Claude, and Gemini access for interactive, high-judgment work
  where their terms permit the selected workflow.
- Reviews evidence, AI outputs, costs, risks, and community contributions.
- Approves promotion from draft to public catalog and assigns stewardship.

Paid AI sessions are founder tools, not credentials exposed to public users or a
production API resold by the website.

### 2. Foundry control plane — workflow coordination

- Maintains the source registry, evidence links, opportunities, projects,
  decisions, ownership, and lifecycle state.
- Decomposes approved work into bounded jobs.
- Routes each job by capability, privacy, latency, and cost.
- Places long-running work on a queue and records status, inputs, outputs,
  model/runtime metadata, measured cost, and provenance.
- Requires human approval for publication, spending, access changes, and project
  stewardship changes.

For the first MVP, Git files and GitHub workflows can provide most of this
control plane. A database and dedicated workflow service should be added only
when repository-based coordination becomes a measured constraint.

### 3. Execution plane — three distinct compute routes

**Paid model route**

- Interactive research, architecture, critique, and difficult synthesis.
- Human remains present and approves durable outputs.

**Local Ollama route**

- Routine agentic work, private drafts, classification, extraction, formatting,
  and inexpensive iteration on the laptop or another trusted local node.
- Local-first data stays local unless the owner approves a cloud route.

**Elastic cloud route**

- CPU workers handle long parsing, indexing, testing, crawling, simulation, and
  batch jobs.
- GPU workers handle only workloads that demonstrate a GPU need, such as larger
  local-model inference, embeddings at scale, or model evaluation.
- Workers claim jobs through outbound connections, write results to the artifact
  store, report status, and terminate when idle.
- Jobs are restartable, budget-capped, and independent of a founder browser
  session.

### 4. Knowledge and artifact plane — canonical project memory

- GitHub repository: versioned sources, schemas, decisions, opportunity briefs,
  project packages, starter code, tests, and contribution history.
- Artifact storage: permitted source snapshots, large generated outputs,
  evaluation results, and build artifacts that do not belong in Git.
- Search index: a derived, replaceable view of approved content; never the only
  copy of a fact.
- Provenance records: connect published claims and project artifacts to evidence,
  human decisions, and reproducible runs.

Every durable fact has one canonical owner. Other pages link to it instead of
copying it.

### 5. Public website — discovery and reuse

- Publishes only approved catalog content from the repository.
- Lets visitors browse domains, evidence, opportunities, project readiness,
  skills needed, expected cost, and ways to participate.
- Provides downloadable or forkable starter projects.
- Links contribution actions to GitHub rather than duplicating an issue tracker,
  identity system, or code-review system in the MVP.

The first website should be a generated static catalog with search and filters.
Public, on-demand LLM features should be a later, separately budgeted capability
with abuse controls—not an MVP dependency.

### 6. GitHub collaboration surface — adoption and contribution

- Issues hold questions, adoption requests, proposals, and reproducible defects.
- A project-adoption template records intended use, named lead, scope, milestones,
  and support requested from the foundry.
- Forks and branches isolate implementation work.
- Pull requests return documentation, evidence, code, tests, and results for
  review.
- CODEOWNERS or named maintainers identify accountable project stewards.

Adopting a project does not silently transfer ownership of the canonical foundry
record, trademarks, or third-party intellectual property. Each project's license,
maintainer rights, and stewardship agreement must make those boundaries explicit.

## End-to-end interaction

1. The founder registers a permitted source and defines the research question.
2. Paid AI assists interactively with difficult exploration and critique.
3. The founder approves an exploration branch and the control plane creates
   bounded jobs.
4. The router sends routine/private agent tasks to Ollama, long CPU work to an
   elastic CPU worker, and demonstrated accelerator work to a GPU worker.
5. Workers return artifacts, run metadata, cost, and evidence links; they do not
   publish directly.
6. The founder reviews and promotes an opportunity or project package in Git.
7. CI validates schemas, links, tests, provenance, and site generation.
8. The public site deploys the approved catalog; GitHub exposes the corresponding
   source, starter, issues, and contribution path.
9. A team proposes adoption, names a lead, and works in a fork or project branch.
10. Reviewed contributions merge back, project readiness is updated, and a proven
    adopter can become the named steward.

## Project lifecycle and accountability

Use an explicit lifecycle rather than treating every generated idea as a project:

`Draft -> Reviewed -> Published -> Available -> Adopted -> Active -> Graduated | Archived`

- **Founder/foundry steward:** guards evidence quality, portfolio coherence, and
  publication standards.
- **Project steward:** owns the roadmap, review responsiveness, and maintenance of
  an adopted project.
- **Contributors:** own their submitted work under the project's contribution and
  licensing terms.
- **Users:** may browse and reuse public outputs under the artifact's license.

No AI system assigns stewardship or publishes a project without human approval.

## MVP deployment boundary

Build the smallest complete loop first:

1. This GitHub repository is the canonical content and collaboration store.
2. The founder works locally with paid AI tools and, once operational, Ollama.
3. Local scripts generate and validate one opportunity and project package.
4. GitHub Actions builds a static public catalog and runs lightweight checks.
5. One optional queue adapter sends a bounded long job to one CPU or GPU worker.
6. A GitHub issue template supports the first external project adopter.

Defer a multi-tenant database, public chat interface, always-on GPU, custom
identity, and custom contribution workflow until real use justifies them.

## Trust and cost boundaries

- Private drafts and licensed source material never enter the public build.
- Secrets stay in local or hosted secret stores, never Git or shared AI memory.
- Generated code runs only in isolated, resource-bounded environments.
- Workers receive the minimum job context and permissions required.
- Cloud execution is scale-to-zero, budget-capped, observable, and interruptible.
- Public AI endpoints require authentication, quotas, moderation, and a funding
  decision before launch.
- Publication, spending, deployment, access expansion, and stewardship changes
  remain explicit human approval gates.
