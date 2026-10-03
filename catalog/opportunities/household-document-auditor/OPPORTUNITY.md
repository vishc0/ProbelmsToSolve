# Opportunity: Household Document Auditor

> A local, user-controlled assistant that explains bills and notices, checks them against public rules, and drafts reviewable responses.

## Problem

Complex documents and dispute processes transfer time and money from households that cannot readily interpret terms, reconstruct charges, or persist through denials and paperwork.

## People

Households reviewing bills, benefits notices, leases, subscription terms, and other consequential documents.

## Root cause

Denial-by-default, fine print, exit friction, paperwork churn, and late fees combine information asymmetry with high effort for the individual.

## Tool response

Run locally; extract claims and charges with citations to the document; compare applicable public rules; then produce an explanation, checklist, and draft response for user review.

## Governance response

Maintain versioned rule sources, show jurisdiction and effective date, separate extraction from inference, and prohibit automatic submission or representation.

## Guardrails

Keep documents local by default, expose uncertainty, and never provide legal or medical advice. The user reviews every checklist and draft before acting.

## Success measure

A user can verify the extracted facts and prepare a reviewable question or dispute draft without uploading the document or accepting an unsupported claim.

## Evidence

TODO: merge verified brief

## Traceability

- `[ai-inference]` `CloudSetup/scratchpad/research/SYNTHESIS-problem-cluster-map.md`
