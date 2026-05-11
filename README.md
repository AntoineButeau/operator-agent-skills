# Operator Agent Skills

Portable context packs and agent skills for operators.

This repository contains reusable operator-agent workflow specifications across management, operating systems, GTM/revenue, AI/agents, publishing, knowledge, and product work. The packs are designed to be useful across Codex, Claude Code / cowork, OpenClaw, Hermes, and similar agent runtimes.

They are intentionally packaged as portable Markdown and YAML rather than tied to one runtime. Use them as focused context: route to a pack, choose a skill, load the smallest useful bundle, then produce the artifact with human review gates preserved.

## Status

- **Repository visibility:** currently private. Do not assume the GitHub URL is public until the launch decision is finalized.
- **Release:** `v0.1.0` initial release candidate / first usable library release.
- **Quality status:** all 73 packs and 292 skills are marked `usable` in `manifest.json` after validation.
- **Automation:** no GitHub Actions or workflow automation is included.

## Contents

- 73 portable context packs, one per source content series
- 292 reusable workflow skills
- Indexes by series, role, workflow, and skill catalog
- Runtime loading notes for Codex, Claude Code / cowork, OpenClaw, and Hermes
- Validation script for pack, skill, manifest, and index consistency

## Structure

- `packs/` — one numbered pack per series, each with pack metadata, README, and skills
- `examples/` — example prompts by pack
- `indexes/` — navigation files by catalog, role, series, and workflow
- `docs/` — context-loading, quality, packaging, and conversion notes
- `manifest.json` — machine-readable registry
- `scripts/validate.py` — repository validation

## How to use

Start with [START_HERE.md](START_HERE.md) if you want a role/workflow route before opening individual packs.

1. Choose a route: role, workflow, series, or direct search.
2. Choose the pack that matches the operating domain.
3. Choose the skill that matches the immediate job.
4. Load only the pack README, selected skill, and optional example.
5. Paste the selected context into Codex, Claude Code / cowork, OpenClaw, Hermes, or another agent runtime.
6. Keep human review gates for external, personnel, financial, legal, security, and high-impact decisions.

## Agent loading protocol

Coding and cowork agents should treat this repository as a context library, not a single document to ingest.

- Read [AGENTS.md](AGENTS.md) for the source-of-truth protocol.
- Read [CLAUDE.md](CLAUDE.md) for Claude Code and cowork-style usage.
- Read [CODEX.md](CODEX.md) for Codex and coding-agent usage.
- Use [docs/context-loading.md](docs/context-loading.md) for token/loading strategy.

In short: start from `START_HERE.md`, `manifest.json`, or an index; select one pack and one skill; load only the pack README, selected skill, and optional example; preserve review gates and output schemas.

## Quality checklist

Every usable pack is reviewed against [the quality standard](docs/quality-standard.md): concrete use case, specific inputs, domain-specific workflow, structured output schema, real failure modes, human review gates, example prompt, and executable instructions. Pack metadata records `quality_status`, `reviewed_at`, and `review_notes`.

Validate locally with:

```bash
python3 scripts/validate.py
```

Expected current result:

```text
Validation passed: 73 packs, 292 skills
```

## License and usage

See [LICENSE](LICENSE). This repository is currently all rights reserved and intended for Antoine Buteau and authorized collaborators only. Do not redistribute, republish, sublicense, or treat it as open source unless a future license explicitly grants those rights.

## Feedback

Use [CONTRIBUTING.md](CONTRIBUTING.md) for lightweight feedback and change suggestions. Until the repository visibility and launch decision are finalized, treat all feedback and catalog work as private/internal.
