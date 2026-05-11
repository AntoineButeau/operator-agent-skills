# Strategic Landscape Map Builder

## Use when
Use this workflow when a team needs to see the strategic landscape before committing to a roadmap, platform choice, AI adoption move, vendor decision, staffing model, or operating cadence. Its distinct job inside the Wardley Mapping Pack is to produce a first-pass user-anchored map; use the neighboring skills for deeper dependency mapping, operating-model fit, and doctrine/gameplay choices.

## Inputs
- Decision context: decision owner, deadline, current options, affected teams, and the cost of staying with the current narrative.
- User anchor: primary user, customer, internal operator, regulator, partner, or agent consuming the outcome.
- User needs: jobs to be done, promises made, success measures, constraints, and moments where failure is visible.
- Existing artifacts: roadmap, strategy memo, org chart, architecture sketch, process map, vendor list, AI/agent stack, customer notes, or operating review notes.
- Evidence quality: source-of-truth links, assumptions, disputed facts, missing user research, and stale dashboards.

## Workflow
1. Name the purpose in one sentence: the user, the need, the decision being considered, and why a map is needed now.
2. Anchor the map in the user need, not the org chart. Separate who receives value from which internal team currently owns the work.
3. List visible capabilities directly required by the user outcome, then add less visible supporting capabilities beneath them.
4. Mark each capability with rough visibility to the user and suspected evolution stage: Genesis, Custom, Product, or Commodity.
5. Flag contested or fast-changing AI-era layers such as model access, context, workflow orchestration, data rights, trust, governance, and agent handoffs.
6. Identify where the current strategy deck, roadmap, or org structure hides dependencies, assumptions, inertia, or vendor lock-in.
7. Produce a first-pass map and a confidence review: what is known, what is guessed, and what evidence must be collected before a major move.

## Output
Return a strategic landscape map brief with this schema:
- `purpose`: user, need, decision, owner, deadline, and cost of delay.
- `user_anchor`: primary user and the need that anchors the map.
- `map_components`: capabilities with visibility, dependencies, suspected evolution stage, owner, and evidence link.
- `strategic_observations`: position, movement, climate signals, inertia, and AI-era commoditization pressures.
- `unknowns`: assumptions, missing evidence, disputed facts, and tests to run.
- `decision_implications`: what the map suggests about build, buy, platform, vendor, staffing, or cadence choices.
- `review_gates`: human approvals required before the map changes plans, budgets, records, or external commitments.
- `next_move`: one evidence-gathering or alignment step due in the next operating cadence.

## Human review gates
- Get the accountable decision owner to approve the user anchor before using the map to redirect resources.
- Ask product, customer, operations, data, security, legal, finance, and platform owners to verify claims in their lanes.
- Require executive review before the map drives budget, headcount, roadmap, vendor, pricing, customer, or system-of-record changes.

## Failure modes
- Starting from the org chart or solution preference instead of the user need.
- Presenting a polished map without marking confidence, assumptions, and missing source evidence.
- Treating AI model access as strategic by default when it may already be moving toward commodity.
- Confusing the first-pass landscape map with a final strategy decision.

## Example prompt
Run the Strategic Landscape Map Builder workflow for this decision: <team, user, need, current options, deadline, source links, suspected AI/platform/vendor dependencies, and constraints>. Return the map brief, mark assumptions, and list the human review gates before acting.
