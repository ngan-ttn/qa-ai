# Requirement Analyzer

## Purpose

The `requirement-analyzer` skill transforms unstructured requirement information into structured requirement understanding that serves as the foundation for downstream QA capabilities.

The skill focuses on understanding and organizing requirement information. It does not interpret business rules, generate testing artifacts, or perform downstream QA activities.

---

## Capability

This skill provides the capability to analyze requirement information and produce a structured understanding of the requested functionality.

Its primary objective is to transform raw requirement content into organized analysis outputs that support subsequent QA capabilities.

Capability flow:

```text
Requirement Information
        ↓
Understand Context
        ↓
Analyze Content
        ↓
Organize Information
        ↓
Structured Requirement Analysis
```

---

## When To Use

Use this skill when:

- A new requirement is introduced
- A user story requires analysis
- A feature specification needs to be understood
- Requirement changes require impact assessment
- Downstream QA skills require structured requirement information

This skill should be executed before generating business rules, test scenarios, or regression analysis.

---

## Input

### Required Input

Examples:

- Requirement document
- User story
- Feature specification
- Acceptance criteria

### Optional Input

Examples:

- Business context
- Existing documentation
- UI mockups
- API specifications
- Existing implementation notes

The skill should identify missing or ambiguous information during analysis.

---

## Processing

The skill performs the following logical processing activities.

### Step 1 — Understand Context

Identify the overall business objective and feature purpose.

---

### Step 2 — Identify Functional Scope

Determine:

- Primary functionality
- User interactions
- Functional boundaries

---

### Step 3 — Identify Key Information

Analyze available information, including:

- Actors
- Inputs
- Outputs
- Dependencies
- Constraints

---

### Step 4 — Detect Uncertainty

Identify:

- Missing information
- Ambiguous statements
- Assumptions requiring clarification

---

### Step 5 — Produce Structured Analysis

Organize the identified information into a structured requirement analysis suitable for downstream QA activities.

---

## Output

The skill produces a structured requirement analysis model that can be consumed by downstream QA skills.

Typical outputs may include:

- Feature summary
- Functional scope
- Actors
- Inputs and outputs
- Dependencies
- Constraints
- Assumptions
- Open questions

The exact output structure should follow the applicable templates defined in the shared resources.

---

## Dependencies

This skill may use resources from the shared module.

| Resource | Purpose |
|----------|---------|
| `shared/standards/` | Apply requirement analysis standards |
| `shared/templates/` | Structure analysis output |
| `shared/prompt-patterns/` | Apply reusable analysis prompts |

The skill consumes these resources but does not redefine them.

---

## Consumers

The output of this skill may be consumed by:

- `skills/business-rule-extractor`
- `skills/scenario-generator`
- `skills/regression-impact`

It may also be invoked by workflows such as:

- `workflows/testcase-generation`
- `workflows/regression-analysis`

---

## Limitations

This skill does not:

- Interpret or extract business rules
- Generate test scenarios
- Generate test cases
- Review testcase quality
- Perform regression impact analysis

These responsibilities belong to other specialized skills.

---

## Validation

The output of this skill should be validated to ensure:

- Requirement information is accurately represented
- Functional scope is clearly identified
- Key entities and dependencies are captured
- Missing information is explicitly identified
- The analysis is structured and reusable by downstream skills
- The output can be consumed without additional interpretation by downstream QA skills

Detailed validation criteria should be maintained in the relevant shared checklists.