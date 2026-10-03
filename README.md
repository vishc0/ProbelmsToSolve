# CloudSetup

CloudSetup is a human–AI project foundry for translating AI foresight, research,
and standards into organization-ready blueprints and runnable reference
projects. Cloud and GPU infrastructure is an enabling layer for the hosted
website and backend model workflows.

Start with [PROJECT_INTENT.md](PROJECT_INTENT.md), then read the
[product requirements](docs/PRODUCT_REQUIREMENTS.md),
[architecture](docs/ARCHITECTURE.md), and
[research-to-project pipeline](docs/RESEARCH_TO_PROJECT_PIPELINE.md).
Repository hygiene and canonical ownership are defined in
[content governance](docs/CONTENT_GOVERNANCE.md).
The free-first hybrid environment begins in [`setup/`](setup/README.md).

## Shared AI context

Codex, Claude Code, and Gemini CLI use the same version-controlled context in
`.ai/`. Their native instruction files at the repository root point to one
canonical instruction file, preventing the tools from drifting apart.

See [`.ai/README.md`](.ai/README.md) for the layout and maintenance rules.

## Status

The product foundation and scalable repository structure are initialized. The
next milestone is a local, no-paid-infrastructure vertical slice using one
confirmed AI 2040 source.
