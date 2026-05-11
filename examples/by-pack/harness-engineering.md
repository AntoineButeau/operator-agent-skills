# Harness Engineering Pack Example

## Input context
A team is working through Harness Engineering: The Runtime Layer Around AI Agents and needs an agent to convert messy operating context into a usable artifact. The agent receives the named owner, current source-of-truth links, recent signals, deadlines, constraints, and the next operating-review date.

## Pack route
1. Start with `skills/agent-runtime-architecture-map.md` when the problem is still ambiguous.
2. Move through the remaining skills only when their distinct job is needed: Eval Harness Spec, Context Window Management Plan, Runtime Failure Mode Review.
3. Stop at each human review gate before changing records, sending executive/customer communication, or committing resources.

## Agent prompt
Use `packs/53-harness-engineering/skills/agent-runtime-architecture-map.md` from the Harness Engineering Pack. Inspect the context for orchestration, memory, tool call, sandbox, evaluation hook, produce the requested output schema, mark assumptions, and recommend the smallest next move.

## Expected output shape
- Concrete use case and decision owner
- Evidence table with facts, assumptions, gaps, and source-of-truth links
- Domain diagnosis using pack terms such as orchestration, memory, tool call, sandbox, evaluation hook
- Two to four options with tradeoffs and blast radius
- Recommended path with owner, acceptance criteria, review cadence, and next action
- Human review gates before external communication, system-of-record changes, or high-impact commitments

## Human review gate
The accountable owner reviews the artifact before it is sent, published, used in an executive forum, or used to change customer, people, finance, legal, security, roadmap, pricing, or CRM/project records.
