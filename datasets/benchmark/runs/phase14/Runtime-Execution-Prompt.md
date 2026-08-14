# Phase 14 Runtime Execution Prompt

Use the same task intent on ChatGPT, Claude, and Cursor after the Phase 13 adapter/instructions are active.

## Prompt

Generate executable test cases for the controlled requirement in `datasets/requirements/simple/REQ-AUTH-001.md` using the canonical QA-AI `testcase-generation` workflow.

Requirements for this run:

- Use the authoritative dataset as the product-behavior source.
- Preserve canonical workflow routing and artifact dependencies.
- Produce the final Structured Test Case Model as the evaluated deliverable.
- Keep traceability visible from requirement/business rules/scenarios into test cases where supported by the canonical contracts.
- Cover the confirmed account-lockout behavior, boundaries, reset behavior, locked-state behavior, duration behavior, and per-account isolation defined by the dataset.
- Do not invent endpoints, database fields, implementation mechanisms, UI messages, timing infrastructure, or other project-specific behavior that the dataset does not define.
- Do not replace executable expected results with generic advice when the dataset provides authoritative expected behavior.
- If you identify information that is genuinely not defined by the dataset, label it explicitly rather than guessing.

Do not use an external requirement or prior conversation behavior to modify the controlled dataset.

## Capture Rule

Save the full raw runtime response unchanged before any manual cleanup or evaluator annotation. The raw response is benchmark evidence and must remain distinguishable from later review comments.