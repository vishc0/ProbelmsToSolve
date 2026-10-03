# Opportunity: Food Machinery Maintenance

> Extend the existing SME machinery copilot concept for safe, affordable maintenance of food and seed production equipment.

## Owner direction

`[human-direction]` Improve food quality and yield through capable large machinery, local manufacturing capacity, and reliable maintenance for food and seed production.

## Problem

Small producers and food processors can be locked out of predictive maintenance, compatible diagnostics, and repair knowledge for expensive machinery, increasing downtime and dependence on a few vendors.

## People

Farmers, food-plant operators, maintenance technicians, small manufacturers, cooperatives, and the communities that depend on reliable food production.

## Root causes

Capital-intensive machinery, proprietary interfaces, limited repair access, and scarce test equipment create single points of failure (`cluster-brittle-essential-systems`, J).

## Tool ideas from the plan

Extend and link to the existing `sme-machinery-copilot` research concept: low-cost acoustic and vibration sensing, a narrow local model, explainable maintenance flags, and technician review. Do not create a duplicate project. Adapt only after evidence and machinery-specific testing.

## Governance options

Compare right-to-repair rules, open telemetry standards, vendor service contracts, cooperative maintenance pools, public training, and manufacturer-led support on safety, cost, availability, and accountability.

## Guardrails

- Advisory diagnostics only; never autonomously control machinery.
- Require equipment-specific safety review and qualified technician confirmation.
- Display uncertainty and avoid warranty, uptime, or fault-detection guarantees.
- Keep sensor data local where possible and use zero-spend prototypes before hardware purchases.

## Evidence

TODO: merge Antigravity brief scratchpad/research/areas/food-machinery-maintenance.md

Brief pending.

## Traceability

- `[human-direction]` `CloudSetup/scratchpad/coordination/PROJECT-AREAS-from-todos.md` (P2)
- Existing concept: `CloudSetup/scratchpad/research/energy-manufacturing-food-draft.md` (`sme-machinery-copilot`)
- Solution pattern: `catalog/solutions/pattern-edge-sensing-small-model/solution.json`
