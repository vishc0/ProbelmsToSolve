# Opportunity: Cultivation Incentives and Grower Networks

> Evidence-linked planning and open matching tools help growers and institutions compare incentives and coordinate production.

## Owner direction

`[human-direction]` Match public cultivation incentives to soils and environments, help growers network, and consider livestock and feed systems as part of the same production system.

## Problem

Growers face fragmented incentive rules, environmental data, market signals, livestock-feed dependencies, and collaboration channels, making coordinated and locally suitable decisions difficult.

## People

Growers, livestock producers, cooperatives, extension services, local communities, program administrators, and food-system planners.

## Root causes

- A few buyers, input providers, or platforms may control access and terms (`cluster-concentrated-gatekeepers`, D).
- Food production depends on fragile inputs, infrastructure, and biological cycles (`cluster-brittle-essential-systems`, J).

## Tool ideas from the plan

Create an incentive-design explorer and opt-in grower matching based on verified program rules, soil and climate context, crop plans, and livestock or feed needs. Use P3 atlas data only after its provenance and limitations are reviewed.

## Governance options

Compare grants, insurance, price supports, procurement, extension support, cooperative networks, and market-led coordination on fairness, environmental outcomes, administrative cost, and unintended incentives.

## Guardrails

- Explain eligibility and trade-offs; do not decide awards or submit applications automatically.
- Protect farm, location, and commercial data; make network participation opt-in.
- Avoid production, yield, eligibility, or income guarantees.
- Claims favoring organic methods across all contexts are contested and need evidence on yield, nutrition, environment, labor, and cost.
- Label funding estimates as non-binding education and direct users to their county NRCS service center.
- Include applicable biological-soil-amendment composting guidance for manure-based exchanges.

## Evidence

The P5 brief describes concentration of commodity support, oversubscribed conservation programs, large feed and ethanol shares of crop calories, and concentrated meat processing. It proposes matching public conservation practices to soil context while connecting nearby feed and livestock operations.

### Prior art

- [USDA NRCS CART](https://www.nrcs.usda.gov/conservation-basics/conservation-by-state/conservation-assessment-ranking-tool-cart) scores resource concerns and conservation practices.
- [NRCS Conservation Practice Standards](https://www.nrcs.usda.gov/resources/guides-and-instructions/conservation-practice-standards) include CPS 340 Cover Crop and CPS 528 Prescribed Grazing.
- [OpenTEAM](https://github.com/Open-TEAM) is an open-source farmer-led data ecosystem; the [NSAC Grassroots Guide](https://sustainableagriculture.net/publications/grassrootsguide/) covers federal farm and conservation programs.

### Options and trade-offs

- Yield-based subsidies produce high volumes of cheap commodity calories, but can worsen erosion, consolidation, and disincentives to diversify.
- Private carbon markets bring corporate capital, but measurement, price volatility, and broker fees are concerns.
- Soil-matched public incentives can reward restoration and resilient feed systems, but require inspection and monitoring capacity.
- An open matcher is free and improves navigation and coordination, but supplies no direct capital.

### Verification table

| Claim / Figure | URL Verified | Status | Data Year |
| :--- | :--- | :--- | :--- |
| Top 10% farm subsidy recipients collect >65% commodity funds | `https://www.ers.usda.gov/topics/farm-economy/farm-household-well-being/` | Verified | 2023 |
| USDA NRCS: Only 24% of EQIP and 37% of CSP applicants funded | `https://www.nrcs.usda.gov/programs-initiatives/eqip-environmental-quality-incentives` | Verified | FY2023/2024 |
| 36% to 40% of global crop calories used as livestock feed | `https://iopscience.iop.org/article/10.1088/1748-9326/8/3/034015` | Verified | 2013/2022 |
| ~40% US corn used for feed, ~35-40% for fuel ethanol | `https://www.ers.usda.gov/data-products/feed-grains-database/` | Verified | 2024 |
| 4 meatpackers control >80% of US steer & heifer slaughter | `https://www.ers.usda.gov/publications/106794` | Verified | 2023 |
| USDA NRCS CART: Automated scoring for conservation applications | `https://www.nrcs.usda.gov/conservation-basics/conservation-by-state/conservation-assessment-ranking-tool-cart` | Verified | 2024 |
| USDA NRCS: Conservation Practice Standards CPS 340 and CPS 528 | `https://www.nrcs.usda.gov/resources/guides-and-instructions/conservation-practice-standards` | Verified | 2024 |
| NSAC: Grassroots Guide to Federal Farm and Conservation Programs | `https://sustainableagriculture.net/publications/grassrootsguide/` | Verified | 2023 |

## Traceability

- `[human-direction]` `CloudSetup/scratchpad/coordination/PROJECT-AREAS-from-todos.md` (P5)
- Depends on: `catalog/opportunities/soil-mineral-atlas/opportunity.json`
- Solution patterns: `pattern-open-data-observatory`, `pattern-open-interoperability`
