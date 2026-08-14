# ChatGPT Adapter Usage

## Setup

1. Create or edit a Custom GPT.
2. Copy the contents of `Instructions.md` into the GPT Instructions field.
3. Upload the approved QA-AI knowledge bundles defined by `Knowledge-Manifest.md`.
4. Add representative conversation starters such as requirement analysis, testcase generation, coverage review, and regression analysis.
5. Enable only the platform capabilities needed by the intended usage.
6. Validate in Preview before publishing or sharing.

## Runtime Use

Provide authoritative project requirements or artifacts in the conversation. The GPT should select the owning skill or workflow, use uploaded QA-AI knowledge as framework reference, and keep unsupported project behavior explicit.

## Validation Checklist

- instruction routing selects the correct owning skill;
- a workflow request follows canonical stage order;
- uploaded knowledge can retrieve skill/workflow/standard content;
- project requirements override generic knowledge;
- missing information produces assumptions/questions rather than invented rules;
- specialized API/SQL requests stay with specialized skills;
- output remains traceable and reviewable.

## Maintenance

When canonical QA-AI source content changes, review `Instructions.md`, rebuild affected Knowledge bundles, and rerun adapter validation before treating the new package as stable.
