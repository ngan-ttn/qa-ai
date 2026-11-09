Generate test artifacts through the canonical QA-AI testcase-generation workflow.

1. Read `workflows/testcase-generation/README.md`.
2. Resolve each required skill from `skills/` in the workflow-defined order.
3. Preserve upstream artifact contracts and traceability.
4. Use authoritative project requirements as the test oracle.
5. Do not invent missing project behavior.
6. Keep generic testcase design technology-neutral unless specialized API/SQL validation is explicitly required.
7. Follow `shared/templates/TestCase.md` exactly: the executable `TC-*` inventory MUST be one canonical Markdown table under `## Test Cases`; do not render section-per-testcase blocks or separate per-testcase steps tables.
8. Keep clarification-dependent/Blocked behavior without an authoritative oracle outside executable testcase rows.
9. Reconcile all reported testcase/scenario/category counts against actual unique IDs/rows before delivery.
10. Run applicable validators when repository artifacts are written or changed.
