# End of Dashboard Pack Example

## Input context
A team needs a practical operating decision in the domain of The End of the Dashboard. The agent receives goals, constraints, owners, timelines, evidence links, and current workflow artifacts.

## Pack route
1. Start with `packs/75-end-of-dashboard/skills/dashboard-decay-diagnosis.md`.
2. Continue with `packs/75-end-of-dashboard/skills/intent-to-action-workflow-spec.md`.
3. Deepen with `packs/75-end-of-dashboard/skills/exception-queue-design.md`.
4. Finalize with `packs/75-end-of-dashboard/skills/trust-lineage-reversibility-controls.md`.

## Agent prompt
Use `packs/75-end-of-dashboard/skills/dashboard-decay-diagnosis.md` from the End of Dashboard Pack. Inspect constraints, dependencies, risks, ownership, evidence quality, and review gates. Return the requested output schema and smallest next evidence-backed move.

## Expected output shape
- decision framing and owner
- evidence-backed diagnosis
- bounded recommendation
- risks, assumptions, and confidence notes
- next move with owner and cadence

## Human review gate
The accountable owner approves before external communication or any customer, legal, security, budget, staffing, roadmap, or system-of-record change.
