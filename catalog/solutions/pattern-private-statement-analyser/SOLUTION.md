# Solution Pattern: Private Statement Analyser

> Analyze financial, pay, or meter statements on-device to surface recurring costs, changes, and discrepancies.

## Applicable context

Use when a person can export structured statements but should not have to disclose the underlying financial, employment, or household data.

## Pattern

Normalize local files, group comparable entries, identify recurrence and changes, show the contributing rows, and let the user confirm or correct classifications.

## Tradeoffs and failure modes

Merchant names and billing cycles vary, and similarity can create false matches. Results should be explainable flags, not claims of fraud or entitlement.

## Safety and cost boundaries

Default to on-device processing, minimize retained data, avoid account credentials, and require no paid service.
