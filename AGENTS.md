# AGENTS.md

This repository is a context library for operator-agent workflow skills. Use it selectively. It is not meant to be loaded wholesale into an agent context window.

## Loading protocol
1. Start with one navigation surface:
   - `START_HERE.md` for role and workflow routing.
   - `manifest.json` for machine-readable pack and skill metadata.
   - `indexes/` for catalog, role, series, or workflow lookup.
2. Select one pack that matches the operating domain.
3. Select one skill that matches the immediate job.
4. Load only:
   - the pack `README.md`,
   - the selected skill file under `packs/<pack>/skills/`,
   - the matching example under `examples/by-pack/` only when the task needs a concrete prompt pattern.
5. Do not load unrelated packs, all skills, or the full manifest unless you are building tooling that needs the registry.

## Operating rules
- Treat skills as workflow context, not autonomous permission to act.
- Preserve every human review gate in the selected skill.
- Keep external, personnel, financial, legal, security, and high-impact actions behind explicit human review.
- Follow the skill's output schema. If the schema conflicts with a runtime's default style, the skill schema wins.
- Ask for missing context when required inputs are absent; do not invent customer facts, org details, numbers, constraints, or approvals.
- State assumptions clearly when minor assumptions are needed to proceed.
- Use the failure modes section as an active checklist before final output.

## Expected agent flow
1. Identify the job and required decision/output.
2. Choose the smallest relevant navigation file.
3. Pick one pack and one skill.
4. Read the pack overview, selected skill, and optional example.
5. Confirm inputs, review gates, and output schema.
6. Produce the requested artifact in the selected schema.
