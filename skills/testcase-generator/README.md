# Testcase Generator

## Purpose

The `testcase-generator` skill transforms structured test scenario models into structured test case models that support downstream QA capabilities.

The skill focuses on generating and organizing executable test cases from structured test scenarios. It does not analyze requirements, extract business rules, generate test scenarios, or perform downstream QA activities.

---

## Capability

This skill provides the capability to generate and organize test cases from structured test scenarios.

Its primary objective is to transform structured test scenario information into a structured test case model that supports subsequent QA capabilities.

Capability flow:

```text
Structured Test Scenario Model
        ↓
Identify Test Cases
        ↓
Structure Test Cases
        ↓
Organize Test Cases
        ↓
Structured Test Case Model
```

---

## When To Use

Use this skill when:

- Structured test scenario models are available
- Test cases need to be generated
- Test logic needs to be defined
- Downstream QA skills require structured test cases

This skill should be executed before reviewing testcase quality or performing regression impact analysis.

---

## Input

### Required Input

Examples:

- Structured test scenario model
- Scenario relationships
- User journeys
- Dependencies
- Assumptions

### Optional Input

Examples:

- Structured business rule model
- Structured requirement analysis
- Original requirement document

The skill should identify missing or ambiguous test cases during generation.

---

## Processing

The skill performs the following logical processing activities.

### Step 1 — Identify Test Cases

Identify the required test cases from structured test scenarios.

---

### Step 2 — Structure Test Cases

Define the logical structure of each test case, including execution conditions, expected behavior, and supporting information.

---

### Step 3 — Organize Test Cases

Organize test cases into logical groups based on features, user flows, or functional areas.

---

### Step 4 — Detect Gaps

Identify:

- Missing test cases
- Duplicate test cases
- Ambiguous test cases

---

### Step 5 — Produce Structured Test Case Model

Organize the identified test cases into a structured representation suitable for downstream QA activities.

---

## Output

The skill produces a structured test case model that can be consumed by downstream QA skills.

Typical outputs may include:

- Test cases
- Preconditions
- Test steps
- Expected results
- Test data references
- Dependencies
- Assumptions
- Open questions

The exact output structure should follow the applicable templates defined in the shared resources.

---

## Dependencies

This skill may use resources from the shared module.

| Resource | Purpose |
|----------|---------|
| `shared/standards/` | Apply testcase generation standards |
| `shared/templates/` | Structure testcase output |
| `shared/prompt-patterns/` | Apply reusable testcase generation prompts |

The skill consumes these resources but does not redefine them.

---

## Consumers

The output of this skill may be consumed by:

- `skills/coverage-reviewer`
- `skills/regression-impact`

It may also be invoked by workflows such as:

- `workflows/testcase-generation`
- `workflows/regression-analysis`

---

## Limitations

This skill does not:

- Analyze raw requirements
- Extract or classify business rules
- Generate test scenarios
- Review testcase quality
- Perform regression impact analysis

These responsibilities belong to other specialized skills.

---

## Validation

The output of this skill should be validated to ensure:

- Test cases are accurately generated from structured test scenarios
- Test case structure is logically organized
- Missing, duplicate, or ambiguous test cases are explicitly identified
- The output is structured and reusable by downstream QA skills
- The output can be consumed without additional interpretation by downstream QA skills

Detailed validation criteria should be maintained in the relevant shared checklists.