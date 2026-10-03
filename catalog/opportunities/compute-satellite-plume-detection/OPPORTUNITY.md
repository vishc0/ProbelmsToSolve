# Opportunity: Satellite Thermal Remote Sensing & Plume Detection

## Decision summary

- Status: proposed
- Owner: Chippa Vishweshwar
- Domain: surveillance-and-sensing
- Horizon: 2027–2032
- Recommendation: Develop an open data pipeline for ingesting public satellite thermal infrared (TIR) imagery (Landsat 8/9, Sentinel) to detect anomalous hydrological heat plumes associated with subterranean or clandestine compute clusters.

## Problem and user

- Affected user or organization: Arms control auditors, treaty verification agencies, and non-proliferation NGOs.
- Current pain or constraint: Subterranean datacenters shield optical and EM emissions, but thermodynamic laws mandate rejecting 4.2 MW per $\text{m}^3/\text{s}$ per $1^\circ\text{C}$ temperature rise. Finding these thermal signatures manually over global river basins is infeasible.
- Evidence: Halstead & Larsen (*AI 2040 Covert AI Projects*) calculate that thermal satellites with $\text{NETD} \approx 0.2\text{ K}$ at 57m resolution can identify surface plumes down to $0.1^\circ\text{C}$ if automated differential time-series processing is applied.

## Proposed capability

- Outcome: An automated ingestion and computer-vision pipeline that queries free USGS/Copernicus thermal imagery, aligns temporal baseline rasters, subtracts seasonal diurnal patterns, and flags candidate thermal effluent plumes near industrial watercourses.
- Smallest valuable experiment: Download historical Landsat TIR tiles covering a known thermal benchmark (e.g. nuclear power plant discharge canal) and prove the detection algorithm flags the thermal anomaly above noise.
- Differentiation or research contribution: First open-source remote-sensing pipeline calibrated specifically for datacenter cooling thermodynamic signatures.

## Traceability

- Source claims: `source-claim: 2026-ai-futures-project-ai-2040-plan-a#covert-ai-projects`
- External evidence: `external-evidence: Landsat 8/9 Thermal Infrared Sensor (TIRS) specifications`
- AI inferences: `ai-inference: Data pipeline can leverage free Copernicus/USGS APIs and run batch processing in Kaggle/Colab free tiers.`
- Human directions and decisions: `human-direction: Zero-cloud spend, free compute first.`

## Assessment

- Expected value: Bridges high-level geopolitical treaty verification with practical geospatial intelligence tools.
- Feasibility: Medium (requires raster math and geospatial libraries: `rasterio`, `xarray`).
- Evidence strength: Physically grounded in thermal radiation physics and satellite telemetry.
- Cost and dependencies: Zero cloud cost; uses free satellite data portals and local/Kaggle compute.
- Risks and mitigations: False positives from industrial factories or natural hydrothermal vents; mitigated by correlating with electrical grid data and GMTI road logistics.
- Time-to-learning: 3–5 days.

## Promotion criteria

- Success metric: Reliable detection of a known $>50\text{ MW}$ aquatic thermal discharge plume with zero false positives on baseline river segments.
- Approval required: Owner authorization to promote to `projects/incubator/thermal-plume-sentinel`.
- Next action: Scaffold incubator project structure.