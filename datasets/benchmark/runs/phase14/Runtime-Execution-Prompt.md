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

- Apply a Markdown table-integrity check to every table in the response: header, separator, and each data row must have the same number of cells; every column boundary must use a pipe character; never merge adjacent column labels into one cell.
- Use the exact canonical column labels and order defined by the applicable QA-AI templates for Business Rules, Test Scenarios, and Test Cases.
- The final Test Cases section must contain one canonical testcase table, with each executable TC-* appearing exactly once as a row; do not use section-per-testcase blocks or separate per-testcase step tables.
- Before finalizing, self-check every table for malformed/merged headers, missing separators, inconsistent cell counts, and duplicated testcase representations. Correct any formatting defect before returning the final artifact.

Do not use an external requirement or prior conversation behavior to modify the controlled dataset.

## Capture Rule

Save the full raw runtime response unchanged before any manual cleanup or evaluator annotation. The raw response is benchmark evidence and must remain distinguishable from later review comments.