# Opportunity: Water Systems Stewardship

> Open service-quality data and operator support improve accountable stewardship of waterways, treatment, and distribution.

## Owner direction

`[human-direction]` Manage and optimize waterways, treatment plants, and distribution as active government projects, not only as policy subjects.

## Problem

Water quality, loss, maintenance, watershed, energy, and service data are divided across operators and jurisdictions, while aging physical systems make failures expensive and difficult to diagnose.

## People

Households, utility workers, watershed communities, treatment operators, local governments, regulators, and people with unreliable or unaffordable water service.

## Root causes

- Watershed, treatment, distribution, and governance actors optimize separate layers without one accountable system view (`cluster-fragmented-systems-no-owner`, I).
- Long-lived, capital-intensive water assets retain single points of failure (`cluster-brittle-essential-systems`, J).

## Tool ideas from the plan

Create a water-loss and service-quality dashboard from licensed public utility data, plus local operator training linked to P1. Later sensing pilots may flag anomalies for human review, never control treatment or distribution.

## Governance options

Compare municipal departments, public authorities, regulated private utilities, cooperatives, concession models, and watershed partnerships on access, quality, cost, workforce capacity, accountability, and resilience.

## Guardrails

- Public ownership is an owner direction and a contested policy claim; comparative outcome evidence is required.
- Never automate chemical dosing, plant controls, shutoffs, or public-health declarations.
- Publish data dates, coverage gaps, definitions, and uncertainty; protect infrastructure-sensitive details.
- Require qualified operators and applicable regulators for operational decisions.
- Distinguish administrative or monitoring violations from acute health advisories and show contaminant levels relative to applicable EPA MCLs.
- Do not provide unverified hydraulic calculations for active pipe repairs.

## Evidence

The P6 brief documents drinking-water capital needs, lead service lines, treated-water losses and main breaks, PFAS limits, and fragmentation across more than 50,000 community systems. It proposes a public audit tool based on open compliance data while recognizing that software cannot replace buried infrastructure.

### Prior art

- [EPA Drinking Water State Revolving Fund](https://www.epa.gov/dwsrf) provides federal-state municipal infrastructure financing.
- [EPA EPANET](https://www.epa.gov/water-research/epanet) is a Public Domain hydraulic and water-quality network model.
- [EPA ECHO](https://echo.epa.gov/tools/data-downloads) provides Public Domain Safe Drinking Water Act compliance and violation data.

### Options and trade-offs

- Private concessions can provide capital without a bond referendum, but the brief cites higher rates and reduced maintenance reinvestment.
- Municipal utilities retain local control and revenue, but small tax bases can drive deferred maintenance and compliance failures.
- Direct public project stewardship could standardize lead abatement and safety, but requires major appropriations and cross-jurisdiction governance.
- Open audit tooling can expose leak and violation trends at zero cost, but cannot replace physical infrastructure.

### Verification table

| Claim / Figure | URL Verified | Status | Data Year |
| :--- | :--- | :--- | :--- |
| EPA 7th DWINSA: $625B 20-year drinking water capital need | `https://www.epa.gov/dwsrf/epas-7th-drinking-water-infrastructure-needs-survey-and-assessment` | Verified | 2021 (Pub 2023) |
| EPA: 9.2 million active lead service lines in the US | `https://www.epa.gov/ground-water-and-drinking-water/lead-and-copper-rule-improvements` | Verified | 2023 |
| ASCE / AWWA: ~6 billion gallons treated water lost per day in US | `https://infrastructurereportcard.org/cat-item/drinking-water-infrastructure/` | Verified | 2021/2024 |
| ASCE: ~240,000 water main breaks occur annually across the US | `https://infrastructurereportcard.org/cat-item/drinking-water-infrastructure/` | Verified | 2021/2024 |
| EPA final PFAS rule: 4.0 ppt standards for PFOA and PFOS | `https://www.epa.gov/sdwa/and-polyfluoroalkyl-substances-pfas` | Verified | 2024 (Apr) |
| EPA SDWIS / ECHO: >50,000 community water systems in the US | `https://echo.epa.gov/tools/data-downloads` | Verified | 2023/2024 |
| Food & Water Watch: Private water utilities charge 59% higher rates | `https://www.foodandwaterwatch.org/2015/08/02/water-privatization-facts-and-figures/` | Verified | 2015/2023 |
| EPA EPANET: Open-source public domain hydraulic modeling engine | `https://www.epa.gov/water-research/epanet` | Verified | 2020/2023 |

## Traceability

- `[human-direction]` `CloudSetup/scratchpad/coordination/PROJECT-AREAS-from-todos.md` (P6)
- Related workforce pathway: `catalog/opportunities/workforce-reskilling-for-buildout/opportunity.json`
- Solution patterns: `pattern-open-data-observatory`, `pattern-edge-sensing-small-model`, `pattern-open-interoperability`
