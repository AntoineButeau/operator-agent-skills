# CLAUDE.md

`AGENTS.md` is the source of truth for how coding agents should use this repository.

## Claude Code / cowork loading protocol
- Do not preload the repository. Claude performs better here with a narrow context bundle.
- Begin with `START_HERE.md`, `manifest.json`, or one file in `indexes/` to choose a route.
- Select exactly one pack, then exactly one skill for the current task.
- Load the pack `README.md`, the selected skill, and the matching example only if the prompt pattern is needed.
- Avoid dragging adjacent packs into context unless the user explicitly asks for comparison across domains.

## Claude-specific cautions
- Keep the active context small enough to reason over the selected workflow instead of summarizing the library.
- Preserve human review gates exactly; do not convert a workflow into permission to take external action.
- Follow the selected skill's output schema even when a shorter cowork reply would be natural.
- If required inputs are missing, ask for them before producing a final artifact.
