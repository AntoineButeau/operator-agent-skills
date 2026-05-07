# CODEX.md

`AGENTS.md` is the source of truth for how coding agents should use this repository.

## Codex loading protocol
- Treat this repository as a context library, not an application to execute.
- Start from `START_HERE.md`, `manifest.json`, or the narrowest relevant file in `indexes/`.
- Choose one pack and one skill before reading deeper.
- Load only the pack `README.md`, the selected skill, and an example when it helps format the prompt or output.
- Do not scan every pack unless the task is explicitly about repository-wide validation, indexing, or refactoring.

## Validation reminders
- Preserve human review gates in any generated workflow or artifact.
- Follow the selected skill's output schema and required sections.
- Ask for absent required inputs rather than fabricating facts.
- After repository edits, run `python3 scripts/validate.py` before committing.
- Verify generated docs do not add automation surfaces such as `.github/workflows` unless explicitly requested.
