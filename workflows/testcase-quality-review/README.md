# Testcase Quality Review Workflow

## Purpose

The `testcase-quality-review` workflow defines the coordinated process for evaluating the quality and coverage of an existing structured test case model.

This workflow orchestrates the `coverage-reviewer` capability with relevant upstream QA artifacts and shared resources to produce a structured coverage assessment.

The workflow defines review orchestration and artifact dependencies. It does not generate or modify test cases, duplicate the internal review logic owned by the coverage-reviewer skill, or redefine detailed review criteria maintained in shared resources.

---

## When To Use

This workflow should be used when:

- Existing structured test cases need quality evaluation
- Test coverage needs to be assessed before execution or reuse
- Testcase completeness, consistency, or traceability needs to be reviewed
- Requirement or business-rule context is available for validating testcase coverage
- QA teams need a structured testcase quality review process

This workflow should not be used for:

- Creating new test cases from requirements
- Modifying existing test cases
- Executing test cases
- Performing regression impact analysis
- Reviewing automation code

---

## Input

### Required Input

The workflow requires a structured test case model suitable for `skills/coverage-reviewer`.

Typical required information includes:

- Structured test cases
- Test case relationships
- Preconditions
- Test steps
- Expected results

### Optional Input

Upstream artifacts may be supplied to strengthen coverage and traceability assessment:

- Structured test scenario model
- Structured business rule model
- Structured requirement analysis
- Previous coverage assessment
- Related QA context

The workflow should not reconstruct missing upstream artifacts as confirmed information. Missing context that affects review confidence should remain visible in the assessment.

---

## Workflow Flow

```text
Structured Test Case Model
        │
        ├── Optional: Structured Test Scenario Model
        ├── Optional: Structured Business Rule Model
        └── Optional: Structured Requirement Analysis
        │
        ▼
Coverage Reviewer
        │
        ▼
Structured Coverage Assessment
```

The structured test case model is the primary review target. Available upstream artifacts provide additional evidence for completeness and traceability assessment.

---

## Workflow Steps

### Step 1: Validate Review Input

Confirm that a structured test case model is available and contains sufficient information for coverage review.

Identify:

- Review scope
- Available test case information
- Available upstream artifacts
- Missing context that may affect assessment confidence

---

### Step 2: Review Test Cases

Execute `skills/coverage-reviewer` using the structured test case model as the required input.

Available upstream artifacts should be supplied as optional context when they are valid and applicable to the current scope.

---

### Step 3: Assess Completeness

Evaluate whether the structured test case model sufficiently represents the applicable testing scope supported by the available evidence.

Coverage gaps should be identified without inventing unsupported requirement behavior.

---

### Step 4: Assess Consistency

Identify inconsistencies, duplicates, or logical conflicts within the structured test case model and against valid upstream artifacts when available.

---

### Step 5: Assess Traceability

Verify traceability from test cases to available upstream QA artifacts, including test scenarios, business rules, and requirement analysis where those artifacts are provided.

Missing upstream artifacts should be reported as a traceability limitation rather than silently reconstructed.

---

### Step 6: Produce and Validate Coverage Assessment

Produce the structured coverage assessment defined by `skills/coverage-reviewer` and validate that findings are supported by the provided artifacts.

Validation should confirm:

- Coverage findings reflect the reviewed test case model
- Coverage gaps are explicitly identified
- Consistency findings are evidence-based
- Traceability findings accurately reflect available upstream artifacts
- Open questions or review limitations remain visible
- Applicable standards and output structures are followed

---

## Required Skills

This workflow coordinates the following skill:

| Skill | Purpose |
|---|---|
| `skills/coverage-reviewer` | Evaluate completeness, consistency, and traceability of structured test cases and produce a structured coverage assessment |

Requirement analysis, business rule extraction, scenario generation, and testcase generation are not implicitly executed by this workflow. Their artifacts may be consumed as optional review context when already available.

---

## Required Resources

The participating skill may resolve applicable resources from the shared module, including:

| Resource | Purpose |
|---|---|
| `shared/standards/` | Apply applicable coverage and artifact standards |
| `shared/templates/` | Structure coverage assessment output |
| `shared/checklists/` | Support applicable review validation |
| `shared/prompt-patterns/` | Provide reusable review instructions where required |

The workflow references these resources without duplicating their detailed review rules.

---

## Output

The workflow produces:

- Structured coverage assessment

Typical assessment content may include:

- Coverage findings
- Coverage gaps
- Consistency findings
- Traceability findings
- Open questions

The exact output structure should follow the applicable templates and output standards defined in shared resources.

This workflow produces review findings only. It does not automatically modify, regenerate, or approve the reviewed test cases.

---

## Validation

The workflow is complete when:

- A valid structured test case model has been reviewed
- Applicable upstream artifacts have been used when available
- Completeness, consistency, and traceability have been assessed
- Findings are supported by the provided artifacts
- Review limitations and unresolved gaps are explicitly represented
- The structured coverage assessment satisfies the coverage-reviewer output contract
- Applicable standards and templates are followed

This workflow does not generate test cases, modify reviewed artifacts, perform regression impact analysis, execute tests, or manage test results.