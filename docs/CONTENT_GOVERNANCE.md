# Content Governance

## Pristine repository rule

The tracked repository contains only canonical, durable, reviewable project
artifacts. Temporary work belongs in the ignored `scratchpad/` directory.

## Canonical ownership

| Information | Canonical location |
|---|---|
| Mission and business need | `PROJECT_INTENT.md` |
| Prior art and project positioning | `docs/PRIOR_ART_AND_POSITIONING.md` |
| Markdown size and splitting rules | `docs/DOCUMENT_STANDARDS.md` |
| Product requirements | `docs/PRODUCT_REQUIREMENTS.md` |
| System architecture | `docs/ARCHITECTURE.md` |
| Repository layout | `docs/INFORMATION_ARCHITECTURE.md` |
| Operating and approval rules | `.ai/OPERATING_POLICY.md` |
| Planning method | `.ai/PLANNING.md` |
| Verified project facts | `.ai/CONTEXT.md` |
| Durable decisions | `.ai/DECISIONS.md` |
| Active work and handoffs | `.ai/TASKS.md` |
| Source identity and rights | `research/sources/registry.yaml` |
| Provider/resource facts | `setup/resources/RESOURCE_CATALOG.md` |

Other files link to these owners instead of repeating their contents.

## Scratchpad policy

- Use `scratchpad/` for temporary downloads, raw extraction, prompt experiments,
  generated drafts, benchmark output, and migration staging.
- The entire directory is Git-ignored.
- Never place credentials, regulated data, or minor/student data there.
- Review and normalize useful findings into the appropriate canonical artifact.
- Remove stale scratch material after the related task is accepted.

## Promotion checklist

Before moving information into tracked files:

1. Confirm provenance and redistribution rights.
2. Separate verified facts, source claims, AI inference, and human decisions.
3. Search for an existing canonical owner.
4. Update that owner in place and link to it from consumers.
5. Remove contradictory or superseded duplication.
6. Validate links, schemas, and secrets scanning.
7. Keep every Markdown file within the 200-line limit in
   `docs/DOCUMENT_STANDARDS.md`.
