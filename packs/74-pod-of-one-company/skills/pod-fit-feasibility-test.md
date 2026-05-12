# Pod Fit Feasibility Test

## Use when
Use this workflow when work in this pack specifically requires **pod fit feasibility test** and a concrete operator-grade artifact. Use it as one step in the pack progression, not as a generic strategy brainstorm.

## Inputs
- decision context, owner, and deadline
- current state evidence and source links
- constraints, risks, and dependencies
- expected audience and review gate

## Workflow
1. Frame the exact decision and success condition.
2. Inspect evidence quality and mark assumptions.
3. Apply the method for this skill to produce a bounded recommendation.
4. Separate reversible from high-impact decisions.
5. Define next action, owner, and review cadence.

## Output
Return:
- concise decision brief
- assumptions and confidence notes
- risks/failure modes
- recommendation with tradeoffs
- next move with owner and due window

## Human review gates
- Require accountable owner sign-off before budget, customer, legal, security, architecture, staffing, or system-of-record changes.
- Escalate when evidence is weak or tradeoffs are irreversible.

## Failure modes
- vague scope and no owner
- output not tied to evidence
- skipping risk and reversibility checks
- collapsing distinct pack skills into one generic answer

## Example prompt
Run `pod-fit-feasibility-test` using the provided context. Return the defined output schema, mark assumptions, and recommend the smallest next evidence-backed move.
