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

## Agent loading protocol
Coding agents should treat this repository as a context library, not a single document to ingest.

- Read [AGENTS.md](AGENTS.md) for the source-of-truth protocol.
- Read [CLAUDE.md](CLAUDE.md) for Claude Code and cowork-style usage.
- Read [CODEX.md](CODEX.md) for Codex and coding-agent usage.
- Use [docs/context-loading.md](docs/context-loading.md) for token/loading strategy.

In short: start from `START_HERE.md`, `manifest.json`, or an index; select one pack and one skill; load only the pack README, selected skill, and optional example; preserve review gates and output schemas.

## Quality checklist
Every usable pack is reviewed against [the quality standard](docs/quality-standard.md): concrete use case, specific inputs, domain-specific workflow, structured output schema, real failure modes, human review gates, example prompt, and executable instructions. Pack metadata records `quality_status`, `reviewed_at`, and `review_notes`.
