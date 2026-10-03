# Solution Pattern: Random Recomputation Audit

Sample execution packets and independently recompute them to estimate whether a
larger run followed declared behavior.

## Applicable context

Use when full recomputation is too expensive, samples can be selected without
operator manipulation, and statistical uncertainty can be communicated.

## Pattern

Commit to execution records, select an unpredictable sample, independently
recompute it, and report mismatches with the sampling assumptions.

## Failure modes

Biased sampling, forged records, correlated failures, and overclaiming what a
clean sample proves must remain explicit.
