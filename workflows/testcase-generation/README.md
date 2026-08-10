# Testcase Generation Workflow

## Purpose

The `testcase-generation` workflow defines the process for transforming QA inputs into structured test scenarios and test cases.

This workflow guides the AI assistant in applying relevant QA skills and shared resources to create consistent and reviewable test artifacts.

The workflow focuses on the execution process of testcase generation, not on storing testing knowledge or defining output formats.

---

## When To Use

This workflow should be used when:

* New requirements need test coverage
* New user stories need validation scenarios
* Acceptance criteria need to be converted into test cases
* Business rules need to be analyzed for testing activities
* Existing feature changes require new test coverage

This workflow should not be used for:

* Reviewing existing testcase quality
* Analyzing regression impact
* Executing test cases
* Managing test execution results

---

## Input

The workflow requires QA-related information as input.

### Required Input

Examples:

* Requirement document
* User story
* Acceptance criteria
* Feature description

### Optional Input

Examples:

* Existing test cases
* Business rules
* Previous release information
* Related QA documents

The workflow should identify missing or unclear information before generating test artifacts.

---

## Workflow Steps

The workflow follows these execution steps:

### Step 1: Understand Input

Analyze the provided QA information.

Identify:

* Feature scope
* User roles
* Main functionality
* Available business information

---

### Step 2: Analyze Requirement

Review the input to identify testing-related information.

Consider:

* Functional behavior
* Business rules
* User flows
* Dependencies
* Constraints

---

### Step 3: Identify Test Scope

Determine the areas that require validation.

Identify:

* Main scenarios
* Alternative flows
* Negative scenarios
* Important business conditions

---

### Step 4: Generate Test Scenarios

Create high-level test scenarios based on the identified scope.

Each scenario should represent a meaningful validation objective.

---

### Step 5: Generate Test Cases

Transform identified test scenarios into structured test cases by applying relevant QA skills and shared resources.

The generated test cases should follow the defined testcase standards and templates.

---

### Step 6: Validate Output

Review generated test artifacts before completion.

Validation should focus on:

* Requirement coverage
* Scenario completeness
* Consistency with applicable QA standards
* Compliance with required output structure

Detailed validation rules should be maintained in shared checklists.

---

## Required Skills

This workflow may require the following skills:

| Skill                         | Purpose                                           |
| ----------------------------- | ------------------------------------------------- |
| `skills/requirement-analysis` | Analyze requirements and identify testing scope   |
| `skills/test-design`          | Create effective test scenarios and test cases    |
| `skills/functional-testing`   | Ensure functional behavior is properly considered |

The workflow references these skills but does not contain their detailed knowledge.

---

## Required Resources

This workflow may use resources from the shared directory.

| Resource                  | Purpose                               |
| ------------------------- | ------------------------------------- |
| `shared/templates/`       | Provide output structures and formats |
| `shared/checklists/`      | Provide validation criteria           |
| `shared/prompt-patterns/` | Provide reusable instruction patterns |

The workflow applies these resources but does not redefine them.

---

## Output

The expected outputs of this workflow include:

* Test scenarios
* Structured test cases
* Test coverage information

Output formats should follow the applicable templates defined in shared resources.

---

## Validation

The workflow output should be validated to ensure:

* Required testing scope has been considered
* Generated artifacts are consistent with the input
* Applicable QA standards are followed
* Output structure follows defined templates
* Results are suitable for further QA activities

Detailed validation criteria should be maintained in the relevant shared checklists.
