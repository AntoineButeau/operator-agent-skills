# AI Control Plane Pack Example

## Input context
A team is working through The AI Control Plane and needs an agent to convert messy operating context into a usable artifact. The agent receives the named owner, current source-of-truth links, recent signals, deadlines, constraints, and the next operating-review date.

## Pack route
1. Start with `skills/agent-registry-map.md` when the problem is still ambiguous.
2. Move through the remaining skills only when their distinct job is needed: Permission Boundary Review, Control Plane Operating Policy, Agent Incident Retrospective.
3. Stop at each human review gate before changing records, sending executive/customer communication, or committing resources.

## Agent prompt
Use `packs/51-ai-control-plane/skills/agent-registry-map.md` from the AI Control Plane Pack. Inspect the context for agent owner, permission, workflow, audit trail, context source, produce the requested output schema, mark assumptions, and recommend the smallest next move.

## Expected output shape
- Concrete use case and decision owner
- Evidence table with facts, assumptions, gaps, and source-of-truth links
- Domain diagnosis using pack terms such as agent owner, permission, workflow, audit trail, context source
- Two to four options with tradeoffs and blast radius
- Recommended path with owner, acceptance criteria, review cadence, and next action
- Human review gates before external communication, system-of-record changes, or high-impact commitments

## Human review gate
The accountable owner reviews the artifact before it is sent, published, used in an executive forum, or used to change customer, people, finance, legal, security, roadmap, pricing, or CRM/project records.
