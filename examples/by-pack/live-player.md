# Reality Contact Pack Example

## Input context
A team is working through How to Be a Live Player and needs an agent to convert messy operating context into a usable artifact. The agent receives the named owner, current source-of-truth links, recent signals, deadlines, constraints, and the next operating-review date.

## Pack route
1. Start with `skills/reality-contact-audit.md` when the problem is still ambiguous.
2. Move through the remaining skills only when their distinct job is needed: Assumption Refresh Loop, Live Option Generator, Field Signal Review.
3. Stop at each human review gate before changing records, sending executive/customer communication, or committing resources.

## Agent prompt
Use `packs/32-live-player/skills/reality-contact-audit.md` from the Reality Contact Pack. Inspect the context for field signal, assumption refresh, reality contact, live option, produce the requested output schema, mark assumptions, and recommend the smallest next move.

## Expected output shape
- Concrete use case and decision owner
- Evidence table with facts, assumptions, gaps, and source-of-truth links
- Domain diagnosis using pack terms such as field signal, assumption refresh, reality contact, live option
- Two to four options with tradeoffs and blast radius
- Recommended path with owner, acceptance criteria, review cadence, and next action
- Human review gates before external communication, system-of-record changes, or high-impact commitments

## Human review gate
The accountable owner reviews the artifact before it is sent, published, used in an executive forum, or used to change customer, people, finance, legal, security, roadmap, pricing, or CRM/project records.
