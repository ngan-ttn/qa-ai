Analyze regression impact through the canonical QA-AI regression-analysis workflow.

1. Read `workflows/regression-analysis/README.md`.
2. Read `skills/regression-impact/README.md` and `shared/templates/Regression.md`.
3. Require an authoritative change description plus sufficient baseline context.
4. Use coverage/test/risk artifacts as supporting evidence when available.
5. Distinguish direct, indirect, retained/unaffected, and uncertain impact using only supported dependencies.
6. Produce the canonical regression scope tiers when existing confirmed coverage is available: `Minimum / Release-Gate Regression`, `Recommended Regression`, and `Full Changed-Feature Verification`.
7. Do not choose tiers by fixed testcase percentages/counts; justify inclusion from change proximity, supported dependency, and risk.
8. Keep clarification-dependent behavior outside executable regression expectations.
9. Reconcile every reported tier count and additional/overlap count with actual unique selected IDs before delivery.
10. Do not invent implementation coupling or create an execution schedule unless separately requested.
