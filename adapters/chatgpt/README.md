# ChatGPT Adapter

## Purpose

Package QA-AI for a Custom GPT while preserving the platform-independent contracts in `skills/`, `workflows/`, and `shared/`.

## Native Mechanism

The adapter uses:

- Custom GPT **Instructions** for behavior, routing, boundaries, and workflow discipline;
- Custom GPT **Knowledge** for reference content;
- conversation starters for common QA entry points;
- optional platform capabilities only when the task requires them.

## Package Files

```text
chatgpt/
├── README.md
├── Instructions.md
├── Knowledge-Manifest.md
├── Skill-Mapping.md
├── Workflow-Mapping.md
└── Usage.md
```

## Constraint

Custom GPT Knowledge has a finite file limit. The adapter therefore selects or bundles canonical reference material rather than attempting to upload the repository one physical file at a time.

## Boundary

The adapter does not own QA reasoning. When adapter wording conflicts with canonical repository content, canonical repository content wins.
