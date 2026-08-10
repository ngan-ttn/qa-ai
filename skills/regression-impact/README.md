# Regression Impact

## Purpose

The `regression-impact` skill transforms structured coverage assessments into structured regression impact analysis that supports downstream QA activities.

The skill focuses on analyzing the impact of changes on existing QA artifacts. It does not generate testing artifacts, review test case quality, or create regression execution plans.

---

## Capability

This skill provides the capability to analyze the impact of changes on structured QA artifacts.

Its primary objective is to transform structured coverage assessment information into a structured regression impact analysis that supports downstream QA activities.

Capability flow:

```text
Structured Coverage Assessment
        ↓
Identify Changes
        ↓
Analyze Impact
        ↓
Identify Regression Scope
        ↓
Prioritize Regression Areas
        ↓
Structured Regression Impact Analysis
```

---

## When To Use

Use this skill when:

- Requirement changes need impact assessment
- Regression testing scope needs to be identified
- Existing QA artifacts require impact analysis
- Regression priorities need to be determined
- Downstream QA activities require structured regression impact analysis

This skill should be executed after coverage assessment and before downstream regression testing activities.

---

## Input

### Required Input

Examples:

- Structured coverage assessment
- Coverage findings
- Coverage gaps
- Traceability findings

### Optional Input

Examples:

- Structured test case model
- Structured test scenario model
- Structured business rule model
- Structured requirement analysis
- Requirement change information

The skill should identify incomplete, uncertain, or missing impact information during analysis.

---

## Processing

The skill performs the following logical processing activities.

### Step 1 — Identify Changes

Identify the changes that require regression impact analysis.

---

### Step 2 — Analyze Impact

Analyze how the identified changes affect existing QA artifacts.

---

### Step 3 — Identify Regression Scope

Determine the areas that require regression testing.

---

### Step 4 — Prioritize Regression Areas

Prioritize regression activities based on the identified impact.

---

### Step 5 — Produce Structured Regression Impact Analysis

Organize the analysis results into a structured representation suitable for downstream QA activities.

---

## Output

The skill produces a structured regression impact analysis that supports downstream QA activities.

Typical outputs may include:

- Impact findings
- Affected areas
- Regression scope
- Priority assessment
- Dependencies
- Assumptions
- Open questions

The exact output structure should follow the applicable templates defined in the shared resources.

---

## Dependencies

This skill may use resources from the shared module.

| Resource | Purpose |
|----------|---------|
| `shared/standards/` | Apply regression impact analysis standards |
| `shared/templates/` | Structure regression impact analysis output |
| `shared/prompt-patterns/` | Apply reusable regression analysis prompts |

The skill consumes these resources but does not redefine them.

---

## Consumers

This skill represents the final analytical stage of the QA capability pipeline.

Its output supports regression-related decision-making and may be used by downstream QA activities.

It may also be invoked by workflows such as:

- `workflows/regression-analysis`

---

## Limitations

This skill does not:

- Analyze raw requirements
- Generate test scenarios
- Generate test cases
- Review testcase quality
- Create regression execution plans
- Schedule testing activities

These responsibilities belong to other specialized processes or specialized skills.

---

## Validation

The output of this skill should be validated to ensure:

- Impact findings accurately reflect the identified changes
- Regression scope is clearly identified
- Priorities are logically determined
- Dependencies are accurately represented
- The output is structured and reusable for downstream QA activities
- The output supports regression-related decision-making without additional interpretation

Detailed validation criteria should be maintained in the relevant shared checklists.