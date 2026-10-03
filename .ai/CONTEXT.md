# Project Context

## Purpose

CloudSetup is a community-benefit human–AI project foundry. It identifies
high-friction problems affecting ordinary people and communities, checks
existing work, and translates validated gaps into safe, affordable, reusable
projects. AI foresight is a source of evidence rather than the mission boundary.
Cloud and GPU infrastructure is an enabling capability.

## Priorities

- Fast, repeatable machine bootstrap
- GPU driver, CUDA, and container-runtime compatibility
- Portable automation across cloud providers where practical
- Secure handling of credentials and remote access
- Cost-optimized provisioning, right-sizing, scheduling, and teardown
- Value-based planning with measurable outcomes and explicit approval gates
- Clear verification and troubleshooting steps
- Source-to-project provenance and uncertainty labeling
- Human steering of AI-generated exploration and project generation
- Reusable outputs for organizations, startups, and applied research teams
- Measurable everyday benefit, accessibility, affordability, and human agency
- Physical, digital, and commercial AI governed by public-interest safeguards
- Existing-work audits before creating new projects

## Current state

- Repository scaffold created.
- The hosted product and model backend are defined at requirements and logical
  architecture level; no implementation stack or hosting provider is selected.
- Codex, Claude Code, and Gemini CLI share the `.ai/` workspace.
- Portfolio-wide Chief-of-Staff, privacy, cost-routing, and approval principles
  are adapted into `.ai/OPERATING_POLICY.md` and `.ai/PLANNING.md`.
- The 2026 `AI 2040: Plan A` scenario is the provisional primary source; the
  owner must confirm it is the intended work before deep analysis.
- The MVP follows a free-first hybrid design: laptop control/worker capacity,
  free scale-to-zero CPU hosting, programmatic burst GPU, and notebook-based
  research experiments.
- Current laptop measurement: 6 cores/12 threads, 31 GiB RAM, and ~731 GiB free
  workspace disk. Local NVIDIA device access and Ollama are not currently
  verified operational.

## Environment facts

Add verified, non-secret environment details here as the project evolves.
