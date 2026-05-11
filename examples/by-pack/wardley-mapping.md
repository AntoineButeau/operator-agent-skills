# Wardley Mapping Pack Example

## Input context
A company is deciding whether to build, buy, or agent-enable an AI customer-support capability. The agent receives the user need, current support workflow, ticket data, model/vendor options, systems of record, context sources, owners, budget constraints, security requirements, and the next operating-review date.

## Pack route
1. Start with `packs/73-wardley-mapping/skills/strategic-landscape-map-builder.md` to anchor the map in the user need and sketch the strategic landscape.
2. Use `packs/73-wardley-mapping/skills/value-chain-dependency-mapper.md` to expose the data, tools, models, people, vendors, controls, and handoffs the outcome depends on.
3. Use `packs/73-wardley-mapping/skills/evolution-operating-model-fit-check.md` to test whether each capability is being run with a method that fits Genesis, Custom, Product, or Commodity maturity.
4. Use `packs/73-wardley-mapping/skills/doctrine-gameplay-decision-brief.md` to separate doctrine fixes from strategic moves such as build, buy, commoditize, differentiate, partner, constrain, wait, or exit.

## Agent prompt
Use `packs/73-wardley-mapping/skills/strategic-landscape-map-builder.md` from the Wardley Mapping Pack. Inspect the context for user need, value chain, evolution stage, inertia, doctrine, gameplay options, AI-era commoditization, platform/vendor dependencies, and agent adoption risks. Produce the requested output schema, mark assumptions, and recommend the smallest next evidence move.

## Expected output shape
- Concrete user anchor and decision owner
- First-pass map components with visibility, dependencies, suspected evolution stage, owner, and evidence
- Dependency risks around data, context, model access, tools, vendors, governance, and human review
- Fit check between capability maturity and operating model
- Doctrine gaps separated from gameplay choices
- Recommendation with tradeoffs, blast radius, acceptance criteria, cadence, and next move
- Human review gates before external communication, system-of-record changes, spend, vendor commitments, customer commitments, or high-impact AI/agent deployment

## Human review gate
The accountable owner reviews the artifact before it is sent, published, used in an executive forum, or used to change customer, people, finance, legal, security, roadmap, pricing, vendor, architecture, AI governance, or CRM/project records.
