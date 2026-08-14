# Claude Adapter

## Purpose

Integrate QA-AI with Claude Code using repository-native instructions and direct access to canonical QA-AI files.

## Native Mechanism

Claude Code automatically loads project `CLAUDE.md` instructions and supports `@path` imports. The adapter therefore uses a concise `CLAUDE.md` that points Claude to canonical QA-AI sources instead of duplicating them.

## Package Files

```text
claude/
├── README.md
├── CLAUDE.md
├── Skill-Mapping.md
├── Workflow-Mapping.md
├── Knowledge-Mapping.md
└── Usage.md
```

## Boundary

Claude-specific instructions define routing and source-loading behavior only. Canonical skill/workflow/shared content remains authoritative.
