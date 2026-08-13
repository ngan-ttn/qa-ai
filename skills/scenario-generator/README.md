# Scenario Generator

## Purpose

The `scenario-generator` skill transforms structured requirement/business-rule context into a structured test scenario model.

It owns scenario-level test design: identifying what behaviors and conditions need coverage. It does not generate executable test cases, API-specialized technical test definitions, SQL validation logic, or concrete test datasets.

---

## Capability

```text
Structured Requirement / Business Rules
        ↓
Establish Coverage Scope
        ↓
Derive Behavioral Scenarios
        ↓
Apply Relevant Test-Design Techniques
        ↓
Incorporate Risk Priorities
        ↓
Organize and Trace Scenarios
        ↓
Structured Test Scenario Model
```

---

## When To Use

Use this skill when structured requirement or business-rule context is available and behavior needs to be decomposed into traceable test scenarios before detailed testcase generation.

---

## Input

### Required Input

At least one sufficiently structured authoritative source:

- Structured Business Rule Model; or
- Structured Requirement Analysis containing enough behavior to derive scenarios.

### Optional Input

- Structured Risk Analysis;
- original requirements/acceptance criteria;
- user flows/state models;
- domain context;
- API/interface context;
- known constraints and dependencies;
- existing coverage for reuse/gap analysis.

---

## Processing

### Step 1 — Establish Coverage Scope

Identify actors, behaviors, rules, states, boundaries, dependencies, and unresolved assumptions that constrain scenario generation.

### Step 2 — Derive Core Scenarios

Identify positive, negative, alternate, exception, permission, state, and dependency scenarios supported by the inputs.

### Step 3 — Apply Test-Design Techniques

Use relevant techniques such as equivalence partitioning, boundary analysis, decision tables, state transitions, use-case testing, risk-based testing, or experience-based techniques when applicable. Techniques guide derivation; they do not justify inventing missing rules.

### Step 4 — Incorporate Risk

When Structured Risk Analysis exists, ensure high-priority risks have scenario-level coverage and preserve risk traceability. Risk prioritizes coverage but does not replace requirement/rule evidence.

### Step 5 — Organize Scenario Relationships

Group scenarios by feature/flow/behavior and identify relationships, prerequisites, mutually exclusive paths, and reusable coverage.

### Step 6 — Detect Gaps and Duplication

Identify missing, duplicate, conflicting, or ambiguous scenario coverage and surface clarification questions.

### Step 7 — Produce Structured Test Scenario Model

Provide stable IDs, objective, traceability, conditions, expected behavior at scenario level, priority/risk context, and assumptions.

---

## Output

Typical fields include:

- Scenario ID;
- objective/title;
- requirement/rule traceability;
- risk traceability where available;
- actor/preconditions;
- scenario condition or flow;
- expected behavior at scenario level;
- technique/coverage rationale where useful;
- priority;
- dependencies;
- assumptions/open questions.

The exact representation follows applicable shared standards/templates.

---

## Dependencies

| Resource | Purpose |
|---|---|
| `shared/standards/` | Output/documentation conventions |
| `shared/templates/` | Scenario artifact structure |
| `shared/checklists/` | Scenario review controls |
| `shared/prompt-patterns/` | Reusable generation reasoning |
| `shared/knowledge/testing-techniques/` | Test-design techniques |
| `shared/knowledge/qa/` | Generic QA context |
| `shared/knowledge/domain/` | Business semantics when relevant |
| `shared/knowledge/api/` | API context without taking API-specialized ownership |
| `shared/knowledge/database/` | Data/persistence context without generating SQL validation |

---

## Consumers

The output may be consumed by:

- `testcase-generator`;
- `test-data-generator`;
- `coverage-reviewer`;
- `api-test-generator` when generic scenarios require API-specific expansion;
- `regression-impact` as existing coverage evidence;
- testcase-generation and regression workflows.

---

## Limitations

This skill does not:

- analyze raw requirements as its primary responsibility;
- extract business rules;
- generate executable detailed test cases;
- generate API-specific request/response test definitions;
- write SQL validation queries;
- create concrete test datasets;
- perform coverage review or regression impact analysis.

---

## Validation

Validate that:

- scenarios trace to supported requirements/rules/risks;
- each scenario has a clear primary coverage objective;
- relevant positive, negative, boundary, state, permission, exception, and dependency behavior is considered;
- test-design techniques are applied only where relevant;
- high-priority risks are represented when risk input exists;
- duplicates are minimized without collapsing materially different outcomes;
- ambiguity and missing rules are explicit;
- scenario detail stops before executable testcase-level implementation;
- downstream consumers can use the model without reconstructing its traceability.