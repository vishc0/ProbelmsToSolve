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

## Pathway Spec for skills-bridge

### Competencies

- AC/DC circuit theory; Ohm's and Kirchhoff's laws.
- Single- and three-phase power calculations and conduit-bending geometry.
- Schematic and ladder-diagram interpretation, including relays, contactors, transformers, and breaker symbols.
- Digital multimeter use, fault-isolation logic, Lockout/Tagout, and NFPA 70E / OSHA safety fundamentals.

### Sources and licences

- [O*NET 47-2111.00](https://www.onetonline.org/link/summary/47-2111.00) task and knowledge statements, USDOL/ETA, [CC BY 4.0](https://www.onetcenter.org/license.html).
- [OpenStax University Physics Vol 2](https://openstax.org/details/books/university-physics-volume-2) circuit modules, Rice University, CC BY 4.0.
- U.S. Navy NEETS Modules 1–3 electrical fundamentals, U.S. Navy, Public Domain.
- [DGT / Bharat Skills CTS Electrician Question Bank](https://bharatskills.gov.in/Home/StudyMaterial?course=9ZlG2Uo6XjY=&name=Electrician), Ministry of Skill Development, open educational access.

### Diagnostic flow

1. Screen trade numeracy: fractions, decimals, algebraic transposition, `V = I × R`, and `P = V × I`.
2. Test schematic decoding through identification of industrial electrical symbols.
3. Test fault-isolation logic with stepwise continuity, voltage-drop, and fuse-isolation scenarios.
4. Produce a gap profile mapped to public IBEW JATC, Red Seal, or ITI entrance criteria.

### Never-do rules

- Never authorize, instruct, or simulate physical live electrical work or energized troubleshooting (arc-flash/electrocution lethal hazard).
- Never issue journeyman licences, state certifications, or claim legal regulatory authority.
- Never monetize test results, exfiltrate user data, or funnel users to predatory private for-profit bootcamps.

### qwen3.5-agent build notes

Implement a lightweight local CLI or web tool using `qwen3.5-agent` with a 16K context through Ollama on CPU or local GPU. Reuse the `homework-helper` Socratic pattern with no network spend and complete user privacy.

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
