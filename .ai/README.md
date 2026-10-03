# Shared AI Workspace

This directory is the durable, version-controlled source of project context for
Codex, Claude Code, and Gemini CLI.

The repository root contains these relative symbolic links:

- `AGENTS.md` -> `.ai/INSTRUCTIONS.md`
- `CLAUDE.md` -> `.ai/INSTRUCTIONS.md`
- `GEMINI.md` -> `.ai/INSTRUCTIONS.md`

Edit `.ai/INSTRUCTIONS.md` once to change the common agent instructions. Keep
project facts, operating policy, planning standards, decisions, and handoffs in
the other `.ai` files. Do not store credentials or other secrets here.

After changing instructions in an already-running tool, start a fresh session
or use that tool's supported memory reload command so the new content is loaded.
