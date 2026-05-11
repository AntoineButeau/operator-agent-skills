# AI Context Layer Pack Example

## Input context
A team is working through The AI Context Layer: Giving Agents a Business Model They Can Safely Use and needs an agent to convert messy operating context into a usable artifact. The agent receives the named owner, current source-of-truth links, recent signals, deadlines, constraints, and the next operating-review date.

## Pack route
1. Start with `skills/agent-context-inventory.md` when the problem is still ambiguous.
2. Move through the remaining skills only when their distinct job is needed: Context Contract Design, Context Risk Review, Business Model for Agents Brief.
3. Stop at each human review gate before changing records, sending executive/customer communication, or committing resources.

## Agent prompt
Use `packs/60-ai-context-layer/skills/agent-context-inventory.md` from the AI Context Layer Pack. Inspect the context for business object, policy, workflow history, source freshness, access rule, produce the requested output schema, mark assumptions, and recommend the smallest next move.

## Expected output shape
- Concrete use case and decision owner
- Evidence table with facts, assumptions, gaps, and source-of-truth links
- Domain diagnosis using pack terms such as business object, policy, workflow history, source freshness, access rule
- Two to four options with tradeoffs and blast radius
- Recommended path with owner, acceptance criteria, review cadence, and next action
- Human review gates before external communication, system-of-record changes, or high-impact commitments

## Human review gate
The accountable owner reviews the artifact before it is sent, published, used in an executive forum, or used to change customer, people, finance, legal, security, roadmap, pricing, or CRM/project records.
