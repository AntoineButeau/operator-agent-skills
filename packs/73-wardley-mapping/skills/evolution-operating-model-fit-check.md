# Evolution Operating Model Fit Check

## Use when
Use this workflow when a team may be using the wrong operating model for the evolution stage of a capability. It is especially useful for AI-era decisions where model access, tooling, data infrastructure, workflow orchestration, governance, or customer experience may be moving at different speeds. Its distinct job inside the Wardley Mapping Pack is to test evolution-stage fit; use the neighboring skills for map building, dependency mapping, and doctrine/gameplay decisions.

## Inputs
- Capability list: map components or dependencies with owners, evidence links, and current operating approach.
- Current methods: planning cadence, budget model, team structure, delivery method, governance controls, quality bar, vendor strategy, and review rhythm.
- Evolution evidence: uniqueness, uncertainty, repeatability, market maturity, vendor availability, pricing trend, customer expectations, switching cost, and operational stability.
- Performance signals: cycle time, reliability, cost, defect rate, adoption, customer pain, incident pattern, and team friction.
- Constraints: regulatory exposure, security needs, customer promises, technical debt, contract terms, and irreversible commitments.

## Workflow
1. Classify each capability as Genesis, Custom, Product, Commodity, or uncertain, and cite the evidence behind the classification.
2. Compare the current operating model against the stage: exploratory discovery for Genesis, close-fit craft for Custom, product management and scaling for Product, industrialization and efficiency for Commodity.
3. Look for mismatch symptoms: over-governed discovery, bespoke commodity work, premature platforming, vendor avoidance, under-instrumented critical plumbing, or one cadence applied to all work.
4. Identify inertia created by the old successful model: skills, status, incentives, budget ownership, architecture, process, contracts, or customer promises.
5. Assess AI-era movement: which capabilities are commoditizing, which layers remain differentiating, and where agents change the cost or control surface.
6. Recommend operating-model changes with blast radius, owner, review cadence, and evidence needed before changing budget, team design, vendor posture, or roadmap.
7. Route unresolved strategic choices to Doctrine Gameplay Decision Brief.

## Output
Return an evolution operating-model fit check with this schema:
- `capability_stage_table`: capability, suspected stage, evidence, confidence, owner, and review date.
- `fit_assessment`: current operating model, fit or mismatch, symptoms, and consequence.
- `inertia_sources`: what the old model protects and who experiences the cost of changing it.
- `ai_commoditization_scan`: capabilities moving toward commodity, contested layers, and strategic control points.
- `recommended_changes`: method, cadence, budget, staffing, platform, vendor, governance, or quality changes with rationale.
- `risks_and_tradeoffs`: blast radius, reversibility, timing, and second-order effects.
- `review_gates`: approvals required before changing operating model or commitments.
- `next_move`: one experiment, review, or evidence check to validate the fit assessment.

## Human review gates
- Get owners of affected capabilities to review stage classifications and operating-model recommendations.
- Require finance, HR, procurement, security, legal, or platform review before changing budgets, roles, contracts, controls, or architecture standards.
- Use executive review when the recommendation changes strategic focus, investment posture, or customer-facing commitments.

## Failure modes
- Assigning evolution stages by vibes instead of observable characteristics and market evidence.
- Assuming commodity means low importance; critical commodity capabilities still need reliability, ownership, and controls.
- Applying one operating cadence, funding model, or governance process to Genesis, Custom, Product, and Commodity work.
- Ignoring inertia from teams whose identity, influence, or budget depends on the old model.

## Example prompt
Run the Evolution Operating Model Fit Check for these capabilities: <capability list, owners, current methods, evidence links, performance signals, AI/vendor context, and constraints>. Return the fit check, stage table, recommended operating-model changes, and review gates.
