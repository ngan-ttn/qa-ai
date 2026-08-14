# Cursor Adapter

## Purpose

Integrate QA-AI with Cursor using Project Rules and reusable Commands while keeping QA semantics in canonical repository sources.

## Native Mechanism

The canonical Cursor package uses:

- `.cursor/rules/*.mdc` for persistent/scoped QA-AI instructions;
- `.cursor/commands/*.md` for reusable QA workflows;
- direct repository context for skills, workflows, standards, and knowledge.

`AGENTS.md` is not the primary package because Cursor Project Rules provide explicit scoping and composition. `.cursorrules` is not used because it is a legacy mechanism.

## Phase 13 Installation Model

Copy the packaged `.cursor/` directory into the **QA-AI repository root**:

```text
<qa-ai-repository>/.cursor/
```

The rules and commands intentionally reference root-level `skills/`, `workflows/`, `shared/`, and `scripts/`. Copying only `.cursor/` into an unrelated repository would break those canonical references and is not a supported Phase 13 baseline.

## Package Files

```text
cursor/
├── README.md
├── Skill-Mapping.md
├── Workflow-Mapping.md
├── Knowledge-Mapping.md
├── Usage.md
└── package/
    └── .cursor/
        ├── rules/
        └── commands/
```

## Boundary

Cursor rules guide routing and repository interaction. They must not duplicate canonical QA capability logic. Authoritative project requirements remain higher priority than reusable QA-AI knowledge and adapter guidance.
