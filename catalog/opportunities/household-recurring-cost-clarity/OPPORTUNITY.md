# Opportunity: Household Recurring Cost Clarity

> Private analysis that helps households identify recurring charges, price increases, and difficult-to-exit costs.

## Problem

Recurring charges, price changes, and fee unbundling are hard to see across long statements, so avoidable household costs persist unnoticed.

## People

People reviewing downloaded bank or card statements who want a private, understandable picture of recurring spending.

## Root cause

Exit friction and unbundled fees exploit fragmented records, inconsistent merchant labels, and the effort required to compare charges over time.

## Tool response

Analyze statements on-device, group likely recurring charges, flag changes with supporting rows, and offer document-auditor checklists for terms or cancellation steps.

## Governance response

Keep classifications explainable and user-correctable, avoid account connections and credentials, and distinguish suspected recurrence from confirmed obligations.

## Prior art

Commercial managers include Rocket Money, Trim, Monarch Money, and Copilot; the brief says these services rely on linked financial accounts and cloud-held transaction histories and may charge subscriptions or a share of negotiated savings. CloudSetup's `subscription-checker` is an existing local CSV proof of concept; the identified gap is a fully private, client-side statement analyser for recurring costs, price changes, and fee clusters.

## Guardrails

Keep financial data local, require no bank credentials, make no fraud determination, and provide neither financial, legal, nor medical advice. Do not recommend investments, refinancing, credit cards, bank accounts, or lending products. Clearly label results as descriptive statement analysis for budgeting clarity, and require the user to review findings before acting.

## Success measure

A user can confirm recurring charges and price changes from cited statement rows without sending financial data to a server.

## Evidence

The source brief labels the following claims verified:

| Claim | URL | Verified | Year |
|---|---|---|---|
| Subscription perception gap: estimated $86/mo vs actual $219/mo (2.5x gap) | [C+R Research Study](https://www.crresearch.com/blog/subscription-service-statistics-and-costs/) | Yes | 2022 |
| Zombie subscription waste: $252/yr ($21/mo) wasted on forgotten services | [CNET Subscription Survey 2026](https://www.cnet.com/tech/services-and-software/subscription-survey-2026/) | Yes | 2026 |
| Eighth Circuit vacated FTC Click-to-Cancel Negative Option Rule on July 8, 2025 | [Sidley Austin Analysis](https://www.sidley.com/en/insights/newsupdates/2025/07/us-ftc-click-to-cancel-rule-struck-down) | Yes | 2025 |
| Overdraft/NSF fees: 34% for <$65k vs 10% for >$175k; 81% frequent had bill strain | [CFPB Overdraft Report](https://www.consumerfinance.gov/data-research/research-reports/overdraft-and-nonsufficient-fund-fees-insights-from-the-making-ends-meet-survey-and-consumer-credit-panel/) | Yes | 2023 |
| Unbundled junk fees in leases & FTC proposed ban on deceptive hidden fees | [FTC Junk Fee Proposed Rule](https://www.ftc.gov/news-events/news/press-releases/2023/10/ftc-proposes-rule-ban-junk-fees) | Yes | 2023 |
| Payday loan APRs equate to almost 400% with repeated debt compounding | [CFPB Payday Loans](https://www.consumerfinance.gov/ask-cfpb/what-is-a-payday-loan-en-1567/) | Yes | 2023 |

## Traceability

- `[ai-inference]` `CloudSetup/scratchpad/research/SYNTHESIS-problem-cluster-map.md`
