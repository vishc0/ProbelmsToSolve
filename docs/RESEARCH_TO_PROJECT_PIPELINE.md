# Research-to-Project Pipeline

## Stages

1. **Register** — capture source identity, rights, version, and provenance.
2. **Parse** — create addressable sections and structured metadata.
3. **Extract** — identify claims, assumptions, scenarios, recommendations,
   uncertainties, risks, actors, and enabling capabilities.
4. **Challenge** — search for corroboration, contradiction, prior art, and
   implementation evidence.
5. **Expand** — register problems once, connect them to sector domains and
   controlled facets, and group shared root causes into cross-domain clusters.
6. **Steer** — human branches, combines, prunes, ranks, or redirects the tree.
7. **Assess** — form opportunities around one or more clusters and score value,
   evidence, feasibility, differentiation, cost, risk, and time-to-learning.
8. **Blueprint** — generate a traceable project charter, requirements,
   architecture, milestones, evaluation, governance, and adoption plan.
9. **Scaffold** — instantiate the smallest runnable starter from approved
   templates.
10. **Validate** — test technical behavior, cost assumptions, safety, usability,
    and organizational fit; extract reusable solution patterns.
11. **Publish** — human approves a versioned public artifact and attribution.
12. **Refresh** — new evidence creates a review task, never a silent rewrite.

## Promotion gates

| From | To | Required evidence |
|---|---|---|
| Source | Analysis | Provenance, rights note, extraction review |
| Analysis | Problem | Traceable pain point, affected user, evidence, uncertainty |
| Problem | Cluster | Supported shared-root-cause hypothesis |
| Cluster | Opportunity | Bounded intervention and measurable public value |
| Opportunity | Incubator | Owner approval, smallest experiment, cost/risk ceiling |
| Incubator | Reference | Runnable artifact, tests, measured results, adoption docs |
| Draft | Published | Attribution, safety/license review, owner approval |

## Authorship labels

Every material assertion uses one of:

- `source-claim`
- `external-evidence`
- `ai-inference`
- `human-direction`
- `human-decision`
- `implementation-result`

## Catalog integrity

The manifests, rather than prose indexes, own lifecycle and relationships.
Run `python3 tooling/foundry.py validate` to catch duplicate IDs and dangling
domain (including aliases), cluster, opportunity, project, or solution links,
and rejects unknown facet values. Run
`python3 tooling/foundry.py index` to rebuild browsable catalog views.
