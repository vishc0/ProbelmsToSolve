# Solution Pattern: Local Document Auditor

> Use local models and deterministic rules to extract facts, compare public rules, and draft user-reviewed responses.

## Applicable context

Use for bills, notices, contracts, renewals, and disputes where a person needs to understand a document and decide what to ask next.

## Pattern

Process the document locally, extract claims and charges, show the source text, apply versioned public rules, produce a checklist, and draft language that the user must review before using.

## Tradeoffs and failure modes

Documents may be incomplete, extraction can be wrong, and rules vary by place and date. Never present output as legal or medical advice or send it automatically.

## Safety and cost boundaries

Keep sensitive documents local, make uncertainty visible, require user review, and retain a zero-spend default.
