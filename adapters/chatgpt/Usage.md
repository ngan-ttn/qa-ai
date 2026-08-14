# ChatGPT Adapter Usage

## Build Knowledge Package

From the QA-AI repository root:

```text
python adapters/chatgpt/build_knowledge_bundles.py
python adapters/chatgpt/build_knowledge_bundles.py --check
```

Use the 13 generated Markdown files under `output/chatgpt-knowledge/` as the Custom GPT Knowledge upload package. Keep `bundle-manifest.json` locally for verification; it is not required as GPT Knowledge.

## Setup

1. Create or edit a Custom GPT.
2. Copy the contents of `Instructions.md` into the GPT Instructions field.
3. Upload the 13 generated QA-AI Knowledge bundles defined by `Knowledge-Manifest.md`.
4. Add representative conversation starters such as requirement analysis, testcase generation, coverage review, and regression analysis.
5. Enable only the platform capabilities needed by the intended usage.
6. Validate in Preview before publishing or sharing.

## Runtime Use

Provide authoritative project requirements or artifacts in the conversation. The GPT should select the owning skill or workflow, use uploaded QA-AI Knowledge as framework reference, and keep unsupported project behavior explicit.

When a controlled benchmark/evaluation prompt refers to a source under `datasets/requirements/`, the GPT must retrieve that exact source from `13-controlled-requirements.md` before asserting source-dependent thresholds, durations, states, or expected results. If retrieval fails, the GPT must report the source as unavailable instead of reconstructing its behavior from memory, nearby examples, or prior conversation context.

## Validation Checklist

- Knowledge package build and `--check` pass;
- exactly 13 QA-AI Markdown Knowledge bundles are selected for upload;
- instruction routing selects the correct owning skill;
- a workflow request follows canonical stage order;
- uploaded knowledge retrieves skill/workflow/standard content in Preview;
- controlled requirement retrieval succeeds for at least one `datasets/requirements/` source;
- project requirements override reusable QA-AI knowledge;
- missing information produces assumptions/questions rather than invented rules;
- an unavailable authoritative source blocks source-dependent expected results instead of causing guessed thresholds or durations;
- specialized API/SQL requests stay with specialized skills;
- output remains traceable and reviewable.

## Maintenance

When canonical QA-AI source content changes, rebuild affected Knowledge bundles, rerun `--check`, review `Instructions.md`, and repeat Preview validation before treating the new package as stable.
