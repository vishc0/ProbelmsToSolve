# Project: Veto and Commitment Tracker

> A reproducible, neutral tracker for institutional vetoes and public commitments.

## Scope

Ingest a small, openly licensed dataset of institutional veto events and public commitments; normalize source metadata; and generate a neutral static table with definitions and limitations.

Out of scope: advocacy rankings, inferred motives, conflict prediction, diplomatic recommendations, or automated claims about compliance.

## Smallest increment

Create one versioned sample dataset and a deterministic static view that lists event date, institution, action, stated commitment, source link, and data limitation. Add a human-review checklist and a draft correction note template.

## Privacy and safety guardrails

- Use public institutional records and minimize personal data.
- Cite every event and preserve observed fact versus interpretation.
- Review source licences before inclusion and publish corrections transparently.
- Limit assistance to explain + checklist + draft for user review.
- Never provide legal or medical advice or present analysis as official policy.
- Use local tooling and static outputs; zero spend is the default.

## Acceptance criteria

A reviewer can regenerate the view, trace every row to a source, confirm licence notes, and verify that the presentation remains neutral.

## Provenance

- Opportunity: `catalog/opportunities/open-governance-observatory/opportunity.json`
- Solution: `catalog/solutions/pattern-open-data-observatory/solution.json`
