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
- Structured Coverage Assessment;
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

Attach observable, measurable expected results to the relevant action or final state. Expected behavior must trace to authoritative requirements/rules. Clarification-dependent behavior without an authoritative oracle must remain outside executable testcase rows.

### Step 5 — Attach Test Data

Reference supplied Structured Test Data or describe logical data needs. Do not fabricate business-valid values when constraints are unknown.

### Step 6 — Incorporate Risk and Priority

Preserve scenario/risk priority and ensure critical validation is explicit. This skill does not recalculate the risk model.

### Step 7 — Use Coverage Review When Available

Treat a supplied Structured Coverage Assessment as active design input:

- `Covered` items do not require artificial extra cases solely to increase count.
- `Weakly Covered` items may justify testcase-level decomposition/precision when authoritative behavior is already known.
- `Gap` items may be closed at testcase level only when the missing confirmed behavior can be represented without changing the upstream scenario contract; otherwise route remediation to the owning upstream skill.
- `Blocked` items must not be converted into executable expected results until the authoritative oracle/dependency is resolved.

The testcase generator does not modify the coverage review or upstream scenarios as a side effect.

### Step 8 — Identify Technical Specialization Needs

Mark cases requiring API-specific, SQL/database-specific, or other specialized validation. Generic cases may reference outputs from specialized skills, but this skill does not duplicate those capabilities.

### Step 9 — Check Atomicity, Reuse, and Gaps

Keep one primary objective per case, avoid unnecessary duplicate cases, and surface missing preconditions, expected behavior, or data.

### Step 10 — Produce Structured Test Case Model

Organize stable IDs, title, preconditions, steps, data references, expected results, traceability, priority, and assumptions in the canonical rendering defined below.

---

## Output

The canonical rendering follows `shared/templates/TestCase.md` and uses a **hybrid + table-oriented document**.

### Mandatory Canonical Representation

The complete executable testcase inventory MUST be rendered as **one canonical Markdown table under `## Test Cases`**.

- Each executable `TC-*` MUST occupy one row.
- Do NOT render `### TC-*` or other section-per-testcase blocks.
- Do NOT create a separate step table for each testcase.
- Ordered steps MUST remain inside the `Test Steps` cell using numbered text separated by `<br>`.
- Shared suite-level context may remain in separate sections, but case-specific setup/data/expected results must remain visible in the row.
- Clarification-dependent cases without an authoritative oracle MUST remain outside the executable `TC-*` inventory.

The executable inventory uses these canonical columns:

| Test Case ID | Module / Function | Scenario ID | Test Case Title | Preconditions / Setup | Test Steps | Test Data | Expected Result | Priority | Traceability |
|---|---|---|---|---|---|---|---|---|---|

The testcase table must preserve:

- stable Test Case ID;
- scenario/requirement/rule/risk traceability;
- module/function grouping;
- single test objective/title;
- case-specific preconditions/setup;
- ordered executable steps;
- test-data references/requirements;
- observable expected result;
- priority;
- uncertainty without inventing expected behavior.

---

## Dependencies

| Resource | Purpose |
|---|---|
| `shared/standards/` | Output/documentation conventions |
| `shared/templates/` | Testcase structure and canonical rendering |
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

- `## Test Cases` contains one canonical executable testcase table;
- every executable `TC-*` appears exactly once as a row in that inventory;
- no `### TC-*`/section-per-testcase rendering exists;
- no testcase uses a separate nested/per-item steps table;
- each testcase row has one primary objective and upstream traceability;
- preconditions and data needs are sufficient and non-invented;
- steps are ordered, executable, and represented with numbered `<br>` content in the `Test Steps` cell;
- expected results are observable and authoritative;
- risk/priority context is preserved where available;
- technical specialization is referenced rather than duplicated;
- duplicate coverage is minimized;
- `Blocked`/clarification-dependent behavior without an authoritative oracle is excluded from executable rows;
- coverage-review findings are closed only where testcase-level precision is source-supported;
- all reported testcase/scenario/coverage counts reconcile with actual unique IDs/rows;
- the canonical testcase table remains readable and export-friendly;
- cases can be executed without downstream consumers having to infer missing core logic.

Any failure of the mandatory canonical representation is a format-validation failure and must be corrected before delivery.
