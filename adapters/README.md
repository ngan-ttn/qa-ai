# Platform Adapters

## Purpose

`adapters/` packages the platform-independent QA-AI core for supported AI runtimes without duplicating QA logic.

## Canonical Platforms

```text
adapters/
├── chatgpt/
├── claude/
└── cursor/
```

## Boundary

Adapters may define platform-native instructions, context-loading rules, commands, installation steps, and mappings. They must not redefine skill behavior, workflow contracts, shared standards, knowledge content, or evaluation semantics.

Canonical source precedence:

```text
Authoritative project input
        ↓
workflows/ and skills/
        ↓
shared/ standards / templates / knowledge
        ↓
platform adapter
        ↓
platform runtime
```

## Common Contract

Every adapter must document:

- supported runtime and native mechanism;
- skill mapping;
- workflow mapping;
- knowledge/context mapping;
- installation or configuration steps;
- platform limitations;
- validation steps;
- fallback behavior when required context is unavailable.

## Supported Baseline

| Platform | Native Integration Mechanism | Status |
|---|---|---|
| ChatGPT | Custom GPT Instructions + Knowledge files | In Progress |
| Claude | Claude Code `CLAUDE.md` + repository references | In Progress |
| Cursor | `.cursor/rules/*.mdc` + `.cursor/commands/*.md` | In Progress |

## Design Principle

Platform-specific packaging is allowed. Platform-specific QA semantics are not.
