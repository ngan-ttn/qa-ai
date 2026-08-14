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
├── Usage.md
└── build_knowledge_bundles.py
```

## Knowledge Packaging

A Custom GPT accepts up to 20 Knowledge files. QA-AI therefore generates a bounded text-forward package instead of uploading the repository one physical file at a time.

Run from the QA-AI repository root:

```text
python adapters/chatgpt/build_knowledge_bundles.py
```

The default package is written to `output/chatgpt-knowledge/` and contains 12 Knowledge bundles plus a local manifest. Upload the 12 Markdown bundles to the Custom GPT; `bundle-manifest.json` is for package verification and does not need to be uploaded.

## Boundary

The adapter does not own QA reasoning. When adapter wording conflicts with canonical repository content, canonical repository content wins. Project requirements supplied by the user remain higher authority than reusable QA-AI Knowledge.
