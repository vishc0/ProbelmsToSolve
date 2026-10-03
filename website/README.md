# Website Publishing Contract

The website is a public view of approved repository content. It is not a second
place to create or maintain opportunities and projects.

## Repository-to-website mapping

| Repository record | Website route | Public content |
|---|---|---|
| `catalog/domains/<id>/domain.json` | `/domains/<id>` | Domain metadata and linked work |
| `catalog/problems/<id>/problem.json` | `/problems/<id>` | Pain point, state, provenance, and links |
| `catalog/clusters/<id>/cluster.json` | `/clusters/<id>` | Shared root cause and related problems |
| `catalog/opportunities/<id>/opportunity.json` | `/opportunities/<slug>` | Card metadata, state, owner, and project link |
| `catalog/opportunities/<id>/OPPORTUNITY.md` | `/opportunities/<slug>` | Evidence-backed opportunity detail |
| `projects/incubator/<id>/project.json` | `/projects/<slug>` | Project metadata, maturity, steward, and repository link |
| `projects/incubator/<id>/PROJECT.md` | `/projects/<slug>` | Scope, requirements, milestones, cost, and provenance |
| `projects/reference/<id>/...` | `/projects/<slug>` | Validated reference project and adoption package |
| `catalog/solutions/<id>/solution.json` | `/solutions/<id>` | Reusable pattern and implementations |

## Publication flow

1. Create and review the repository record as a draft.
2. Validate it with `python3 tooling/foundry.py validate`.
3. Approve publication and change `visibility` from `draft` to `public`.
4. The website build runs `python3 tooling/foundry.py validate`, then
   `python3 tooling/foundry.py export-catalog`.
5. The site renders the exported metadata and the referenced Markdown.
6. “Adopt this project” and “Contribute” link to GitHub issues and pull
   requests, where identity, discussion, and review already exist.

## Source-of-truth rule

- Edit foundry records in GitHub, not in the deployed website.
- Do not commit exported catalog JSON; it is a disposable build artifact.
- Markdown indexes under `catalog/indexes/` are generated navigation; rebuild
  them with `python3 tooling/foundry.py index`.
- A site page disappears on the next build if its record is no longer public.
- The public site never reads `.ai/`, `scratchpad/`, private sources, or drafts.

## Implementation boundary

The website framework and host are intentionally not selected yet. Any static
site generator or web framework is acceptable if it follows this contract. The
MVP needs catalog listing, detail pages, search/filtering, GitHub links, and no
public LLM endpoint.
