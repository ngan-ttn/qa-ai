# ChatGPT Knowledge Manifest

## Purpose

Define which QA-AI repository material should be exposed to a Custom GPT as Knowledge.

## Packaging Principle

Custom GPT Knowledge is reference context, not behavioral instruction. Behavioral rules remain in `Instructions.md`.

Because the Custom GPT Knowledge file count is limited, the repository must not be uploaded one article per file. Prefer text-forward bundled files generated from canonical sources.

## Recommended Bundles

| Bundle | Canonical Sources | Purpose |
|---|---|---|
| Framework | `README.md`, `FRAMEWORK.md`, `docs/` | Architecture, concepts, conventions, usage |
| Standards | `shared/standards/`, `shared/templates/`, `shared/checklists/` | Output and review contracts |
| Prompt Patterns | `shared/prompt-patterns/` | Reusable reasoning patterns |
| Skills | `skills/` | Canonical capability contracts |
| Workflows | `workflows/` | Multi-skill orchestration contracts |
| QA Knowledge | `shared/knowledge/qa/` | Generic QA knowledge |
| Testing Techniques | `shared/knowledge/testing-techniques/` | Test-design techniques |
| API Knowledge | `shared/knowledge/api/` | API-specific knowledge |
| Database Knowledge | `shared/knowledge/database/` | Database-specific knowledge |
| Domain Knowledge | `shared/knowledge/domain/` | Reusable domain concepts |
| Glossary | `shared/glossary/` | Canonical terminology |
| Evaluation | `datasets/evaluation/`, `datasets/benchmark/` | Quality evaluation semantics |

## Selection Rules

- Prefer canonical approved/frozen material.
- Preserve source-path headings inside a bundle so retrieved content remains traceable.
- Do not merge project-specific user data into reusable QA-AI bundles.
- Do not duplicate behavioral instructions from `Instructions.md` into Knowledge solely for enforcement.
- Rebuild bundles after a canonical source changes.

## Installation Check

After upload, test retrieval for at least one skill, one workflow, one standard, and one knowledge domain before considering the ChatGPT adapter ready.
