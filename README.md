# CloudSetup

CloudSetup turns research ideas into opportunities that teams can adopt as
runnable projects.

## Start here

There are four working areas:

| Area | What belongs there |
|---|---|
| [`research/`](research/) | Source material and analysis |
| [`catalog/opportunities/`](catalog/opportunities/) | Ideas assessed as concrete opportunities |
| [`projects/`](projects/) | Reusable implementations created from approved opportunities |
| [`website/`](website/README.md) | Rules for publishing approved opportunities and projects |

The normal path is:

`research -> opportunity -> incubator project -> reference project -> website`

## Create a reusable opportunity

```bash
python3 tooling/foundry.py new-opportunity \
  --id domain-short-name \
  --title "Opportunity title" \
  --summary "Who benefits and what becomes possible" \
  --domain domain-id \
  --owner "Owner name"
```

This creates one self-contained folder in `catalog/opportunities/`. Complete its
`OPPORTUNITY.md`; `opportunity.json` connects it to the website.

## Turn an opportunity into a project

After human approval:

```bash
python3 tooling/foundry.py new-project \
  --id project-short-name \
  --title "Project title" \
  --summary "The concrete reusable deliverable" \
  --opportunity domain-short-name \
  --steward "Responsible person or team"
```

This creates a reusable project under `projects/incubator/`, links it back to
the opportunity, and includes source, tests, architecture, infrastructure, and
adoption sections.

## Publish it on the website

1. Review the opportunity or project.
2. Change `"visibility": "draft"` to `"visibility": "public"` in its JSON
   manifest.
3. Run `python3 tooling/foundry.py validate`.
4. The website build runs `python3 tooling/foundry.py export-catalog` and renders
   the corresponding Markdown page.

GitHub remains the source of truth. The website is the public view; it does not
hold a separate copy that must be maintained manually. See the complete
[website publishing contract](website/README.md).

## Deeper documentation

- [Mission and business need](PROJECT_INTENT.md)
- [System architecture](docs/ARCHITECTURE.md)
- [Research-to-project stages](docs/RESEARCH_TO_PROJECT_PIPELINE.md)
- [Content ownership and repository hygiene](docs/CONTENT_GOVERNANCE.md)
- [Free-first compute setup](setup/README.md)

## Shared AI context

Codex, Claude Code, and Gemini CLI use the same version-controlled context in
`.ai/`. Their native instruction files at the repository root point to one
canonical instruction file, preventing the tools from drifting apart.

See [`.ai/README.md`](.ai/README.md) for the layout and maintenance rules.

## Status

The repository foundation, reusable templates, and publishing contract are in
place. The next milestone is to publish one validated opportunity/project pair
through a minimal static website.
