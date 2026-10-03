# Decision Log

Record durable decisions here. Keep entries brief and link to implementation or
supporting documentation when useful.

## 2026-10-02 — Shared AI workspace

- Use `.ai/` as the canonical, version-controlled context directory.
- Point `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` to the same
  `.ai/INSTRUCTIONS.md` file using relative symbolic links.
- Keep secrets and transient conversation data out of shared AI memory.

## 2026-10-02 — Portfolio operating principles

- Apply the owner's existing Chief-of-Staff model: AI prepares, coordinates,
  implements approved work, and verifies; the owner retains consequential
  financial, access, legal, and infrastructure decisions.
- Route work to the cheapest capable tool without weakening privacy or quality.
- Use value-based planning and smallest-valuable-increment delivery.
- Require explicit approval before billable infrastructure mutation, destructive
  operations, access expansion, or external commitments.
- Keep private subscription details and credentials outside project memory.

## 2026-10-02 — Research-to-project foundry

- Make a hosted human–AI workbench and public project catalog the product shape.
- Preserve a traceable pipeline from sources through claims, opportunities,
  blueprints, boilerplates, validation, and publication.
- Record evidence, assumptions, alternatives, concise rationales, edits, and
  approvals; do not store or expose private model chain-of-thought.
- Separate the CPU control plane from optional scale-to-zero GPU workers.
- Validate one local vertical slice before selecting paid hosting or building a
  broad multi-source platform.

## 2026-10-02 — Canonical content and scratch data

- Keep the tracked repository pristine and free of temporary working data.
- Use the Git-ignored `scratchpad/` directory for all intermediate material.
- Assign every durable fact one canonical owner and link to it elsewhere.

## 2026-10-02 — Free-first hybrid compute

- Use the laptop as the initial persistent development/control node.
- Use pull-based, outbound worker connections; do not expose laptop ports.
- Use free notebook GPUs for reproducible research, never as hidden permanent
  servers or distributed workers.
- Prefer scale-to-zero CPU services and Modal free credit for the first
  programmatic burst-GPU benchmark.
- Build the MVP evidence package before pursuing larger startup or research
  credits.

## 2026-10-03 — Community-benefit project focus

- Broaden the mission from expanding AI-futures papers to solving documented,
  present-day problems affecting ordinary people and communities.
- Treat AI 2040 as a case study and source of foresight, not the product boundary.
- Cover physical, digital, and sustainable commercial AI while making public
  benefit, accessibility, affordability, privacy, consent, and human agency the
  governing tests.
- Audit existing efforts before development and issue one of `CONTRIBUTE`,
  `EXTEND`, `CREATE`, `OBSERVE`, or `DECLINE` for each candidate.
- Permit sponsorship only with disclosed interests, reviewable milestones,
  protected community interests, and clear access, licensing, and stewardship
  terms.

## 2026-10-03 — Markdown size limit

- Limit every hand-authored Markdown file to 200 lines.
- Treat 60 lines as the target for indexes and operational notes, 120 for normal
  documents, and 200 only for major canonical specifications.
- Split by stable subject and link to one canonical owner instead of duplicating
  content.

## 2026-10-03 — Orchestrator and worker roles

- Claude Code is the single orchestrator; Antigravity (Gemini), Codex, and the
  local Ollama model are workers that receive bounded, file-scoped tasks.
- Workers use separate git worktrees, never commit, and return handoffs; the
  orchestrator verifies, merges after owner-approved commit policy, and alone
  updates task state.
- All AI use runs on flat-rate subscriptions or local models; Gemini CLI and
  per-token API keys are retired from routine work.

## 2026-10-03 — Manifest-backed foundry catalog

- Use globally unique, typed records for domains, problems, cross-domain
  root-cause clusters, opportunities, projects, and reusable solution patterns.
- Keep relationships in manifests and generate navigation indexes from them;
  handwritten folder lists are not sources of truth.
- Use schema `2.0` for the common ownership, provenance, link, visibility, and
  timestamp envelope while accepting legacy `1.0` opportunity/project records
  during migration.

## 2026-10-03 — 14-sector domain taxonomy with subdomains, facets, and aliases

- Use 14 top-level sector domains, with technical AI governance and evaluation
  areas nested under `digital-systems-and-ai`.
- Represent mission, capability, population, geography, and topic as controlled
  facets; preserve retired domain IDs as compatibility aliases.
