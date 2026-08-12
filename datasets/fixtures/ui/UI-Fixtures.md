# UI Fixtures

## Fixture Metadata

- Fixture Model ID: `FIXTURE-MODEL-UI-001`
- Fixture Type: `UI`
- Scope: `QA-AI Controlled UI Testing Context`
- Status: `Approved`
- Purpose: Define reusable and deterministic UI fixtures for QA-AI testing, evaluation, examples, and benchmark execution.

---

## Purpose

This document defines the canonical UI fixture model for QA-AI.

UI fixtures provide controlled user-interface context that QA-AI capabilities may use when screen structure, field behavior, component state, navigation, validation, or role-specific presentation is relevant to a QA task.

They support repeatable activities such as:

- Requirement analysis involving UI behavior
- UI test-scenario generation
- Test-case generation
- Validation testing
- Role-based UI testing
- State-transition testing
- Responsive-context testing
- Evaluation
- Benchmark execution
- Regression testing

A UI fixture represents controlled UI context.

It is not:

- A production UI
- A complete design system
- A screenshot baseline
- A visual-regression engine
- A frontend implementation
- A generated QA artifact
- A benchmark result

---

## Fixture Role in QA-AI

The canonical relationship is:

`Requirement Dataset + UI Fixture → QA-AI Execution → Generated Artifact`

For UI-oriented testing:

`Requirement + UI Fixture → UI Scenarios / Test Cases`

For evaluation:

`Requirement + UI Fixture → QA-AI Execution → Artifact → Evaluation`

For benchmarking:

`Same Dataset + Same UI Fixture Version + Compatible Evaluation Configuration → Comparable Execution`

UI fixtures control interface context so QA-AI does not need to invent:

- Screen structure
- Field availability
- Enabled or disabled states
- Component visibility
- Navigation paths
- UI validation behavior
- Role-specific controls

---

## Fixture Objectives

A UI fixture should provide only the interface information required for the intended QA task.

A fixture may define:

- Screen or page
- UI sections
- Components
- Fields
- Labels
- Control types
- Required state
- Enabled or disabled state
- Visible or hidden state
- Read-only state
- Default values
- Allowed values
- UI validation
- Navigation
- Modal or popup behavior
- Role-specific presentation
- UI state transitions
- Responsive context
- Empty, loading, error, or populated states

The fixture should not attempt to describe the entire application unless explicitly required.

---

## Fixture Design Principles

Canonical UI fixtures should be:

### Deterministic

The same fixture version should represent the same controlled UI context.

### Minimal

Only UI information needed for the intended QA task should be included.

### Explicit

Relevant components, states, fields, and interactions should be described directly.

### Source-Supported

UI behavior should be based on authoritative requirements, specifications, designs, or approved UI references.

### Reusable

Fixtures should support repeated QA-AI executions where the same UI context applies.

### Traceable

Each fixture should have a stable identifier and version.

### Platform-Neutral

The fixture should describe application UI behavior independently of the AI platform executing QA-AI.

### Implementation-Neutral

Unless implementation details are explicitly provided, the fixture should describe observable UI behavior rather than frontend code structure.

---

## Fixture Scope

UI fixtures may represent:

- A page
- A screen
- A modal
- A popup
- A form
- A table
- A dashboard
- A navigation flow
- A role-specific screen state
- A responsive viewport context
- A component state
- A validation state
- An empty state
- A loading state
- An error state

A fixture should remain scoped to the UI behavior needed by the associated dataset or evaluation.

---

## Canonical Fixture Structure

A reusable UI fixture should contain enough information to identify:

1. Fixture metadata
2. UI context
3. Screen or page
4. Components
5. Field definitions
6. Component states
7. Validation behavior
8. Navigation behavior
9. Role context
10. UI states
11. Responsive context when applicable
12. Related fixtures
13. Source references
14. Fixture boundaries

Sections that do not apply may be omitted.

Missing UI behavior must not be filled with invented values.

---

## Fixture Identification

Each UI fixture should have a stable identifier.
### Fixture Model ID vs Fixture ID

The fixture model and fixture instances use separate identifier namespaces.

- `Fixture Model ID` identifies this canonical fixture specification.
- `Fixture ID` identifies a concrete UI fixture instance created from the model.

The canonical UI fixture model uses:

`FIXTURE-MODEL-UI-001`

Concrete UI fixture instances use the pattern defined below.

These identifiers must not be treated as interchangeable.
Recommended pattern:

`UI-FIX-<DOMAIN>-<NUMBER>`

Examples:

- `UI-FIX-AUTH-001`
- `UI-FIX-PRODUCT-001`
- `UI-FIX-ORDER-001`
- `UI-FIX-INVENTORY-001`

The identifier should remain stable while the semantic UI context remains unchanged.

---

## Fixture Versioning

A UI fixture should be versioned when interface behavior changes materially.

Examples include:

- Field added or removed
- Required state changed
- Control type changed
- Enabled or disabled rule changed
- Visibility rule changed
- Validation behavior changed
- Navigation changed
- Role-specific UI behavior changed
- State transition changed
- Responsive behavior changed materially

Formatting-only documentation changes do not necessarily require a semantic fixture version change.

Material fixture changes require benchmark compatibility review.

---

## UI Context

A fixture may define the minimum application context required for interpretation.

Example:

    ui_context:
      domain: authentication
      surface: web
      screen: login

Only known context should be included.

Do not infer:

- Frontend framework
- Component library
- CSS architecture
- JavaScript framework
- Browser engine dependency

unless explicitly defined by an authoritative technical source.

---

## Screen Definition

A screen fixture may identify:

- Screen ID
- Screen name
- Purpose
- Entry condition
- Role context

Example:

    screen:
      id: login
      name: Login
      purpose: Allow registered users to authenticate.

Do not invent page URLs unless they are known.

---

## Section Definition

A screen may contain logical sections.

Example:

    sections:
      - id: credentials
        name: Credentials

      - id: actions
        name: Actions

Sections are useful when they help QA-AI understand layout or interaction grouping.

They should not be introduced merely to reproduce implementation markup.

---

## Component Definition

UI components may include:

- Text input
- Password input
- Dropdown
- Multi-select
- Checkbox
- Radio button
- Button
- Link
- Table
- Pagination
- Tab
- Modal
- Date picker
- File upload
- Label
- Tooltip
- Notification
- Search box

Example:

    component:
      id: login_button
      type: button
      label: Login

Only behavior relevant to testing needs to be recorded.

---

## Field Definition

A field fixture may define:

- ID
- Label
- Control type
- Required status
- Editable state
- Default value
- Placeholder
- Allowed values
- Validation
- Display format

Example:

    fields:
      email:
        label: Email
        type: text
        required: true
        editable: true

      password:
        label: Password
        type: password
        required: true
        editable: true

UI fields should be represented as observable interface behavior.

---

## Field Requirement

Required-state behavior may be represented explicitly.

Example:

    field:
      id: email
      required: true

A UI required indicator should not automatically be interpreted as a database NOT NULL constraint.

Each fixture domain retains its own responsibility.

---

## Editable State

Fields may be represented as:

- Editable
- Read-only
- Disabled

These states are not interchangeable.

### Editable

The user can modify the value.

### Read-Only

The value is visible but cannot be modified through the control.

### Disabled

The control is inactive for user interaction.

Example:

    fields:
      approval_number:
        editable: false
        state: disabled

The fixture should preserve source terminology when the difference matters.

---

## Visibility State

A component may be:

- Visible
- Hidden
- Conditionally visible

Example:

    component:
      id: edit_action
      visible_when:
        remaining_quantity_less_than_approval_quantity: true

Visibility rules must be source-supported.

Do not invent hidden-state logic based solely on expected UX conventions.

---

## Enabled State

Interactive controls may have conditional enabled behavior.

Example:

    component:
      id: submit_button
      enabled_when:
        required_fields_valid: true

This condition should only be included when defined.

Avoid generic assumptions such as:

`Submit is always disabled until all fields are valid`

unless the source establishes that behavior.

---

## Default Values

Known UI defaults may be represented.

Example:

    field:
      id: count_date
      default: "<today>"
      editable: false

Dynamic defaults may use semantic placeholders.

Avoid fixture values that become stale or environment-dependent.

---

## Allowed Values

Dropdowns, radio groups, or selectors may define known choices.

Example:

    field:
      id: status
      type: dropdown

      allowed_values:
        - Active
        - Inactive

Allowed values must come from authoritative UI or domain information.

---

## Conditional UI Behavior

UI components may change based on another field or state.

Example:

    condition:
      when:
        is_approved: true

      then:
        approval_number:
          visible: true
          required: true

Conditional behavior should be represented explicitly when it affects testing.

---

## UI Validation

Fixtures may define UI-level validation behavior.

Example:

    validation_rules:
      - id: UI-VR-001
        field: email
        condition: empty
        expected_behavior: Validation is displayed.

      - id: UI-VR-002
        field: email
        condition: invalid_email_format
        expected_behavior: Invalid email validation is displayed.

Only known UI validation should be included.

---

## Validation Message Content

Exact validation text should only be included when the source defines it.

Example:

    expected_message: Email is required.

If the requirement only states that validation must occur, the fixture should not invent exact wording.

In that case:

    expected_behavior: Required-field validation is displayed.

This preserves the difference between:

- Validation behavior
- Exact presentation copy

---

## Client-Side Versus Server-Side Validation

A UI fixture should not infer where validation is technically implemented.

Observable UI behavior may be defined without assuming:

- Client-side validation
- Server-side validation
- API validation
- Database constraint

Example:

    expected_ui_behavior:
      invalid_input_is_rejected: true

This does not specify the technical validation layer.

---

## Action Controls

Action components may define:

- Label
- Visibility
- Enabled state
- Trigger
- Resulting UI state

Example:

    action:
      id: edit
      type: button
      label: Edit
      visible: true

      result:
        state: edit_mode

Action results should describe known observable behavior.

---

## Modal and Popup Fixtures

A modal fixture may define:

- Trigger
- Title
- Fields
- Read-only state
- Actions
- Close behavior

Example:

    modal:
      id: edit_permit
      trigger: edit_action

      fields:
        device_family:
          state: disabled

        new_upn:
          state: editable

      actions:
        - Update
        - Cancel

Do not invent modal dimensions, animations, or visual styling unless relevant and authoritative.

---

## Table Fixtures

A table fixture may define:

- Columns
- Row actions
- Selection behavior
- Pagination
- Sorting
- Filtering
- Empty-state behavior

Example:

    table:
      id: product_requests

      columns:
        - request_id
        - status
        - owner

      row_actions:
        - view

Table behavior should remain limited to known requirements.

---

## Row-Level State

Different rows may expose different UI actions based on state.

Example:

    row_states:
      allocated:
        selectable: false

      unallocated:
        selectable: true

This supports role- and state-aware test generation.

---

## Selection Fixtures

UI fixtures may define:

- Single selection
- Multi-selection
- Select-all behavior
- Disabled selection
- Page-scoped selection

Example:

    selection:
      type: multi

      select_all:
        scope: current_page

Selection scope must not be assumed when the source is silent.

---

## Filter Fixtures

A filter fixture may define:

- Available filters
- Control type
- Allowed values
- Combination behavior
- Reset behavior when known

Example:

    filters:
      status:
        type: multi-select
        allowed_values:
          - Open
          - Closed

Do not invent filter persistence or default values unless defined.

---

## Search Fixtures

Search behavior may define:

- Search field
- Search target
- Match behavior
- Trigger behavior

Example:

    search:
      field: product_name
      match_type: contains

Exact matching semantics should only be included when authoritative.

---

## Sorting Fixtures

Sorting fixtures may define known sortable fields and supported directions.

Example:

    sorting:
      fields:
        - created_date

      directions:
        - ascending
        - descending

Do not assume every visible column is sortable.

---

## Pagination Fixtures

Known pagination behavior may be represented.

Example:

    pagination:
      enabled: true
      page_size: 20

A page size must not be invented.

If pagination exists but exact size is unspecified:

    pagination:
      enabled: true

---

## Navigation Fixtures

Navigation fixtures may describe:

- Entry point
- Trigger
- Destination
- Role dependency
- Authentication dependency

Example:

    navigation:
      from: request_list
      trigger: open_request
      to: request_detail

Navigation should describe the observable user flow rather than implementation routing technology.

---

## Deep-Link Context

When a QA task involves deep links, a fixture may define controlled navigation state.

Example:

    deep_link:
      target: request_detail
      authentication_required: true

      unauthenticated_behavior:
        destination: login

Exact URL patterns should only be included when known.

---

## Role-Based UI Fixtures

UI behavior may vary by role.

Example:

    roles:
      requestor:
        actions:
          - view

      admin:
        actions:
          - view
          - edit
          - delete

Role behavior must be source-supported.

A fixture must not infer permissions from job titles or common application conventions.

---

## UI State Fixtures

A screen may have multiple controlled states.

Examples include:

- Default
- Empty
- Loading
- Populated
- Error
- Disabled
- Edit
- Read-only
- Locked

Example:

    state:
      name: empty

      table:
        row_count: 0

      empty_state:
        visible: true

A UI state fixture should describe only known behavior.

---

## Initial UI State

Some QA tasks require a defined initial state.

Example:

    initial_state:
      screen: permit_detail
      mode: view

      edit_action:
        visible: true

Explicit initial state prevents QA-AI from assuming hidden navigation or setup behavior.

---

## Resulting UI State

When an interaction changes the interface, the resulting state may be represented.

Example:

    action:
      trigger: edit_action

    resulting_state:
      mode: restricted_edit

      fields:
        device_family:
          state: disabled

        add_upn:
          state: editable

This supports state-transition testing.

---

## Positive UI Fixtures

Positive fixtures represent valid and supported UI states or interactions.

Example:

    fixture_case:
      id: UI-FIX-AUTH-001-P01
      description: Valid login form input

      fields:
        email: qa.user@example.test
        password: TestPass123

      login_button:
        enabled: true

Positive fixtures should reflect known interface behavior.

---

## Negative UI Fixtures

Negative fixtures may represent:

- Missing required data
- Invalid input
- Unsupported state
- Disabled action
- Hidden action
- Unauthorized role

Example:

    fixture_case:
      id: UI-FIX-AUTH-001-N01
      description: Email is empty

      fields:
        email: ""

      expected:
        email_validation:
          visible: true

Do not invent exact validation wording unless defined.

---

## Boundary UI Fixtures

Boundary fixtures may represent known limits such as:

- Minimum length
- Maximum length
- Minimum date
- Maximum date
- Maximum selected items
- Maximum upload size

Example:

    boundary:
      field: title
      maximum_length: 100

Boundary rules must come from authoritative sources.

---

## File Upload Fixtures

A file-upload fixture may define:

- Allowed file type
- Number of files
- Maximum size when known
- Required state
- Validation behavior

Example:

    upload:
      allowed_extensions:
        - .xlsx

      maximum_files: 1

Do not invent file-size limits if they are unspecified.

---

## Responsive Context

When responsive behavior is part of the evaluation, the fixture may identify a controlled viewport context.

Example:

    viewport:
      category: mobile
      width: 390
      height: 844

or:

    viewport:
      category: desktop

Exact dimensions should only be required when the evaluation depends on them.

A generic mobile or desktop context may be sufficient when exact support dimensions are not defined.

---

## Responsive Behavior

Known responsive behavior may define:

- Component relocation
- Collapsed navigation
- Horizontal scrolling
- Responsive table behavior
- Adaptive form layout

Example:

    responsive_behavior:
      navigation:
        mobile: collapsed

This must be source-supported.

Do not infer expected responsive layouts from common design practices.

---

## Visual Fixtures

UI fixtures may describe visual properties when they are authoritative and relevant.

Examples include:

- Component presence
- Label text
- Icon presence
- Alignment rule
- Required indicator
- Error styling behavior

However, this fixture model is not a pixel-diff specification.

Avoid defining:

- Exact pixel coordinates
- Colors
- Font values
- Spacing
- Dimensions

unless those properties are explicitly part of the evaluation requirement.

---

## Accessibility Context

Accessibility information may be included when authoritative requirements or fixtures define it.

Examples:

- Accessible label
- Keyboard focus behavior
- Required semantic role
- Alternative text

A UI fixture should not assume full accessibility compliance requirements unless the evaluation scope explicitly includes them.

---

## Dynamic Data

UI fixtures used for benchmarking should avoid uncontrolled dynamic content.

Prefer deterministic values such as:

    user_name: QA User
    request_id: REQ-001

For time-dependent values, semantic placeholders may be used.

Example:

    count_date: "<today>"

The meaning of the placeholder should remain stable across executions.

---

## Fixture Relationships

UI fixtures may reference:

`UI Fixture → Domain Fixture`

`UI Fixture → API Fixture`

`UI Fixture → Database Fixture`

Example:

    related_fixtures:
      - DOMAIN-FIX-PERMIT-001
      - API-FIX-PERMIT-001

Fixtures should reference related controlled context rather than duplicate entire contracts.

---

## Fixture and Requirement Relationship

UI fixtures support requirement interpretation.

They do not replace the requirement.

If a UI fixture conflicts with an authoritative requirement:

1. Identify the conflict.
2. Do not silently select one behavior.
3. Determine which source is authoritative for the disputed UI behavior.
4. Flag the inconsistent fixture or requirement for review.

A fixture must not silently introduce new product behavior.

---

## Fixture and Domain Relationship

A domain fixture may define concepts such as:

- Status values
- Roles
- Entity terminology
- Business classifications

A UI fixture may reference those concepts for display or interaction context.

The UI fixture should not duplicate domain definitions unnecessarily.

---

## Fixture and API Relationship

A UI action may trigger API behavior.

However:

`UI field ≠ automatically API field`

and:

`UI validation ≠ automatically API validation`

Mapping should only be recorded when known.

Fixtures must preserve the separation between observable UI behavior and API contract behavior.

---

## Fixture and Database Relationship

Displayed UI values may differ from stored database values.

Examples include:

- Label versus code
- Formatted date versus raw timestamp
- Calculated display value versus persisted data
- Localized value versus canonical stored value

A UI fixture must not assume one-to-one database mapping without source evidence.

---

## Fixture and Golden Output Relationship

UI fixtures provide controlled supporting context.

Golden outputs remain reviewed QA reference artifacts.

A UI fixture must not encode:

- Expected test cases
- Expected scenario list
- Evaluation scores
- Rubric ratings
- Exact AI-generated wording

---

## Fixture and Benchmark Relationship

UI fixtures improve benchmark reproducibility by controlling interface context.

Example:

`Dataset v1 + UI Fixture v1 + Evaluation Configuration v1`

may be reused for:

- Baseline benchmark
- Cross-platform benchmark
- Regression benchmark

If a UI fixture changes materially, benchmark compatibility must be reviewed.

---

## Fixture Immutability During Benchmark Execution

Once a benchmark execution selects a UI fixture version, its semantic behavior should remain unchanged for that run.

If a fixture defect is discovered:

1. Identify affected benchmark results.
2. Invalidate results when necessary.
3. Correct and version the fixture.
4. Re-run affected evaluations.

This prevents benchmark results from being produced against shifting UI context.

---

## Fixture Storage

UI fixtures belong under:

`datasets/fixtures/ui/`

The canonical fixture model may be documented in Markdown.

Machine-readable UI fixture instances may later use formats such as:

- JSON
- YAML

when a real automated consumer requires them.

Screenshots or design exports may be referenced when needed, but should not replace structured fixture semantics where QA-AI requires machine-readable context.

---

## Recommended Fixture Record

A canonical UI fixture record may contain:

| Field | Description |
|---|---|
| Fixture ID | Stable fixture identifier |
| Version | Fixture version |
| Domain | Related domain |
| Surface | Web, mobile, or other UI surface |
| Screen | Screen or page |
| Purpose | Fixture purpose |
| Role Context | Applicable user role |
| Components | Relevant UI components |
| Fields | Field definitions |
| Component States | Visible, hidden, enabled, disabled, read-only |
| Validation | Known UI validation |
| Navigation | Known navigation behavior |
| Initial State | Controlled starting UI state |
| Resulting State | Expected UI state after action |
| Responsive Context | Viewport or device context when applicable |
| Related Fixtures | Referenced fixture identifiers |
| Source References | Authoritative source |
| Status | Fixture lifecycle state |

Unused fields should not be populated with fabricated values.

---

## Example Canonical Fixture

The following serialized representation is illustrative only.

Its screen, fields, actions, states, and values demonstrate the fixture structure and are not derived from any QA-AI requirement dataset.

    fixture_id: UI-FIX-EXAMPLE-001
    version: 1.0.0
    domain: example
    surface: web
    status: Example

    screen:
      id: example_form
      name: Example Form

    fields:
      resource_name:
        label: Resource Name
        type: text
        required: true
        state: editable

      resource_type:
        label: Resource Type
        type: dropdown
        required: false
        state: editable

    actions:
      submit:
        type: button
        label: Submit
        visible: true

    states:
      default:
        submit:
          visible: true

      read_only:
        resource_name:
          state: read-only

        resource_type:
          state: read-only

    source_reference:
      type: illustrative-example
      authoritative: false

The example demonstrates the canonical UI fixture structure only.

Its screen, fields, labels, control types, actions, states, and values are synthetic and must not be treated as authoritative UI behavior.

A real UI fixture instance must replace illustrative values with information supported by authoritative requirements, specifications, designs, or approved UI references.

An illustrative example must not reference a requirement dataset as its source unless the represented UI behavior is actually defined by that dataset.
## Fixture Lifecycle

The recommended UI fixture lifecycle is:

`Draft → Review → Validate → Approve → Use → Maintain`

### Draft

Create the fixture from authoritative UI information.

### Review

Verify:

- Correctness
- Scope
- UI-state accuracy
- Validation behavior
- Traceability

### Validate

Confirm that the fixture provides sufficient controlled UI context for the intended QA task.

### Approve

Accept the fixture as reusable evaluation context.

### Use

Reference the approved fixture during QA-AI execution or benchmark evaluation.

### Maintain

Version the fixture when UI semantics change materially.

---

## Fixture Validation

Before approval, verify:

- Fixture ID is unique.
- Version is defined.
- Purpose is clear.
- Screen or component scope is clear.
- Component definitions are source-supported.
- Field states are source-supported.
- Visibility rules are source-supported.
- Enabled or disabled rules are source-supported.
- Validation behavior is source-supported.
- Exact message text is only included when authoritative.
- Navigation is source-supported.
- Role-specific behavior is source-supported.
- UI states are internally consistent.
- Dynamic values are controlled.
- Related fixture references are valid.
- No generated QA artifact is encoded in the fixture.
- Fixture behavior is deterministic enough for its intended evaluation.

---

## Security and Privacy

UI fixtures must use synthetic data.

Do not include:

- Real customer information
- Production screenshots containing PII
- Real account credentials
- Session tokens
- Confidential customer identifiers
- Sensitive financial information
- Internal production URLs when they should not be exposed

Use controlled values such as:

- `QA User`
- `qa.user@example.test`
- `REQ-001`
- `<token>`

Screenshots containing sensitive information must be sanitized before they are used as fixture references.

---

## Determinism Requirements

UI fixtures used for evaluation or benchmarking should avoid uncontrolled state such as:

- Current production data
- Random generated records
- Uncontrolled timestamps
- Dynamic third-party content
- Live notification counts
- Environment-dependent feature flags

Where dynamic behavior is part of the feature, use semantic context.

Example:

    generated_timestamp: "<current-valid-timestamp>"

rather than embedding a value that becomes stale.

---

## Fixture Quality Controls

A UI fixture should be:

### Correct

It reflects authoritative observable UI behavior.

### Complete Enough

It contains enough UI context for the intended QA task.

### Scoped

It does not reproduce unrelated application screens.

### Deterministic

The same fixture version represents the same test context.

### Traceable

Its source and associated dataset are identifiable.

### Implementation-Neutral

It avoids unsupported frontend implementation assumptions.

### Maintainable

Material UI changes can be versioned without silently changing benchmark meaning.

---

## Fixture Boundaries

UI fixtures must not:

- Replace source requirements.
- Invent UI validation.
- Invent exact validation messages.
- Invent hidden or disabled behavior.
- Assume UI behavior implies API behavior.
- Assume UI behavior implies database behavior.
- Invent role permissions.
- Infer frontend implementation technology.
- Encode generated scenarios or test cases.
- Encode benchmark scores.
- Encode evaluation ratings.
- Require exact AI-generated output.
- Act as a visual-regression baseline unless explicitly designed for that purpose.
- Depend unnecessarily on live production UI state.

---

## Validation Checklist

Before using a UI fixture, verify:

- Fixture ID exists.
- Version exists.
- Status is appropriate.
- Purpose is clear.
- Screen or component scope is defined.
- UI surface is identified when relevant.
- Role context is correct when applicable.
- Components are source-supported.
- Field states are correct.
- Visibility behavior is correct.
- Enabled or disabled behavior is correct.
- Read-only behavior is distinguished from disabled behavior.
- Validation behavior is supported.
- Exact text is not invented.
- Navigation behavior is supported.
- State transitions are supported.
- Responsive context is defined only when applicable.
- Dynamic values are controlled.
- Synthetic data is safe.
- Related fixtures are valid.
- Fixture version is compatible with the target dataset.
- Benchmark comparability remains valid.

---

## Final UI Fixture Definition

A QA-AI UI fixture is:

> A controlled, versioned, deterministic, source-supported representation of observable user-interface context used to make QA-AI UI reasoning, test generation, evaluation, and benchmark execution reproducible without depending on uncontrolled live application state.

The canonical UI fixture model provides:

- Controlled screen and component context
- Field definitions
- Visibility and interaction states
- UI validation behavior
- Navigation context
- Role-aware presentation
- UI state transitions
- Positive, negative, and boundary contexts
- Responsive evaluation context
- Safe synthetic UI data
- Requirement and fixture traceability
- Fixture versioning
- Benchmark reproducibility
- Cross-platform consistency
- Regression compatibility
- Protection against unsupported frontend assumptions

It enables QA-AI to reason about UI behavior consistently while preserving the boundary between observable interface behavior, business requirements, API contracts, database implementation, and visual design details.
