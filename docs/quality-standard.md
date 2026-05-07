# Quality Standard for Operator-Agent Skills

A high-quality skill is executable by an agent or operator without extra explanation. It should turn a live operating situation into a reusable artifact, decision, or review gate.

## Required qualities

1. **Concrete use case** — names the operating situation, decision, owner, timing, and why the skill exists.
2. **Specific inputs** — asks for source-of-truth links, owners, deadlines, constraints, evidence, and review context rather than generic background.
3. **Non-generic workflow** — uses pack-specific mechanics and domain terms; it should not read like a consultant template that could fit any problem.
4. **Useful output schema** — returns a structured artifact with fields another agent or human can reuse.
5. **Real failure modes** — calls out stale evidence, missing owners, blurred decision rights, skipped gates, and domain-specific risks.
6. **Human review gates** — stops before external communication, customer escalation, personnel claims, financial/legal/security exposure, or system-of-record changes.
7. **Example prompt** — shows exactly how to invoke the skill with context, evidence, owner, deadline, and constraints.
8. **Executable enough** — an operator can run it, inspect the output, and decide the next move without asking what format or process to use.

## Metadata standard

Each reviewed pack should include:

- `maturity: "usable"` only after pack-level review.
- `quality_status: "usable"` when the pack meets this standard.
- `reviewed_at: "YYYY-MM-DD"` for the review date.
- `review_notes` describing what was checked.

If a pack does not meet the standard, keep `maturity: "draft"`, set `quality_status: "draft"`, and state the blocker in `review_notes`.

## Pack-level review checklist

- The four skills form a clear progression.
- Each skill has a distinct job and does not duplicate the others.
- The README explains when to use the pack and the order to run the skills.
- The pack example uses a real operating scenario and names expected output.
- Skill language includes domain terms such as forecast commit, QBR, win/loss, manager cascade, decision rights, source of truth, review gate, customer escalation, account plan, pipeline inspection, acceptance criteria, change load, or operating review when relevant.
- Generic phrases are removed unless they are the correct domain term.

## Skill-level checklist

Before marking a skill usable, confirm it has:

- A concrete `Use when` section.
- Inputs with owner, evidence, source-of-truth links, constraints, and review context.
- A domain-specific workflow.
- A structured output schema.
- Human review gates.
- Failure modes that can actually happen in the domain.
- An example prompt that can be copied into an agent run.
