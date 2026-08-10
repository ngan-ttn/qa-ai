# QA-AI Examples

## Purpose

The `examples/` directory contains curated reference examples that demonstrate how the QA-AI framework consumes QA inputs and produces structured QA deliverables.

Examples provide practical demonstrations of framework behavior without becoming part of the framework's runtime definition.

They help users understand:

- How inputs can be provided to QA-AI.
- How individual QA capabilities transform inputs into artifacts.
- What expected QA-AI deliverables look like.
- How framework standards and templates are reflected in outputs.
- How skills and workflows are applied in practical scenarios.
- How multiple QA capabilities can work together in an end-to-end flow.

The examples are designed for learning, demonstration, framework verification, and reference.

They are not runtime dependencies of the QA-AI Skill Pack.

---

## Scope

The directory contains representative examples for selected QA-AI capabilities and end-to-end framework execution.

```text
examples/
├── README.md
│
├── requirement-analysis/
│   ├── input/
│   └── expected-output/
│
├── business-rule-extraction/
│   ├── input/
│   └── expected-output/
│
├── risk-analysis/
│   ├── input/
│   └── expected-output/
│
├── scenario-generation/
│   ├── input/
│   └── expected-output/
│
├── testcase-generation/
│   ├── input/
│   └── expected-output/
│
├── coverage-review/
│   ├── input/
│   └── expected-output/
│
├── regression-analysis/
│   ├── input/
│   └── expected-output/
│
├── test-data-generation/
│   ├── input/
│   └── expected-output/
│
├── bug-report-review/
│   ├── input/
│   └── expected-output/
│
└── end-to-end/
    ├── input/
    └── expected-output/
```

The examples included in this directory are representative rather than exhaustive.

The directory does not need to contain a one-to-one example for every skill in `skills/`.

Additional examples should be introduced only when they demonstrate a meaningful capability, workflow, edge case, or usage pattern that is not adequately represented by the existing examples.

---

## Example Model

A QA-AI example represents a controlled transformation from known input to a reviewed expected output.

```text
Example Input
     │
     ▼
QA-AI Framework
     │
     ▼
Applicable Skill / Workflow
     │
     ▼
Expected Output
```

Each example should demonstrate behavior already defined by the framework.

An example must not introduce new framework behavior.

---

## Example Structure

Capability examples follow a common structure:

```text
<example-name>/
├── input/
└── expected-output/
```

This separation makes the relationship between source information and expected QA deliverables explicit.

### `input/`

The `input/` directory contains the source information required to execute the demonstrated QA capability.

Depending on the capability, input may include:

- Requirement.
- User story.
- Acceptance criteria.
- Existing QA artifact.
- Bug report.
- Supporting specification.
- Existing test scenarios.
- Other capability-specific context.

Input should contain enough information to demonstrate the intended capability without adding unrelated complexity.

Information intentionally omitted from the input may be used to demonstrate:

- Missing-information detection.
- Clarification handling.
- Assumption management.
- No-fabrication behavior.

### `expected-output/`

The `expected-output/` directory contains the reviewed reference artifact expected from the demonstrated QA-AI execution.

Expected output must comply with the applicable:

- Skill output contract.
- Workflow contract.
- QA-AI standards.
- QA-AI templates.
- QA-AI checklists.
- Framework execution rules.

Expected output represents a reference result, not an exact textual response that every AI runtime must reproduce word-for-word.

---

## Capability Examples

### Requirement Analysis

```text
requirement-analysis/
├── input/
└── expected-output/
```

Demonstrates how unstructured or semi-structured requirement information is transformed into structured requirement analysis.

The example should demonstrate applicable behaviors such as:

- Requirement understanding.
- Feature summarization.
- User-flow identification.
- Business-rule identification.
- Edge-case identification.
- Assumption handling.
- Clarification-question generation.

The expected output must follow the contract defined by the requirement-analysis capability.

---

### Business Rule Extraction

```text
business-rule-extraction/
├── input/
└── expected-output/
```

Demonstrates how explicit and derived business rules are identified and structured from available requirement context.

The example should preserve the distinction between:

- Confirmed business rules.
- Derived information.
- Assumptions.
- Missing information.

The example must not convert unsupported assumptions into confirmed business rules.

---

### Risk Analysis

```text
risk-analysis/
├── input/
└── expected-output/
```

Demonstrates identification and assessment of QA-relevant risks based on requirement and available context.

The expected output should reflect the applicable QA-AI risk-analysis contract and risk conventions.

Risk information should remain traceable to available requirement or analysis context where required.

---

### Scenario Generation

```text
scenario-generation/
├── input/
└── expected-output/
```

Demonstrates generation of structured test scenarios from requirement and applicable upstream analysis.

The example should demonstrate meaningful QA coverage without duplicating equivalent scenarios.

Scenario coverage should remain aligned with confirmed requirements and applicable business rules.

---

### Test Case Generation

```text
testcase-generation/
├── input/
└── expected-output/
```

Demonstrates generation of detailed, executable test cases from requirement information and applicable upstream artifacts.

Expected test cases should follow the relevant QA-AI template and output contract.

The example should demonstrate characteristics such as:

- Clear test objective.
- Defined preconditions.
- Executable test steps.
- Relevant test data.
- Verifiable expected results.
- Appropriate priority.
- Traceability where applicable.

---

### Coverage Review

```text
coverage-review/
├── input/
└── expected-output/
```

Demonstrates evaluation of existing QA coverage against requirement information and the applicable testing scope.

The example should show how QA-AI identifies:

- Covered areas.
- Missing coverage.
- Duplicate coverage.
- Potential quality gaps.
- Recommended coverage improvements.

The coverage-review example evaluates existing QA artifacts rather than redefining the underlying requirement.

---

### Regression Analysis

```text
regression-analysis/
├── input/
└── expected-output/
```

Demonstrates identification of regression impact resulting from a requirement or system change.

The expected output should identify relevant affected areas according to the regression-analysis capability without assuming unsupported system dependencies.

Unknown dependencies should remain visible as clarification or investigation items when applicable.

---

### Test Data Generation

```text
test-data-generation/
├── input/
└── expected-output/
```

Demonstrates generation of structured test data required to support QA execution.

Test data should be aligned with:

- Requirement rules.
- Test objectives.
- Relevant boundaries.
- Positive and negative conditions.
- Applicable validation constraints.

Generated test data must not introduce unsupported project-specific rules.

---

### Bug Report Review

```text
bug-report-review/
├── input/
└── expected-output/
```

Demonstrates review and improvement of an existing bug report.

The example should show how QA-AI evaluates the bug report for characteristics such as:

- Reproducibility.
- Clarity.
- Completeness.
- Expected versus actual behavior.
- Relevant environment or test information.
- Evidence requirements.
- Missing information.

The review should improve the quality of the provided bug report without inventing evidence or system behavior that was not supplied.

---

## End-to-End Example

The `end-to-end/` directory demonstrates the primary requirement-driven usage of the QA-AI framework.

```text
end-to-end/
├── input/
└── expected-output/
```

Unlike capability examples, which focus on a specific QA capability, the end-to-end example demonstrates coordinated execution across multiple QA-AI components.

Conceptually:

```text
Requirement
     │
     ▼
QA-AI Framework
     │
     ▼
Request Resolution
     │
     ▼
Workflow Resolution
     │
     ▼
Skill Resolution
     │
     ▼
Context Assembly
     │
     ▼
Skill Execution
     │
     ▼
Quality Validation
     │
     ▼
QA Deliverables
```

The end-to-end example should demonstrate:

- Requirement-driven framework execution.
- Reuse of upstream artifacts.
- Consistency across related QA artifacts.
- Traceability where applicable.
- Quality validation.
- Proper handling of missing information and assumptions.
- Coordinated final deliverables.

The exact skill sequence and artifact set must be determined by the applicable workflow.

The example must not independently define a new execution pipeline.

---

## Expected Output Semantics

An expected output represents a **reviewed reference result**.

It does not mean that every compatible AI runtime must generate identical wording.

For the same example input, compatible runtimes should demonstrate comparable QA behavior in areas such as:

- Requirement interpretation.
- Business-rule handling.
- Coverage.
- Artifact structure.
- Assumption handling.
- Missing-information handling.
- Quality compliance.

For example:

```text
Same Example Input
        │
        ├── AI Runtime A
        │       ↓
        │   Output A
        │
        └── AI Runtime B
                ↓
            Output B
```

`Output A` and `Output B` may differ in wording while still conforming to the same QA-AI contract.

---

## Examples vs Runtime Output

The `examples/` and `output/` directories serve different purposes.

| Directory | Responsibility |
|---|---|
| `examples/` | Curated and reviewed reference examples |
| `output/` | QA artifacts generated during actual framework execution |

Example artifacts should remain stable unless the underlying framework contract changes.

Runtime output may vary based on:

- Requirement.
- User objective.
- Available context.
- Selected workflow.
- Selected skills.
- Project constraints.
- Open assumptions or clarification items.

Generated runtime output must not overwrite curated examples.

---

## Examples vs Evaluation Datasets

The `examples/` and `datasets/` directories also have different responsibilities.

| Directory | Responsibility |
|---|---|
| `examples/` | Demonstrate expected QA-AI usage and behavior |
| `datasets/` | Evaluate and benchmark QA-AI behavior |

Examples are primarily human-readable reference material.

Datasets are designed for systematic evaluation.

Evaluation-specific content such as:

- Benchmark cases.
- Scoring criteria.
- Expected evaluation dimensions.
- Comparison results.
- Regression benchmark results.

belongs under `datasets/`.

An example may later be adapted into an evaluation case, but ownership and purpose must remain separate.

---

## Source of Truth

Examples demonstrate framework behavior but do not define framework behavior.

The authoritative relationship is:

```text
FRAMEWORK.md
      │
      ├── workflows/
      ├── skills/
      └── shared/
             │
             ▼
          examples/
```

Framework components are the source of truth.

Examples are derived reference material.

If an example conflicts with an authoritative framework definition:

```text
Conflict Detected
      │
      ▼
Check Authoritative Framework Contract
      │
      ▼
Correct Example
```

The core framework must not be changed solely to preserve outdated example behavior.

---

## Example Quality Rules

Every reference example should satisfy the following principles.

### Realistic

The example should represent a realistic QA use case.

It should be understandable without requiring unnecessary domain-specific knowledge unless domain behavior is intentionally being demonstrated.

### Focused

A capability example should primarily demonstrate the capability represented by its directory.

Unrelated complexity should be avoided.

### Sufficient

Input must contain enough information for meaningful execution.

Intentional gaps are allowed when they are used to demonstrate missing-information or clarification behavior.

### Traceable

Expected output should remain traceable to the provided input and applicable upstream artifacts where traceability is required.

### Evidence-Based

Expected output must distinguish confirmed information from assumptions and derived information.

Unsupported project-specific behavior must not be introduced.

### Framework-Compliant

Expected output must follow applicable:

```text
Framework Rules
      +
Skill / Workflow Contract
      +
Standards
      +
Templates
      +
Checklists
```

### Reviewed

Expected outputs must be internally reviewed before being treated as reference examples.

An unreviewed generated response must not automatically become an expected output.

---

## Example Creation Workflow

New examples should follow a controlled creation process.

```text
Select Capability / Workflow
        │
        ▼
Define Example Objective
        │
        ▼
Create Input
        │
        ▼
Validate Input Scope
        │
        ▼
Execute Applicable QA-AI Capability
        │
        ▼
Review Generated Artifact
        │
        ▼
Correct Framework Compliance Issues
        │
        ▼
Freeze Expected Output
```

The expected output should only be frozen after it accurately represents the current QA-AI framework.

---

## Maintenance

Examples must remain aligned with the framework version they demonstrate.

Examples should be reviewed when changes affect:

- Framework execution rules.
- Skill contracts.
- Workflow contracts.
- Standards.
- Templates.
- Checklists.
- Relevant shared knowledge.
- Artifact structures.
- Output conventions.

A framework change does not automatically require every example to change.

Only affected examples should be reviewed and updated.

---

## Adding New Examples

A new example should be added when it provides meaningful reference value not already covered by the existing set.

Appropriate reasons may include:

- A new major QA capability.
- A new supported workflow.
- A materially different input pattern.
- A complex framework behavior requiring demonstration.
- A useful end-to-end usage pattern.

Examples should not be added merely to mirror every folder or file in `skills/`.

The examples library should remain representative, maintainable, and easy to understand.

---

## References

Related QA-AI components:

```text
FRAMEWORK.md

skills/
workflows/

shared/
├── standards/
├── templates/
├── checklists/
├── prompt-patterns/
├── knowledge/
└── glossary/

datasets/
output/
```

Use the authoritative framework components when determining expected behavior.

Use `examples/` to understand how that behavior is applied in practice.