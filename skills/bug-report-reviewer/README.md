# Bug Report Reviewer

## Purpose

The `bug-report-reviewer` skill evaluates a bug report for completeness, reproducibility, evidence quality, consistency, and actionability.

It improves the quality of defect communication without taking ownership of the defect lifecycle, deciding whether code is actually defective, or inventing missing execution evidence.

---

## Capability

```text
Bug Report + Supporting Context
        ↓
Parse Report Structure
        ↓
Check Reproducibility
        ↓
Check Expected vs Actual Behavior
        ↓
Check Evidence and Environment
        ↓
Check Severity/Priority Support
        ↓
Identify Gaps and Ambiguities
        ↓
Structured Bug Report Review
```

The reviewer distinguishes report-quality findings from product-defect conclusions.

---

## When To Use

Use this skill when:

- a newly created bug needs QA quality review;
- a defect cannot be reproduced reliably from the report;
- expected and actual behavior may be ambiguous;
- evidence, environment, test data, or preconditions may be incomplete;
- severity or priority rationale needs consistency review;
- bug reports from multiple contributors need a common quality standard;
- a report should be improved before handoff to development or triage.

---

## Input

### Required Input

- bug report or structured defect artifact.

The report should contain whatever information is currently available; incomplete reports are valid inputs because identifying missing information is part of the capability.

### Optional Input

- requirement or acceptance criteria;
- Structured Requirement Analysis;
- related business rules;
- test case or scenario that exposed the issue;
- screenshots, logs, request/response samples, database evidence, or video references;
- environment/build/version information;
- related defect history;
- project severity/priority definitions.

The skill must not fabricate evidence that was not supplied.

---

## Processing

### Step 1 — Parse the Report

Identify title, context, environment, preconditions, steps, test data, actual result, expected result, evidence, severity, priority, and references when present.

### Step 2 — Review Title and Scope

Check whether the title identifies the affected function and observable failure without being vague, overly broad, or embedding unsupported root-cause claims.

### Step 3 — Review Reproducibility

Check whether another qualified tester or developer could reproduce the reported behavior from the supplied:

- preconditions;
- environment/build;
- account/role/state;
- test data;
- ordered steps;
- timing or concurrency conditions where relevant.

Flag missing or contradictory information rather than filling it in.

### Step 4 — Review Expected and Actual Results

Verify that actual behavior is observable and specific, and that expected behavior is supported by a requirement, rule, accepted design, or clearly labeled expectation.

If expected behavior is not authoritative, flag the need for clarification instead of declaring the implementation wrong.

### Step 5 — Review Evidence

Assess whether evidence is relevant, readable, attributable to the reported execution, and sufficient for the claim being made.

When API, database, logs, or network evidence is relevant, identify what is missing without inventing values.

### Step 6 — Review Severity and Priority

Evaluate severity and priority only against supplied project definitions or clearly stated generic reasoning.

Severity reflects impact; priority reflects urgency/order. The skill must not invent business urgency, affected-user counts, revenue loss, or production exposure.

### Step 7 — Check Consistency and Duplication Signals

Identify contradictions between title, steps, actual result, evidence, environment, and classification. Note possible duplicate indicators only when supporting references are available; do not declare two defects duplicates without evidence.

### Step 8 — Produce Review Findings

Classify findings by importance and produce actionable corrections or clarification requests while preserving the reporter's factual evidence.

---

## Output

The skill produces a Structured Bug Report Review containing, where applicable:

- overall review status;
- completeness findings;
- reproducibility findings;
- expected/actual consistency findings;
- evidence findings;
- environment/test-data findings;
- severity/priority findings;
- ambiguity or unsupported-claim findings;
- required corrections;
- clarification questions;
- optional improved wording that does not change facts.

Suggested finding structure:

| Field | Description |
|---|---|
| Finding ID | Stable review identifier |
| Area | Title, Steps, Evidence, Severity, etc. |
| Issue | Specific report-quality problem |
| Impact | Why the issue reduces actionability |
| Recommendation | Concrete correction or clarification |
| Blocking | Whether reliable triage/reproduction is blocked |

---

## Dependencies

| Resource | Purpose |
|---|---|
| `shared/standards/` | Documentation and output conventions |
| `shared/checklists/` | Defect/test quality checks where available |
| `shared/templates/` | Bug/QA artifact structure where applicable |
| `shared/knowledge/qa/` | Defect lifecycle, severity/priority, reporting, RCA boundaries |
| `shared/knowledge/api/` | API evidence interpretation when relevant |
| `shared/knowledge/database/` | Database evidence interpretation when relevant |
| `shared/knowledge/domain/` | Business expectation context when relevant |

---

## Consumers

The output may be consumed by:

- QA reviewers;
- defect triage activities;
- developers receiving defect reports;
- workflows that enforce QA artifact quality;
- future deterministic validation tooling where checks can be automated.

The review does not replace human/product decisions about acceptance, ownership, or release priority.

---

## Limitations

This skill does not:

- execute reproduction steps;
- prove that a product defect exists;
- determine root cause from insufficient evidence;
- modify source code;
- assign a defect to a person/team;
- manage defect workflow states;
- invent missing logs, screenshots, API responses, database values, or test data;
- infer project-specific severity/priority policy when none is supplied;
- rewrite factual evidence to make a report appear stronger.

---

## Validation

The review should be validated to ensure:

- findings concern report quality rather than unsupported product conclusions;
- missing information is explicitly identified;
- expected behavior is traceable or marked as needing confirmation;
- reproduction steps are assessed for order, state, data, and environment sufficiency;
- evidence recommendations are proportional to the reported issue;
- severity and priority are not conflated;
- no evidence is fabricated;
- recommendations preserve the original factual meaning;
- blocking issues are distinguishable from optional improvements;
- the final review is actionable for the reporter and downstream triage.