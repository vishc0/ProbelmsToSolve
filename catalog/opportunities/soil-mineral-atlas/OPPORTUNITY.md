# Opportunity: Soil and Mineral Atlas

> An open evidence atlas connects soil conditions, crop nutrient uptake, and context-specific restoration practices.

## Owner direction

`[human-direction]` Make soil mineral gaps, crop-to-human nutrient pathways, and ways to revive soil for future growing cycles easier to understand and act on.

## Problem

Soil tests, land characteristics, crop nutrient research, and restoration guidance are fragmented, use incompatible definitions, and can be difficult for growers and communities to interpret together.

## People

Growers, extension workers, soil laboratories, nutrition researchers, land stewards, public agencies, and communities concerned with long-term food quality.

## Root causes

Testing coverage, agronomic evidence, and locally relevant guidance depend on specialized institutions and costly physical systems with uneven access (`cluster-brittle-essential-systems`, J).

## Tool ideas from the plan

Create a reproducible atlas from public soil datasets, crop-mineral uptake evidence, and restoration practices, with a farmer-friendly explainer. Accept optional local sensor or laboratory inputs only with clear provenance, units, uncertainty, and geographic limits.

## Governance options

Compare public mapping, university extension, cooperative data trusts, commercial testing, and farmer-controlled data-sharing arrangements. Assess data quality, consent, local relevance, maintenance cost, and access without prescribing ownership.

## Guardrails

- Do not infer individual health outcomes or give medical advice from soil or crop data.
- Do not prescribe fertilizer, amendments, or land treatments without qualified local review.
- Label modelled values separately from measurements and publish dataset dates and licences.
- Claims that organic production is inherently more nutritious, productive, or environmentally beneficial are contested and need evidence by context.
- Warn that regional estimates cannot replace certified wet-chemistry tests before concentrated mineral amendments; excess boron, copper, or selenium can damage soil or crops.

## Evidence

The P3 brief connects degraded soil management, micronutrient deficiency, soil-carbon depletion, crop nutrient trends, and the cost of commercial soil testing. It proposes an informational atlas built from open soil and food-composition datasets, not a substitute for laboratory assays.

### Prior art

- [ISRIC SoilGrids](https://www.isric.org/explore/soilgrids) provides CC BY 4.0 global 250 m layers for pH, organic carbon, CEC, and bulk density.
- [USDA NRCS SSURGO](https://www.nrcs.usda.gov/resources/data-and-reports/soil-survey-geographic-database-ssurgo) and [USDA FoodData Central](https://fdc.nal.usda.gov/food-search) are Public Domain soil and food-composition datasets.
- QGIS and GDAL provide open geospatial raster and overlay tooling.

### Options and trade-offs

- Synthetic micronutrient additives can correct acute deficiencies quickly, but recur in cost, risk phytotoxicity, and do not rebuild biological structure.
- Rock dust, cover crops, and compost rebuild soil carbon and mineral cycling, but work slowly and can create logistics burdens.
- Genetic biofortification can raise target nutrient uptake, but can involve IP restrictions and does not resolve underlying soil degradation.
- An open knowledge commons is low-cost and actionable, but cannot replace wet-chemistry assays.

### Verification table

| Claim / Figure | URL Verified | Status | Data Year |
| :--- | :--- | :--- | :--- |
| FAO SWSR: 52.5% poor/very poor soil management; 58% worsening | `https://www.fao.org/global-soil-partnership/Scientific-and-technical-support/itps/status-of-the-worlds-soil-resources/en` | Verified | 2026 |
| WHO: >2 billion people suffer micronutrient deficiencies | `https://www.who.int/health-topics/micronutrients` | Verified | 2024 |
| FAO GSOCmap: 50% to 70% soil organic carbon lost in cultivated soils | `https://openknowledge.fao.org/handle/20.500.14283/ca7597en` | Verified | 2020 |
| Davis et al. / USDA: 5% to 40% nutrient decline in 43 crops | `https://pubmed.ncbi.nlm.nih.gov/15637215/` | Verified | 2004 |
| Commercial soil testing panel fees range from $50 to $150/sample | `https://soilhealth.cals.cornell.edu/testing-services/comprehensive-soil-health-assessment/` | Verified | 2024 |
| ISRIC SoilGrids: Global 250m machine-learning digital soil maps | `https://www.isric.org/explore/soilgrids` | Verified | 2020/2024 |
| USDA NRCS SSURGO: Soil survey coverage across >95% of US counties | `https://www.nrcs.usda.gov/resources/data-and-reports/soil-survey-geographic-database-ssurgo` | Verified | 2023 |
| USDA FoodData Central: Open nutritional composition food portal | `https://fdc.nal.usda.gov/food-search` | Verified | 2024 |

## Traceability

- `[human-direction]` `CloudSetup/scratchpad/coordination/PROJECT-AREAS-from-todos.md` (P3)
- Solution patterns: `pattern-open-data-observatory`, `pattern-edge-sensing-small-model`
