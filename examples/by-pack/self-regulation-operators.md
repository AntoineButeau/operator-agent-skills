# Self-Regulation Operator Pack Example

## Input context
A team is working through Self-Regulation for Operators and needs an agent to convert messy operating context into a usable artifact. The agent receives the named owner, current source-of-truth links, recent signals, deadlines, constraints, and the next operating-review date.

## Pack route
1. Start with `skills/trigger-pattern-map.md` when the problem is still ambiguous.
2. Move through the remaining skills only when their distinct job is needed: Response Gap Plan, Emotional Load Review, Operator Reset Protocol.
3. Stop at each human review gate before changing records, sending executive/customer communication, or committing resources.

## Agent prompt
Use `packs/64-self-regulation-operators/skills/trigger-pattern-map.md` from the Self-Regulation Operator Pack. Inspect the context for trigger, body cue, interpretation, impulse, consequence, produce the requested output schema, mark assumptions, and recommend the smallest next move.

## Expected output shape
- Concrete use case and decision owner
- Evidence table with facts, assumptions, gaps, and source-of-truth links
- Domain diagnosis using pack terms such as trigger, body cue, interpretation, impulse, consequence
- Two to four options with tradeoffs and blast radius
- Recommended path with owner, acceptance criteria, review cadence, and next action
- Human review gates before external communication, system-of-record changes, or high-impact commitments

## Human review gate
The accountable owner reviews the artifact before it is sent, published, used in an executive forum, or used to change customer, people, finance, legal, security, roadmap, pricing, or CRM/project records.
