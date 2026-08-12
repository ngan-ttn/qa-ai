# Database Fixtures

## Fixture Metadata

- Fixture ID: `FIXTURE-DATABASE-001`
- Fixture Type: `Database`
- Scope: `QA-AI Controlled Database Testing Context`
- Status: `Approved`
- Purpose: Define reusable and deterministic database fixtures for QA-AI testing, validation, evaluation, and benchmark execution.

---

## Purpose

This document defines the canonical database fixture model for QA-AI.

Database fixtures provide controlled database-related context that QA-AI capabilities may use when database structure or data state is relevant to a QA task.

They support repeatable activities such as:

- SQL validation generation
- Database test design
- Requirement analysis involving stored data
- Scenario generation
- Test-case generation
- Test-data generation
- Data-integrity validation
- Evaluation
- Benchmark execution
- Regression testing

A database fixture represents controlled evaluation or testing context.

It is not:

- A production database
- A live environment
- A migration script
- A database implementation
- A complete enterprise data model
- A generated QA artifact
- A benchmark result

---

## Fixture Role in QA-AI

The canonical relationship is:

`Requirement Dataset + Database Fixture → QA-AI Execution → Generated Artifact`

For database validation:

`Requirement + Database Fixture → SQL / Data Validation Output`

For evaluation:

`Requirement + Database Fixture → QA-AI Execution → Artifact → Evaluation`

For benchmarking:

`Same Dataset + Same Fixture Version + Compatible Evaluation Configuration → Comparable Execution`

The fixture controls database context so QA-AI does not need to invent schema, relationships, field types, or stored data.

---

## Fixture Objectives

A database fixture should provide only the database information required for the intended QA activity.

A fixture may define:

- Database entities
- Tables
- Columns
- Data types
- Keys
- Relationships
- Constraints
- Nullable behavior
- Default values
- Controlled records
- Initial data state
- Resulting data state
- Query expectations
- Referential-integrity context
- Audit-related data when explicitly defined

Database fixtures should not attempt to reproduce an entire production database unless explicitly required.

---

## Fixture Design Principles

Canonical database fixtures should be:

### Deterministic

The same fixture version represents the same schema and controlled data state.

### Minimal

Only information needed for the intended QA task should be included.

### Explicit

Relevant schema, relationships, and data states should be represented directly.

### Source-Supported

Database behavior should be based on authoritative technical or requirement information.

### Reusable

Fixtures should support repeated QA-AI executions where the same database context applies.

### Traceable

Each fixture should have a stable identifier and version.

### Safe

Fixtures must not contain real production records, credentials, secrets, or personal information.

### Platform-Neutral

The fixture should describe database context independently of the AI execution platform.

---

## Fixture Scope

Database fixtures may represent:

- One table
- A related table set
- An entity relationship
- A controlled transaction state
- Data-integrity rules
- Referential-integrity relationships
- Before-and-after database states
- Data needed for SQL validation
- Data supporting API or UI evaluation
- Audit records where explicitly defined

The fixture should remain scoped to the capability being evaluated.

---

## Canonical Fixture Structure

A reusable database fixture should contain enough information to identify:

1. Fixture metadata
2. Database context
3. Schema or entity definitions
4. Keys and relationships
5. Constraints
6. Initial records
7. Expected resulting records when applicable
8. Query-validation context
9. Related fixtures
10. Source references
11. Fixture boundaries

Sections that do not apply may be omitted.

Do not populate missing sections with invented schema or data.

---

## Fixture Identification

Each database fixture should have a stable identifier.

Recommended pattern:

`DB-FIX-<DOMAIN>-<NUMBER>`

Examples:

- `DB-FIX-AUTH-001`
- `DB-FIX-PRODUCT-001`
- `DB-FIX-ORDER-001`
- `DB-FIX-INVENTORY-001`

The identifier should remain stable while the fixture represents the same semantic database context.

---

## Fixture Versioning

A new fixture version should be created when database semantics change materially.

Examples include:

- Column added or removed
- Data type changed
- Primary key changed
- Foreign-key relationship changed
- Nullability changed
- Constraint changed
- Default behavior changed
- Controlled dataset meaning changed
- Expected state transition changed

Formatting-only documentation changes do not necessarily require a semantic version change.

Benchmark compatibility must be reviewed whenever a fixture changes materially.

---

## Database Context

A fixture may describe the minimum database context required for interpretation.

Example:

    database_context:
      domain: authentication
      database_type: relational

Only known information should be recorded.

Do not infer:

- Database vendor
- Storage engine
- Hosting environment
- Replication architecture
- Sharding strategy
- ORM technology

unless explicitly supplied by an authoritative source.

---

## Table Definition

A table fixture may define:

- Table name
- Purpose
- Columns
- Keys
- Constraints

Example:

    table:
      name: users
      purpose: Store registered user account state.

      columns:
        id:
          type: string
          nullable: false

        email:
          type: string
          nullable: false

        status:
          type: string
          nullable: false

The fixture should represent only known schema behavior.

---

## Column Definition

Relevant column attributes may include:

- Name
- Logical data type
- Nullable status
- Default value
- Allowed values
- Key role
- Description

Example:

    columns:
      failed_attempt_count:
        type: integer
        nullable: false
        default: 0

      locked_until:
        type: datetime
        nullable: true

A fixture must not invent columns merely because they would be convenient for testing.

If implementation storage is unknown, the fixture should not assume it.

---

## Logical Versus Physical Schema

Fixtures may describe either:

### Logical Schema

Represents required data concepts without asserting a physical implementation.

Example:

    logical_entity:
      name: Account

      attributes:
        failed_attempt_count:
          type: integer

        lock_state:
          type: enum

### Physical Schema

Represents actual known tables and columns.

Physical schema should only be used when authoritative database information is available.

When implementation details are unknown, prefer logical representation rather than fabricated table structures.

---

## Primary Keys

Known primary-key behavior may be represented explicitly.

Example:

    primary_key:
      columns:
        - id

Composite keys may also be represented.

Example:

    primary_key:
      columns:
        - order_id
        - product_id

Do not infer key structure without evidence.

---

## Foreign Keys

Known relationships may be represented using foreign keys.

Example:

    foreign_keys:
      - column: user_id
        references:
          table: users
          column: id

Fixtures may also describe the expected referential behavior when explicitly defined.

Example:

    on_delete: restrict

Do not invent cascade behavior.

---

## Entity Relationships

Logical relationships may be used when physical foreign-key implementation is not known.

Example:

    relationships:
      - from: Order.customer_id
        to: Customer.id
        cardinality: many-to-one

This allows QA-AI to reason about data relationships without assuming database-specific implementation details.

---

## Constraints

Database constraints may include:

- NOT NULL
- UNIQUE
- CHECK
- Foreign-key constraints
- Allowed values
- Numeric ranges

Example:

    constraints:
      - id: DB-C-001
        field: email
        type: unique

      - id: DB-C-002
        field: quantity
        type: minimum
        value: 0

Constraints must be source-supported.

Do not derive a database constraint merely from a UI validation unless the fixture source explicitly establishes that the rule exists at database level.

---

## Nullability

Nullability should be represented only when known.

Example:

    field:
      name: approved_at
      nullable: true

A UI-optional field does not automatically imply a nullable database column.

The fixture should preserve this distinction.

---

## Default Values

Default database values may be represented when explicitly known.

Example:

    default_values:
      status: active
      failed_attempt_count: 0

Do not infer database defaults from application behavior unless the technical source confirms them.

---

## Controlled Records

Fixtures may contain deterministic synthetic records.

Example:

    records:
      - id: usr_001
        email: qa.user1@example.test
        status: active

      - id: usr_002
        email: qa.user2@example.test
        status: blocked

Controlled records should use stable synthetic identifiers.

---

## Synthetic Data Requirements

Fixture records must not contain real:

- Customer names
- Email addresses
- Phone numbers
- Account numbers
- Government identifiers
- Payment data
- Production IDs
- Credentials
- Confidential values

Use synthetic values such as:

- `usr_001`
- `ord_001`
- `qa.user@example.test`
- `TEST-ACCOUNT-001`

Synthetic records should be deterministic when benchmark reproducibility matters.

---

## Initial Database State

Some QA tasks require a defined pre-action state.

Example:

    initial_state:
      users:
        - id: usr_001
          failed_attempt_count: 4
          account_state: unlocked

The initial state provides explicit context for downstream reasoning.

QA-AI should not assume additional hidden records unless required by the task.

---

## Resulting Database State

When a behavior is expected to change data and the database effect is authoritative, the fixture may define the resulting state.

Example:

    action:
      description: Fifth consecutive failed login

    resulting_state:
      users:
        - id: usr_001
          failed_attempt_count: 5
          account_state: locked

This representation should only be used when the database-visible state is actually defined.

Do not convert business behavior into assumed database persistence.

---

## Before-and-After Fixtures

A database fixture may explicitly model state transitions.

Example:

    before:
      inventory:
        product_id: prd_001
        quantity: 10

    action:
      description: Confirm outbound quantity of 2

    after:
      inventory:
        product_id: prd_001
        quantity: 8

This format is useful for:

- Data validation
- State-transition testing
- Integration testing
- Regression benchmarking

---

## Positive Data Fixtures

Positive fixtures represent valid controlled database states.

Example:

    fixture_case:
      id: DB-FIX-USER-001-P01

      records:
        users:
          - id: usr_001
            status: active

Positive fixtures may support:

- Normal queries
- Valid state transitions
- Successful integrations

---

## Negative Data Fixtures

Negative fixtures may represent defined invalid or conflicting states when such states are relevant to the evaluation.

Example:

    fixture_case:
      id: DB-FIX-ORDER-001-N01
      description: Duplicate business key condition

Negative fixture data must remain technically valid enough to represent the intended evaluation context.

If the database constraint would prevent the state from existing, the fixture should not pretend that the invalid stored state is possible unless the test explicitly targets constraint enforcement.

---

## Boundary Data Fixtures

Controlled records may represent known boundaries.

Example:

    boundary_records:
      quantity:
        minimum:
          value: 0

        maximum:
          value: 999

Boundary values should come from authoritative rules.

They may support:

- SQL validation
- Boundary Value Analysis
- Test-data generation

---

## Referential-Integrity Fixtures

Fixtures may define related records required for foreign-key or entity-relationship validation.

Example:

    customers:
      - id: cus_001

    orders:
      - id: ord_001
        customer_id: cus_001

This supports validation such as:

- Valid relationship
- Missing parent
- Duplicate association
- Relationship cardinality

Only known relationship behavior should be tested.

---

## Transaction Fixtures

A fixture may provide transaction-state context when database transaction behavior is relevant and known.

Example:

    transaction_context:
      initial_balance: 100
      transaction_amount: 30
      expected_balance: 70

Do not infer:

- Isolation level
- Lock behavior
- Rollback mechanism
- Transaction boundaries

unless supplied by technical documentation.

---

## Concurrent Data Context

Concurrency-related fixtures may represent controlled initial state.

Example:

    concurrency_context:
      shared_record:
        id: inv_001
        quantity: 10

      operations:
        - outbound: 2
        - inbound: 3

The fixture defines the controlled inputs.

Expected concurrent processing semantics must come from the requirement or authoritative technical behavior.

Fixtures must not invent concurrency rules.

---

## Audit Data Fixtures

Audit records may be represented when audit behavior is explicitly part of the source contract.

Example:

    audit_record:
      entity_id: ord_001
      action: status_changed
      actor_id: usr_admin_001

Do not automatically assume every state change creates:

- Audit history
- Created-by fields
- Updated-by fields
- Timestamps

unless defined.

---

## Timestamp Fixtures

Time-sensitive database fixtures should use deterministic values when possible.

Example:

    created_at: 2026-01-15T10:00:00Z

When the test requires relative time rather than a specific instant, semantic placeholders may be used.

Example:

    locked_until: "<15-minutes-after-lock-start>"

Avoid uncontrolled current-time dependencies in benchmark fixtures.

---

## Query Validation Context

A database fixture may describe the result a query should observe.

Example:

    validation:
      objective: Verify active users only

      expected_records:
        - usr_001
        - usr_003

This does not require the fixture to prescribe the exact SQL query.

QA-AI may generate valid implementation-specific SQL based on the available database contract.

---

## SQL Fixture Usage

Database fixtures may support SQL generation by providing:

- Table names
- Column names
- Relationships
- Test records
- Expected result conditions

Example context:

    query_context:
      table: orders

      fields:
        - id
        - status

      expected_filter:
        status: pending

The fixture should not contain a pre-written SQL answer unless the fixture's purpose specifically requires one.

---

## Expected Query Results

Expected results should be deterministic.

Example:

    expected_result:
      row_count: 2

      records:
        - ord_001
        - ord_002

Expected result data should remain compatible with the fixture's controlled records.

---

## Data Integrity Validation

Fixtures may support validation of:

- Uniqueness
- Referential integrity
- Required data
- Allowed values
- Quantity calculations
- Status consistency
- Cross-table consistency

Example:

    integrity_rule:
      description: Every order must reference an existing customer.

The rule must be supported by authoritative database or domain information.

---

## Fixture Relationships

Database fixtures may reference:

`Database Fixture → Domain Fixture`

`Database Fixture → API Fixture`

`Database Fixture → UI Fixture`

Example:

    related_fixtures:
      - DOMAIN-FIX-ORDER-001
      - API-FIX-ORDER-001

Related fixtures should be referenced rather than unnecessarily duplicated.

---

## Fixture and Requirement Relationship

Database fixtures provide technical or data context.

The requirement remains the primary source of business behavior unless another authoritative source is explicitly identified.

If a database fixture conflicts with the requirement:

1. Identify the conflict.
2. Do not silently override either source.
3. Determine which source is authoritative for the conflicting behavior.
4. Flag the fixture or requirement for review as needed.

A fixture must not silently introduce new business rules.

---

## Fixture and API Relationship

An API fixture may describe external API behavior while a database fixture describes stored state.

Example:

`API Request → Defined Behavior → Database Validation`

The database fixture must not assume that every API field maps directly to a database column.

Mapping should only be included when known.

---

## Fixture and UI Relationship

A UI fixture may define displayed values while a database fixture defines stored values.

These may differ legitimately.

Examples:

- Display label versus stored code
- Formatted date versus timestamp
- Computed UI value versus persisted field

Do not assume one-to-one mapping without source evidence.

---

## Fixture and Golden Output Relationship

Database fixtures provide controlled supporting context.

Golden outputs remain reviewed QA reference artifacts.

A database fixture should not encode expected test cases, scenarios, or evaluation ratings.

---

## Fixture and Benchmark Relationship

Database fixtures improve benchmark repeatability by controlling schema and data state.

Example:

`Dataset v1 + Database Fixture v1 + Evaluation Model v1`

may be reused across:

- Baseline benchmark
- Cross-platform benchmark
- Regression benchmark

If a database fixture changes materially, benchmark compatibility must be reviewed.

---

## Fixture Immutability During Benchmark Execution

The fixture version selected for a benchmark execution should remain unchanged for that execution.

If a material fixture defect is discovered:

1. Identify affected benchmark results.
2. Invalidate them when necessary.
3. Correct and version the fixture.
4. Repeat affected evaluation runs.

This protects benchmark integrity.

---

## Fixture Storage

Database fixtures belong under:

`datasets/fixtures/database/`

The fixture model may be documented in Markdown.

Machine-readable fixture instances may later use formats such as:

- SQL seed data
- CSV
- JSON
- YAML

A format should only be introduced when a real consumer exists.

Production database dumps must not be stored as fixtures.

---

## Recommended Fixture Record

A canonical database fixture record may contain:

| Field | Description |
|---|---|
| Fixture ID | Stable fixture identifier |
| Version | Fixture version |
| Domain | Related business or technical domain |
| Purpose | Fixture purpose |
| Database Context | Logical database context |
| Entities / Tables | Relevant schema |
| Columns | Relevant fields and types |
| Primary Keys | Known key definitions |
| Foreign Keys | Known relationships |
| Constraints | Known data constraints |
| Initial State | Controlled starting records |
| Resulting State | Expected data state when applicable |
| Expected Results | Query or validation expectations |
| Related Fixtures | Referenced fixture identifiers |
| Source References | Authoritative technical or requirement sources |
| Status | Fixture lifecycle state |

Unused fields should not be populated with invented values.

---

## Example Canonical Fixture

The following serialized representation is illustrative only.

Its schema, records, relationships, and values demonstrate the fixture structure and are not derived from any QA-AI requirement dataset.

    fixture_id: DB-FIX-EXAMPLE-001
    version: 1.0.0
    domain: example
    status: Example

    schema_level: physical-example

    tables:
      example_parent:
        primary_key:
          - id

        columns:
          id:
            type: string
            nullable: false

          name:
            type: string
            nullable: false

      example_child:
        primary_key:
          - id

        columns:
          id:
            type: string
            nullable: false

          parent_id:
            type: string
            nullable: false

          status:
            type: string
            nullable: false

        foreign_keys:
          - column: parent_id
            references:
              table: example_parent
              column: id

    records:
      example_parent:
        - id: parent_001
          name: Example Parent

      example_child:
        - id: child_001
          parent_id: parent_001
          status: active

    source_reference:
      type: illustrative-example
      authoritative: false

The example demonstrates the canonical database fixture structure only.

Its table names, columns, keys, relationships, constraints, and records are synthetic and must not be treated as authoritative database behavior.

A real database fixture instance must replace illustrative values with schema and data supported by authoritative technical sources.

A requirement dataset must not be cited as the source of a physical database schema unless that dataset explicitly defines the implementation details being represented.
## Fixture Lifecycle

The recommended lifecycle is:

`Draft → Review → Validate → Approve → Use → Maintain`

### Draft

Build the fixture from authoritative schema, data, or requirement information.

### Review

Verify:

- Schema correctness
- Data correctness
- Scope
- Safety
- Traceability

### Validate

Confirm that controlled records and relationships support the intended QA activity.

### Approve

Accept the fixture as reusable evaluation context.

### Use

Reference the fixture from QA-AI execution or evaluation.

### Maintain

Version the fixture when database semantics change materially.

---

## Fixture Validation

Before approval, verify:

- Fixture ID is unique.
- Version is defined.
- Purpose is clear.
- Logical or physical schema level is explicit.
- Tables or entities are source-supported.
- Columns are source-supported.
- Key relationships are correct.
- Constraints are source-supported.
- Controlled records are internally consistent.
- Expected results match controlled data.
- State assumptions are explicit.
- Synthetic data is safe.
- No production records are present.
- No credentials or secrets are included.
- Related fixture references are valid.
- Fixture is deterministic enough for its intended evaluation.

---

## Security and Privacy

Database fixtures must not include:

- Production database dumps
- Real customer records
- Password hashes
- Authentication secrets
- API keys
- Real financial data
- Real payment information
- Personal identifiers
- Confidential enterprise data

Use synthetic and sanitized values.

Even hashed or masked production data should not be assumed safe for repository use without explicit approval.

---

## Determinism Requirements

Database fixtures used for evaluation or benchmark execution should avoid uncontrolled values such as:

- Random IDs
- Current timestamps
- Environment-specific data
- Live database sequences
- Auto-generated values with unpredictable output

Use deterministic values where possible.

Example:

`usr_001`

rather than:

`<random-uuid>`

When dynamic behavior is required, define the semantic expectation rather than relying on an uncontrolled concrete value.

---

## Fixture Quality Controls

A database fixture should be:

### Correct

Schema and controlled data reflect authoritative information.

### Complete Enough

The fixture contains enough context for the intended QA task.

### Scoped

It does not model unrelated database structures.

### Deterministic

The same fixture version produces the same evaluation context.

### Traceable

Its source and related dataset can be identified.

### Safe

No sensitive or production data is included.

### Maintainable

Material schema or data-state changes are versioned.

---

## Fixture Boundaries

Database fixtures must not:

- Replace source requirements.
- Invent physical database implementation.
- Invent database constraints.
- Assume UI validation equals database validation.
- Assume API fields map directly to database columns.
- Store production records.
- Store credentials or secrets.
- Encode generated test cases.
- Encode benchmark scores.
- Encode evaluation ratings.
- Force exact AI-generated output.
- Hide unknown schema behavior with fabricated structures.
- Depend unnecessarily on a live database.

---

## Validation Checklist

Before using a database fixture, verify:

- Fixture ID exists.
- Version exists.
- Status is appropriate.
- Purpose is clear.
- Schema level is clear.
- Entity or table definitions are correct.
- Relevant columns are correct.
- Key definitions are correct.
- Relationships are correct.
- Constraints are source-supported.
- Controlled records are synthetic.
- Initial state is explicit.
- Expected resulting state is supported when defined.
- Expected query results match fixture records.
- No sensitive data exists.
- Related fixture references are valid.
- Fixture version is compatible with the dataset.
- Benchmark comparability remains valid.

---

## Final Database Fixture Definition

A QA-AI database fixture is:

> A controlled, versioned, deterministic, source-supported representation of database schema and data context used to make QA-AI database reasoning, validation, evaluation, and benchmark execution reproducible without depending on production data or live database environments.

The canonical database fixture model provides:

- Controlled schema context
- Logical and physical schema separation
- Deterministic synthetic records
- Key and relationship definitions
- Data constraints
- Before-and-after states
- Query-validation context
- Data-integrity support
- Safe synthetic test data
- Requirement and fixture traceability
- Fixture versioning
- Benchmark reproducibility
- Cross-platform consistency
- Regression compatibility

It enables QA-AI to reason about database behavior consistently while preventing production-data dependence and unsupported schema assumptions from contaminating generated QA artifacts.
