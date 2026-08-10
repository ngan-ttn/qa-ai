# Testcase Quality Review Workflow

## Purpose

The `testcase-quality-review` workflow defines the process for evaluating and improving existing test artifacts.

This workflow guides the AI assistant in reviewing testcase quality by applying relevant QA skills, standards, and validation resources.

The workflow focuses on the review process, not on storing testcase design knowledge or defining review criteria in detail.

---

## When To Use

This workflow should be used when:

* Existing test cases need quality evaluation
* Test coverage needs to be reviewed before execution
* Requirements changes require existing test cases to be assessed
* Test artifacts need improvement before being reused
* QA teams need a structured review process

This workflow should not be used for:

* Creating new test cases from requirements
* Executing test cases
* Analyzing regression scope
* Reviewing automation code

---

## Input

The workflow requires existing QA artifacts as input.

### Required Input

Examples:

* Existing test cases
* Existing test scenarios

### Optional Input

Examples:

* Requirement documents
* User stories
* Acceptance criteria
* Business rules
* Previous review results
* Related QA documents

The workflow should identify missing information or unclear review scope before performing the review.

---

## Workflow Steps

The workflow follows these execution steps:

### Step 1: Understand Review Scope

Analyze the provided test artifacts and available context.

Identify:

* Review objectives
* Related features
* Applicable requirements
* Expected review scope

---

### Step 2: Analyze Test Coverage

Evaluate whether existing test artifacts sufficiently represent the intended testing scope.

Consider:

* Feature coverage
* Scenario coverage
* Business rule coverage
* Missing validation areas

---

### Step 3: Review Testcase Quality

Review the test artifacts using applicable QA standards and practices.

Consider:

* Clarity
* Consistency
* Completeness
* Maintainability

---

### Step 4: Identify Gaps and Improvements

Identify areas that may require improvement.

Examples:

* Missing scenarios
* Unclear information
* Incomplete coverage
* Potential duplication

---

### Step 5: Generate Review Result

Produce review outcomes based on identified findings.

The review result should provide actionable information for improving the test artifacts.

---

### Step 6: Validate Review Findings

Ensure review results are:

* Relevant to the provided input
* Clearly explained
* Traceable to identified issues
* Consistent with applicable QA standards

---

## Required Skills

This workflow may require the following skills:

| Skill                         | Purpose                                               |
| ----------------------------- | ----------------------------------------------------- |
| `skills/requirement-analysis` | Understand requirement context during testcase review |
| `skills/test-design`          | Evaluate scenario and coverage quality                |
| `skills/testing-fundamentals` | Apply general testing principles during review        |

The workflow references these skills but does not contain their detailed knowledge.

---

## Required Resources

This workflow may use resources from the shared directory.

| Resource                  | Purpose                                  |
| ------------------------- | ---------------------------------------- |
| `shared/standards/`       | Provide QA standards and review guidance |
| `shared/templates/`       | Provide review output structures         |
| `shared/checklists/`      | Provide validation criteria              |
| `shared/prompt-patterns/` | Provide reusable instruction patterns    |

The workflow applies these resources but does not redefine them.

---

## Output

The expected outputs of this workflow include:

* Testcase review findings
* Coverage improvement suggestions
* Quality assessment results

Output formats should follow applicable templates defined in shared resources.

---

## Validation

The workflow output should be validated to ensure:

* Findings are based on provided test artifacts
* Identified issues are actionable
* Improvement suggestions are relevant
* Review results follow applicable QA standards
* Output structure follows defined templates

Detailed validation criteria should be maintained in the relevant shared checklists.
