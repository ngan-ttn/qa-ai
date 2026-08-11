# Regression Analysis Workflow

## Purpose

The `regression-analysis` workflow defines the coordinated process for analyzing the regression impact of a change and determining an appropriate regression scope from validated QA artifacts.

This workflow orchestrates the `regression-impact` capability using a structured coverage assessment as its required upstream artifact and relevant change information as supporting context.

The workflow defines orchestration, artifact dependencies, and workflow-level validation. It does not duplicate regression analysis logic owned by the skill, generate new test artifacts, or define regression execution plans.

---

## When To Use

This workflow should be used when:

- Requirement changes need regression impact assessment
- Bugs or fixes may affect existing covered behavior
- Feature enhancements require regression scope analysis
- Existing QA artifacts need to be assessed for change impact
- A release requires regression prioritization based on validated coverage information

This workflow should not be used for:

- Creating new test cases
- Reviewing testcase quality
- Executing regression tests
- Scheduling regression execution
- Managing release activities

---

## Input

### Required Input

The workflow requires a structured coverage assessment suitable for `skills/regression-impact`.

Typical required information includes:

- Coverage findings
- Coverage gaps
- Traceability findings
- Consistency findings where applicable

### Optional Input

Supporting context may include:

- Requirement change information
- Structured test case model
- Structured test scenario model
- Structured business rule model
- Structured requirement analysis
- Previous regression analysis
- Release scope
- Related QA artifacts

The workflow should preserve the distinction between confirmed impact evidence and unknown system dependencies.

Missing context that prevents reliable impact assessment should remain visible as clarification or investigation items rather than being silently inferred.

---

## Workflow Flow

```text
Structured Coverage Assessment
        │
        ├── Optional: Requirement Change Information
        ├── Optional: Structured Test Case Model
        ├── Optional: Structured Test Scenario Model
        ├── Optional: Structured Business Rule Model
        └── Optional: Structured Requirement Analysis
        │
        ▼
Regression Impact
        │
        ▼
Structured Regression Impact Analysis
```

The structured coverage assessment is the required upstream artifact. Additional context strengthens impact analysis but does not replace the required coverage assessment.

---

## Workflow Steps

### Step 1: Validate Regression Input

Confirm that a structured coverage assessment is available and suitable for regression impact analysis.

Identify:

- Change objective
- Available coverage findings
- Available traceability information
- Available upstream QA artifacts
- Missing context that may affect analysis confidence

---

### Step 2: Identify Changes

Execute the change-identification activity defined by `skills/regression-impact` using the structured coverage assessment and available change information.

The workflow should distinguish confirmed change information from assumptions and unknown dependencies.

---

### Step 3: Analyze Impact

Evaluate how the identified change affects existing validated QA artifacts and covered behavior.

Impact analysis should remain traceable to available coverage findings, change information, and upstream artifacts.

---

### Step 4: Determine Regression Scope

Identify the areas requiring regression testing based on the confirmed impact evidence.

The regression scope may include:

- Affected covered behavior
- Existing test assets that remain applicable
- Coverage gaps requiring attention
- Areas requiring additional investigation

Unsupported system components or dependencies must not be promoted to confirmed impact.

---

### Step 5: Prioritize Regression Areas

Prioritize regression areas according to the impact evidence available to the `regression-impact` skill.

Prioritization should be justified by confirmed change and coverage information rather than unsupported implementation assumptions.

---

### Step 6: Produce and Validate Regression Analysis

Produce the structured regression impact analysis defined by `skills/regression-impact`.

Validation should confirm:

- Impact findings are traceable to identified changes and available QA artifacts
- Regression scope is clearly represented
- Priorities are logically supported
- Unknown dependencies remain explicitly identified
- Assumptions and open questions remain visible
- Applicable standards and output structures are followed

---

## Required Skills

This workflow coordinates the following skill:

| Skill | Purpose |
|---|---|
| `skills/regression-impact` | Transform a structured coverage assessment into structured regression impact analysis |

Requirement analysis, business rule extraction, scenario generation, testcase generation, and coverage review are not implicitly re-executed by this workflow. Their valid artifacts may be consumed as supporting context when already available.

---

## Required Resources

The participating skill may resolve applicable resources from the shared module, including:

| Resource | Purpose |
|---|---|
| `shared/standards/` | Apply applicable regression and artifact standards |
| `shared/templates/` | Structure regression impact analysis output |
| `shared/checklists/` | Support applicable validation activities |
| `shared/prompt-patterns/` | Provide reusable regression analysis instructions where required |

The workflow references these resources without duplicating their detailed content.

---

## Output

The workflow produces:

- Structured regression impact analysis

Typical output content may include:

- Impact findings
- Affected areas
- Regression scope
- Priority assessment
- Dependencies
- Assumptions
- Open questions

The exact output structure should follow the applicable templates and output standards defined in shared resources.

This workflow identifies regression impact and scope. It does not execute regression tests, create a test execution schedule, or modify existing test artifacts.

---

## Validation

The workflow is complete when:

- A valid structured coverage assessment has been consumed
- Available change information and relevant upstream artifacts have been applied where appropriate
- Impact findings are traceable to available evidence
- Regression scope and priorities are clearly represented
- Unknown dependencies and unresolved information are explicitly surfaced
- The structured regression impact analysis satisfies the regression-impact output contract
- Applicable standards and templates are followed

This workflow does not generate test cases, review testcase quality, execute regression tests, or manage release activities.