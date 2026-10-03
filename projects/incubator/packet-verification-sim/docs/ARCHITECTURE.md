# Packet Verification Simulator Architecture

## Architecture overview

The simulator is a pure-Python, zero-dependency engine designed to run locally on CPU in <1 second.

### Components
1. `theoretical_detection_probability`: Calculates Poisson bound $P = 1 - e^{-C \cdot N_{\text{fake}}}$.
2. `exact_detection_probability`: Calculates exact hyper-geometric bound $P = 1 - (1 - C)^{N_{\text{fake}}}$.
3. `run_monte_carlo_audit`: Simulates random draws without replacement over $M$ independent trials to measure empirical detection rates.
4. `CLI Interface`: Exposes parameter sweeps for total workload size, injected rogue packets, and audit budget percentages.

### Test verification
- Verified via `tests/test_packet_sim.py` using standard Python `unittest`.
