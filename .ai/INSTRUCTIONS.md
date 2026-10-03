# Shared AI Workspace Instructions

This repository provisions and configures cloud compute machines, with special
attention to GPU-enabled virtual machines.

These instructions are the single shared source for Codex, Claude Code, and
Gemini CLI. The repository-root `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` files
must remain symbolic links to this file.

## Start of every task

Before planning or changing files:

1. Read `.ai/CONTEXT.md` for the current environment and project facts.
2. Read `.ai/DECISIONS.md` for durable architectural decisions.
3. Read `.ai/OPERATING_POLICY.md` for approval, privacy, cost, and scope rules.
4. Read `.ai/PLANNING.md` for value-based planning and delivery gates.
5. Read `.ai/TASKS.md` for active work and handoffs.
6. Inspect the relevant repository files; do not assume the current cloud,
   operating system, GPU, driver, or runtime configuration.

## Working rules

- Prefer reproducible, idempotent automation over undocumented manual steps.
- Search the repository and established tools before building non-trivial new
  plumbing.
- Keep provider-specific logic isolated from shared provisioning logic.
- Pin compatibility-sensitive versions, especially GPU drivers, CUDA, container
  runtimes, infrastructure providers, and machine images.
- Never commit credentials, API keys, private keys, tokens, `.env` files,
  Terraform state, or cloud service-account files.
- Use least-privilege access and secure defaults. Call out changes that may
  create billable cloud resources or expose network services before applying
  them.
- Preserve user changes and avoid destructive infrastructure operations unless
  the user explicitly authorizes them.
- Never silently expand scope. Surface the option, value, cost, and risk for the
  owner to decide.
- Add validation or smoke checks for provisioning changes when practical.
- Keep documentation and examples provider-neutral unless they intentionally
  target a named provider.
- Update the canonical document that owns a concern rather than creating a new
  document for every activity or conversation.
- Put temporary notes, downloads, experiments, generated intermediates, and
  working data only in the ignored `scratchpad/` directory.
- Keep each fact in one canonical location. Link to it elsewhere instead of
  copying content that can drift.

## Shared memory hygiene

- Put stable project facts in `.ai/CONTEXT.md`.
- Record consequential technical choices in `.ai/DECISIONS.md`.
- Keep current status and cross-agent handoffs in `.ai/TASKS.md`.
- Keep project-level policy in `.ai/OPERATING_POLICY.md` and planning standards
  in `.ai/PLANNING.md`.
- Do not write secrets, credentials, personal data, or transient chat logs into
  `.ai/`.
- Never promote scratchpad content into canonical files without reviewing its
  provenance, accuracy, duplication, and long-term value.
- Update shared memory only when a task materially changes project state or
  establishes a durable fact.

## Verification

Before reporting completion:

- Run the narrowest relevant validation, lint, or dry-run command.
- Review the diff for accidental secrets and machine-specific data.
- Summarize what changed, what was verified, and any remaining risk.
