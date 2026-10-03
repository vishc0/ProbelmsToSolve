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

## Prior art

Proprietary services such as DoNotPay, Goodbill, and ClaimMedic may charge commissions and can raise unauthorized-practice-of-law concerns. `pdfplumber` and `tesseract` provide raw document parsing, while CloudSetup's `letter-explainer` provides basic text simplification; the brief identifies the missing layer as a fully local, open-source auditor that combines extraction, rule checks, explanations, and reviewable drafts.

## Guardrails

Keep documents local with no cloud transmission of medical history, Social Security numbers, or lease contracts; expose uncertainty; and operate only as explain + checklist + draft for user review, never legal or medical advice. The tool does not represent clients, assess treatment appropriateness, or provide binding counsel. The user reviews, confirms, and signs every draft before acting.

## Success measure

A user can verify the extracted facts and prepare a reviewable question or dispute draft without uploading the document or accepting an unsupported claim.

## Evidence

The source brief labels the following claims verified:

| Claim | URL | Verified | Year |
|---|---|---|---|
| In-network claim denials average 16.6% (48M+ claims denied; <0.2% appealed) | [KFF ACA Claim Denials](https://www.kff.org/private-insurance/claims-denials-and-appeals-in-aca-marketplace-plans/) | Yes | 2021 |
| 15M Americans carry $49B in medical debt on credit reports | [CFPB Medical Collections](https://www.consumerfinance.gov/data-research/research-reports/recent-changes-in-medical-collections-on-consumer-credit-records/) | Yes | 2023 |
| US healthcare admin paperwork $812B (34.2%, $2,479/capita vs Canada $551) | [PNHP Himmelstein et al.](https://pnhp.org/news/health-care-paperwork-cost-u-s-812-billion-in-2017-four-times-more-per-capita-than-in-canada/) | Yes | 2017 |
| 22.4M renter households cost-burdened (>30% income); 12.1M severely burdened | [Harvard JCHS 2024](https://www.jchs.harvard.edu/state-nations-housing-2024) | Yes | 2022 |
| Census ACS 2023: 49.7% of renter households cost-burdened; median ratio 31.0% | [Census ACS 2023 Release](https://www.census.gov/newsroom/press-releases/2024/renter-households-cost-burdened-race.html) | Yes | 2023 |
| Loss of 6.1M rental units below $1,000/mo between 2012 and 2022 | [Harvard JCHS 2024](https://www.jchs.harvard.edu/state-nations-housing-2024) | Yes | 2012–2022 |
| LSC 2022 Justice Gap: 92% civil legal needs unmet; 74% households 1+ problem | [LSC Justice Gap Study](https://justicegap.lsc.gov/resource/executive-summary/) | Yes | 2022 |
| 109,900 debt collection complaints to CFPB in 2023; top issue debt not owed | [CFPB Consumer Response 2023](https://www.consumerfinance.gov/data-research/research-reports/consumer-response-annual-report-2023/) | Yes | 2023 |

## Traceability

- `[ai-inference]` `CloudSetup/scratchpad/research/SYNTHESIS-problem-cluster-map.md`
