# Scenario Generator

## Purpose

The `scenario-generator` skill transforms structured business rule models into structured test scenario models that support downstream QA capabilities.

The skill focuses on identifying and organizing test scenarios based on structured business rules. It does not analyze requirements, extract business rules, generate test cases, or perform downstream QA activities.

---

## Capability

This skill provides the capability to identify and organize test scenarios from structured business rules.

Its primary objective is to transform structured business rule information into a structured test scenario model that supports subsequent QA capabilities.

Capability flow:

```text
Structured Business Rule Model
        ↓
Identify Test Scenarios
        ↓
Organize Scenarios
        ↓
Establish Scenario Relationships
        ↓
Structured Test Scenario Model
```

---

## When To Use

Use this skill when:

- Structured business rule models are available
- Business behavior needs to be represented as test scenarios
- User journeys require scenario decomposition
- Downstream QA skills require structured test scenarios

This skill should be executed before generating test cases.

---

## Input

### Required Input

Examples:

- Structured business rule model
- Rule relationships
- Dependencies
- Constraints
- Exceptions

### Optional Input

Examples:

- Structured requirement analysis
- Original requirement document
- User story
- Acceptance criteria

The skill should identify missing or ambiguous scenarios during generation.

---

## Processing

The skill performs the following logical processing activities.

### Step 1 — Identify Test Scenarios

Identify test scenarios from structured business rules.

---

### Step 2 — Organize Scenarios

Organize scenarios into logical user journeys and business behaviors.

---

### Step 3 — Establish Scenario Relationships

Identify logical relationships between scenarios, business rules, and user flows.

---

### Step 4 — Detect Missing Scenarios

Identify:

- Missing scenarios
- Duplicate scenarios
- Ambiguous scenarios

---

### Step 5 — Produce Structured Test Scenario Model

Organize the identified scenarios into a structured representation suitable for downstream QA activities.

---

## Output

The skill produces a structured test scenario model that can be consumed by downstream QA skills.

Typical outputs may include:

- Test scenarios
- User journeys
- Scenario relationships
- Dependencies
- Assumptions
- Open questions

The exact output structure should follow the applicable templates defined in the shared resources.

---

## Dependencies

This skill may use resources from the shared module.

| Resource | Purpose |
|----------|---------|
| `shared/standards/` | Apply test scenario generation standards |
| `shared/templates/` | Structure test scenario output |
| `shared/prompt-patterns/` | Apply reusable scenario generation prompts |

The skill consumes these resources but does not redefine them.

---

## Consumers

The output of this skill may be consumed by:

- `skills/testcase-generator`
- `skills/regression-impact`

It may also be invoked by workflows such as:

- `workflows/testcase-generation`
- `workflows/regression-analysis`

---

## Limitations

This skill does not:

- Analyze raw requirements
- Extract or classify business rules
- Generate test cases
- Review testcase quality
- Perform regression impact analysis

These responsibilities belong to other specialized skills.

---

## Validation

The output of this skill should be validated to ensure:

- Test scenarios are accurately identified
- Scenario relationships are clearly represented
- Missing or ambiguous scenarios are explicitly identified
- The output is structured and reusable by downstream QA skills
- The output can be consumed without additional interpretation by downstream QA skills

Detailed validation criteria should be maintained in the relevant shared checklists.