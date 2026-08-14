# Software Testing Life Cycle (STLC)

> Version: 1.0.0  
> Status: Draft  
> Last Updated: 2026-08-14

## Overview

The **Software Testing Life Cycle (STLC)** is a structured lifecycle for organizing software testing activities from requirement analysis through test closure.

STLC provides a systematic view of how testing activities are analyzed, planned, designed, prepared, executed, evaluated, and completed.

A generalized STLC can be represented as:

```text
Requirement Analysis
        │
        ▼
Test Planning
        │
        ▼
Test Design
        │
        ▼
Environment & Data Preparation
        │
        ▼
Test Execution
        │
        ▼
Defect Handling
        │
        ▼
Retesting & Regression
        │
        ▼
Test Closure
```

STLC is narrower than the Software Development Life Cycle (SDLC).

SDLC describes the broader lifecycle of creating, delivering, operating, and maintaining software, while STLC focuses specifically on testing activities within and across that lifecycle.

The exact STLC phases, names, sequence, responsibilities, artifacts, and criteria may vary across organizations and development models.

STLC should therefore be understood as a testing lifecycle concept rather than one mandatory testing process.

---

## Purpose

The purpose of STLC is to provide a structured understanding of how testing activities connect throughout software development.

STLC helps QA practitioners:

- understand that testing begins before test execution;
- identify testing needs from requirements;
- identify risks, assumptions, and dependencies early;
- define testing scope and objectives;
- design appropriate test coverage;
- prepare required environments and test data;
- execute tests systematically;
- evaluate actual behavior against expected behavior;
- investigate and verify defects;
- evaluate regression impact after changes;
- assess testing coverage and remaining risk;
- determine when testing activities are sufficiently complete;
- preserve reusable testing knowledge and artifacts.

Within QA-AI, STLC knowledge supports:

- requirement analysis;
- business-rule extraction;
- risk analysis;
- scenario generation;
- testcase generation;
- coverage review;
- regression analysis;
- defect-related reasoning;
- test-data preparation.

STLC knowledge should guide testing-lifecycle reasoning without assuming that every project follows the same phases, gates, artifacts, responsibilities, or completion criteria.

---

## Core Concepts

### Lifecycle Perspective

Software testing is not a single activity performed after development.

It is a lifecycle involving multiple connected activities.

```text
Understand
    │
    ▼
Plan
    │
    ▼
Design
    │
    ▼
Prepare
    │
    ▼
Execute
    │
    ▼
Evaluate
    │
    ▼
Close
```

Activities may overlap, repeat, or return to earlier stages when new information becomes available.

For example:

```text
Test Execution
      │
      ▼
Requirement Gap Found
      │
      ▼
Requirement Clarification
      │
      ▼
Test Design Updated
      │
      ▼
Continue Testing
```

STLC therefore provides structure without requiring a strictly one-directional process.

---

### Requirement Analysis

Requirement Analysis establishes what needs to be understood before meaningful test coverage can be designed.

Typical concerns include:

- expected behavior;
- actors and user flows;
- business rules;
- acceptance criteria;
- validations;
- constraints;
- dependencies;
- assumptions;
- ambiguities;
- missing information;
- testability;
- initial quality risks.

QA may use requirement analysis to determine:

- what behavior requires verification;
- which conditions influence behavior;
- which information requires clarification;
- which areas may require deeper testing;
- which dependencies affect testing;
- which risks should influence test priorities.

A generalized flow is:

```text
Requirement
     │
     ▼
Understand Expected Behavior
     │
     ▼
Identify Rules & Conditions
     │
     ▼
Identify Gaps & Risks
     │
     ▼
Prepare for Test Planning
```

Detailed requirement-analysis practices belong to `Requirement-Analysis.md`.

---

### Test Planning

Test Planning establishes how testing will be organized for the relevant scope.

Typical concerns include:

- testing objectives;
- scope;
- in-scope areas;
- out-of-scope areas;
- test levels;
- test types;
- testing priorities;
- risks;
- resources;
- roles and responsibilities;
- dependencies;
- environment needs;
- test-data needs;
- schedule;
- reporting;
- entry considerations;
- exit considerations.

Planning may be lightweight or formal depending on:

- product risk;
- project complexity;
- release size;
- regulatory requirements;
- team structure;
- delivery methodology.

STLC does not require one universal test-plan format or approval process.

Detailed planning practices belong to `Test-Planning.md`.

---

### Test Design

Test Design transforms testing inputs into structured test coverage.

Typical activities include:

- identifying test conditions;
- creating test scenarios;
- creating test cases;
- identifying positive behavior;
- identifying negative behavior;
- identifying boundary conditions;
- identifying decision combinations;
- identifying state transitions;
- identifying exception paths;
- identifying role-based behavior;
- identifying required test data;
- reviewing coverage.

Testing techniques may support test design.

Examples include:

- Equivalence Partitioning;
- Boundary Value Analysis;
- Decision Table Testing;
- State Transition Testing;
- Cause-Effect Graphing;
- Use Case Testing.

Conceptually:

```text
Requirement
     │
     ▼
Business Rules
     │
     ▼
Test Conditions
     │
     ▼
Test Scenarios
     │
     ▼
Test Cases
```

The objective is meaningful coverage of relevant behavior rather than simply producing a large number of test cases.

---

### Environment and Data Preparation

Testing requires suitable execution conditions before reliable results can be produced.

Environment preparation may involve:

- application availability;
- application configuration;
- service availability;
- integration configuration;
- database readiness;
- supported browsers;
- supported devices;
- network conditions;
- required permissions;
- external dependencies.

Test-data preparation may involve:

- user accounts;
- roles;
- permissions;
- valid data;
- invalid data;
- boundary data;
- historical data;
- required business states;
- integration data.

A generalized preparation flow is:

```text
Test Scenario
      │
      ▼
Identify Required State
      │
      ▼
Prepare Environment
      │
      ▼
Prepare Test Data
      │
      ▼
Validate Readiness
      │
      ▼
Execute
```

Environment and data problems may produce misleading failures unrelated to product behavior.

---

### Test Execution

Test Execution evaluates actual software behavior against expected behavior.

A generalized execution flow is:

```text
Test Condition
      │
      ▼
Execute
      │
      ▼
Observe Actual Result
      │
      ▼
Compare with Expected Result
      │
      ▼
Record Outcome
```

Execution may include:

- manual testing;
- automated testing;
- functional testing;
- integration testing;
- API testing;
- database validation;
- exploratory testing;
- compatibility testing;
- non-functional testing where applicable.

Common execution outcomes may include:

- Passed;
- Failed;
- Blocked;
- Not Run.

Actual status definitions depend on the project's testing process.

Execution provides evidence about observed software behavior.

A failed test does not automatically prove that the software contains a defect.

Possible causes may include:

- product behavior;
- incorrect test data;
- environment problems;
- dependency failures;
- requirement ambiguity;
- incorrect assumptions;
- incorrect test design.

---

### Defect Handling

Unexpected behavior discovered during testing may require investigation and defect reporting.

A generalized flow is:

```text
Unexpected Behavior
        │
        ▼
Investigation
        │
        ▼
Confirm Deviation
        │
        ▼
Defect Reporting
        │
        ▼
Analysis
        │
        ▼
Resolution
```

Defect handling may involve:

- reproducing the issue;
- comparing actual and expected behavior;
- collecting evidence;
- identifying affected conditions;
- assessing severity and priority;
- tracking resolution;
- communicating status.

Detailed defect states and transitions belong to `Defect-Lifecycle.md`.

Detailed defect-reporting practices belong to `Defect-Reporting.md`.

---

### Retesting

Retesting evaluates whether a specific previously reported defect has been corrected.

Conceptually:

```text
Defect
   │
   ▼
Fix
   │
   ▼
Retest Failed Condition
   │
   ▼
Verify Result
   │
   ├── Pass
   │
   └── Reopen
```

Retesting focuses on the behavior associated with the reported defect.

It does not by itself determine whether the change has affected other existing functionality.

---

### Regression Testing

Regression Testing evaluates whether a software change has negatively affected existing behavior.

Regression may be triggered by:

- defect fixes;
- new functionality;
- requirement changes;
- refactoring;
- configuration changes;
- integration changes;
- infrastructure changes;
- dependency changes.

A generalized regression flow is:

```text
Change
   │
   ▼
Impact Analysis
   │
   ▼
Identify Affected Areas
   │
   ▼
Determine Regression Scope
   │
   ▼
Execute Regression
   │
   ▼
Evaluate Results
```

Regression scope should be based on relevant impact and risk.

Factors may include:

- changed functionality;
- dependent functionality;
- business criticality;
- technical dependencies;
- integration impact;
- historical defects;
- previous regression failures.

STLC does not imply that every change requires execution of every existing test.

---

### Test Closure

Test Closure evaluates the completed testing cycle and preserves relevant testing outcomes.

Typical concerns include:

- execution status;
- achieved coverage;
- unresolved defects;
- blocked tests;
- untested areas;
- remaining risks;
- applicable exit criteria;
- testing summary;
- reusable test assets;
- lessons learned.

Conceptually:

```text
Testing Evidence
      │
      ▼
Coverage Review
      │
      ▼
Defect & Risk Review
      │
      ▼
Completion Assessment
      │
      ▼
Test Closure
```

Test closure does not mean that the software is defect-free.

It represents a testing completion point based on available evidence and the applicable project context.

Detailed closure practices belong to `Test-Closure.md`.

---

### Entry and Exit Criteria

Entry and exit criteria may be used to control when testing activities begin and when they are considered sufficiently complete.

Possible entry considerations include:

- requirement availability;
- requirement stability;
- build availability;
- environment readiness;
- test-data readiness;
- account availability;
- dependency availability.

Possible exit considerations include:

- planned coverage;
- execution status;
- unresolved defect status;
- remaining risk;
- required testing evidence;
- agreed quality criteria.

The exact criteria are project-specific.

STLC knowledge should not invent mandatory entry or exit criteria when authoritative project information is unavailable.

---

### Traceability

Traceability connects testing information throughout the lifecycle.

A generalized relationship may be:

```text
Requirement
     │
     ▼
Business Rule
     │
     ▼
Test Scenario
     │
     ▼
Test Case
     │
     ▼
Test Result
     │
     ▼
Defect
```

Traceability can support:

- coverage analysis;
- requirement-change analysis;
- regression analysis;
- defect investigation;
- testing-status reporting.

Traceability helps answer questions such as:

- Which requirements have been tested?
- Which business rules have test coverage?
- Which tests are affected by a requirement change?
- Which defects relate to a specific requirement?
- Which requirements still have missing coverage?

The required level of traceability depends on project context.

---

### STLC vs SDLC

STLC and SDLC describe related but different lifecycle perspectives.

| Aspect | SDLC | STLC |
|---|---|---|
| Scope | Entire software lifecycle | Testing lifecycle |
| Primary Objective | Create, deliver, operate, and maintain software | Organize and perform testing activities |
| Includes Development | Yes | No |
| Includes Testing | Yes | Core focus |
| Includes Deployment | Yes | Testing may support deployment validation |
| Includes Operation | Yes | Testing may use operational feedback |

Conceptually:

```text
SDLC
│
├── Planning
├── Requirements
├── Design
├── Development
├── Testing
│      └── STLC Activities
├── Deployment
└── Operation & Maintenance
```

STLC operates within or alongside the broader SDLC.

Detailed lifecycle context belongs to `SDLC.md`.

---

### Shift-Left Testing

Shift-left testing introduces testing and quality activities earlier in the software lifecycle.

Examples include:

- requirement review;
- acceptance-criteria review;
- early risk analysis;
- early test design;
- design review;
- API-contract review;
- static testing.

Conceptually:

```text
Requirement
     │
     ▼
Early QA Analysis
     │
     ▼
Test Design
     │
     ▼
Development
     │
     ▼
Executable Testing
```

Potential benefits include:

- earlier defect detection;
- reduced rework;
- improved requirement quality;
- improved testability;
- faster feedback.

Shift-left does not mean moving every testing activity to the beginning of the lifecycle.

---

### Shift-Right Testing

Shift-right testing continues quality evaluation after deployment.

Examples may include:

- production verification;
- monitoring;
- observability;
- real-user monitoring;
- incident analysis;
- user feedback;
- operational metrics.

Conceptually:

```text
Testing
   │
   ▼
Deployment
   │
   ▼
Production Observation
   │
   ▼
Feedback
   │
   └────────────► Future Testing
```

Operational evidence may improve:

- future risk analysis;
- regression coverage;
- test-data design;
- scenario design;
- quality decisions.

Shift-right complements pre-production testing rather than replacing it.

---

## How It Works

STLC works as a connected lifecycle rather than a set of completely isolated phases.

A generalized flow is:

```text
Requirement
      │
      ▼
Analyze Testing Needs
      │
      ▼
Identify Risks
      │
      ▼
Plan Testing
      │
      ▼
Design Coverage
      │
      ▼
Prepare Environment & Data
      │
      ▼
Execute Tests
      │
      ▼
Evaluate Results
      │
      ▼
Handle Defects
      │
      ▼
Retest & Regress
      │
      ▼
Evaluate Coverage & Risk
      │
      ▼
Close Testing
```

The lifecycle is often iterative.

### Requirement Feedback

Test design may reveal missing or ambiguous requirements.

```text
Test Design
     │
     ▼
Missing Business Rule Found
     │
     ▼
Requirement Clarification
     │
     ▼
Test Design Updated
```

### Execution Feedback

Execution may reveal defects or new testing risks.

```text
Test Execution
     │
     ▼
Unexpected Behavior
     │
     ▼
Investigation
     │
     ▼
Fix
     │
     ▼
Retesting & Regression
```

### Change Feedback

Requirement or implementation changes may affect existing coverage.

```text
Change
   │
   ▼
Impact Analysis
   │
   ▼
Coverage Update
   │
   ▼
Regression Scope Update
```

### Operational Feedback

Production information may influence future testing.

```text
Production Issue
      │
      ▼
Root Cause
      │
      ▼
Coverage Gap
      │
      ▼
Scenario Improvement
      │
      ▼
Future Regression
```

STLC reasoning therefore helps QA understand both **which testing activity is being performed** and **how information moves between testing activities**.

---

## When to Use

STLC knowledge is useful whenever QA needs to reason about testing beyond isolated test execution.

### Requirement Analysis

Use STLC understanding to identify how requirement quality affects downstream planning, design, preparation, and execution.

### Test Planning

Use lifecycle context to identify:

- testing scope;
- risks;
- priorities;
- dependencies;
- environment needs;
- test-data needs;
- execution considerations.

### Test Design

Use STLC relationships to connect:

```text
Requirement
→ Business Rule
→ Risk
→ Scenario
→ Test Case
→ Test Data
```

### Test Preparation

Use lifecycle knowledge to identify environment, data, account, permission, and integration dependencies before execution.

### Test Execution

Use lifecycle context to distinguish product failures from:

- environment issues;
- data issues;
- dependency failures;
- requirement problems;
- test-design problems.

### Defect Verification

Use STLC knowledge to distinguish retesting of a specific defect from broader regression evaluation.

### Regression Analysis

Use lifecycle relationships to identify how changes may affect existing behavior and coverage.

### Test Closure

Use accumulated testing evidence to evaluate:

- coverage;
- execution status;
- unresolved defects;
- blocked areas;
- remaining risks;
- testing completion.

---

## When Not to Use

STLC knowledge should not be used to impose one universal testing process.

Do not assume:

- every project uses the same STLC phases;
- every phase requires a separate document;
- every phase has mandatory entry and exit gates;
- testing is always sequential;
- test execution begins only after development is complete;
- every defect fix requires full regression;
- every project requires formal test closure;
- QA owns every testing-related decision;
- generic STLC guidance defines project responsibilities.

Avoid:

```text
Generic STLC Model
        │
        ✗
        ▼
Assume Project Process
```

Instead:

```text
Generic STLC Knowledge
        │
        ▼
Understand Testing Activities
        │
        ▼
Check Actual Project Process
```

Project-specific phases, responsibilities, artifacts, status values, gates, and workflows must come from authoritative project information.

---

## Advantages

STLC provides several benefits when applied appropriately.

### Earlier Testing Awareness

Testing activities can begin before executable software exists.

This allows QA to identify:

- requirement ambiguity;
- missing business rules;
- testability problems;
- dependencies;
- testing risks.

### Better Test Organization

Testing activities are connected from requirement understanding through execution and closure.

### Better Coverage

Structured analysis and design help reduce missing or duplicated coverage.

### Better Traceability

Testing artifacts can be connected to:

```text
Requirements
→ Business Rules
→ Scenarios
→ Test Cases
→ Results
→ Defects
```

### Better Risk Management

Risks can influence:

- planning;
- test priorities;
- test design;
- execution order;
- regression scope.

### Better Test Preparation

Environment and data requirements can be identified before execution becomes blocked.

### Better Defect Verification

STLC helps distinguish:

- failure investigation;
- defect reporting;
- retesting;
- regression testing.

### Better Testing Feedback

Execution, defect, and production findings can improve future analysis and coverage.

### Better Completion Assessment

Testing evidence can be evaluated systematically when determining whether a testing cycle is sufficiently complete.

---

## Limitations

STLC knowledge also has limitations.

### STLC Implementations Differ

Organizations may use different:

- phase names;
- activities;
- responsibilities;
- artifacts;
- gates;
- completion criteria.

### Activities May Overlap

In Agile and continuous-delivery environments, analysis, design, execution, and regression may occur continuously.

### Generic STLC Does Not Define Governance

STLC knowledge does not define:

- mandatory approvals;
- release gates;
- required documents;
- project roles;
- exact entry criteria;
- exact exit criteria;
- defect thresholds.

### Process Does Not Guarantee Coverage

Following STLC activities does not guarantee that test design or execution is effective.

### Testing Cannot Prove Defect Absence

Successful completion of testing does not demonstrate that no defects remain.

### Artifacts Require Maintenance

Requirements, scenarios, test cases, data, and traceability may become outdated when software changes.

### STLC Does Not Replace SDLC

STLC provides the testing lifecycle but does not define the broader software-development lifecycle.

---

## Examples

### Example 1 — Login Feature

A requirement defines login using an email address and password.

Testing activities may progress as:

```text
Requirement
     │
     ▼
Analyze Login Rules
     │
     ▼
Identify Authentication Risks
     │
     ▼
Design Login Scenarios
     │
     ▼
Prepare Accounts & Data
     │
     ▼
Execute Tests
     │
     ▼
Evaluate Results
```

Potential scenarios may include:

- valid login;
- invalid password;
- unknown account;
- required-field validation;
- account-state behavior.

The exact coverage depends on the supplied requirements and project context.

---

### Example 2 — Defect Fix

A defect causes an incorrect checkout total.

```text
Defect Reported
      │
      ▼
Fix Implemented
      │
      ▼
Retest Original Failure
      │
      ▼
Analyze Change Impact
      │
      ▼
Regression Testing
```

Retesting answers:

> Has the original defect been corrected?

Regression testing answers:

> Has the change negatively affected related existing behavior?

---

### Example 3 — Requirement Change

A business rule changes after testing has started.

```text
Business Rule Change
        │
        ▼
Requirement Impact
        │
        ▼
Scenario Impact
        │
        ▼
Testcase Impact
        │
        ▼
Test Data Impact
        │
        ▼
Regression Impact
```

STLC reasoning helps QA propagate the change through downstream testing activities.

---

### Example 4 — Agile Iteration

An Agile iteration may involve:

```text
Story Refinement
      │
      ▼
QA Analysis
      │
      ▼
Test Design
      │
      ▼
Development
      │
      ▼
Continuous Testing
      │
      ▼
Defect Retesting
      │
      ▼
Regression
      │
      ▼
Feedback
```

The testing lifecycle still exists even though activities overlap and repeat.

---

### Example 5 — Production Feedback

A defect is discovered after release.

```text
Production Defect
      │
      ▼
Investigation
      │
      ▼
Root Cause
      │
      ▼
Missing Test Coverage Identified
      │
      ▼
Scenario Added
      │
      ▼
Regression Suite Improved
```

This demonstrates how later lifecycle feedback can improve future testing activities.

---

## Common Mistakes

### Treating STLC as a Strict Sequential Process

A common mistake is assuming that every STLC phase must be completed permanently before the next phase begins.

```text
Requirement Analysis
        ↓
Test Planning
        ↓
Test Design
        ↓
Test Execution
```

This representation is useful for understanding the lifecycle, but real testing activities may overlap and repeat.

For example:

```text
Test Execution
      │
      ▼
Requirement Gap Found
      │
      ▼
Requirement Clarification
      │
      ▼
Test Design Updated
      │
      ▼
Continue Testing
```

STLC should provide structure without preventing iteration.

### Starting Testing Only After Development

Testing should not be interpreted as an activity that begins only when executable software becomes available.

Waiting until development is complete may delay discovery of:

- ambiguous requirements;
- missing business rules;
- testability problems;
- environment dependencies;
- test-data requirements;
- integration risks.

### Treating Test Execution as the Entire STLC

Test execution is only one part of the testing lifecycle.

```text
Analysis
→ Planning
→ Design
→ Preparation
→ Execution
→ Evaluation
→ Closure
```

Focusing only on execution may result in weak preparation and incomplete coverage.

### Applying the Same STLC Process to Every Project

STLC is a lifecycle concept, not one mandatory project process.

Projects may differ in:

- methodology;
- product risk;
- team structure;
- release frequency;
- regulatory requirements;
- documentation needs;
- automation maturity.

The lifecycle should be adapted to the actual project context.

### Confusing Retesting with Regression Testing

Retesting and regression testing have different objectives.

```text
Retesting
→ Verify that the specific defect has been corrected

Regression Testing
→ Evaluate whether the change affected existing behavior
```

A defect fix may require both activities.

### Assuming a Failed Test Always Means a Product Defect

A failed test result requires investigation.

Possible causes include:

- product defect;
- incorrect test data;
- environment problem;
- dependency failure;
- requirement ambiguity;
- incorrect test assumption;
- incorrect test case.

The cause should be understood before the result is classified as a product defect.

### Running Full Regression for Every Change

STLC does not imply that every change requires the entire regression suite.

Regression scope should consider:

- changed functionality;
- dependent functionality;
- business impact;
- technical dependencies;
- integration impact;
- historical defects;
- failure risk.

Change-impact and risk analysis should guide regression selection.

### Treating Exit Criteria as Proof of Quality

Meeting exit criteria does not prove that:

```text
All Defects Have Been Found
```

Exit criteria indicate that agreed testing conditions have been satisfied.

Residual risk may still remain.

### Ignoring Requirement Changes During Testing

Requirements may change after test design or execution has started.

A change should trigger appropriate impact analysis:

```text
Requirement Change
        │
        ▼
Business Rule Impact
        │
        ▼
Scenario Impact
        │
        ▼
Testcase Impact
        │
        ▼
Regression Impact
```

Failing to propagate changes can leave testing artifacts inconsistent with the current requirement.

### Creating Process Artifacts Without Testing Value

STLC should not become a documentation exercise.

Artifacts should support purposes such as:

- testing decisions;
- traceability;
- execution;
- communication;
- coverage evaluation;
- risk management.

Documentation that provides no meaningful testing value should not be created solely because a generic STLC model suggests it.

---

## Best Practices

### Start Testing Early

Begin QA activities during requirement analysis rather than waiting for implementation to finish.

Early involvement helps identify:

- requirement gaps;
- ambiguous behavior;
- testability issues;
- dependencies;
- quality risks.

### Understand the Actual Project Process

Use generic STLC knowledge as a foundation.

Use authoritative project information to determine:

- actual phases;
- responsibilities;
- workflows;
- gates;
- artifacts;
- criteria.

### Keep Testing Risk-Based

Prioritize testing according to factors such as:

- business impact;
- failure probability;
- technical complexity;
- integration complexity;
- security sensitivity;
- regulatory impact;
- historical defects.

### Maintain Useful Traceability

Where appropriate, preserve relationships between:

```text
Requirement
→ Business Rule
→ Scenario
→ Test Case
→ Test Result
→ Defect
```

Traceability should provide testing value rather than administrative overhead.

### Prepare Environment and Data Early

Identify environment, account, permission, integration, and data needs during planning and design.

Do not wait until execution begins.

### Review Coverage Continuously

Coverage should be reviewed during:

- requirement analysis;
- test design;
- execution;
- requirement changes;
- defect analysis;
- regression planning.

### Separate Retesting and Regression

Use:

```text
Retesting
→ Did the specific fix work?

Regression Testing
→ Did the change affect existing behavior?
```

Both may be required after a change.

### Update Testing Artifacts After Changes

When requirements or implementation change, review downstream impact on:

- business rules;
- risks;
- scenarios;
- test cases;
- test data;
- regression scope.

### Preserve Remaining Risk

Testing completion should preserve information about:

- untested areas;
- blocked tests;
- unresolved defects;
- accepted limitations;
- environment constraints;
- residual risks.

### Keep Testing Artifacts Maintainable

Create and maintain artifacts that support:

- reasoning;
- execution;
- traceability;
- communication;
- reuse;
- quality decisions.

For QA-AI:

- use STLC knowledge to understand relationships between testing activities;
- distinguish generic testing guidance from project-specific facts;
- do not invent mandatory phases, gates, artifacts, or responsibilities;
- do not infer entry or exit criteria without evidence;
- preserve requirement and business-rule traceability;
- use change impact and risk to guide regression reasoning;
- propagate authoritative requirement changes to downstream artifacts;
- keep generated outputs aligned with available evidence.

---

## Related Knowledge

### Software Development Life Cycle

`SDLC.md` provides the broader software lifecycle within which STLC operates.

### Requirement Analysis

`Requirement-Analysis.md` provides deeper guidance for understanding, structuring, and validating testing-relevant requirements.

### Requirement Review

`Requirement-Review.md` focuses on evaluating requirement quality, completeness, consistency, clarity, and testability.

### Test Planning

`Test-Planning.md` describes how testing objectives, scope, risks, resources, dependencies, and execution considerations are organized.

### Test Strategy

`Test-Strategy.md` describes the higher-level testing approach used to guide testing decisions.

### Test Estimation

`Test-Estimation.md` addresses estimation of testing effort, scope, complexity, and related factors.

### Test Monitoring and Control

`Test-Monitoring-and-Control.md` addresses how testing progress, results, risks, and corrective actions are monitored during testing.

### Defect Lifecycle

`Defect-Lifecycle.md` describes how defects progress through reporting, analysis, resolution, verification, and closure.

### Defect Reporting

`Defect-Reporting.md` provides guidance for communicating defects clearly and reproducibly.

### Test Closure

`Test-Closure.md` provides deeper guidance for evaluating testing completion, remaining risks, and final testing outcomes.

### Verification and Validation

`Verification-and-Validation.md` explains complementary quality perspectives used to evaluate whether software is built correctly and whether it satisfies intended needs.

---

## References

This article is conceptually aligned with established software testing guidance, including:

- ISO/IEC/IEEE 29119 — Software testing processes.
- ISTQB Certified Tester Foundation Level syllabus — fundamental test process and software testing lifecycle concepts.

Specific organizations may implement testing lifecycles differently.

Project-specific STLC phases, responsibilities, artifacts, entry criteria, exit criteria, quality gates, defect thresholds, and workflows must come from authoritative project documentation.