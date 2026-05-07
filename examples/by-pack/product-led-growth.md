# PLG Operating Pack Example

## Input context
A team is working through Product-Led Growth and needs an agent to convert messy operating context into a usable artifact. The agent receives the named owner, current source-of-truth links, recent signals, deadlines, constraints, and the next operating-review date.

## Pack route
1. Start with `skills/activation-path-audit.md` when the problem is still ambiguous.
2. Move through the remaining skills only when their distinct job is needed: Self-Serve Conversion Map, Product-Qualified Signal Design, PLG Experiment Brief.
3. Stop at each human review gate before changing records, sending executive/customer communication, or committing resources.

## Agent prompt
Use `packs/16-product-led-growth/skills/activation-path-audit.md` from the PLG Operating Pack. Inspect the context for activation path, PQL, self-serve funnel, conversion map, produce the requested output schema, mark assumptions, and recommend the smallest next move.

## Expected output shape
- Concrete use case and decision owner
- Evidence table with facts, assumptions, gaps, and source-of-truth links
- Domain diagnosis using pack terms such as activation path, PQL, self-serve funnel, conversion map
- Two to four options with tradeoffs and blast radius
- Recommended path with owner, acceptance criteria, review cadence, and next action
- Human review gates before external communication, system-of-record changes, or high-impact commitments

## Human review gate
The accountable owner reviews the artifact before it is sent, published, used in an executive forum, or used to change customer, people, finance, legal, security, roadmap, pricing, or CRM/project records.
