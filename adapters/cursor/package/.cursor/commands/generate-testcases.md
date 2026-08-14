Generate test artifacts through the canonical QA-AI testcase-generation workflow.

1. Read `workflows/testcase-generation/README.md`.
2. Resolve each required skill from `skills/` in the workflow-defined order.
3. Preserve upstream artifact contracts and traceability.
4. Use authoritative project requirements as the test oracle.
5. Do not invent missing project behavior.
6. Keep generic testcase design technology-neutral unless specialized API/SQL validation is explicitly required.
7. Run applicable validators when repository artifacts are written or changed.
