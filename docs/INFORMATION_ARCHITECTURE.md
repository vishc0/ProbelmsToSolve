# Repository Information Architecture

## Top-level map

| Path | Canonical purpose |
|---|---|
| `.ai/` | Shared instructions, policy, context, decisions, and handoffs |
| `docs/` | Product, architecture, methodology, roadmap, and governance |
| `research/sources/` | Source metadata and legally permitted snapshots |
| `research/analysis/` | Source-specific structured analysis |
| `research/synthesis/` | Cross-source findings and scenario comparisons |
| `catalog/domains/` | Stable domain taxonomy |
| `catalog/opportunities/` | Prioritized, evidence-backed opportunity briefs |
| `projects/incubator/` | Selected concepts being validated |
| `projects/reference/` | Verified, reusable reference projects |
| `templates/` | Canonical artifact and project templates |
| `website/` | Contract between repository records and public site pages |
| `setup/` | Free-resource catalog and reproducible hybrid-node setup |
| `tooling/` | Repository automation and generators |
| `tests/` | Repository-wide policy, schema, and integration tests |
| `scratchpad/` | Ignored temporary working data; never canonical |
| `archive/` | Superseded material retained for traceability |

## Placement rules

- Keep the repository root limited to entry points and cross-cutting config.
- Update canonical documents in place; do not create a file per conversation.
- Keep temporary and generated intermediate data in ignored `scratchpad/` only.
- Keep one canonical owner per fact and link to it rather than duplicating it.
- One source analysis lives under `research/analysis/<source-id>/`.
- One opportunity lives under `catalog/opportunities/<opportunity-id>/`.
- Promote a concept from `incubator` to `reference` only after its acceptance
  criteria pass and evidence is recorded.
- Generated content must identify its template version and upstream inputs.
- Prefer small index files that link to deeper artifacts over giant documents.

## Naming

- Directories and machine-readable IDs use lowercase kebab-case.
- Human-facing Markdown files use concise uppercase canonical names when they are
  entry points, such as `README.md`, `PROJECT.md`, and `DECISIONS.md`.
- Source IDs use `<year>-<publisher>-<short-title>`.
- Opportunity IDs use `<domain>-<capability-or-problem>`.
