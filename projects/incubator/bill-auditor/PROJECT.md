# Project: Bill Auditor

> A local-first tool that explains household bills, checks visible charges, and drafts user-reviewed questions or disputes.

## Scope

Accept a user-supplied bill, extract labeled charges with source locations, identify arithmetic or rule-check questions, and return a plain-language explanation, checklist, and draft message for user review.

Out of scope: automatic submission, representation, account access, eligibility decisions, medical interpretation, and conclusions that a charge is unlawful.

## Smallest increment

Support one redacted, text-based sample bill with deterministic charge extraction and arithmetic checks. Produce an explanation, a cited checklist of questions, and a clearly labeled draft inquiry that cannot be sent by the tool.

## Privacy and safety guardrails

- Process documents locally and do not retain them by default.
- Show source text for extracted facts and label uncertainty.
- Limit output to explain + checklist + draft for user review.
- Never provide legal or medical advice or claim professional authority.
- Require the user to review and decide before any external action.
- Use only local and free dependencies; zero spend is the default.

## Acceptance criteria

The sample output traces every extracted amount to its source, passes arithmetic tests, carries the advice boundary, and makes no network request.

## Provenance

- Opportunity: `catalog/opportunities/household-document-auditor/opportunity.json`
- Solution: `catalog/solutions/pattern-local-document-auditor/solution.json`
