# Contributing / Feedback

This repository is currently private and all rights reserved. Contributions are limited to Antoine Buteau and explicitly authorized collaborators until a public launch decision and license change are made.

## Good feedback

Helpful feedback is specific and tied to an operator job:

- Which pack and skill did you use?
- What input did you give the agent?
- What output did you expect?
- What review gate, failure mode, or output section was missing?
- Did the skill work across Codex, Claude Code / cowork, OpenClaw, or Hermes?

## Change checklist

Before suggesting or committing a change:

1. Preserve the skill's human review gates.
2. Keep the workflow platform-neutral unless the file is explicitly runtime-specific.
3. Update examples or indexes when names, paths, or skill purposes change.
4. Run validation:

```bash
python3 scripts/validate.py
```

5. Do not add GitHub Actions or workflow automation unless explicitly requested.

## Current release posture

`v0.1.0` is the initial usable library release: 39 packs, 156 skills, private repository, no GitHub Actions.
