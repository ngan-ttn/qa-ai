# API Fixtures

## Fixture Metadata

- Fixture ID: `FIXTURE-API-001`
- Fixture Type: `API`
- Scope: `QA-AI Controlled API Testing Context`
- Status: `Approved`
- Purpose: Define reusable and deterministic API fixtures for QA-AI testing, evaluation, examples, and benchmark execution.

---

## Purpose

This document defines the canonical API fixture model for QA-AI.

API fixtures provide controlled API-related inputs that QA-AI capabilities can use without depending on live external services.

They are intended to support repeatable QA activities such as:

- API test generation
- Requirement analysis involving API behavior
- Business-rule extraction
- Scenario generation
- Test-case generation
- Test-data generation
- Evaluation
- Benchmark execution
- Regression testing

An API fixture represents controlled test context.

It is not:

- A live API
- Production data
- An API implementation
- A complete OpenAPI specification
- A generated QA artifact
- A benchmark result

---

## Fixture Role in QA-AI

The canonical relationship is:

`Requirement Dataset + API Fixture → QA-AI Execution → Generated Artifact`

For evaluation:

`Requirement Dataset + API Fixture → QA-AI Execution → Artifact → Evaluation`

For regression benchmarking:

`Same Dataset + Same Fixture + Compatible Configuration → Comparable Execution`

Fixtures therefore help control environmental information that could otherwise make QA-AI outputs inconsistent or non-reproducible.

---

## Fixture Objectives

API fixtures should provide enough controlled information for QA-AI to reason about API behavior without inventing unsupported technical details.

A fixture may define:

- Endpoint
- HTTP method
- Request structure
- Response structure
- Headers
- Authentication context
- Query parameters
- Path parameters
- Validation rules
- Status codes
- Error responses
- Example request data
- Example response data
- Relevant API state

Only information required by the intended dataset or evaluation should be included.

---

## Fixture Design Principles

Canonical API fixtures should be:

### Deterministic

The same fixture should represent the same API behavior across executions.

### Minimal

Include only information needed for the intended QA task.

### Explicit

Important API behavior should be directly represented rather than implied.

### Reusable

A fixture should support multiple QA-AI executions where the same API context applies.

### Traceable

The fixture should have a stable identifier and version.

### Safe

Fixtures must not contain real secrets, credentials, tokens, or sensitive production data.

### Platform-Neutral

The fixture should describe API behavior independently of the AI execution platform.

---

## Fixture Scope

API fixtures may represent:

- One endpoint
- A related endpoint group
- Authentication behavior
- Validation behavior
- Error handling
- Pagination
- Filtering
- Sorting
- State-dependent API behavior
- Integration behavior relevant to the QA task

Fixtures should not attempt to model an entire production API unless that scope is explicitly required.

---

## Canonical Fixture Structure

A reusable API fixture should contain enough information to identify:

1. Fixture metadata
2. API context
3. Endpoint definition
4. Request contract
5. Response contract
6. Validation behavior
7. Error behavior
8. State assumptions
9. Example data
10. Fixture boundaries

Not every fixture requires every section.

Sections that do not apply may be omitted rather than populated with invented values.

---

## Fixture Identification

Each fixture should have a stable identifier.

Recommended pattern:

`API-FIX-<DOMAIN>-<NUMBER>`

Examples:

- `API-FIX-AUTH-001`
- `API-FIX-PRODUCT-001`
- `API-FIX-ORDER-001`

The identifier should remain stable while the semantic meaning of the fixture remains unchanged.

---

## Fixture Versioning

Fixtures should be versioned when API behavior changes materially.

Examples include:

- Endpoint contract changes
- Required parameter changes
- Validation-rule changes
- Response-schema changes
- Status-code changes
- Authentication changes
- State-transition changes

Formatting-only changes do not necessarily require a new fixture version.

Example:

`1.0.0 → 1.1.0`

for a backward-compatible fixture extension.

A breaking semantic change may require:

`1.x → 2.0.0`

Versioning policy should remain consistent with the repository's canonical versioning standards.

---

## API Context

The fixture should describe the API context required for interpretation.

Example:

    api_context:
      domain: authentication
      protocol: HTTPS
      style: REST
      content_type: application/json

Only known context should be recorded.

Do not infer implementation technology such as:

- Programming language
- Framework
- Database
- Hosting platform

unless explicitly defined by the source material.

---

## Endpoint Definition

An endpoint fixture may define:

- Method
- Path
- Purpose
- Authentication requirement

Example:

    endpoint:
      method: POST
      path: /api/v1/login
      purpose: Authenticate a user using email and password.
      authentication_required: false

The fixture should use a logical endpoint contract.

A real production host is normally unnecessary.

---

## Path Parameters

When an endpoint contains path parameters, define them explicitly.

Example:

    path_parameters:
      - name: userId
        type: string
        required: true
        description: Identifier of the requested user.

Example endpoint:

`GET /api/v1/users/{userId}`

Fixtures should identify applicable validation when known.

---

## Query Parameters

Query parameters should define:

- Name
- Type
- Required status
- Allowed values or constraints when known
- Purpose

Example:

    query_parameters:
      - name: page
        type: integer
        required: false
        minimum: 1
        default: 1

      - name: status
        type: string
        required: false
        allowed_values:
          - active
          - inactive

Do not invent defaults or allowed values when the source does not define them.

---

## Request Headers

Relevant request headers may be represented when they affect QA behavior.

Example:

    request_headers:
      Content-Type:
        required: true
        value: application/json

      Authorization:
        required: true
        format: Bearer <token>

Real authorization tokens must never be stored in fixtures.

Use placeholders only.

---

## Request Body

Request bodies should describe the input contract.

Example:

    request_body:
      type: object
      required_fields:
        - email
        - password

      fields:
        email:
          type: string
          format: email

        password:
          type: string
          min_length: 8

Fixtures should distinguish between:

- Required fields
- Optional fields
- Data types
- Known constraints

Do not create undocumented validation rules.

---

## Successful Response

Successful response behavior should identify:

- HTTP status
- Response structure
- Relevant headers when applicable
- Example response

Example:

    success_response:
      status: 200

      body:
        user_id: usr_001
        access_token: "<token>"
        expires_in: 3600

Sensitive-looking values must use clearly synthetic placeholders.

---

## Error Responses

Known error behavior should be explicitly represented.

Example:

    error_responses:
      - condition: Invalid credentials
        status: 401
        body:
          code: INVALID_CREDENTIALS
          message: Invalid email or password.

      - condition: Missing required email
        status: 400
        body:
          code: VALIDATION_ERROR
          field: email

Error responses should reflect source-defined behavior.

A fixture must not invent error codes merely to make the fixture appear complete.

---

## Validation Rules

Validation rules may be represented independently when they apply across multiple examples.

Example:

    validation_rules:
      - id: VR-001
        field: email
        rule: Required

      - id: VR-002
        field: email
        rule: Must use a valid email format

      - id: VR-003
        field: password
        rule: Minimum length is 8 characters

Validation rules must remain traceable to authoritative requirement or API information when used for evaluation.

---

## Authentication Fixtures

Authentication-related fixtures may describe:

- No authentication
- Bearer token
- API key
- Session cookie
- OAuth-related test context
- Role-specific authorization

Example:

    authentication:
      type: bearer
      token: "<valid-test-token>"

      roles:
        - user

The fixture must never contain:

- Production tokens
- Private keys
- Real passwords
- Secret API keys

---

## Authorization Context

When API behavior differs by role or permission, the fixture should represent the applicable authorization context.

Example:

    authorization_context:
      role: admin
      permissions:
        - user.read
        - user.update

Alternative fixture:

    authorization_context:
      role: viewer
      permissions:
        - user.read

This allows QA-AI to generate role-aware API scenarios without inventing permission behavior.

---

## Stateful API Fixtures

Some APIs behave differently depending on existing state.

Examples include:

- Resource exists
- Resource does not exist
- Account is blocked
- Order is canceled
- Token is expired
- Inventory is unavailable

State should be explicit.

Example:

    initial_state:
      user:
        id: usr_001
        status: active

      session:
        authenticated: true

QA-AI should reason from this state rather than assume hidden system conditions.

---

## State Transition Fixtures

When the API changes state, the expected transition may be represented.

Example:

    initial_state:
      order_status: pending

    action:
      method: POST
      path: /api/v1/orders/ord_001/cancel

    resulting_state:
      order_status: canceled

This is useful for:

- State-transition testing
- Workflow testing
- Regression benchmarking

Only defined transitions should be included.

---

## Pagination Fixtures

Pagination behavior may be represented when required.

Example:

    pagination:
      type: page-based
      default_page: 1
      page_size: 20
      maximum_page_size: 100

If pagination behavior is not defined by the source, do not introduce arbitrary limits.

---

## Filtering and Sorting Fixtures

Filtering and sorting behavior may be represented when relevant.

Example:

    filters:
      status:
        allowed_values:
          - active
          - inactive

    sorting:
      supported_fields:
        - created_at
        - name

      directions:
        - asc
        - desc

These rules should reflect known API behavior.

---

## Boundary Data

API fixtures may include controlled boundary values.

Example:

    boundary_data:
      username:
        minimum_length: 3
        maximum_length: 50

      quantity:
        minimum: 1
        maximum: 999

Boundary values are particularly useful for:

- Boundary Value Analysis
- Negative testing
- Test-data generation

Only authoritative boundaries should be recorded.

---

## Equivalence Data

Fixtures may define representative equivalence classes.

Example:

    equivalence_classes:
      quantity:
        valid:
          - 1
          - 50
          - 999

        invalid:
          - 0
          - -1
          - 1000

Such values should be derived from known validation rules.

---

## Example Request

Example requests should use deterministic synthetic data.

Example:

    example_request:
      method: POST
      path: /api/v1/login

      body:
        email: qa.user@example.test
        password: TestPass123

The `.test` domain is preferred for synthetic email addresses.

Examples should not resemble real customer credentials.

---

## Example Response

Example responses should also use deterministic synthetic data.

Example:

    example_response:
      status: 200

      body:
        user_id: usr_001
        access_token: "<token>"
        expires_in: 3600

Identifiers should be stable when repeatability matters.

---

## Positive Fixtures

A positive fixture represents a valid request or valid API state.

Example:

    fixture_case:
      id: API-FIX-AUTH-001-P01
      description: Valid login request

      request:
        email: qa.user@example.test
        password: TestPass123

      expected_status: 200

Positive fixtures help verify:

- Happy paths
- Valid equivalence partitions
- Successful state transitions

---

## Negative Fixtures

A negative fixture represents controlled invalid input or invalid state.

Example:

    fixture_case:
      id: API-FIX-AUTH-001-N01
      description: Login with invalid password

      request:
        email: qa.user@example.test
        password: WrongPassword

      expected_status: 401

Negative fixtures should represent defined failure behavior.

They must not create unsupported expectations.

---

## Edge Fixtures

Edge fixtures represent known boundaries or special conditions.

Examples include:

- Minimum value
- Maximum value
- Empty collection
- Expired token
- Duplicate resource
- Already-completed state

Example:

    fixture_case:
      id: API-FIX-TOKEN-001-E01
      description: Expired authentication token

      authentication:
        token: "<expired-test-token>"

      expected_status: 401

---

## Fixture Relationships

An API fixture may reference related controlled data.

Examples:

`API Fixture → Domain Fixture`

`API Fixture → Database Fixture`

Such relationships should only be introduced when required by the QA task.

Example:

    related_fixtures:
      - DOMAIN-FIX-USER-001
      - DB-FIX-USER-001

A fixture should not duplicate large amounts of data already owned by another canonical fixture.

---

## Fixture and Requirement Relationship

Fixtures support requirements.

They do not override them.

When fixture information conflicts with an authoritative requirement:

1. Identify the conflict.
2. Do not silently choose the fixture.
3. Treat the requirement as the authoritative business source unless the repository explicitly defines otherwise.
4. Flag the fixture for review.

A fixture must not become an accidental source of new business behavior.

---

## Fixture and Golden Output Relationship

Golden outputs represent reviewed QA interpretations.

API fixtures provide controlled technical context.

Conceptually:

`Requirement + Fixture → QA-AI Execution`

and:

`Golden Output → Evaluation Reference`

A fixture should not encode a golden answer merely to force generated artifacts toward exact expected wording.

---

## Fixture and Benchmark Relationship

Fixtures improve benchmark reproducibility by controlling API context.

Example:

`Dataset v1 + API Fixture v1 + Evaluation Configuration v1`

can be reused for:

- Baseline execution
- Cross-platform execution
- Regression execution

If a fixture changes materially, benchmark compatibility must be reviewed.

A changed fixture may invalidate direct comparison with previous results.

---

## Fixture Immutability During Benchmark Execution

Once a benchmark run begins, the selected fixture version should remain unchanged for that run.

Do not modify fixture semantics during execution.

If a fixture defect is discovered:

1. Stop or invalidate affected benchmark results when necessary.
2. Correct and version the fixture.
3. Re-run affected evaluations.

This protects benchmark reproducibility.

---

## Fixture Storage

API fixtures should live under:

`datasets/fixtures/api/`

The fixture model may be documented in Markdown.

Executable fixture instances may later use structured formats such as:

- JSON
- YAML

when machine-readable execution becomes necessary.

The repository should not introduce additional fixture formats without a clear consumer.

---

## Recommended Fixture Record

A canonical API fixture record may contain:

| Field | Description |
|---|---|
| Fixture ID | Stable fixture identifier |
| Version | Fixture version |
| Domain | API business or technical domain |
| Purpose | Fixture purpose |
| Endpoint | API endpoint |
| Method | HTTP method |
| Authentication | Authentication context |
| Authorization | Role or permission context |
| Path Parameters | Controlled path parameters |
| Query Parameters | Controlled query parameters |
| Headers | Relevant request headers |
| Request Contract | Input structure |
| Response Contract | Output structure |
| Validation Rules | Known validation behavior |
| Error Responses | Known error behavior |
| Initial State | Required starting state |
| Resulting State | Expected state when applicable |
| Example Data | Synthetic deterministic examples |
| Related Fixtures | Referenced fixture IDs |
| Source Reference | Authoritative source when applicable |
| Status | Fixture lifecycle state |

Not every field is mandatory for every fixture.

Unused fields should not be populated with fabricated values.

---

## Example Canonical Fixture

The following serialized representation is illustrative only.

Its values demonstrate the fixture structure and are not derived from any QA-AI requirement dataset.

    fixture_id: API-FIX-EXAMPLE-001
    version: 1.0.0
    domain: example
    status: Example

    endpoint:
      method: POST
      path: /api/example/resources

    authentication:
      required: true
      type: bearer
      token: "<valid-test-token>"

    request:
      content_type: application/json

      fields:
        resource_name:
          type: string
          required: true

    responses:
      success:
        status: 200

        body:
          resource_id: res_001
          resource_name: Example Resource

      invalid_request:
        status: 400

        body:
          code: EXAMPLE_VALIDATION_ERROR

    example_data:
      resource_name: Example Resource

    source_reference:
      type: illustrative-example
      authoritative: false

The example demonstrates the canonical fixture structure only.

Its endpoint, fields, response codes, validation behavior, and example values are synthetic and must not be treated as authoritative API behavior.

A real fixture instance must replace illustrative values with information supported by its authoritative source.

An illustrative example must not reference a requirement dataset as its source unless the represented API behavior is actually defined by that dataset.
## Fixture Lifecycle

The recommended fixture lifecycle is:

`Draft → Review → Validate → Approve → Use → Maintain`

### Draft

Create the fixture from authoritative source information.

### Review

Check:

- Correctness
- Completeness
- Scope
- Safety
- Traceability

### Validate

Confirm that the fixture can support its intended QA task.

### Approve

Accept the fixture as controlled reusable test context.

### Use

Reference the approved fixture from datasets, examples, evaluation, or benchmark execution.

### Maintain

Version the fixture when its semantics change.

---

## Fixture Validation

Before approval, verify that:

- Fixture purpose is clear.
- Fixture ID is unique.
- Version is defined.
- API behavior is source-supported.
- Required request information is present.
- Expected response behavior is present when applicable.
- Validation rules are not invented.
- Error behavior is not invented.
- State assumptions are explicit.
- Synthetic data is safe.
- No real credentials are present.
- Related fixture references are valid.
- Benchmark-sensitive behavior is deterministic.

---

## Security and Privacy

Fixtures must use synthetic test data.

Do not store:

- Real access tokens
- Real refresh tokens
- API secrets
- Private keys
- Production passwords
- Customer PII
- Confidential production payloads

Use placeholders such as:

- `<token>`
- `<api-key>`
- `<session-id>`
- `qa.user@example.test`

Synthetic identifiers should be preferred over real identifiers.

---

## Determinism Requirements

Benchmark fixtures should minimize unnecessary variability.

Avoid values such as:

- Current timestamp
- Random UUID
- Dynamic token
- Live service response
- Environment-dependent host

unless the behavior under test specifically requires them.

When dynamic values are necessary, define their semantics rather than depending on an uncontrolled runtime value.

Example:

    created_at: "<valid-current-timestamp>"

rather than embedding a timestamp that becomes stale.

---

## Fixture Quality Controls

An API fixture should be:

### Correct

It reflects authoritative API behavior.

### Complete Enough

It contains the information needed for its intended QA task.

### Scoped

It does not model unrelated API behavior.

### Deterministic

It supports repeatable execution.

### Traceable

Its origin and intended use can be identified.

### Safe

It contains no production secrets or sensitive data.

### Maintainable

Material behavior changes can be versioned without silently changing benchmark meaning.

---

## Fixture Boundaries

API fixtures must not:

- Define unsupported business rules.
- Replace source requirements.
- Replace golden outputs.
- Replace API specifications when an authoritative specification exists.
- Contain real secrets.
- Depend unnecessarily on live services.
- Encode platform-specific AI behavior.
- Encode benchmark scores.
- Encode expected evaluation ratings.
- Force exact generated output.
- Hide unknown API behavior by inventing values.
- Duplicate unrelated fixture domains.

---

## Validation Checklist

Before using an API fixture, verify:

- Fixture ID is defined.
- Fixture version is defined.
- Fixture status is appropriate.
- Purpose is clear.
- Endpoint information is correct.
- HTTP method is correct.
- Authentication context is explicit when applicable.
- Authorization context is explicit when applicable.
- Request contract is supported by source information.
- Response contract is supported by source information.
- Validation rules are supported.
- Error behavior is supported.
- Required state is explicit.
- Example data is synthetic.
- No secret or production data is present.
- Related fixture references are valid.
- Fixture version is compatible with the target dataset.
- Benchmark comparison remains valid when the fixture is used.

---

## Final API Fixture Definition

A QA-AI API fixture is:

> A controlled, versioned, deterministic, source-supported representation of API context used to make QA-AI generation, evaluation, and benchmark execution reproducible without depending on live external services.

The canonical API fixture model provides:

- Controlled API context
- Deterministic test inputs
- Request and response contracts
- Validation and error behavior
- Authentication and authorization context
- Explicit API state
- Safe synthetic data
- Requirement traceability
- Fixture versioning
- Benchmark reproducibility
- Cross-platform consistency
- Regression compatibility

It enables QA-AI to reason about API behavior consistently while preventing live-environment variability and unsupported technical assumptions from contaminating generated QA artifacts.
