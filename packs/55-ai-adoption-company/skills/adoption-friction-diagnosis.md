# Adoption Friction Diagnosis

## Use when
Use this workflow when you are working on AI Adoption That Actually Changes the Company and need to handle the system step without overlapping the other skills in the pack. Its distinct job inside the AI Adoption Pack is to produce the friction diagnosis; use the neighboring skills for AI Adoption Readiness Map, Behavior Change Plan, Adoption Measurement System.

## Inputs
- Current operating context: team, owner, deadline, decision needed, and why this now matters.
- Evidence: source-of-truth links, dashboards, customer notes, meeting records, CRM/project data, or draft artifacts.
- Domain signals to inspect: trust gap, skill gap, workflow mismatch, policy fear, local workaround.
- Constraints: decision rights, budget or headcount limits, customer commitments, legal/security exposure, and review cadence.
- Audience: accountable owner, reviewer, implementer, and anyone affected by the next operating review.

## Workflow
1. Name the concrete use case in one sentence: decision to make, artifact to produce, owner, deadline, and the cost of doing nothing.
2. Build an evidence table with facts, assumptions, missing source-of-truth links, and disputed signals; do not smooth over gaps.
3. Inspect the domain mechanics for this pack: trust gap, skill gap, workflow mismatch, policy fear, local workaround. Call out where handoffs, incentives, review gates, or decision rights break down.
4. Separate this skill's job from the rest of the pack: deliver the friction diagnosis, and list what should be routed to AI Adoption Readiness Map, Behavior Change Plan, Adoption Measurement System.
5. Draft the artifact with owner, decision, options, tradeoffs, acceptance criteria, first action, and operating-review cadence.
6. Add a human review gate for commitments, people claims, customer escalation, financial exposure, legal/security risk, or changes to a system of record.
7. Finish with the smallest useful next move and the exact evidence a human must verify before acting.

## Output
Return a friction diagnosis with this schema:
- `use_case`: the specific operating situation and decision.
- `evidence`: facts, source links, missing data, and assumption flags.
- `diagnosis`: what is happening, why it matters, and which trust gap signal changed.
- `options`: 2-4 paths with tradeoffs, owner, timing, and blast radius.
- `recommendation`: chosen path, rationale, acceptance criteria, and decision rights.
- `review_gates`: human approvals required before sending, changing records, or committing resources.
- `next_move`: one action due within the next operating cadence.

## Human review gates
- Get the accountable owner to approve any recommendation that changes decision rights, budget, headcount, roadmap, pricing, customer commitment, or source-of-truth records.
- Ask legal, security, finance, HR, or the customer owner to verify claims in their lane before the artifact is shared outside the working team.
- Use an explicit review gate before publishing, sending to executives, or triggering a customer escalation.

## Failure modes
- Producing a generic consultant summary instead of a decision-ready friction diagnosis tied to trust gap.
- Treating stale dashboards, anecdotes, or meeting memory as facts without source-of-truth checks.
- Blurring this skill with AI Adoption Readiness Map, Behavior Change Plan, Adoption Measurement System, which creates duplicate work and hides the real owner.
- Skipping the human review gate for commitments, sensitive people/customer data, or system-of-record changes.

## Example prompt
Run the Adoption Friction Diagnosis workflow for the following AI Adoption That Actually Changes the Company situation. Context: <describe team, decision, deadline, evidence links, owner, and known constraints>. Return the friction diagnosis using the output schema, mark assumptions, and list the human review gates before anyone acts.
