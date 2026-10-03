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
