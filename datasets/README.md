# Datasets

The `datasets/` directory contains controlled evaluation assets used to validate, benchmark, and improve the QA-AI framework.

It provides reusable requirement inputs, reviewed reference outputs, evaluation definitions, benchmark data, and supporting fixtures so framework behavior can be assessed consistently over time.

Datasets are development and evaluation assets. They are not part of the core QA-AI runtime Skill Pack.

---

## Purpose

The purpose of `datasets/` is to provide a repeatable foundation for evaluating QA-AI capabilities.

The dataset library supports:

- Requirement-processing evaluation
- QA artifact quality evaluation
- Golden-output comparison
- Evaluation scoring
- Baseline benchmarking
- Cross-platform comparison
- Regression detection
- Controlled technical and domain fixtures

The directory allows QA-AI behavior to be evaluated against traceable data rather than relying only on ad-hoc examples.

---

## Scope

The dataset library contains five primary categories:

```text
datasets/
├── requirements/
├── golden-output/
├── evaluation/
├── benchmark/
└── fixtures/
```

| Category | Responsibility |
|---|---|
| `requirements/` | Controlled requirement inputs organized by evaluation complexity. |
| `golden-output/` | Reviewed reference QA artifacts associated with requirement datasets. |
| `evaluation/` | Criteria, rubrics, and scoring definitions used to assess generated outputs. |
| `benchmark/` | Data used for baseline, cross-platform, and regression comparisons. |
| `fixtures/` | Supporting API, database, domain, and UI data for controlled evaluation contexts. |

The directory must not define Skill behavior, Workflow orchestration, runtime instructions, or normal project execution outputs.

---

## Dataset Architecture

The current structure is:

```text
datasets/
├── README.md
│
├── requirements/
│   ├── simple/
│   ├── medium/
│   └── complex/
│
├── golden-output/
│   ├── requirement-analysis/
│   ├── business-rules/
│   ├── risk-analysis/
│   ├── test-scenarios/
│   ├── test-cases/
│   └── regression-analysis/
│
├── evaluation/
│   ├── criteria/
│   ├── rubrics/
│   └── scoring/
│
├── benchmark/
│   ├── baseline/
│   ├── cross-platform/
│   └── regression/
│
└── fixtures/
    ├── api/
    ├── database/
    ├── domain/
    └── ui/
```

The high-level evaluation relationship is:

```text
Requirement Input
      ↓
QA-AI Execution
      ↓
Generated Artifact
      ↓
Evaluation Definition
      ↓
Reference / Benchmark Comparison
      ↓
Evaluation Result
```

Fixtures may be supplied as additional controlled context when required by the dataset.

---

## Dataset Categories

### `requirements/`

`requirements/` contains controlled requirement inputs used to evaluate QA-AI capabilities.

Requirements are organized by evaluation complexity:

```text
requirements/
├── simple/
├── medium/
└── complex/
```

#### Simple

Simple datasets represent focused features with characteristics such as:

- Limited functional scope
- Few business rules
- Clear acceptance criteria
- Minimal dependencies
- Limited state or role complexity

They are primarily used to validate fundamental framework behavior.

#### Medium

Medium datasets introduce additional complexity such as:

- Multiple business rules
- Multiple user flows
- Validation rules
- Boundary conditions
- Role-specific behavior
- Moderate feature dependencies

They are used to evaluate whether QA-AI can maintain correctness, coverage, and traceability across broader feature scopes.

#### Complex

Complex datasets may include:

- Multiple interacting flows
- Complex business rules
- State transitions
- Cross-module dependencies
- Roles and permissions
- Integration concerns
- Ambiguous or incomplete information
- Significant regression impact

They are intended to evaluate advanced decomposition, reasoning, traceability, risk identification, and assumption control.

Complexity classification describes the characteristics of an evaluation dataset. It is not a general project estimation model.

---

### `golden-output/`

`golden-output/` contains reviewed reference artifacts associated with requirement datasets.

Current reference artifact categories are:

```text
golden-output/
├── requirement-analysis/
├── business-rules/
├── risk-analysis/
├── test-scenarios/
├── test-cases/
└── regression-analysis/
```

Golden outputs may be used to evaluate qualities such as:

- Requirement fidelity
- Correctness
- Completeness
- Business-rule extraction
- Risk identification
- Scenario coverage
- Test-case quality
- Regression reasoning
- Traceability
- Assumption control

A golden output represents a reviewed reference interpretation of a dataset requirement.

It is not a mandatory byte-for-byte response. AI-generated artifacts may differ in wording, ordering, or decomposition while still satisfying the required quality criteria.

Evaluation should therefore use the definitions maintained under `evaluation/` rather than relying only on literal text comparison.

---

### `evaluation/`

`evaluation/` defines how QA-AI outputs are assessed.

```text
evaluation/
├── criteria/
├── rubrics/
└── scoring/
```

#### `criteria/`

Defines the dimensions that should be evaluated.

Examples may include:

- Correctness
- Completeness
- Requirement fidelity
- Coverage
- Traceability
- Clarity
- Testability
- Consistency
- Assumption control

Criteria define **what is evaluated**.

#### `rubrics/`

Defines observable descriptions for different quality levels within evaluation criteria.

Rubrics help reduce evaluator subjectivity and improve consistency between evaluation runs.

Rubrics define **how quality is judged**.

#### `scoring/`

Defines how evaluation judgments are converted into measurable results.

Scoring definitions may include:

- Score ranges
- Criterion weighting
- Pass/fail thresholds
- Aggregation rules
- Result interpretation

Scoring defines **how evaluation results are measured**.

Criteria, rubrics, and scoring remain separated so evaluation logic can evolve without changing source requirement datasets or reference artifacts.

---

### `benchmark/`

`benchmark/` contains data used to compare QA-AI behavior across controlled executions.

```text
benchmark/
├── baseline/
├── cross-platform/
└── regression/
```

#### `baseline/`

Contains approved benchmark references representing known framework behavior under a defined evaluation configuration.

A baseline provides a stable comparison point for later runs.

#### `cross-platform/`

Supports comparison of QA-AI behavior across supported AI platforms or execution environments.

Equivalent requirement inputs and evaluation definitions should be used when comparing platforms.

Platform-specific differences are not automatically defects unless they violate the applicable QA-AI contract or evaluation criteria.

#### `regression/`

Supports detection of quality regressions between framework versions, configurations, or evaluation runs.

A typical comparison is:

```text
Approved Baseline
      ↓
Current Execution
      ↓
Evaluation
      ↓
Comparison
      ↓
Regression Result
```

The purpose is to identify whether a framework change reduces previously validated QA capability.

---

### `fixtures/`

`fixtures/` contains supporting data used to establish controlled evaluation conditions.

```text
fixtures/
├── api/
├── database/
├── domain/
└── ui/
```

Fixtures may provide contextual information such as:

- API contracts
- Example API requests and responses
- Database schemas
- Synthetic database records
- Domain definitions
- UI field definitions
- UI states

Fixtures are supporting evaluation inputs, not primary requirement sources.

A fixture must not silently introduce business rules that should be defined by the requirement or another authoritative source.

Not every requirement dataset requires a fixture.

---

## Dataset Relationships

A standard evaluation flow is:

```text
Requirement Dataset
      ↓
QA-AI Skill / Workflow
      ↓
Generated Artifact
      ↓
Evaluation Criteria + Rubric
      ↓
Golden Output
      ↓
Evaluation Result
```

Benchmarking extends this flow:

```text
Evaluation Result
      ↓
Baseline / Platform / Previous Run
      ↓
Comparison
      ↓
Benchmark Result
```

When supporting context is required:

```text
Requirement Dataset
       +
Controlled Fixture
       ↓
QA-AI Execution
```

The requirement remains the primary feature source unless the dataset explicitly identifies another authoritative input.

---

## Dataset Lifecycle

Datasets should follow a controlled lifecycle:

```text
Create
  ↓
Review
  ↓
Validate
  ↓
Approve
  ↓
Use in Evaluation
  ↓
Maintain
```

A dataset or reference artifact must not be treated as approved solely because it was generated by an AI system.

Golden outputs and benchmark baselines require review before they become authoritative evaluation references.

When a source requirement, framework contract, Skill, Workflow, or evaluation definition changes materially, related datasets should be reviewed for continued validity.

---

## Dataset Quality Principles

Dataset assets should follow these principles.

### Representative

Datasets should represent realistic QA problems and behaviors relevant to the capability being evaluated.

### Controlled

Inputs and evaluation references should be sufficiently defined to support repeatable assessment.

### Traceable

Relationships between requirements, reference artifacts, evaluation definitions, and benchmark results should be identifiable.

### Independent

Datasets should avoid unnecessary dependencies on unrelated evaluation assets.

### Reviewable

A reviewer should be able to understand the source input, expected quality, and reason a reference artifact is considered acceptable.

### Reusable

Datasets should support repeated evaluation rather than one-time execution only.

### Stable

Approved datasets should not change without a clear reason and corresponding review.

### Non-Sensitive

Datasets must not contain production secrets, credentials, personal data, or confidential customer information.

Synthetic or sanitized data should be used where necessary.

---

## Naming and Organization

Dataset naming should follow the applicable repository standards under `shared/standards/`.

Names should be:

- Descriptive
- Stable
- Consistent
- Easy to trace across related assets

Related requirement and golden-output assets should use identifiers or naming conventions that make their relationship clear.

Conceptually:

```text
Requirement Dataset
      ↓
Requirement Analysis Reference
      ↓
Business Rules Reference
      ↓
Risk Analysis Reference
      ↓
Test Scenario Reference
      ↓
Test Case Reference
      ↓
Regression Analysis Reference
```

The exact identifier and file-naming convention should come from the applicable repository standard rather than being redefined independently by each dataset category.

---

## Traceability

Dataset traceability should support navigation between:

```text
Requirement
    ↓
Golden Output
    ↓
Evaluation Definition
    ↓
Benchmark Result
```

Where applicable, golden outputs should retain traceability to their source requirement dataset.

Evaluation and benchmark results should identify enough context to determine:

- Dataset evaluated
- Artifact or capability evaluated
- Evaluation definition used
- Baseline or comparison target used, when applicable

Traceability should not depend only on file location when a stable dataset identifier is available.

---

## Usage Guidelines

Datasets may be used for:

- Skill validation
- Workflow validation
- Prompt evaluation
- Output-quality assessment
- Cross-platform comparison
- Regression evaluation
- Framework benchmarking
- Automated evaluation

Generated execution results should normally be stored separately from approved source datasets and golden references.

Evaluation processes must not overwrite approved reference artifacts unless an intentional dataset maintenance change has been reviewed and accepted.

---

## Boundaries and Responsibilities

QA-AI separates examples, evaluation assets, runtime definitions, automation, and generated outputs.

```text
examples/
    Demonstrate how QA-AI is used

datasets/
    Evaluate how well QA-AI performs

shared/
    Provide reusable standards, knowledge,
    templates, checklists, and prompt patterns

skills/
    Define reusable QA capabilities

workflows/
    Orchestrate Skills into QA processes

scripts/
    Automate validation, evaluation,
    execution, and repository operations

output/
    Store generated execution artifacts
```

The `datasets/` directory must not:

- Define Skill behavior
- Define Workflow orchestration
- Replace shared QA knowledge
- Store normal project execution output
- Act as primary user documentation
- Contain platform-specific runtime logic

---

## Validation

Dataset validation should verify at minimum:

- Required dataset structure exists
- Naming follows repository standards
- Requirement inputs are readable and self-contained enough for their intended evaluation
- Golden outputs reference valid source datasets
- Traceability is not broken
- Evaluation definitions are valid and applicable
- Benchmark references exist where required
- Fixtures are valid for their intended context
- Sensitive information is not included
- Approved reference assets are not unintentionally modified

Automated validation may be introduced through repository scripts in a later implementation phase.

Until automated validation is available, dataset assets should be reviewed manually against the applicable repository standards and dataset contracts.

---

## References

Related repository resources include:

- `FRAMEWORK.md`
- `docs/`
- `shared/standards/`
- `shared/templates/`
- `shared/checklists/`
- `skills/`
- `workflows/`
- `examples/`
- `scripts/`

These resources define the architecture, standards, reusable capabilities, workflows, examples, and automation that interact with the dataset library.