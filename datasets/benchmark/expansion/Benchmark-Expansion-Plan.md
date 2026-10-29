# Controlled Benchmark Expansion Plan

> Plan ID: BENCH-EXPANSION-001  
> Created: 2026-10-29  
> Status: Proposed only; no runs or scores are recorded by this plan.

## Goal

Extend the current Simple requirement / Structured Test Case Model pilot to Medium and Complex requirements and additional QA artifacts. Reuse the canonical criteria, rubric, and scoring model unless an approved applicability review says otherwise.

## Proposed coverage matrix

| ID | Complexity | Artifact | Evaluation focus | Priority |
|---|---|---|---|---|
| B1 | Simple | Structured Test Case Model | Existing pilot regression | P0 |
| B2 | Medium | Requirement Analysis + Business Rules | Rule extraction, ambiguity, traceability | P1 |
| B3 | Medium | Test Scenarios | Positive/negative/boundary/state coverage | P1 |
| B4 | Medium | Test Cases | Executable steps and observable expected results | P1 |
| B5 | Complex | Requirement Analysis + Business Rules | Conflicts, dependencies, unknowns, assumptions | P1 |
| B6 | Complex | Scenarios + Coverage Review | Cross-flow coverage and gaps | P1 |
| B7 | Complex | Test Cases + Regression Analysis | Change impact, traceability, regression scope | P1 |
| B8 | Medium/Complex | Risk Analysis | Risk rationale and risk-to-test linkage | P2 |

## Dataset selection rules

- Simple: explicit criteria and limited state/boundary behavior.
- Medium: multiple related rules or states, negative paths, boundaries, and limited ambiguity requiring clarification.
- Complex: multiple flows, dependencies, exceptions, permissions, conflicting statements, or missing decisions.
- Classify by reasoning challenge, not document length.
- Each dataset must have a versioned authoritative source, complexity rationale, required coverage obligations, open-question list, critical-failure examples, and reviewed reference evidence.

## Run evidence requirements

Capture unique run/run-set IDs; dataset version/hash; artifact/workflow; framework commit; platform and exact model/runtime version when visible; adapter reference; prompt reference/hash when available; timezone-aware ISO-8601 timestamp; operator; unchanged raw output; criterion-level evidence; score; critical failures; reviewer and review timestamp; adjudication and approval.

If a value is unavailable, record `unknown` and explain why. Do not guess.

## Evaluation procedure

1. Freeze dataset and evaluation configuration before execution.
2. Use the same controlled input across target platforms.
3. Save raw output before evaluator annotation.
4. Rate each criterion with evidence.
5. Double-score a subset and adjudicate material differences.
6. Repeat selected cases to estimate output variability.
7. Compare only after metadata and scoring checks pass.
8. Promote baselines only after human review.

## Metrics

Track normalized score, criterion-level results, critical failures, acceptance-criteria coverage, traceability, unsupported assumptions, incorrect or non-observable expected results, duplicate tests, reviewer agreement, metadata completeness, and repeated-run variability.

## Gates

- No critical source contradiction or fabricated business rule.
- Every mandatory acceptance criterion maps to a test obligation or a documented exclusion.
- Raw output and metadata are retained; unknowns are explicit.
- A high aggregate score cannot override critical failures.
- Critical scoring disagreements are adjudicated.

## Non-goals

This is a plan, not evidence of execution. Do not fabricate results, add skills solely to pass a benchmark, redesign architecture as part of this work, or compare different artifact types by raw score without confirming compatible scoring semantics.
