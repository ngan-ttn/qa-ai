# Business Rule Extractor

## Purpose

The `business-rule-extractor` skill transforms structured requirement analysis into structured business rules that support downstream QA capabilities.

The skill focuses on identifying, classifying, and organizing business rules. It does not analyze requirements, generate testing artifacts, or perform downstream QA activities.

---

## Capability

This skill provides the capability to identify and organize business rules from structured requirement information.

Its primary objective is to transform analyzed requirement information into structured business rules that support subsequent QA capabilities.

Capability flow:

```text
Structured Requirement Analysis
        ↓
Identify Business Rules
        ↓
Classify Rules
        ↓
Resolve Relationships
        ↓
Structured Business Rules
```

---

## When To Use

Use this skill when:

- Structured requirement analysis is available
- Business rules need to be identified
- Business logic requires classification
- Rule relationships require clarification
- Downstream QA skills require structured business rules

This skill should be executed before generating test scenarios or test cases.

---

## Input

### Required Input

Examples:

- Structured requirement analysis
- Functional scope
- Feature summary
- Dependencies
- Constraints

### Optional Input

Examples:

- Original requirement document
- User story
- Acceptance criteria
- Business documentation

The skill should identify missing, conflicting, or ambiguous business rules during extraction.

---

## Processing

The skill performs the following logical processing activities.

### Step 1 — Identify Business Rules

Identify explicit and implicit business rules from the analyzed requirement information.

---

### Step 2 — Classify Rules

Organize identified rules into logical categories based on their purpose and behavior.

---

### Step 3 — Resolve Relationships

Identify relationships between:

- Business rules
- Requirements
- Dependencies
- Constraints

---

### Step 4 — Detect Gaps

Identify:

- Missing business rules
- Conflicting rules
- Ambiguous rules

---

### Step 5 — Produce Structured Business Rules

Organize the identified business rules into a structured representation suitable for downstream QA activities.

---

## Output

The skill produces a structured business rule model that can be consumed by downstream QA skills.

Typical outputs may include:

- Business rules
- Rule categories
- Rule relationships
- Dependencies
- Constraints
- Exceptions
- Open questions

The exact output structure should follow the applicable templates defined in the shared resources.

---

## Dependencies

This skill may use resources from the shared module.

| Resource | Purpose |
|----------|---------|
| `shared/standards/` | Apply business rule extraction standards |
| `shared/templates/` | Structure business rule output |
| `shared/prompt-patterns/` | Apply reusable extraction prompts |

The skill consumes these resources but does not redefine them.

---

## Consumers

The output of this skill may be consumed by:

- `skills/scenario-generator`
- `skills/testcase-generator`
- `skills/regression-impact`

It may also be invoked by workflows such as:

- `workflows/testcase-generation`
- `workflows/regression-analysis`

---

## Limitations

This skill does not:

- Analyze raw requirements
- Generate test scenarios
- Generate test cases
- Review testcase quality
- Perform regression impact analysis

These responsibilities belong to other specialized skills.

---

## Validation

The output of this skill should be validated to ensure:

- Business rules are accurately identified
- Rule classifications are logically organized
- Rule relationships are clearly represented
- Missing, conflicting, or ambiguous rules are explicitly identified
- The output is structured and reusable by downstream QA skills
- The output can be consumed without additional interpretation by downstream QA skills

Detailed validation criteria should be maintained in the relevant shared checklists.