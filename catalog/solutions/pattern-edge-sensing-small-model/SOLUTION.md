# Solution Pattern: Edge Sensing and Small Model

> Combine inexpensive local sensors with a small model and explicit human oversight.

## Applicable context

Use for bounded observation tasks in infrastructure, manufacturing, or agriculture where local processing improves privacy, latency, or resilience.

## Pattern

Collect the minimum sensor signal, run a narrow model at the edge, communicate confidence, and route findings to a person rather than directly controlling equipment.

## Tradeoffs and failure modes

Sensor drift, distribution shifts, environmental damage, and false confidence can make a small model unsafe outside its tested context.

## Safety and cost boundaries

Research and advisory use only until hardware-specific safety review; no autonomous electrical, chemical, or machinery control.
