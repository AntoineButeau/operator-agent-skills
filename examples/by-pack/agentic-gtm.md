# Agentic GTM Pack Example

## Input context
A team needs a practical operating decision in the domain of Agentic GTM. The agent receives goals, constraints, owners, timelines, evidence links, and current workflow artifacts.

## Pack route
1. Start with `packs/76-agentic-gtm/skills/gtm-loop-inventory-prioritization.md`.
2. Continue with `packs/76-agentic-gtm/skills/account-trigger-enrichment-loop-spec.md`.
3. Deepen with `packs/76-agentic-gtm/skills/relevance-gated-personalization-review.md`.
4. Finalize with `packs/76-agentic-gtm/skills/revops-agent-handoff-governance.md`.

## Agent prompt
Use `packs/76-agentic-gtm/skills/gtm-loop-inventory-prioritization.md` from the Agentic GTM Pack. Inspect constraints, dependencies, risks, ownership, evidence quality, and review gates. Return the requested output schema and smallest next evidence-backed move.

## Expected output shape
- decision framing and owner
- evidence-backed diagnosis
- bounded recommendation
- risks, assumptions, and confidence notes
- next move with owner and cadence

## Human review gate
The accountable owner approves before external communication or any customer, legal, security, budget, staffing, roadmap, or system-of-record change.
