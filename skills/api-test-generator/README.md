# API Test Generator

## Purpose

The `api-test-generator` skill transforms authoritative API requirements and interface context into structured API-specific test coverage.

It specializes QA test design for APIs while preserving the ownership of generic scenario and testcase generation in the existing generic skills.

---

## Capability

```text
API Requirement / Contract / Context
        ↓
Identify API Surface
        ↓
Model Request and Response Rules
        ↓
Identify Protocol and State Risks
        ↓
Derive API Test Coverage
        ↓
Add Security / Reliability / Data Checks
        ↓
Structured API Test Model
```

The capability may produce API scenarios, checks, or detailed test definitions according to the requested output contract, but it must remain API-specific rather than becoming a second generic testcase generator.

---

## When To Use

Use this skill when:

- REST/HTTP or another supported API surface requires dedicated testing;
- endpoint behavior, request/response contracts, status codes, authentication, or authorization need validation;
- API negative and boundary coverage is required;
- integration behavior must be validated below or independently from UI flows;
- idempotency, retries, pagination, filtering, concurrency, or error contracts are relevant;
- generic test artifacts need API-specific expansion.

---

## Input

### Required Input

At least one authoritative API source, such as:

- API specification or contract;
- endpoint requirement;
- OpenAPI-derived description supplied as project input;
- structured requirement containing sufficient API behavior.

### Optional Input

- Structured Requirement Analysis;
- Structured Business Rule Model;
- Structured Risk Analysis;
- generic Test Scenario/Test Case models;
- authentication/authorization rules;
- sample requests and responses;
- error-code definitions;
- API versioning rules;
- integration/dependency context;
- database or persistence expectations;
- performance/security requirements.

Observed examples must not be treated as canonical rules when an authoritative contract contradicts them.

---

## Processing

### Step 1 — Establish API Scope

Identify API style, endpoints/operations, actors/clients, environments, versions, dependencies, and authoritative sources.

### Step 2 — Model the Contract

For each operation, identify supported information including:

- method/operation;
- path/resource;
- path/query/header/body inputs;
- required and optional fields;
- data types and formats;
- validation rules;
- authentication and authorization;
- response schema;
- status/error behavior;
- business rules;
- state/persistence effects.

Do not invent undocumented status codes, schemas, limits, or authentication behavior.

### Step 3 — Derive Positive Coverage

Cover valid requests, expected responses, supported state changes, role/permission behavior, and important business outcomes.

### Step 4 — Derive Negative and Boundary Coverage

Consider missing/invalid inputs, type/format violations, unsupported values, boundary values, invalid state, unauthorized/forbidden access, malformed payloads, conflicts, and dependency failures when applicable.

### Step 5 — Derive Protocol and Reliability Coverage

When supported by the API context, consider:

- idempotency and duplicate submission;
- retries/timeouts;
- pagination/filtering/sorting;
- caching/conditional requests;
- concurrency and race conditions;
- partial failure;
- asynchronous processing;
- version compatibility;
- rate limiting;
- correlation/traceability.

Only include behaviors relevant to the supplied contract or justified risk context.

### Step 6 — Add Security and Data Validation

Identify API-specific validation for authentication, authorization, exposure of sensitive data, input handling, response leakage, persistence side effects, and auditability where applicable.

This is QA coverage, not a substitute for specialist penetration testing.

### Step 7 — Define Assertions and Evidence

Specify verifiable checks such as status/result, response body/schema, headers, side effects, database state, events/messages, audit records, or absence of unauthorized changes when supported by context.

### Step 8 — Produce Structured API Test Model

Organize tests with traceability, priority/risk context, preconditions, request data, execution, and expected API-specific assertions.

---

## Output

The Structured API Test Model may contain:

| Field | Description |
|---|---|
| API Test ID | Stable identifier |
| Requirement / Risk Trace | Upstream traceability |
| Operation | Method + endpoint or equivalent operation |
| Objective | Single primary API behavior under test |
| Preconditions | Required state/authentication/dependencies |
| Request | Inputs, headers, body, parameters |
| Execution | API action(s) |
| Assertions | Response and side-effect expectations |
| Test Data | Required values/partitions |
| Priority | Supported QA priority |
| Notes / Assumptions | Explicit uncertainty or context |

The exact representation should follow shared output standards and the requested artifact level.

---

## Dependencies

| Resource | Purpose |
|---|---|
| `shared/standards/` | Output and documentation conventions |
| `shared/templates/` | Reusable QA artifact structures |
| `shared/checklists/` | Quality validation where applicable |
| `shared/knowledge/api/` | API protocol, contract, security, reliability, and testing knowledge |
| `shared/knowledge/testing-techniques/` | EP, BVA, decision, state, risk, and other design techniques |
| `shared/knowledge/qa/` | Generic QA principles and lifecycle context |
| `shared/knowledge/database/` | Persistence validation when API behavior affects data |
| `shared/knowledge/domain/` | Business semantics when required |

---

## Consumers

The output may be consumed by:

- API-focused QA execution;
- `coverage-reviewer` when reviewing API coverage;
- `test-data-generator` for API data needs;
- `sql-validation` when persistence assertions are required;
- workflows that generate or review technical test coverage;
- future platform adapters and deterministic exporters.

---

## Limitations

This skill does not:

- redefine generic scenario/testcase generation;
- invent undocumented API contracts;
- implement or modify APIs;
- execute HTTP requests;
- perform penetration testing;
- guarantee production performance from design-time information;
- assume database implementation details from an API contract;
- generate unsupported credentials, secrets, tokens, or sensitive test data;
- infer legal/security requirements that are absent from authoritative inputs.

---

## Validation

The output should be validated to ensure:

- every test maps to a supported API behavior, risk, or explicit assumption;
- endpoint/method/operation references are correct;
- positive, negative, boundary, authorization, state, and failure coverage are considered where applicable;
- expected status/error behavior is not invented;
- assertions are observable and measurable;
- side-effect validation is included only when supported;
- API-specific tests do not duplicate generic tests without adding technical value;
- security-sensitive data is not fabricated or exposed;
- traceability and test-data needs are explicit;
- project contract information overrides generic API knowledge.