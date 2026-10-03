# Value-Based Planning

## Planning standard

For non-trivial work, define these before implementation:

1. **Outcome:** the user-visible or operational result.
2. **Value:** time saved, reliability gained, risk reduced, capability unlocked,
   or recurring cost avoided.
3. **Baseline:** current state and evidence that the problem exists.
4. **Options:** reuse, buy, configure, or build; include a do-nothing option when
   useful.
5. **Cost:** setup effort, recurring cloud spend, AI/model cost, maintenance,
   operational burden, and exit cost.
6. **Risk:** security, privacy, lock-in, data loss, downtime, quota, compatibility,
   and rollback concerns.
7. **Smallest valuable increment:** the least expensive reversible step that
   tests the main assumption.
8. **Success measure:** a checkable acceptance criterion, SLO, benchmark, or
   cost ceiling.
9. **Approval point:** the exact step requiring the owner's decision.

## Delivery gates

Use this sequence unless the task is a clearly safe and bounded edit:

`discover -> propose -> approve -> implement -> verify -> document -> review cost`

- Search for existing solutions before designing new components.
- Prove one provider, image, or GPU path before generalizing to many.
- Prefer reversible experiments and dry runs before live infrastructure changes.
- Separate estimates from measured results.
- Do not optimize merely for lower price: optimize total value across capability,
  reliability, time, operational effort, and cost.
- Stop when marginal value no longer justifies complexity or recurring expense.

## Proposal format

Keep proposals concise and decision-ready:

- Recommendation
- Expected value
- Alternatives considered
- One-time and recurring cost
- Key risks and mitigations
- Validation plan and success metric
- Approval required
