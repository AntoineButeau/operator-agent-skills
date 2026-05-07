# Rework Root Cause Review

## Use when
Use this workflow when you are working on shipping velocity / how teams actually ship faster and need to diagnose the current state and name the operating risk. Its distinct job inside the Shipping System Pack is to produce the risk-and-evidence audit; use the neighboring skills for Shipping Delay Audit, Scope Slicer, Quality-Speed Tradeoff Check.

## Inputs
- Current operating context: team, owner, deadline, decision needed, and why this now matters.
- Evidence: source-of-truth links, dashboards, customer notes, meeting records, CRM/project data, or draft artifacts.
- Domain signals to inspect: scope cut, release train, acceptance criteria, rework loop, quality gate.
- Constraints: decision rights, budget or headcount limits, customer commitments, legal/security exposure, and review cadence.
- Audience: accountable owner, reviewer, implementer, and anyone affected by the next operating review.

## Workflow
1. Name the concrete use case in one sentence: decision to make, artifact to produce, owner, deadline, and the cost of doing nothing.
2. Build an evidence table with facts, assumptions, missing source-of-truth links, and disputed signals; do not smooth over gaps.
3. Inspect the domain mechanics for this pack: scope cut, release train, acceptance criteria, rework loop, quality gate. Call out where handoffs, incentives, review gates, or decision rights break down.
4. Separate this skill's job from the rest of the pack: deliver the risk-and-evidence audit, and list what should be routed to Shipping Delay Audit, Scope Slicer, Quality-Speed Tradeoff Check.
5. Draft the artifact with owner, decision, options, tradeoffs, acceptance criteria, first action, and operating-review cadence.
6. Add a human review gate for commitments, people claims, customer escalation, financial exposure, legal/security risk, or changes to a system of record.
7. Finish with the smallest useful next move and the exact evidence a human must verify before acting.

## Output
Return a risk-and-evidence audit with this schema:
- `use_case`: the specific operating situation and decision.
- `evidence`: facts, source links, missing data, and assumption flags.
- `diagnosis`: what is happening, why it matters, and which scope cut signal changed.
- `options`: 2-4 paths with tradeoffs, owner, timing, and blast radius.
- `recommendation`: chosen path, rationale, acceptance criteria, and decision rights.
- `review_gates`: human approvals required before sending, changing records, or committing resources.
- `next_move`: one action due within the next operating cadence.

## Human review gates
- Get the accountable owner to approve any recommendation that changes decision rights, budget, headcount, roadmap, pricing, customer commitment, or source-of-truth records.
- Ask legal, security, finance, HR, or the customer owner to verify claims in their lane before the artifact is shared outside the working team.
- Use an explicit review gate before publishing, sending to executives, or triggering a customer escalation.

## Failure modes
- Producing a generic consultant summary instead of a decision-ready risk-and-evidence audit tied to scope cut.
- Treating stale dashboards, anecdotes, or meeting memory as facts without source-of-truth checks.
- Blurring this skill with Shipping Delay Audit, Scope Slicer, Quality-Speed Tradeoff Check, which creates duplicate work and hides the real owner.
- Skipping the human review gate for commitments, sensitive people/customer data, or system-of-record changes.

## Example prompt
Run the Rework Root Cause Review workflow for the following Shipping Velocity / How Teams Actually Ship Faster situation. Context: <describe team, decision, deadline, evidence links, owner, and known constraints>. Return the risk-and-evidence audit using the output schema, mark assumptions, and list the human review gates before anyone acts.
