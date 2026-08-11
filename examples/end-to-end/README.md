# End-to-End Examples

## Purpose

The `end-to-end` examples demonstrate how QA-AI transforms a requirement into a connected set of QA artifacts by applying the repository's skills, workflows, shared resources, and framework rules.

Unlike standalone examples, which demonstrate one capability at a time, an end-to-end example demonstrates how multiple QA capabilities and supporting analysis activities work together across a complete requirement-driven QA flow.

The primary objective is to demonstrate:

```text
Requirement
    ↓
QA-AI
    ↓
Structured QA Artifacts
```

The example is reference and validation material for the repository. It is not a runtime dependency and must not redefine framework behavior.

---

## Scope

The end-to-end example starts with a single requirement document.

From that requirement, QA-AI produces the following artifacts:

```text
Requirement-Analysis.md
Business-Rules.md
Risk-Analysis.md
Test-Scenarios.md
Test-Cases.md
Coverage-Review.md
Regression-Analysis.md
Test-Data.md
```

Each artifact has a specific responsibility and must remain within the boundary of the capability or supporting analysis activity that produces it.

The example does not demonstrate bug-report review because that activity requires an existing bug report as its primary input rather than being naturally generated from a requirement.

---

## Directory Structure

```text
end-to-end/
├── README.md
│
├── input/
│   └── Sample-Requirement.md
│
└── expected-output/
    ├── Requirement-Analysis.md
    ├── Business-Rules.md
    ├── Risk-Analysis.md
    ├── Test-Scenarios.md
    ├── Test-Cases.md
    ├── Coverage-Review.md
    ├── Regression-Analysis.md
    └── Test-Data.md
```

---

## Input

The primary input is:

```text
input/Sample-Requirement.md
```

The requirement represents the source information available to the QA-AI execution.

The end-to-end example intentionally starts from the requirement without silently introducing undocumented system behavior.

If an artifact requires information that cannot be established from the supplied requirement or valid upstream artifacts, the output must identify the missing context instead of inventing it.

---

## End-to-End Flow

The logical artifact flow is:

```text
Sample-Requirement.md
        │
        ▼
Requirement-Analysis.md
        │
        ├──────────────► Business-Rules.md
        │
        └──────────────► Risk-Analysis.md
                              │
                              ▼
                      Test-Scenarios.md
                              │
                              ▼
                        Test-Cases.md
                              │
                              ▼
                      Coverage-Review.md
                              │
                              ├────────────► Regression-Analysis.md
                              │
                              └────────────► Test-Data.md
```

This diagram represents the primary logical dependency chain used by this example.

The critical quality-review dependency is:

```text
Test-Scenarios.md
        ↓
Test-Cases.md
        ↓
Coverage-Review.md
```

Coverage review occurs after test case generation because the current `coverage-reviewer` contract evaluates a structured test case model and produces a structured coverage assessment.

A workflow or supported framework composition may also assemble the original requirement together with relevant upstream artifacts according to the input contract of each participating capability.

---

## Artifact Responsibilities

### Requirement Analysis

`Requirement-Analysis.md` structures and interprets the supplied requirement.

It may identify:

- Feature purpose
- Actors
- User flows
- Functional behavior
- Requirement gaps
- Assumptions
- Clarification questions

It must not generate detailed test cases.

---

### Business Rules

`Business-Rules.md` extracts explicit and safely derivable business rules from the requirement analysis.

It should distinguish between:

```text
Explicit Rule
Derived Rule
Undefined Behavior
```

Undefined behavior must not be converted into an assumed business rule.

---

### Risk Analysis

`Risk-Analysis.md` identifies and prioritizes risks associated with the requirement.

It may analyze areas such as:

- Business-critical behavior
- State transitions
- Boundaries
- Failure impact
- Requirement ambiguity

Risk analysis identifies testing focus but does not replace test scenarios.

`Risk-Analysis.md` is part of this end-to-end reference artifact set, but the current core `skills/` module does not define a dedicated risk-analysis skill contract. The example must therefore not claim a non-existent skill mapping.

---

### Test Scenarios

`Test-Scenarios.md` converts structured business behavior and relevant testing focus into structured testing objectives.

Scenarios may provide coverage such as:

- Positive
- Negative
- Boundary
- State transition
- Isolation
- End-to-end behavior

A scenario defines **what to verify**, not detailed execution steps.

Within the core skill pipeline, this artifact corresponds to `skills/scenario-generator`.

---

### Test Cases

`Test-Cases.md` converts structured test scenarios into executable test cases.

Test cases should contain sufficient information to execute and verify the intended behavior without unnecessary interpretation.

Typical information includes:

- Test Case ID
- Module
- Test Title
- Preconditions
- Test Steps
- Test Data
- Expected Result
- Priority
- Status

Each focused test case should have one primary testing objective.

Within the core skill pipeline, this artifact corresponds to `skills/testcase-generator`.

---

### Coverage Review

`Coverage-Review.md` evaluates the generated structured test case model.

The review should assess:

- Completeness
- Consistency
- Traceability
- Coverage gaps
- Duplicate or conflicting test cases
- Open questions or review limitations

Where upstream artifacts are available, coverage review should trace test cases back to test scenarios, business rules, and requirement analysis.

Clarification-dependent behavior must remain separate from confirmed coverage gaps.

Within the core skill pipeline, this artifact corresponds to `skills/coverage-reviewer`.

Coverage review does not generate or modify test cases. It assesses the testcase set after generation.

---

### Regression Analysis

`Regression-Analysis.md` evaluates regression impact and identifies an appropriate regression scope from the validated QA artifacts and available change information.

In this end-to-end example, only the requirement is provided as source system information.

Therefore, regression analysis must distinguish between:

```text
Requirement-Derived Impact
Potential Regression Area
Unknown Dependency
Investigation Required
```

It must not invent existing architecture, services, databases, integrations, or dependencies that are not supported by the input.

Within the core skill pipeline, this artifact corresponds to `skills/regression-impact` and should consume the structured coverage assessment produced after testcase review.

---

### Test Data

`Test-Data.md` defines representative data and required logical system states needed to execute the generated testing coverage.

Test data may include:

- Valid inputs
- Invalid inputs
- Boundary values
- Account or entity states
- Time-based conditions
- Data-isolation requirements
- Reusable scenario data sets

The artifact should describe required logical states without inventing implementation-specific setup mechanisms.

`Test-Data.md` is part of this end-to-end reference artifact set, but the current core `skills/` module does not define a dedicated test-data-generation skill contract. The example must therefore not claim a non-existent skill mapping.

---

## Core Skill Mapping

The artifacts that map directly to the current core capability pipeline are:

| Artifact | Core Skill |
|---|---|
| Requirement-Analysis.md | `skills/requirement-analyzer` |
| Business-Rules.md | `skills/business-rule-extractor` |
| Test-Scenarios.md | `skills/scenario-generator` |
| Test-Cases.md | `skills/testcase-generator` |
| Coverage-Review.md | `skills/coverage-reviewer` |
| Regression-Analysis.md | `skills/regression-impact` |

The current core `skills/` module does not define dedicated skill contracts for `Risk-Analysis.md` or `Test-Data.md`.

Those artifacts remain part of this reference example because they are included in the repository's broader QA artifact model. Their presence must not be interpreted as evidence that a corresponding core skill currently exists.

---

## Artifact Consistency

All generated artifacts must remain consistent with the original requirement and with each other.

The principal traceability chain is:

```text
Requirement
    ↓
Business Rule
    ↓
Scenario
    ↓
Test Case
    ↓
Coverage Assessment
```

Risk analysis may influence testing focus, while regression analysis consumes validated coverage information for impact assessment.

A downstream artifact must not silently introduce behavior that contradicts or exceeds supported upstream information.

When information cannot be established, it should be represented as:

```text
Clarification Required
```

or:

```text
Investigation Required
```

depending on the artifact and context.

---

## Traceability

Traceability should be maintained throughout the generated artifact set.

Typical relationships include:

```text
Requirement
    ↓
Business Rule

Requirement
    ↓
Risk

Business Rule / Risk
    ↓
Test Scenario

Test Scenario
    ↓
Test Case

Test Case
    ↓
Coverage Review

Coverage Review
    ↓
Regression Analysis

Test Scenario / Test Case
    ↓
Test Data
```

Coverage review uses the available relationships to identify missing, inconsistent, insufficient, or duplicate testcase coverage.

Traceability must remain meaningful rather than being added only to increase the number of references.

---

## Handling Missing Information

QA-AI must not fabricate behavior when the requirement does not provide enough information.

Example:

```text
Requirement does not define concurrent behavior
        ↓
Do not invent concurrency semantics
        ↓
Identify clarification or investigation need
```

The same principle applies to:

- System architecture
- Database implementation
- APIs
- External integrations
- Existing production behavior
- Persistence mechanisms
- Background jobs
- Security policies
- Platform-specific behavior

Missing information should remain visible so that downstream QA work does not rely on unsupported assumptions.

---

## Execution Model

The end-to-end example represents expected QA-AI behavior rather than a provider-specific runtime implementation.

A compatible execution should conceptually:

1. Read `FRAMEWORK.md` as the framework entry point.
2. Resolve the applicable workflow or supported capability composition.
3. Load the required skills and their declared shared-resource dependencies.
4. Read the sample requirement input.
5. Generate and reuse valid upstream artifacts according to capability contracts.
6. Generate test cases before executing coverage review.
7. Use the structured coverage assessment as the required upstream artifact for regression impact analysis.
8. Review the complete artifact set for cross-artifact consistency.

Conceptually:

```text
FRAMEWORK.md
    +
workflows/
    +
skills/
    +
shared/
    +
Sample Requirement
        ↓
QA-AI Execution
        ↓
Reference QA Artifact Set
```

---

## Runtime and Reference Boundary

The default QA-AI runtime pack is based on:

```text
FRAMEWORK.md
manifest.json
shared/
skills/
workflows/
```

The `examples/` directory is reference and validation material outside that default runtime pack.

Therefore:

```text
Runtime Framework
    → FRAMEWORK.md + manifest.json + shared/ + skills/ + workflows/

Reference Validation
    → examples/
```

A compatible AI environment may load or package the runtime framework differently, but platform-specific mechanisms must not redefine QA-AI capability contracts, workflow ordering, or artifact responsibilities.

---

## Platform Independence

The example does not depend on a specific AI provider.

The same QA-AI behavior may be exercised in compatible environments such as ChatGPT, Claude, or other AI runtimes capable of consuming the framework assets.

Platform-specific packaging or import mechanisms may differ, but the core QA behavior is defined by the runtime framework components rather than by `examples/`.

The example therefore demonstrates expected output behavior and serves as development, learning, evaluation, and validation material.

---

## Expected Output

A successful end-to-end example should contain a coherent artifact set in:

```text
expected-output/
```

The artifacts should collectively demonstrate that QA-AI can transform a requirement into structured QA analysis and testing documentation while preserving artifact boundaries.

Success is not measured only by whether every file exists.

The output must also satisfy:

- Requirement fidelity
- Artifact responsibility boundaries
- Cross-artifact consistency
- Meaningful traceability
- Risk-based testing consideration
- Executable test design
- Testcase coverage assessment after testcase generation
- Explicit handling of missing information
- No fabricated business or system behavior

---

## End-to-End Review

After all expected outputs are generated, the complete artifact set should be reviewed together.

The final review should validate:

```text
Requirement
    ↓
Requirement Analysis consistency
    ↓
Business Rule consistency
    ↓
Risk identification
    ↓
Scenario coverage
    ↓
Test Case quality and traceability
    ↓
Coverage assessment
    ↓
Regression impact assumptions
    ↓
Test Data support
```

The review should also detect:

- Contradictions between artifacts
- Missing requirement coverage
- Unsupported assumptions
- Duplicate testing objectives
- Risks without appropriate testing consideration
- Test cases without scenario or requirement basis
- Coverage findings that do not reflect the generated test cases
- Test data that does not support execution
- Regression conclusions without sufficient evidence

---

## Example Completion Criteria

The end-to-end example is complete when:

- The sample requirement is available
- All expected artifacts are generated
- Each artifact follows its responsibility boundary
- Requirement traceability is preserved
- Confirmed behavior and undefined behavior remain distinguishable
- Test scenarios cover the defined requirement appropriately
- Test cases are generated from the approved scenario model
- Coverage review evaluates the generated testcase model
- Coverage findings are traceable and evidence-based
- Regression analysis uses the structured coverage assessment and does not invent system dependencies
- Test data supports the generated testing objectives
- Cross-artifact review passes

Only after these conditions are satisfied should the end-to-end example be considered frozen.