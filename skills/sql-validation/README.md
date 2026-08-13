# SQL Validation

## Purpose

The `sql-validation` skill transforms QA validation needs and authoritative data context into structured database/SQL validation logic.

It helps QA verify persistence, integrity, relationships, state changes, and data outcomes without taking ownership of database design, production query optimization, or application implementation.

---

## Capability

```text
QA Validation Need + Data Context
        ↓
Identify Data Assertions
        ↓
Map Assertions to Known Schema
        ↓
Define Safe Read Validation
        ↓
Define Before/After or Relationship Checks
        ↓
Handle Ambiguity and Data Safety
        ↓
Structured SQL Validation Model
```

SQL is a means of verification. The capability starts from the QA assertion, not from writing arbitrary queries.

---

## When To Use

Use this skill when:

- UI/API behavior has persistence side effects that require database verification;
- data integrity or relationship rules need validation;
- before/after state should be compared;
- duplicate, missing, inconsistent, or orphaned data needs checking;
- audit/history records require verification;
- calculations or stored values need independent QA validation;
- a testcase requires explicit SQL validation guidance.

---

## Input

### Required Input

At least one QA validation objective plus sufficient authoritative data context, such as:

- expected persisted outcome and known schema/table/field information;
- database fixture/schema documentation;
- supplied SQL/database contract;
- existing testcase with database validation requirement.

### Optional Input

- Structured Requirement Analysis;
- Structured Business Rule Model;
- Structured Test Case Model;
- Structured API Test Model;
- database relationships and constraints;
- sample records;
- audit/history model;
- transaction behavior;
- environment-specific safe-query constraints.

If schema details are missing, the skill must describe the required validation logically rather than invent table or column names.

---

## Processing

### Step 1 — Define the QA Assertion

State exactly what must be verified: record creation, update, deletion/soft deletion, relationship, quantity, status, audit entry, uniqueness, aggregation, or absence of unintended changes.

### Step 2 — Identify Authoritative Data Mapping

Map business entities and expected outcomes to known tables, columns, keys, relationships, views, or records.

Distinguish confirmed mappings from inferred or missing mappings.

### Step 3 — Select Validation Strategy

Choose the least invasive validation approach that can prove the assertion, normally read-only queries such as `SELECT`, aggregation, joins, existence checks, before/after comparisons, or constraint inspection when permitted.

### Step 4 — Define Query Logic

Construct or describe query logic with:

- deterministic filters;
- stable identifiers;
- appropriate joins;
- expected cardinality;
- null handling;
- ordering only when relevant;
- expected values or relationships.

Avoid broad unbounded reads when narrower validation is possible.

### Step 5 — Validate Integrity and Side Effects

Where applicable, check:

- expected row count;
- uniqueness;
- referential relationships;
- persisted state;
- calculated/aggregated values;
- timestamps/version fields when authoritative;
- audit/history records;
- absence of unintended updates;
- transaction consistency visible to the tester.

### Step 6 — Address Transaction and Timing Context

If asynchronous processing, eventual consistency, transaction boundaries, or concurrent operations are relevant, identify the required observation point and uncertainty. Do not invent commit timing or isolation behavior.

### Step 7 — Apply Data Safety

Prefer read-only validation. Any destructive or mutating SQL is outside the default capability and must not be proposed as routine validation. Sensitive data should be minimized and masked according to authoritative project rules.

### Step 8 — Produce Structured SQL Validation Model

Provide the assertion, required schema context, query/query pattern where safely supported, expected result, and assumptions.

---

## Output

Typical Structured SQL Validation Model fields:

| Field | Description |
|---|---|
| Validation ID | Stable identifier |
| Traceability | Requirement/test/API behavior being verified |
| QA Assertion | What persistence fact must be proven |
| Data Source | Known table/view/entity context |
| Preconditions | Required record/state |
| Query / Query Pattern | Read-only SQL or logical query pattern |
| Parameters | Stable identifiers/test values |
| Expected Result | Verifiable row/value/relationship expectation |
| Safety Notes | Environment/data restrictions |
| Assumptions / Missing Mapping | Unresolved schema information |

When exact schema is unavailable, output pseudonymous placeholders such as `<table>` or a logical query description instead of pretending a concrete schema exists.

---

## Dependencies

| Resource | Purpose |
|---|---|
| `shared/standards/` | Output/documentation conventions |
| `shared/knowledge/database/` | SQL, transactions, integrity, relationships, database-testing knowledge |
| `shared/knowledge/qa/` | Generic QA verification principles |
| `shared/knowledge/api/` | API-to-persistence context when relevant |
| `shared/knowledge/domain/` | Business entity/rule semantics when relevant |
| `shared/templates/` | Reusable QA artifact structure where applicable |

---

## Consumers

The output may be consumed by:

- `testcase-generator` as database-validation detail;
- `api-test-generator` for persistence assertions;
- QA engineers performing database checks;
- `coverage-reviewer` when database validation is required for coverage;
- workflows that produce technical validation artifacts;
- future deterministic tooling that validates syntax or executes approved read-only queries.

---

## Limitations

This skill does not:

- design database schemas;
- invent tables, columns, keys, or relationships;
- optimize production queries;
- perform DBA operations;
- execute SQL;
- mutate production/test data by default;
- generate destructive `DELETE`, `DROP`, `TRUNCATE`, or uncontrolled `UPDATE` operations as validation steps;
- infer transaction isolation or replication behavior without evidence;
- expose secrets or unnecessary personal/sensitive data;
- replace application-level validation when database access is unavailable or prohibited.

---

## Validation

The output should be validated to ensure:

- every SQL check starts from a clear QA assertion;
- schema references are authoritative or explicitly marked as placeholders;
- query filters identify the intended test data deterministically;
- expected row count/value/relationship is measurable;
- joins and aggregation do not introduce false conclusions;
- null, duplicate, and cardinality behavior are considered where relevant;
- transaction/timing assumptions are visible;
- default validation is read-only and environment-safe;
- sensitive data exposure is minimized;
- database checks add evidence rather than duplicate application assertions without purpose;
- project schema and database rules override generic knowledge.