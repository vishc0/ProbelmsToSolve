# Markdown Document Standard

## Fixed limit

Every hand-authored Markdown file in this repository has a hard maximum of
**200 lines**, measured with `wc -l`.

This limit applies to root documents, `.ai/`, `docs/`, research, opportunities,
projects, templates, setup guides, and READMEs. Generated or vendored material
must not be committed as ordinary project documentation.

## Right-sizing targets

The 200-line limit is a ceiling, not a target:

- **Up to 60 lines:** index, status, handoff, README, or single decision record.
- **Up to 120 lines:** normal guide, opportunity brief, project specification,
  research note, or operating procedure.
- **Up to 200 lines:** major canonical specification that cannot be made clear in
  a smaller file.

## Split rule

When a file approaches 200 lines:

1. Keep the overview and navigation in the canonical file.
2. Split details by stable subject, not by date or conversation.
3. Give each fact one canonical owner and link to it from other files.
4. Do not create `part-1`, `part-2`, or duplicate summaries.
5. Remove obsolete material or move superseded records to `archive/` when
   traceability requires preservation.

## Writing rules

- Lead with purpose, decision, or outcome.
- Prefer short sections and bounded lists.
- Keep examples only when they clarify a reusable rule.
- Link to sources and canonical records rather than copying them.
- Put temporary research and drafting in ignored `scratchpad/`.
- Do not use documentation volume as evidence of implementation.

## Verification

Run:

```bash
python3 tooling/check_markdown_size.py
```

The check fails when any tracked or untracked project Markdown file, except
ignored scratch data, exceeds 200 lines.
