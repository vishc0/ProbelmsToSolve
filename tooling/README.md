# Foundry Tooling

`foundry.py` creates typed foundry records, validates their relationships,
generates browsable indexes, and exports public website data.

## Create catalog records

```bash
python3 tooling/foundry.py new-domain --help
python3 tooling/foundry.py new-problem --help
python3 tooling/foundry.py new-cluster --help
python3 tooling/foundry.py new-solution --help
```

Problems can link to several domains and clusters. Clusters capture shared root
causes across domains. Projects link to one or more opportunities and reusable
solution patterns. Domains may use `--parent` and repeatable `--alias`; all
record commands accept repeatable controlled facet options such as `--mission`,
`--capability`, `--population`, `--geography`, and `--topic`.

Controlled values are:

- `mission`: `everyday-ai-empowerment`
- `capability`: `sensing`, `verification`
- `population`: `households`, `workers`, `communities`, `institutions`
- `geography`: `local`, `national`, `global`
- `topic`: `addiction`, `ai-control`, `compute-governance`,
  `consumer-protection`, `energy-resilience`, `household-costs`,
  `mental-health`, `research-evaluation`, `supply-chains`

## Create an opportunity

```bash
python3 tooling/foundry.py new-opportunity \
  --id domain-short-name \
  --title "Human-readable title" \
  --summary "One sentence describing the value" \
  --domain domain-id \
  --cluster shared-root-cause \
  --owner "Owner name"
```

Complete the generated
`catalog/opportunities/domain-short-name/OPPORTUNITY.md`. Keep its
`opportunity.json` metadata in sync when its status or visibility changes.

## Promote an approved opportunity

```bash
python3 tooling/foundry.py new-project \
  --id project-short-name \
  --title "Project name" \
  --summary "One sentence describing the deliverable" \
  --opportunity domain-short-name \
  --steward "Steward name"
```

This creates a complete incubator project and links the opportunity manifest to
it. It refuses to overwrite an existing directory.

## Validate and preview website data

```bash
python3 tooling/foundry.py validate
python3 tooling/foundry.py index
python3 tooling/foundry.py export-catalog --include-drafts
```

The index command regenerates marked Markdown views by domain, controlled
facet, problem cluster, lifecycle state, and solution pattern.

The production website omits `--include-drafts`, so only records whose
`visibility` is `public` are published. Generated catalog output is build data;
do not commit it as a second source of truth.

## Check document size

```bash
python3 tooling/check_markdown_size.py
```

Every Markdown file must remain within the fixed 200-line repository limit.
