# End-to-End Examples

## Purpose

The `end-to-end` examples demonstrate how QA-AI transforms a requirement into a connected set of QA artifacts by applying the repository's skills, workflows, templates, standards, and shared knowledge.

Unlike standalone examples, which demonstrate one capability at a time, an end-to-end example demonstrates how multiple QA capabilities work together as a complete analysis and test-design flow.

The primary objective is to demonstrate:

```text
Requirement
    ↓
QA-AI
    ↓
Structured QA Artifacts
```

The example is designed to remain platform-independent so that the same QA-AI knowledge package can be used with supported AI environments such as ChatGPT or Claude.

---

## Scope

The end-to-end example starts with a single requirement document.

From that requirement, QA-AI produces the following artifacts:

```text
Requirement-Analysis.md
Business-Rules.md
Risk-Analysis.md
Test-Scenarios.md
Coverage-Review.md
Test-Cases.md
Regression-Analysis.md
Test-Data.md
```

Each artifact has a specific responsibility and must remain within the boundary of the capability that produces it.

The example does not demonstrate bug-report review because that capability requires an existing bug report as its primary input rather than being naturally generated from a requirement.

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
    ├── Coverage-Review.md
    ├── Test-Cases.md
    ├── Regression-Analysis.md
    └── Test-Data.md
```

---

## Input

The primary input is:

```text
input/Sample-Requirement.md
```

The requirement represents the source information available to the QA-AI workflow.

The end-to-end example intentionally starts from the requirement without silently introducing undocumented system behavior.

If an artifact requires information that cannot be derived from the supplied requirement, the output must identify the missing context instead of inventing it.

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
                      Coverage-Review.md
                              │
                              ▼
                        Test-Cases.md
                              │
                              ├────────────► Test-Data.md
                              │
                              └────────────► Regression-Analysis.md
```

This diagram represents logical information dependencies.

It does not require every capability to consume only the immediately preceding artifact.

A workflow may assemble the original requirement together with relevant upstream artifacts according to the input contract of each skill.

---

## Artifact Responsibilities

### Requirement Analysis

`Requirement-Analysis.md` structures and interprets the supplied requirement.

It may identify:

- Feature purpose.
- Actors.
- User flows.
- Functional behavior.
- Requirement gaps.
- Assumptions.
- Clarification questions.

It must not generate detailed test cases.

---

### Business Rules

`Business-Rules.md` extracts explicit and safely derivable business rules from the requirement.

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

It should analyze areas such as:

- Business-critical behavior.
- State transitions.
- Boundaries.
- Failure impact.
- Requirement ambiguity.

Risk analysis identifies testing focus but does not replace test scenarios.

---

### Test Scenarios

`Test-Scenarios.md` converts requirement-defined behavior and relevant risk areas into structured testing objectives.

Scenarios should provide appropriate coverage such as:

- Positive.
- Negative.
- Boundary.
- State transition.
- Isolation.
- End-to-end behavior.

A scenario defines **what to verify**, not detailed execution steps.

---

### Coverage Review

`Coverage-Review.md` evaluates whether the generated scenario set sufficiently covers the requirement.

The review should identify:

```text
Covered
Partial
Missing
Duplicate
Clarification-Dependent
```

Clarification-dependent behavior must remain separate from confirmed coverage gaps.

---

### Test Cases

`Test-Cases.md` converts approved testing objectives into executable test cases.

Test cases should contain sufficient information to execute and verify the intended behavior without unnecessary interpretation.

Typical information includes:

- Test Case ID.
- Module.
- Test Title.
- Preconditions.
- Test Steps.
- Test Data.
- Expected Result.
- Priority.
- Status.

Each test case should have one primary testing objective.

---

### Regression Analysis

`Regression-Analysis.md` evaluates potential regression impact caused by the requirement change.

In this end-to-end example, only the requirement is provided as source system information.

Therefore, regression analysis must distinguish between:

```text
Requirement-Derived Impact
Potential Regression Area
Unknown Dependency
Investigation Required
```

It must not invent existing architecture, services, databases, integrations, or dependencies that are not supported by the input.

---

### Test Data

`Test-Data.md` defines representative data and required logical system states needed to execute the generated testing coverage.

Test data may include:

- Valid inputs.
- Invalid inputs.
- Boundary values.
- Account or entity states.
- Time-based conditions.
- Data-isolation requirements.
- Reusable scenario data sets.

The artifact should describe required logical states without inventing implementation-specific setup mechanisms.

---

## Skill Mapping

The expected artifacts correspond to QA-AI capabilities as follows:

| Artifact | Primary Capability |
|---|---|
| Requirement-Analysis.md | requirement-analyzer |
| Business-Rules.md | business-rule-extractor |
| Risk-Analysis.md | risk-analyzer |
| Test-Scenarios.md | scenario-generator |
| Coverage-Review.md | coverage-reviewer |
| Test-Cases.md | testcase-generator |
| Regression-Analysis.md | regression-analyzer |
| Test-Data.md | test-data-generator |

The workflow coordinates these capabilities and supplies the relevant context required by each step.

---

## Artifact Consistency

All generated artifacts must remain consistent with the original requirement and with each other.

For example:

```text
Requirement
    ↓
Business Rule
    ↓
Risk
    ↓
Scenario
    ↓
Test Case
    ↓
Test Data
```

A downstream artifact must not silently introduce behavior that contradicts or exceeds the supported upstream information.

When new information cannot be established, it should be represented as:

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

Requirement / Risk
    ↓
Test Scenario

Test Scenario
    ↓
Test Case

Test Scenario / Test Case
    ↓
Test Data
```

Coverage review uses these relationships to identify missing, partial, or duplicate testing coverage.

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

- System architecture.
- Database implementation.
- APIs.
- External integrations.
- Existing production behavior.
- Persistence mechanisms.
- Background jobs.
- Security policies.
- Platform-specific behavior.

Missing information should remain visible so that downstream QA work does not rely on unsupported assumptions.

---

## Execution Model

The end-to-end example represents a logical QA workflow rather than a platform-specific implementation.

A compatible AI environment should:

1. Load the QA-AI instructions and relevant shared knowledge.
2. Read the requirement input.
3. Execute the required QA capabilities according to the workflow.
4. Pass relevant upstream artifacts into downstream steps.
5. Review generated artifacts for consistency and coverage.
6. Produce the final artifact set.

Conceptually:

```text
QA-AI Knowledge Package
        +
Sample Requirement
        ↓
Workflow Execution
        ↓
QA Artifact Set
```

---

## Platform Independence

The example does not depend on a specific AI provider.

The same conceptual package may be supplied to environments such as:

```text
ChatGPT
Claude
Other compatible AI environments
```

Platform-specific packaging or import mechanisms may differ, but the QA knowledge model remains based on the repository's:

```text
skills/
workflows/
shared/
templates/
knowledge/
examples/
```

The example therefore documents expected QA behavior rather than provider-specific runtime behavior.

---

## Expected Output

A successful end-to-end execution should produce a coherent artifact set in:

```text
expected-output/
```

The artifacts should collectively demonstrate that QA-AI can transform a requirement into structured QA analysis and testing documentation.

Success is not measured only by whether every file exists.

The output must also satisfy:

- Requirement fidelity.
- Artifact responsibility boundaries.
- Cross-artifact consistency.
- Meaningful traceability.
- Risk-based coverage.
- Executable test design.
- Explicit handling of missing information.
- No fabricated business behavior.

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
Coverage completeness
    ↓
Test Case traceability
    ↓
Test Data support
    ↓
Regression assumptions
```

The review should also detect:

- Contradictions between artifacts.
- Missing requirement coverage.
- Unsupported assumptions.
- Duplicate testing objectives.
- Risks without appropriate testing consideration.
- Test cases without scenario or requirement basis.
- Test data that does not support execution.
- Regression conclusions without sufficient evidence.

---

## Example Completion Criteria

The end-to-end example is complete when:

- The sample requirement is available.
- All expected artifacts are generated.
- Each artifact follows its capability boundary.
- Requirement traceability is preserved.
- Confirmed behavior and undefined behavior remain distinguishable.
- Test scenarios cover the defined requirement appropriately.
- Coverage review identifies meaningful gaps where applicable.
- Test cases are executable.
- Test data supports the generated testing objectives.
- Regression analysis does not invent system dependencies.
- Cross-artifact review passes.

Only after these conditions are satisfied should the end-to-end example be considered frozen.