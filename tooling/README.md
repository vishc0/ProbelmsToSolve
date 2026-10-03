# Foundry Tooling

`foundry.py` is the deterministic entry point for creating opportunities,
promoting them into reusable projects, validating their website manifests, and
exporting public catalog data.

## Create an opportunity

```bash
python3 tooling/foundry.py new-opportunity \
  --id domain-short-name \
  --title "Human-readable title" \
  --summary "One sentence describing the value" \
  --domain domain-id \
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
python3 tooling/foundry.py export-catalog --include-drafts
```

The production website omits `--include-drafts`, so only records whose
`visibility` is `public` are published. Generated catalog output is build data;
do not commit it as a second source of truth.
