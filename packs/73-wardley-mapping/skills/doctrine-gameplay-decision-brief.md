# Doctrine Gameplay Decision Brief

## Use when
Use this workflow when a team has a map and needs to decide what to do next without mistaking basic operating discipline for clever strategy. Its distinct job inside the Wardley Mapping Pack is to separate doctrine fixes from gameplay choices such as build, buy, commoditize, differentiate, partner, constrain, migrate, wait, or exit.

## Inputs
- Map context: user anchor, value chain, evolution stages, dependency risks, operating-model fit findings, and confidence levels.
- Decision question: the concrete move being considered, owner, deadline, alternatives, and what happens if no decision is made.
- Doctrine health: user understanding, assumption challenge, transparency, appropriate methods, learning loops, inertia management, effectiveness, and review cadence.
- Gameplay options: build, buy, outsource, standardize, platform, differentiate, partner, open source, automate, constrain, delay, migrate, retire, or exit.
- Evidence and constraints: budget, headcount, customer commitments, vendor contracts, regulatory exposure, security posture, data rights, and AI-agent governance.

## Workflow
1. Restate the decision in map terms: user need, position, movement, climate, doctrine gap, gameplay choice, and decision owner.
2. Check doctrine first. Identify basic operating practices that must be fixed before any strategic play can work: user focus, assumption testing, transparency, appropriate methods, inertia management, and learning cadence.
3. Separate doctrine fixes from gameplay moves. Do not label hygiene, instrumentation, ownership clarity, or review discipline as strategy.
4. Evaluate gameplay options against evolution stage, dependency risk, AI commoditization, strategic control points, reversibility, time horizon, and blast radius.
5. Name inertia explicitly: who benefits from the current model, what success history it protects, and what evidence could change minds.
6. Recommend a move, a wait condition, or a staged sequence with owner, decision rights, proof points, review cadence, and stop conditions.
7. Add human review gates before external communication, budget shifts, vendor commitments, data/control changes, or customer-impacting moves.

## Output
Return a doctrine gameplay decision brief with this schema:
- `decision`: user need, map position, decision owner, deadline, and cost of no action.
- `doctrine_check`: doctrine strengths, gaps, required fixes, owners, and due dates.
- `gameplay_options`: options with fit to evolution stage, control point, evidence, tradeoffs, reversibility, and blast radius.
- `inertia_analysis`: protected old model, affected stakeholders, resistance signals, and evidence required to move.
- `recommendation`: chosen doctrine fixes and gameplay move, sequencing, rationale, acceptance criteria, and stop conditions.
- `operating_cadence`: how the map changes planning, reviews, resource allocation, platform governance, AI adoption, or vendor management.
- `review_gates`: approvals required before commitments or record changes.
- `next_move`: one decision or evidence action due before the next review.

## Human review gates
- Get the accountable executive or decision owner to approve the recommended move and stop conditions.
- Require finance, procurement, security, legal, data, HR, platform, or customer-owner review when the move changes spend, contracts, controls, roles, data access, or customer commitments.
- Use a documented decision log before changing roadmap, architecture, systems of record, vendor posture, or public messaging.

## Failure modes
- Skipping doctrine and treating poor user understanding, missing ownership, or weak review discipline as a need for grand strategy.
- Choosing a move because it sounds strategic rather than because the map supports it.
- Over-investing in differentiating work where the capability is commoditizing, or outsourcing a control point that should remain strategic.
- Naming inertia abstractly without identifying owners, incentives, and the evidence needed to change behavior.

## Example prompt
Run the Doctrine Gameplay Decision Brief for this mapped decision: <user anchor, value chain, evolution stages, doctrine gaps, gameplay options, AI/platform/vendor context, source links, owner, deadline, and constraints>. Return the doctrine check, gameplay recommendation, operating cadence changes, and human review gates.
