# Testcase Generator

## Purpose

The `testcase-generator` skill transforms structured test scenarios into executable, generic QA test cases.

It owns testcase-level execution detail while remaining technology-neutral. API-specific request/response expansion belongs to `api-test-generator`; database-specific verification logic belongs to `sql-validation`; reusable data derivation belongs to `test-data-generator`.

---

## Capability

```text
Structured Test Scenario Model
        ↓
Resolve Preconditions and Objective
        ↓
Define Executable Steps
        ↓
Define Observable Expected Results
        ↓
Attach Data / Risk / Traceability Context
        ↓
Check Atomicity and Duplication
        ↓
Structured Test Case Model
```

---

## When To Use

Use this skill when scenario-level coverage has been established and executable test cases are required for manual execution, downstream specialization, coverage review, or export.

---

## Input

### Required Input

- Structured Test Scenario Model with sufficient objective and traceability.

### Optional Input

- Structured Requirement Analysis;
- Structured Business Rule Model;
- Structured Risk Analysis;
- Structured Test Data Model;
- authoritative acceptance criteria;
- API/database/UI context needed to make generic steps executable;
- existing test cases for reuse/duplication checks.

Test data may be supplied before generation or attached later. `test-data-generator` is therefore an optional enrichment relationship, not a mandatory cyclic dependency.

---

## Processing

### Step 1 — Resolve Test Objective

Confirm the single primary behavior being verified and its upstream scenario/rule/requirement traceability.

### Step 2 — Define Preconditions

Specify actor/role, state, setup, dependencies, and required data conditions without inventing environment facts.

### Step 3 — Define Executable Steps

Create ordered, actionable steps at the level needed by a qualified tester. Avoid implementation-specific detail that is unsupported by the input.

### Step 4 — Define Expected Results

Attach observable, measurable expected results to the relevant action or final state. Expected behavior must trace to authoritative requirements/rules or be explicitly marked as needing confirmation.

### Step 5 — Attach Test Data

Reference supplied Structured Test Data or describe logical data needs. Do not fabricate business-valid values when constraints are unknown.

### Step 6 — Incorporate Risk and Priority

Preserve scenario/risk priority and ensure critical validation is explicit. This skill does not recalculate the risk model.

### Step 7 — Identify Technical Specialization Needs

Mark cases requiring API-specific, SQL/database-specific, or other specialized validation. Generic cases may reference outputs from specialized skills, but this skill does not duplicate those capabilities.

### Step 8 — Check Atomicity, Reuse, and Gaps

Keep one primary objective per case, avoid unnecessary duplicate cases, and surface missing preconditions, expected behavior, or data.

### Step 9 — Produce Structured Test Case Model

Organize stable IDs, title, preconditions, steps, data references, expected results, traceability, priority, and assumptions.

---

## Output

Typical fields include:

- Test Case ID;
- scenario/requirement/rule/risk traceability;
- title/objective;
- preconditions;
- ordered steps;
- test-data references/requirements;
- expected results;
- priority;
- technical-validation references;
- assumptions/open questions.

---

## Dependencies

| Resource | Purpose |
|---|---|
| `shared/standards/` | Output/documentation conventions |
| `shared/templates/` | Testcase structure |
| `shared/checklists/` | Testcase quality controls |
| `shared/prompt-patterns/` | Reusable generation reasoning |
| `shared/knowledge/qa/` | Generic testcase principles |
| `shared/knowledge/testing-techniques/` | Preserve scenario design intent |
| `shared/knowledge/domain/` | Business semantics when relevant |

API/database knowledge should normally be consumed through the specialized skills when detailed technical validation is required.

---

## Consumers

The output may be consumed by:

- `coverage-reviewer`;
- `test-data-generator` when concrete data still needs derivation;
- `api-test-generator` for API-specific expansion;
- `sql-validation` for database assertions;
- `regression-impact` as existing coverage evidence;
- testcase-generation/regression workflows;
- QA execution and future exporters.

Feedback from specialized skills may enrich a testcase, but no specialized skill is a mandatory prerequisite for generic testcase generation.

---

## Limitations

This skill does not:

- analyze raw requirements or extract rules;
- generate scenario-level coverage;
- perform API-specialized test design;
- design SQL/database validation logic;
- own reusable test-data generation;
- perform coverage review;
- perform regression impact analysis;
- execute tests.

---

## Validation

Validate that:

- each case has one primary objective and upstream traceability;
- preconditions and data needs are sufficient and non-invented;
- steps are ordered and executable;
- expected results are observable and authoritative or explicitly uncertain;
- risk/priority context is preserved where available;
- technical specialization is referenced rather than duplicated;
- duplicate coverage is minimized;
- assumptions/open questions are visible;
- cases can be executed without downstream consumers having to infer missing core logic.