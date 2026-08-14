# ChatGPT Knowledge Manifest

## Purpose

Define the reproducible QA-AI Knowledge package uploaded to a Custom GPT.

## Packaging Principle

Custom GPT Knowledge is reference context, not behavioral instruction. Behavioral rules remain in `Instructions.md`.

A Custom GPT currently accepts up to 20 Knowledge files. QA-AI therefore bundles canonical text sources into a smaller deterministic package instead of uploading one article per file.

## Generated Upload Package

`build_knowledge_bundles.py` generates 13 Markdown files:

| Upload File | Canonical Sources | Purpose |
|---|---|---|
| `01-framework.md` | `README.md`, `FRAMEWORK.md`, `docs/` | Architecture, concepts, conventions, usage |
| `02-standards.md` | `shared/standards/`, `shared/templates/`, `shared/checklists/` | Output and review contracts |
| `03-prompt-patterns.md` | `shared/prompt-patterns/` | Reusable reasoning patterns |
| `04-skills.md` | `skills/` | Canonical capability contracts |
| `05-workflows.md` | `workflows/` | Multi-skill orchestration contracts |
| `06-qa-knowledge.md` | `shared/knowledge/qa/` | Generic QA knowledge |
| `07-testing-techniques.md` | `shared/knowledge/testing-techniques/` | Test-design techniques |
| `08-api-knowledge.md` | `shared/knowledge/api/` | API-specific knowledge |
| `09-database-knowledge.md` | `shared/knowledge/database/` | Database-specific knowledge |
| `10-domain-knowledge.md` | `shared/knowledge/domain/` | Reusable domain concepts |
| `11-glossary.md` | `shared/glossary/` | Canonical terminology |
| `12-evaluation.md` | `datasets/evaluation/`, `datasets/benchmark/` | Quality evaluation semantics |
| `13-controlled-requirements.md` | `datasets/requirements/` | Controlled benchmark/evaluation requirement datasets referenced by repository path |

The builder also writes `bundle-manifest.json` containing source groups, bundle hashes, and byte sizes. The JSON manifest is for local verification and is not part of the 13-file Knowledge upload set.

## Build

From repository root:

```text
python adapters/chatgpt/build_knowledge_bundles.py
python adapters/chatgpt/build_knowledge_bundles.py --check
```

The default output directory is:

```text
output/chatgpt-knowledge/
```

## Selection Rules

- Prefer canonical approved/frozen material.
- Preserve source-path headings inside each bundle so retrieved content remains traceable.
- Include controlled requirement datasets used by repository benchmark/evaluation prompts so a Custom GPT can resolve those authoritative paths without guessing.
- Do not merge external or user-project data into reusable QA-AI bundles.
- Do not duplicate behavioral instructions from `Instructions.md` into Knowledge solely for enforcement.
- Rebuild bundles after canonical source changes.
- Keep the upload package within the platform Knowledge-file limit.

## Installation Check

After upload, test retrieval for at least one skill, one workflow, one standard, one knowledge domain, and one controlled requirement dataset before considering the ChatGPT adapter ready for controlled runtime evaluation.
