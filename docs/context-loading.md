# Context Loading Guide

Use this guide to keep agent context focused when working with the operator-agent skill library.

## What to load

### Index level
Load an index when the job is still unclear or the user describes a role, workflow, or series rather than a named skill.

Good entry points:
- `START_HERE.md` for role and domain routing.
- `indexes/by-role.md` when the operator role is known.
- `indexes/by-workflow.md` when the task type is known.
- `indexes/by-series.md` when the content series is known.
- `indexes/skill-catalog.md` when the skill name is known or you need exact paths.
- `manifest.json` when tooling needs structured metadata.

### Pack level
Load a pack `README.md` after choosing the operating domain. The pack overview gives the skill list, use order, quality status, examples link, and review context.

Load only one pack by default. Load a second pack only when the user asks for comparison or when the first pack clearly does not fit.

### Skill level
Load one selected skill for the immediate job. The skill file is the governing workflow context: inputs, workflow, output schema, review gates, failure modes, and example prompt.

### Example level
Load the matching file under `examples/by-pack/` only when you need a concrete prompt pattern, sample formatting, or clarification on how the pack should be applied.

## Approximate token strategy

### Minimal mode
Use when the task is simple or the skill is already named.

Load:
- one index or `START_HERE.md`,
- one selected skill.

Aim: smallest viable context.

### Pack mode
Use for most agent work.

Load:
- one index or `START_HERE.md`,
- one pack `README.md`,
- one selected skill.

Aim: enough domain context to apply the skill correctly without absorbing the full library.

### Deep mode
Use only for cross-pack comparison, repository maintenance, conversion work, or quality review.

Load:
- relevant indexes or `manifest.json`,
- the pack READMEs being compared,
- selected skills only,
- examples only when needed.

Aim: explicit breadth for a repository-level task, still avoiding unrelated packs.

## Guardrails
- Do not load the whole repository into a coding-agent context window.
- Treat skills as workflow guidance, not permission to act autonomously.
- Preserve human review gates.
- Follow output schemas exactly.
- Ask for missing required inputs instead of inventing facts.
