# Project: Skills Bridge

> A private local tutor maps worker experience to trade competencies and accredited learning pathways.

- Project ID: `skills-bridge`
- Primary domain: `work-and-livelihoods`
- Additional domains: `education-and-skills`, `energy-and-infrastructure`
- Originating opportunity: `catalog/opportunities/workforce-reskilling-for-buildout/opportunity.json`
- Initial steward: Unassigned

## Outcome

A worker can privately describe prior experience, see an explainable mapping to one trade competency framework, identify gaps, and receive a study plan that points to accredited training and certification.

## Users and use cases

The first user is a worker exploring a transition into electrical maintenance. Training providers and workforce advisers may use the same export with the worker's consent.

## Smallest increment

Support one electrical-maintenance pathway in one stated jurisdiction: import a versioned public competency framework, map a user-reviewed experience profile, identify evidence-backed gaps, generate a study plan, and quiz against cited public material.

## In scope

- Local intake of worker experience and goals.
- Explainable mapping to versioned public competencies.
- Study planning, practice questions, and links to accredited providers or certifiers.
- User-controlled correction, export, and deletion.

## Out of scope

- Awarding or replacing certification, licensing, apprenticeships, or supervised practice.
- Guaranteeing eligibility, employment, pay, admission, or exam success.
- Ranking or rejecting workers for employers.
- Unsupervised safety-critical electrical or industrial instructions.

## Architecture

Run a local model over locally stored user data. Use deterministic retrieval from a small, reviewed competency corpus; show the cited source and reasoning for every mapping; require user confirmation before saving or exporting it.

## Acceptance criteria

- A reviewer can reproduce each mapping from the cited competency framework.
- The interface distinguishes demonstrated, inferred, and missing competencies.
- Every certification reference names its issuer, jurisdiction, and source version.
- A user can run the increment without a paid API and delete all local personal data.
- Safety tests reject claims that the tool certifies the worker or authorizes hazardous work.

## Cost model

Zero-spend default: existing laptop, local model, public curricula, and static/local storage. Any paid course, exam, hardware, API, cloud service, or publication requires explicit owner approval and must be optional.

## Risks, governance, and approval gates

Protect work histories as sensitive personal data; test for biased competency inference; display uncertainty; review curriculum licences; and require human review. Accredited bodies remain authoritative. Publishing, paid services, and external data sharing require owner approval.

## Evidence and provenance

- `[human-direction]` `CloudSetup/scratchpad/coordination/PROJECT-AREAS-from-todos.md` (P1)
- Opportunity: `catalog/opportunities/workforce-reskilling-for-buildout/opportunity.json`
- Reused pattern: `catalog/solutions/pattern-local-document-auditor/solution.json`
