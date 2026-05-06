# Operator Agent Skills

A private collection of reusable operator-agent workflow skill packs derived from Antoine Buteau's content series.

These are practical workflow specifications for agents and operators. They are intentionally packaged as portable Markdown and YAML rather than OpenClaw runtime AgentSkills, so they can later be converted, curated, or published through ClawHub/OpenClaw if useful.

## Contents
- 39 packs, one per content series
- 156 reusable workflow skills
- Indexes by series, role, workflow, and skill catalog

## Structure
- `packs/` — one numbered pack per series
- `indexes/` — navigation files
- `docs/` — packaging and conversion notes
- `manifest.json` — machine-readable registry

## How to use
Start with [START_HERE.md](START_HERE.md) if you want a role/workflow route before opening individual packs.

1. Pick the pack that matches the operating domain.
2. Open the skill that matches the immediate job.
3. Paste the skill into an agent prompt with the current context, or adapt it into a runtime-specific skill format.
4. Keep human review gates for external, personnel, financial, legal, security, and high-impact decisions.
