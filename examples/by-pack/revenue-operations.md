# RevOps System Pack Example

## Input context
A team is using the Revenue Operations material to turn an ambiguous operating issue into a reusable decision artifact. The agent receives current goals, constraints, recent signals, existing notes, and the named human owner for the work.

## Agent prompt
Use `packs/12-revenue-operations/skills/funnel-integrity-audit.md` from the RevOps System Pack. Diagnose the situation, separate facts from assumptions, recommend the smallest useful next move, and return an artifact the human owner can review and adapt.

## Expected output shape
- One-sentence operating problem
- Relevant actors, handoffs, constraints, and incentives
- Two to four options with tradeoffs
- Recommended path with owner, cadence, success signals, risks, and open questions
- Reusable artifact matching the skill output format

## Human review gate
Before sending or implementing, the accountable owner reviews any claims about customers, people, finances, legal exposure, security, brand, or commitments to external partners.
