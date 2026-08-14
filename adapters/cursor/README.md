# Cursor Adapter

## Purpose

Integrate QA-AI with Cursor using project rules and reusable commands while keeping QA semantics in canonical repository sources.

## Native Mechanism

The canonical Cursor package uses:

- `.cursor/rules/*.mdc` for persistent/scoped QA-AI instructions;
- `.cursor/commands/*.md` for reusable QA workflows;
- direct repository context for skills, workflows, standards, and knowledge.

`AGENTS.md` is not the primary package because Cursor Project Rules provide better scoping and composition.

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

Cursor rules guide routing and repository interaction. They must not duplicate canonical QA capability logic.
