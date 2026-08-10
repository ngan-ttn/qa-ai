# Coverage Reviewer

## Purpose

The `coverage-reviewer` skill transforms structured test case models into structured coverage assessments that support downstream QA capabilities.

The skill focuses on evaluating the completeness, consistency, and traceability of structured test cases. It does not generate testing artifacts or perform regression impact analysis.

---

## Capability

This skill provides the capability to review and assess structured test cases.

Its primary objective is to transform structured test case information into a structured coverage assessment that supports subsequent QA capabilities.

Capability flow:

```text
Structured Test Case Model
        ↓
Review Test Cases
        ↓
Assess Completeness
        ↓
Assess Consistency
        ↓
Assess Traceability
        ↓
Structured Coverage Assessment
```

---

## When To Use

Use this skill when:

- Structured test case models are available
- Test case quality needs to be reviewed
- Test coverage needs to be assessed
- Traceability needs to be verified
- Downstream QA skills require a structured coverage assessment

This skill should be executed before performing regression impact analysis.

---

## Input

### Required Input

Examples:

- Structured test case model
- Test case relationships
- Preconditions
- Test steps
- Expected results

### Optional Input

Examples:

- Structured test scenario model
- Structured business rule model
- Structured requirement analysis

The skill should identify missing, inconsistent, or insufficient coverage during assessment.

---

## Processing

The skill performs the following logical processing activities.

### Step 1 — Review Test Cases

Review the available structured test cases.

---

### Step 2 — Assess Completeness

Assess the completeness of the structured test case model.

---

### Step 3 — Assess Consistency

Identify inconsistencies, duplicates, or logical conflicts across the structured test case model.

---

### Step 4 — Assess Traceability

Verify that the structured test case model can be traced back to upstream QA artifacts, including test scenarios, business rules, and requirement analysis.

---

### Step 5 — Produce Structured Coverage Assessment

Organize the assessment results into a structured representation suitable for downstream QA activities.

---

## Output

The skill produces a structured coverage assessment that can be consumed by downstream QA skills.

Typical outputs may include:

- Coverage findings
- Coverage gaps
- Consistency findings
- Traceability findings
- Open questions

The exact output structure should follow the applicable templates defined in the shared resources.

---

## Dependencies

This skill may use resources from the shared module.

| Resource | Purpose |
|----------|---------|
| `shared/standards/` | Apply coverage review standards |
| `shared/templates/` | Structure coverage assessment output |
| `shared/prompt-patterns/` | Apply reusable review prompts |

The skill consumes these resources but does not redefine them.

---

## Consumers

The output of this skill may be consumed by:

- `skills/regression-impact`

It may also be invoked by workflows such as:

- `workflows/regression-analysis`

---

## Limitations

This skill does not:

- Analyze raw requirements
- Extract business rules
- Generate test scenarios
- Generate test cases
- Modify existing test cases
- Perform regression impact analysis

These responsibilities belong to other specialized skills.

---

## Validation

The output of this skill should be validated to ensure:

- Coverage findings accurately reflect the structured test case model
- Coverage gaps are explicitly identified
- Consistency issues are clearly represented
- Traceability is accurately represented
- The output is structured and reusable by downstream QA skills
- The output can be consumed without additional interpretation by downstream QA skills

Detailed validation criteria should be maintained in the relevant shared checklists.