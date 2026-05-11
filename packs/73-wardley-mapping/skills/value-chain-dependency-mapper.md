# Value Chain Dependency Mapper

## Use when
Use this workflow when a user outcome depends on many hidden capabilities and the team needs to understand what actually has to work before changing process, platform, staffing, vendor, AI agent, or operating cadence decisions. Its distinct job inside the Wardley Mapping Pack is to map value-chain dependencies; use the neighboring skills for landscape framing, evolution fit, and doctrine/gameplay choices.

## Inputs
- User outcome: the user need, promise, service level, business result, or workflow result being mapped.
- Current delivery path: teams, systems, data sources, models, vendors, queues, approvals, controls, and manual workarounds.
- Evidence: process traces, architecture diagrams, CRM/project records, observability data, support tickets, sales/customer notes, spend data, and incident history.
- Dependency details: owner, source of truth, interface, failure mode, latency, cost, quality signal, and current review cadence for each capability.
- Strategic concerns: AI commoditization, vendor dependence, system-of-record conflict, context quality, governance exposure, and known inertia.

## Workflow
1. State the user outcome and the moment where value is delivered or failure becomes visible.
2. Walk backward from that moment into the value chain: visible user-facing capabilities first, then supporting data, tools, models, processes, people, policies, vendors, and infrastructure.
3. For each component, record owner, source of truth, dependency type, current reliability, cost signal, and evidence link.
4. Mark weak links: manual glue, unclear ownership, duplicated records, context gaps, brittle integrations, hidden approvals, vendor constraints, and agent handoff risks.
5. Separate commodity dependencies from differentiating capabilities so the team does not over-customize plumbing or under-invest in strategic context.
6. Identify dependencies whose evolution stage is uncertain and route them to Evolution Operating Model Fit Check.
7. Summarize the dependency risks that should change roadmap, platform, AI adoption, staffing, vendor, or governance choices.

## Output
Return a value chain dependency map with this schema:
- `user_outcome`: user, need, success measure, failure moment, and decision owner.
- `dependency_chain`: ordered capabilities with owner, source of truth, evidence, visibility, and dependency type.
- `critical_links`: dependencies that most affect reliability, speed, cost, trust, customer experience, or regulatory exposure.
- `ai_agent_dependencies`: model, context, data rights, tool access, human review, evaluation, and governance dependencies.
- `risk_register`: weak link, likely consequence, evidence, owner, severity, and mitigation.
- `strategic_implications`: what to simplify, standardize, build, buy, instrument, govern, or retire.
- `review_gates`: approvals required before changing systems, contracts, controls, or customer commitments.
- `next_move`: one dependency to verify or instrument next.

## Human review gates
- Get system owners to verify source-of-truth, data lineage, permission, and reliability claims.
- Require security, legal, compliance, finance, or procurement review before changing data access, vendor contracts, controls, or spend.
- Ask customer or revenue owners to approve any change that affects service levels, promises, pricing, or account commitments.

## Failure modes
- Mapping teams and tools without tracing the actual user value chain.
- Treating undocumented manual work as harmless because the dashboard still looks green.
- Missing AI-agent dependencies around context quality, permissions, evaluations, and human review.
- Turning every dependency into an investment instead of distinguishing commodity plumbing from strategic leverage.

## Example prompt
Run the Value Chain Dependency Mapper workflow for this user outcome: <user need, delivery path, known systems, teams, vendors, models, data sources, incidents, source links, and constraints>. Return the dependency map with weak links, AI-agent dependencies, and review gates.
