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
| `benchmark/` | Canonical definitions for baseline, cross-platform, and regression benchmarking. |
| `fixtures/` | Canonical API, database, domain, and UI fixture models for controlled evaluation contexts. |

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

`benchmark/` defines the controlled benchmark framework used to compare QA-AI behavior across executions.

At the current framework stage, the files under this directory define canonical benchmark models for:

- Baseline benchmarking
- Cross-platform benchmarking
- Regression benchmarking

```text
benchmark/
├── baseline/
├── cross-platform/
└── regression/
```

The benchmark model documents define how benchmark records should be structured, executed, compared, interpreted, and maintained.

They are not themselves benchmark execution records.

#### Benchmark Definition and Benchmark Record

QA-AI distinguishes between a benchmark definition and a benchmark record.

##### Benchmark Definition

A benchmark definition specifies the canonical purpose, inputs, comparison rules, evaluation requirements, lifecycle, and boundaries for a benchmark type.

The current benchmark files under `datasets/benchmark/` are benchmark definitions.

They establish reusable benchmarking contracts without claiming that a benchmark execution has already occurred.

##### Benchmark Record

A benchmark record represents the controlled result of an actual benchmark execution performed according to a benchmark definition.

Depending on the benchmark type, a record may identify:

- Requirement dataset and version
- Fixture instances and versions when applicable
- QA-AI framework version
- Skill or workflow version
- Execution platform
- Model or execution configuration when applicable
- Evaluation criteria
- Evaluation rubric
- Scoring configuration
- Generated artifact reference
- Evaluation result
- Comparison target
- Benchmark outcome
- Execution timestamp or run identifier

A benchmark record must be traceable to the exact inputs and evaluation configuration used for that execution.

The canonical relationship is:

`Benchmark Definition → governs → Benchmark Execution → produces → Benchmark Record`

Benchmark execution may use controlled dataset components:

`Requirement Dataset + Fixture Instance + QA-AI Configuration → Execution → Generated Artifact → Evaluation → Benchmark Record`

Not every benchmark requires every optional input.

#### `baseline/`

`baseline/` defines the canonical baseline benchmark model.

A baseline benchmark establishes an approved reference point representing known QA-AI behavior under a controlled dataset and evaluation configuration.

Conceptually:

`Controlled Execution → Evaluation → Approved Baseline Record`

An approved baseline record may later be used as the comparison target for regression or other controlled benchmark executions.

A baseline definition is not itself proof that an approved baseline record already exists.

#### `cross-platform/`

`cross-platform/` defines the canonical model for comparing QA-AI behavior across supported AI platforms or execution environments.

Equivalent controlled inputs and compatible evaluation definitions should be used when comparing platforms.

Conceptually:

`Same Controlled Inputs → Platform A Execution`

`Same Controlled Inputs → Platform B Execution`

followed by:

`Evaluation Results → Cross-Platform Comparison Record`

Platform-specific differences are not automatically defects.

A difference becomes relevant when it affects the applicable QA-AI contract, evaluation criteria, quality threshold, or comparison objective.

#### `regression/`

`regression/` defines the canonical model for detecting quality regressions between framework versions, configurations, or controlled executions.

A typical comparison is:

```text
Approved Baseline Record
      ↓
Current Controlled Execution
      ↓
Evaluation
      ↓
Comparison
      ↓
Regression Benchmark Record
```

The purpose is to identify whether a framework, skill, workflow, prompt, configuration, or other controlled change reduces previously validated QA capability.

Regression comparison requires compatible inputs and evaluation conditions.

If material benchmark inputs change, direct comparison must be reviewed before a regression conclusion is accepted.

#### Current Benchmark Scope

Phase 8 establishes the canonical benchmark-definition foundation.

The presence of a benchmark definition does not imply that an actual benchmark execution or benchmark record already exists.

Benchmark records should be created only when QA-AI performs a real controlled benchmark execution.

This prevents specification examples or hypothetical values from being mistaken for measured framework performance.

When benchmark records are introduced, they must conform to the applicable benchmark definition and remain traceable to their execution inputs.

#### Benchmark Boundaries

Benchmark definitions and records must remain separate from source requirements and golden outputs.

A benchmark definition or record must not:

- Modify source requirement behavior.
- Treat illustrative examples as measured results.
- Fabricate execution results.
- Fabricate evaluation scores.
- Claim cross-platform equivalence without controlled comparison.
- Claim regression without a compatible comparison target.
- Silently compare materially different dataset or fixture versions.
- Encode unsupported product behavior.
- Replace golden outputs as reviewed QA reference artifacts.

If no benchmark execution has occurred, no benchmark record should be created merely for structural completeness.

---

### `fixtures/`

`fixtures/` provides controlled supporting context used to establish reproducible QA-AI execution and evaluation conditions.

At the current framework stage, the files under this directory define canonical fixture models for:

- API context
- Database context
- Domain context
- UI context

```text
fixtures/
├── api/
├── database/
├── domain/
└── ui/
```

The fixture model documents define how fixture instances should be structured, validated, versioned, and used.

They are not themselves executable fixture instances.

#### Fixture Model and Fixture Instance

QA-AI distinguishes between a fixture model and a fixture instance.

##### Fixture Model

A fixture model defines the canonical structure, rules, boundaries, lifecycle, and quality requirements for a fixture type.

Examples:

- `FIXTURE-MODEL-API-001`
- `FIXTURE-MODEL-DATABASE-001`
- `FIXTURE-MODEL-DOMAIN-001`
- `FIXTURE-MODEL-UI-001`

The current files under `datasets/fixtures/` are fixture model specifications.

##### Fixture Instance

A fixture instance is concrete controlled context created according to a fixture model.

Examples:

- `API-FIX-AUTH-001`
- `DB-FIX-ORDER-001`
- `DOMAIN-FIX-INVENTORY-001`
- `UI-FIX-PERMIT-001`

Depending on the fixture type, an instance may provide contextual information such as:

- API contracts
- Example API requests and responses
- Database schemas
- Synthetic database records
- Domain definitions
- UI field definitions
- UI states

Fixture instances must remain source-supported, deterministic, traceable, and safe.

The canonical relationship is:

`Fixture Model → defines → Fixture Instance`

A fixture instance may then participate in QA-AI execution:

`Requirement Dataset + Fixture Instance → QA-AI Execution → Generated Artifact`

#### Current Fixture Scope

Phase 8 establishes the canonical fixture-model foundation.

The presence of a fixture model does not imply that a concrete fixture instance already exists for every dataset.

Concrete fixture instances should be introduced only when a dataset, example, evaluation, benchmark, or executable workflow requires controlled supporting context.

This avoids creating speculative fixture data before a real consumer exists.

When fixture instances are introduced, they must conform to the applicable canonical fixture model.

Not every requirement dataset requires a fixture instance.

#### Fixture Boundaries

Fixtures are supporting execution and evaluation inputs, not primary requirement sources.

A fixture instance must not:

- Introduce unsupported feature behavior.
- Silently override authoritative requirements.
- Introduce business rules that belong in the requirement or another authoritative source.
- Encode golden-output answers.
- Encode benchmark scores or evaluation ratings.
- Invent technical implementation where the source does not define it.
- Depend unnecessarily on uncontrolled production data.
- Contain real secrets or sensitive production information.

If no external context is required for a dataset, a fixture instance does not need to be created merely for structural completeness.
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