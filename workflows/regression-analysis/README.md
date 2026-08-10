# Regression Analysis Workflow

## Purpose

The `regression-analysis` workflow defines the process for analyzing the impact of changes and determining an appropriate regression testing scope.

This workflow guides the AI assistant in applying relevant QA skills and shared resources to identify affected areas, assess potential risks, and recommend regression activities.

The workflow focuses on the analysis process, not on defining regression testing methodologies or execution strategies.

---

## When To Use

This workflow should be used when:

* Requirements are modified
* Bugs are fixed
* Features are enhanced
* Existing functionality is refactored
* A release requires regression planning
* The impact of a change needs to be evaluated

This workflow should not be used for:

* Creating new test cases
* Reviewing testcase quality
* Executing regression tests
* Managing release activities

---

## Input

The workflow requires change-related information as input.

### Required Input

Examples:

* Change request
* Requirement updates
* Bug fix description
* Feature enhancement information

### Optional Input

Examples:

* Existing test cases
* Requirement documents
* Release scope
* Previous regression analysis
* Related QA artifacts

The workflow should identify missing information before determining regression scope.

---

## Workflow Steps

The workflow follows these execution steps.

### Step 1: Understand the Change

Analyze the available change information.

Identify:

* Nature of the change
* Business objective
* Functional scope
* Affected components

---

### Step 2: Identify Impacted Areas

Determine which parts of the system may be affected by the change.

Consider:

* Functional dependencies
* User flows
* Business processes
* Related modules
* Existing integrations

---

### Step 3: Assess Regression Risk

Evaluate the potential impact of the identified changes.

The assessment should consider:

* Scope of affected functionality
* Potential side effects
* Areas requiring additional verification

---

### Step 4: Determine Regression Scope

Define the regression scope based on the impact assessment.

The scope should identify:

* Features requiring regression testing
* Existing test assets that remain applicable
* Areas that require additional validation

---

### Step 5: Recommend Regression Activities

Provide recommendations that support regression planning.

Examples include:

* Priority areas for validation
* Suggested regression focus
* Additional verification activities

---

### Step 6: Validate Analysis Result

Review the completed analysis before finalizing the output.

Validation should ensure:

* The analysis is traceable to the identified changes
* The proposed regression scope is justified
* Recommendations are consistent with applicable QA standards

---

## Required Skills

This workflow may require the following skills.

| Skill                         | Purpose                                          |
| ----------------------------- | ------------------------------------------------ |
| `skills/requirement-analysis` | Understand the context and scope of the change   |
| `skills/regression-testing`   | Support regression scope analysis                |
| `skills/risk-analysis`        | Evaluate potential impact and testing priorities |

The workflow references these skills but does not contain their detailed knowledge.

---

## Required Resources

This workflow may use resources from the shared directory.

| Resource                  | Purpose                                        |
| ------------------------- | ---------------------------------------------- |
| `shared/standards/`       | Provide QA principles and analysis guidance    |
| `shared/templates/`       | Define output structures and reporting formats |
| `shared/checklists/`      | Provide validation criteria                    |
| `shared/prompt-patterns/` | Provide reusable instruction patterns          |

The workflow applies these resources but does not redefine them.

---

## Output

The expected outputs of this workflow include:

* Change impact analysis
* Identified affected areas
* Recommended regression scope
* Regression recommendations

Output formats should follow the applicable templates defined in shared resources.

---

## Validation

The workflow output should be validated to ensure:

* The analysis is based on the provided change information
* Impacted areas are relevant and traceable
* Recommended regression scope is appropriate
* Recommendations are consistent with applicable QA standards
* Output structure follows defined templates

Detailed validation criteria should be maintained in the relevant shared checklists.
