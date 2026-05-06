# Converting to OpenClaw Skills

These packs are not runtime OpenClaw AgentSkills yet. To convert one:

1. Choose a single reusable skill with frequent expected use.
2. Create an OpenClaw skill folder using the target skill name.
3. Move the workflow into `SKILL.md` with concise frontmatter: `name` and `description`.
4. Keep only the instructions needed at runtime. Move long examples or templates into references.
5. Validate with a real task, then package through the standard OpenClaw skill packaging flow.
6. Keep this repository as the broader design source and the runtime skill as the execution-optimized derivative.
