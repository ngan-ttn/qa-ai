# Platform Adapters

## Purpose

`adapters/` packages the platform-independent QA-AI core for supported AI runtimes without duplicating QA logic.

## Canonical Platforms

```text
adapters/
├── README.md
├── Integration-Contract.md
├── chatgpt/
├── claude/
└── cursor/
```

## Boundary

Adapters may define platform-native instructions, context-loading rules, commands, installation steps, packaging, and mappings. They must not redefine skill behavior, workflow contracts, shared standards, knowledge content, or evaluation semantics.

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

`Integration-Contract.md` defines the supported Phase 13 runtime topology and repository-root assumptions.

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

| Platform | Native Integration Mechanism | Phase 13 State |
|---|---|---|
| ChatGPT | Custom GPT Instructions + bounded Knowledge bundles | In Progress |
| Claude | Claude Code repository-root `CLAUDE.md` + repository references | In Progress |
| Cursor | Repository-root `.cursor/rules/*.mdc` + `.cursor/commands/*.md` | In Progress |

## Baseline Installation Model

- ChatGPT consumes generated/uploaded Knowledge bundles and does not require direct repository access.
- Claude and Cursor Phase 13 packages are installed into the QA-AI repository root so canonical `skills/`, `workflows/`, `shared/`, and `scripts/` paths resolve.
- Copying only Claude/Cursor adapter files into an unrelated repository is not a supported baseline unless the QA-AI core is also exposed under a separately validated path contract.

## Design Principle

Platform-specific packaging is allowed. Platform-specific QA semantics are not.
