# Test Data Generator

## Purpose

The `test-data-generator` skill transforms test objectives, rules, constraints, and data models into structured test-data requirements and reusable test datasets.

It focuses on data needed to exercise QA coverage. It does not provision environments, create production-like identities, or own runtime fixture infrastructure.

---

## Capability

```text
Test Objective + Rules + Data Constraints
        ↓
Identify Data Dimensions
        ↓
Derive Valid / Invalid / Boundary Partitions
        ↓
Model Relationships and State
        ↓
Apply Privacy and Safety Constraints
        ↓
Build Reusable Data Sets
        ↓
Structured Test Data Model
```

Generated data must preserve traceability to the behavior it is intended to test and must not invent unsupported business-valid values.

---

## When To Use

Use this skill when:

- scenarios or test cases require explicit test data;
- valid, invalid, boundary, null, duplicate, or state-specific data is needed;
- business-rule combinations require representative datasets;
- API or database tests require payload/record values;
- role/account/status combinations need structured representation;
- reusable data partitions are needed across multiple tests;
- sensitive production data should be replaced with safe synthetic equivalents.

---

## Input

### Required Input

At least one test objective or structured testing artifact, such as:

- Structured Test Scenario Model;
- Structured Test Case Model;
- Structured API Test Model;
- explicit test-data requirement with sufficient rules/constraints.

### Optional Input

- Structured Requirement Analysis;
- Structured Business Rule Model;
- Structured Risk Analysis;
- field/schema definitions;
- API request schemas;
- database constraints;
- domain entities;
- equivalence partitions and boundaries;
- account/role/state definitions;
- existing reusable fixtures;
- data privacy or masking rules.

---

## Processing

### Step 1 — Identify Data Objectives

For each test objective, determine which input values, entity states, relationships, roles, historical conditions, or persisted records are required to trigger the behavior.

### Step 2 — Extract Data Constraints

Capture authoritative constraints including:

- required/optional/nullability;
- type and format;
- min/max or length boundaries;
- allowed/forbidden values;
- uniqueness;
- relationships;
- state/status;
- temporal conditions;
- business-rule dependencies;
- permission/ownership context.

Do not invent constraints absent from authoritative inputs.

### Step 3 — Derive Data Partitions

Use applicable testing techniques to derive representative:

- valid partitions;
- invalid partitions;
- minimum/maximum and just-inside/outside boundaries;
- empty/null/missing variants;
- duplicate/conflict variants;
- special-character/format variants;
- state combinations;
- role/ownership combinations;
- date/time variants;
- relationship/cardinality variants.

Only include partitions relevant to the test objective.

### Step 4 — Model Dependencies and Setup

Identify dependencies between data values and required setup, such as parent/child records, existing balances/quantities, prior workflow states, related accounts, or prerequisite transactions.

Separate data definition from environment provisioning.

### Step 5 — Apply Privacy and Safety Controls

Prefer synthetic, non-sensitive values. Do not generate real credentials, government identifiers, payment secrets, access tokens, or personal data that could be mistaken for real protected information.

When realistic format is required, use clearly synthetic placeholders consistent with authoritative project rules.

### Step 6 — Optimize Reuse Without Losing Coverage

Reuse datasets when the same state/value combination satisfies multiple tests, but keep distinct data when isolation, mutation, concurrency, or traceability requires it.

### Step 7 — Define Expected Data State

Where applicable, specify pre-execution and expected post-execution state so consumers can distinguish input data from verification data.

### Step 8 — Produce Structured Test Data Model

Organize datasets with stable IDs, traceability, setup requirements, values/partitions, expected state, and safety notes.

---

## Output

Typical Structured Test Data Model fields:

| Field | Description |
|---|---|
| Data Set ID | Stable identifier |
| Traceability | Scenario/test/rule/risk supported by the data |
| Purpose | Behavior or partition exercised |
| Preconditions / State | Required existing state |
| Data Values | Synthetic or project-supplied values |
| Partition / Boundary | Valid/invalid/boundary classification |
| Relationships | Required linked entities/records |
| Setup Requirement | Logical setup needed before execution |
| Expected Post-State | Expected data state when relevant |
| Reuse Scope | Tests that may safely reuse the dataset |
| Safety Notes | Privacy, masking, isolation, cleanup considerations |
| Assumptions | Missing constraints or unresolved data rules |

The skill may output logical data requirements instead of concrete values when authoritative constraints are insufficient.

---

## Dependencies

| Resource | Purpose |
|---|---|
| `shared/standards/` | Output and documentation conventions |
| `shared/templates/` | Test artifact structures |
| `shared/knowledge/testing-techniques/` | EP, BVA, decision/state and combinatorial reasoning |
| `shared/knowledge/qa/` | Test design and data-quality context |
| `shared/knowledge/api/` | Payload/API constraints when relevant |
| `shared/knowledge/database/` | Data types, integrity, relationships, persistence context |
| `shared/knowledge/domain/` | Business entities, rules, and domain constraints |
| `datasets/fixtures/` | Canonical fixture models when they are applicable inputs |

Fixture models define reusable structures; this skill does not automatically provision runtime fixture instances.

---

## Consumers

The output may be consumed by:

- `testcase-generator`;
- `api-test-generator`;
- `sql-validation`;
- QA execution activities;
- workflows requiring explicit test data;
- future fixture-generation or export tooling implemented in later phases.

---

## Limitations

This skill does not:

- provision accounts, databases, environments, or external systems;
- execute setup APIs or SQL;
- create real credentials or secrets;
- copy sensitive production data;
- infer unsupported business-valid values;
- own fixture architecture defined under datasets;
- guarantee data availability in a runtime environment;
- perform combinatorial explosion without prioritization;
- modify application state directly.

If required data cannot be constructed from available rules, the output must state the missing constraint or setup dependency.

---

## Validation

The output should be validated to ensure:

- every dataset supports a specific test objective or reusable coverage need;
- values obey authoritative constraints for the intended valid/invalid partition;
- boundary values are calculated only from supplied boundaries;
- linked entities and state dependencies are represented;
- invalid data is invalid for the intended reason rather than accidentally violating unrelated constraints;
- mutable/concurrent tests receive isolated data when necessary;
- synthetic data does not expose real secrets or personal information;
- expected pre/post-state is clear where state changes matter;
- unnecessary duplicate datasets are minimized;
- assumptions and missing constraints are explicit;
- project-specific data rules override generic examples.