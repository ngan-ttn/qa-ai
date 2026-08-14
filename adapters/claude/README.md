# Claude Adapter

## Purpose

Integrate QA-AI with Claude Code using repository-native instructions and direct access to canonical QA-AI files.

## Native Mechanism

Claude Code loads project `CLAUDE.md` instructions and supports repository-relative `@path` imports. The adapter therefore uses a concise `CLAUDE.md` that points Claude to canonical QA-AI sources instead of duplicating them.

## Phase 13 Installation Model

The supported baseline installs the adapter instruction file as:

```text
<qa-ai-repository>/CLAUDE.md
```

This placement is required because the instruction file references canonical root paths such as `skills/`, `workflows/`, `shared/`, `datasets/`, and `scripts/`.

Copying only `CLAUDE.md` into an unrelated repository without exposing the QA-AI core is not a valid Phase 13 installation.

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

Claude-specific instructions define routing and source-loading behavior only. Canonical skill/workflow/shared content remains authoritative, and authoritative project requirements remain higher priority than reusable QA-AI knowledge.
