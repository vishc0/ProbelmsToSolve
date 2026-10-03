# Covert AI Projects & Technical Detection Vectors

A central failure mode of any international AI slowdown agreement is defection via clandestine, unmonitored clusters ("covert projects"). *AI 2040* models the physical, logistical, and computational constraints an actor faces when attempting to build and operate a covert supercomputing cluster.

---

## 1. Threat Model & Covert Project Requirements

To successfully develop game-changing or unaligned AI in secret without detection, an adversary must achieve all of the following:

1. **Procure Sufficient Compute:** Divert or acquire $\approx 1.5\text{ Million H100e}$ (approx. 7% of Chinese 2028 stock). Pathways include:
   - Siphoning smuggled consumer/enterprise accelerator cards.
   - Fraudulent decommissioning (falsifying destruction/recycling manifests of retired silicon).
   - Falsifying upstream fab foundry records (TSMC/SMIC packaging output).
2. **Conceal Physical Datacenter:** Construct subterranean facilities to defeat optical satellite reconnaissance.
3. **Power & Cool Subterranean Facilities:** Provide 50–200 MW of continuous electrical power and reject massive thermal energy without generating an infrared-visible surface signature.
4. **Operate Without Information Leakage:** Shield the project from human intelligence (HUMINT), signals intelligence (SIGINT), cyber backdoors, and AI-assisted whistleblower algorithms.

---

## 2. Thermodynamics of Covert Heat Rejection

Heat dissipation is the most difficult physical constraint for subterranean datacenters to conceal:

### Thermodynamic Discharge Equations
Water carries 4.2 Megawatts per degree Celsius of temperature rise per cubic meter per second:
$$\dot{Q} = \dot{m} \cdot C_p \cdot \Delta T \approx 4.2 \text{ MW} \cdot \left(\frac{\text{m}^3}{\text{s}}\right) \cdot (^\circ\text{C})^{-1}$$

For a modest 100 MW covert datacenter:
- If coolant discharge is heated by $\Delta T = 10^\circ\text{C}$, it requires a flow rate of $\approx 2.4 \text{ m}^3/\text{s}$.
- If diluted directly into a river or ocean, thermal satellites with modern sensor sensitivity ($\Delta T_{\text{NETD}} \approx 0.2\text{ K}$ at 57m resolution) can detect surface plumes exceeding **$0.1^\circ\text{C}$**.
- To remain undetectable ($\Delta T < 0.1^\circ\text{C}$), the facility must dilute effluent into a high-flow water body requiring at least **$240 \text{ m}^3/\text{s}$** of cold water circulation (equivalent to the coolant volume of a major nuclear power station).

### Detection Feasibility Matrix

| Siting Strategy | Thermal Camouflage | Satellite Vulnerability | Seismic / Radar Vulnerability |
| :--- | :--- | :--- | :--- |
| **Deep Underground + River Heat Exchanger** | High (if deep diffuser manifolds dilute plume) | Medium (IR satellites flag water temperature deltas) | Low |
| **Subsurface + Cooling Towers** | Zero (Atmospheric vapor plumes and IR bloom immediately visible) | Extremely High (Optical and IR) | Low |
| **Co-located Industrial Plant (e.g. Aluminum Smelter)** | High (Datacenter waste heat masked by heavy metallurgy) | Low (Thermal baseline already elevated) | High (Perfluorocarbon [PFC] emissions and electrical feed discrepancies) |
| **Deep Sea / Ocean Siting** | Very High (Thermal mixing at depth) | Very Low | High (Naval sonar and maritime logistics tracking) |

---

## 3. Remote Sensing & Space-Based Surveillance Vectors

The AI Futures Project outlines key surveillance vectors deployed to police the accord:

- **Thermal Infrared (TIR) Satellites:** Multi-temporal thermal imaging (e.g., Landsat 8/9, commercial thermal constellations) measuring diurnal surface variations over suspected subterranean sites.
- **Ground Moving Target Indicator (GMTI) Radar:** Space Force GMTI satellite constellations (projected operational by 2028–2030) detecting vehicle movement, earth-moving logistics, and anomalous supply patterns in remote mountainous terrain.
- **Supply-Chain Micro-Audits:** Tracking high-purity electrical infrastructure (transformers, harmonic filters, switchgear, liquid-cooling manifolds) whose manufacturing and procurement cannot easily be faked.

---

## 4. The Software Leakage Dilemma: Why Software Accelerates Covert Actors

A pivotal theoretical insight in *AI 2040* is the asymmetric benefit of software efficiency to covert projects:

1. **Hardware vs. Software Bounds:**
   - A covert project is strictly **hardware-constrained** (bound to dark compute $\le 1\%$ of global stock).
   - The open consortium is **hardware-rich** (controlling 99%+ of global compute).
2. **The Leakage Vector:**
   - Under Plan A's Total Research Transparency, algorithmic breakthroughs (synthetic data recipes, architectural optimizations, test-time compute search) become public within days.
   - If the legal consortium advances algorithmic progress at $0.5 \text{ OOMs/year}$, the covert project gains that same $0.5 \text{ OOMs/year}$ software uplift on its dark hardware, drastically shrinking the time required to reach dangerous takeoff.
3. **The Recommended Mitigation:**
   - **Minimizing Algorithmic Progress:** The consortium deliberately constrains software improvements during Stage 1 (~0.2 OOM software per 1.0 OOM hardware scaling) and scales primarily via verified hardware capacity, which covert actors cannot replicate.