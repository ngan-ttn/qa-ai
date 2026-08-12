# Baseline Benchmark

## Benchmark Metadata

- Benchmark ID: `BENCH-BASELINE-001`
- Benchmark Type: `Baseline`
- Scope: `QA-AI Artifact Quality`
- Status: `Approved`
- Purpose: Define how approved evaluation results become stable baseline references for future QA-AI comparisons.

---

## Purpose

This document defines the canonical baseline benchmark model for QA-AI.

A baseline represents an approved and reproducible quality reference produced under a known evaluation configuration.

Baselines are used to answer:

> What level of QA-AI quality has already been validated and approved for this dataset, artifact, capability, or framework configuration?

A baseline provides a stable comparison point for later executions.

It may support:

- Framework quality tracking
- Skill evaluation
- Workflow evaluation
- Prompt evaluation
- Cross-platform comparison
- Framework regression detection

A baseline is not itself:

- A golden output
- A source requirement
- An evaluation rubric
- A scoring model
- A generated execution artifact

---

## Benchmark Position in the Evaluation Flow

The canonical flow is:

`Requirement → QA-AI Execution → Generated Artifact → Evaluation → Score → Baseline`

Once approved, later executions may be compared against that baseline:

`Approved Baseline → Current Evaluation → Comparison`

The baseline therefore captures an approved evaluation result, not merely an artifact file.

---

## Baseline Definition

A QA-AI baseline is a recorded evaluation state containing enough information to reproduce and interpret the approved result.

A valid baseline should identify:

- Dataset
- Artifact or capability
- Framework version
- Skill or Workflow configuration
- Execution platform when relevant
- Evaluation criteria
- Evaluation rubric
- Scoring model
- Evaluation profile
- Criterion-level results
- Final score
- Quality band
- PASS/FAIL result
- Critical failures
- Supporting evidence
- Approval status
- Baseline version

---

## Baseline Unit

The smallest canonical baseline unit is:

`Dataset + Evaluated Artifact/Capability + Evaluation Configuration`

Example:

`REQ-AUTH-001 + Test Cases + EVAL-SCORING-001`

This allows different artifact types from the same requirement dataset to maintain independent baseline results.

A complete workflow benchmark may aggregate multiple artifact baselines, but artifact-level results should remain traceable individually.

---

## Baseline Eligibility

An evaluation result is eligible to become an approved baseline only when all required conditions are satisfied.

### Required Conditions

1. The source dataset is approved.
2. The evaluated artifact or capability is clearly identified.
3. The applicable evaluation criteria are defined.
4. The rubric is defined.
5. The scoring model is defined.
6. The evaluation profile is identified.
7. Supporting evaluation evidence is available.
8. The final result is reproducible.
9. No unresolved critical failure exists.
10. The baseline has completed review and approval.

### Default Quality Requirement

Under the canonical scoring model:

`Final Score ≥ 85`

and:

`No unresolved critical failure`

are required before the result is eligible for approval as a baseline.

A project may define a stricter baseline threshold, but it must not silently weaken the canonical quality gate.

---

## Baseline Approval

A passing evaluation result does not automatically become a baseline.

The lifecycle is:

`Candidate → Review → Validate → Approve → Baseline`

### Candidate

An evaluation result proposed as a future comparison reference.

### Review

The result and its evidence are checked for:

- Correct dataset
- Correct evaluation configuration
- Correct scoring
- Reproducibility
- Traceability
- Absence of unresolved critical defects

### Validate

The benchmark metadata and evaluation result are verified.

Where repeat execution is practical, reproducibility should be checked.

### Approve

The candidate is formally accepted as the comparison reference.

### Baseline

The approved result becomes stable and should not be changed casually.

---

## Baseline Record

A canonical baseline record should preserve the following fields.

| Field | Description |
|---|---|
| Baseline ID | Stable identifier for the baseline |
| Baseline Version | Version of the approved baseline |
| Dataset ID | Dataset used in the evaluation |
| Dataset Version | Version or immutable reference of the dataset |
| Artifact Type | Evaluated artifact or capability |
| Framework Version | QA-AI framework version evaluated |
| Skill / Workflow | Capability or workflow executed |
| Execution Platform | Platform or execution environment when relevant |
| Evaluation Criteria | Criteria definition used |
| Evaluation Rubric | Rubric definition used |
| Scoring Model | Scoring definition used |
| Evaluation Profile | Criterion-weight profile used |
| Criterion Levels | L4–L0 / N/A results |
| Unrounded Score | Precise normalized result |
| Final Score | Rounded final score |
| Quality Band | Resulting quality band |
| Critical Failures | Confirmed critical failures |
| Result | PASS / FAIL |
| Evidence | Supporting evaluation evidence |
| Approved By | Baseline approver |
| Approval Date | Baseline approval date |
| Notes | Relevant benchmark context |

---

## Example Baseline Record

Example serialized representation:

    baseline_id: BASE-REQ-AUTH-001-TC-001
    baseline_version: 1.0.0

    dataset:
      id: REQ-AUTH-001
      artifact_type: Test-Cases

    framework:
      version: 1.0.0
      capability: testcase-generator

    evaluation:
      criteria: EVAL-CRITERIA-001
      rubric: EVAL-RUBRIC-001
      scoring_model: EVAL-SCORING-001
      profile: default-artifact-quality

    criterion_levels:
      C01: L4
      C02: L4
      C03: L4
      C04: L4
      C05: L4
      C06: L4
      C07: L4
      C08: L4
      C09: L4
      C10: L4
      C11: L4
      C12: L4

    unrounded_score: 100.0
    final_score: 100
    quality_band: Excellent
    critical_failures: []
    result: PASS

    status: Approved

The exact persistence format may evolve.

The semantic information required for reproducibility should remain available.

---

## Baseline Immutability

An approved baseline should be treated as stable.

It must not be overwritten simply because:

- A newer execution scores higher.
- Another platform produces different wording.
- A model produces a different artifact decomposition.
- Formatting changes.
- A new result appears preferable.

If an approved baseline must change, create a new baseline version.

Conceptually:

`Baseline v1 → Review Change → Baseline v2`

Previous baseline history should remain traceable where practical.

---

## Baseline Versioning

A baseline should be versioned when any material comparison input changes.

Examples include:

- Source dataset behavior
- Golden-output interpretation
- Evaluation criteria
- Evaluation rubric
- Scoring model
- Evaluation profile
- Skill behavior
- Workflow behavior
- Framework contract
- Approved benchmark expectation

A formatting-only change does not necessarily require a new benchmark version if evaluation meaning remains unchanged.

---

## Evaluation Compatibility

Two results should be treated as directly comparable only when their evaluation configuration is compatible.

At minimum, compare:

- Dataset
- Artifact type
- Criteria
- Rubric
- Scoring model
- Scoring profile

If any material evaluation definition differs, direct score comparison may be invalid.

The result should instead be marked as:

`Non-Comparable`

or compared using an explicitly defined compatibility rule.

---

## Dataset Compatibility

A baseline created for one dataset must not automatically become the baseline for another dataset.

Example:

`REQ-AUTH-001`

and:

`REQ-CART-001`

may both evaluate Test Cases but represent different problem spaces.

Their artifact scores may be aggregated for broader benchmarking, but their individual baseline references remain dataset-specific.

---

## Artifact Compatibility

Artifact types must remain comparable.

A Requirement Analysis score must not be directly compared with a Test Case score as though they measure the same output.

Valid comparison:

`Test Cases baseline → Test Cases current run`

Invalid direct comparison:

`Requirement Analysis baseline → Test Cases current run`

Cross-artifact aggregation requires a separately defined benchmark model.

---

## Execution Configuration

Where execution configuration can materially affect the result, the baseline should identify it.

Relevant configuration may include:

- Platform
- Model
- Adapter
- Skill version
- Workflow version
- Prompt version
- Knowledge-pack version
- Framework version

Only known and relevant configuration should be recorded.

The baseline must not invent configuration values that were not captured during execution.

---

## Platform Handling

A baseline may be:

### Platform-Specific

Represents validated behavior for one execution platform.

Example:

`ChatGPT baseline`

### Platform-Neutral

Represents a framework-level approved expectation independent of platform implementation.

A platform-neutral baseline should only be used when the comparison contract genuinely supports platform-independent interpretation.

Platform-specific behavior is not automatically a defect.

A difference becomes a quality problem only when it violates applicable evaluation criteria or framework contracts.

---

## Golden Outputs and Baselines

Golden outputs and baselines serve different purposes.

### Golden Output

Represents a reviewed reference interpretation of a source requirement.

It helps evaluators understand expected QA quality.

### Baseline

Represents an approved measured evaluation result under a known configuration.

Conceptually:

`Golden Output → Supports Evaluation`

while:

`Evaluated Execution → Approved Result → Baseline`

A baseline may reference golden outputs but must not reduce evaluation to literal text matching.

---

## Baseline Evidence

Baseline approval should retain evidence sufficient to explain the result.

Evidence may include:

- Generated artifact
- Requirement dataset
- Golden output
- Criterion ratings
- Rubric evidence
- Scoring record
- Critical-failure review
- Reviewer notes

The amount of evidence retained should be sufficient for later benchmark review without requiring unsupported reconstruction.

---

## Baseline Quality Controls

A baseline should satisfy the following controls.

### Valid

The recorded result was produced using valid evaluation definitions.

### Reproducible

A reviewer can determine how the result was produced.

### Traceable

The baseline links to its dataset and evaluation configuration.

### Stable

Approved baseline content is not silently changed.

### Reviewable

A reviewer can understand why the baseline was approved.

### Comparable

The record contains enough configuration information to determine whether another result may be compared against it.

---

## Baseline Selection

When multiple baseline versions exist, comparison should use an explicitly selected baseline.

Do not automatically choose:

- The highest-scoring baseline
- The newest baseline
- The oldest baseline

without a defined benchmark policy.

The selected baseline should be recorded in the comparison result.

---

## Baseline Replacement

A new candidate may replace the active baseline when:

1. A material framework version is approved.
2. A dataset or evaluation definition changes.
3. A previous baseline is invalidated.
4. A newly validated capability becomes the approved reference.
5. The benchmark governance process intentionally promotes a new baseline.

Replacement should follow:

`Current Baseline → Candidate → Review → Approve → New Active Baseline`

The previous baseline should remain identifiable for historical regression analysis where practical.

---

## Baseline Invalidity

A baseline should be marked invalid or deprecated when:

- Its source dataset is no longer valid.
- Its scoring model is no longer compatible.
- Evaluation evidence is discovered to be incorrect.
- A critical defect existed in the approved reference.
- Its framework configuration can no longer be reproduced.
- The baseline was created using materially incomplete metadata.

Invalid baselines must not be used silently for current comparisons.

---

## Baseline Comparison Inputs

A later comparison should identify:

- Baseline ID
- Baseline Version
- Current Evaluation ID
- Dataset ID
- Artifact Type
- Evaluation Configuration
- Baseline Score
- Current Score
- Criterion-level differences
- Critical-failure differences

The interpretation of score differences belongs to the applicable comparison model.

This baseline definition does not independently declare whether a particular delta is acceptable regression.

---

## Baseline Relationship to Regression Benchmarking

Baseline benchmarking establishes the reference.

Regression benchmarking asks:

> Has current QA-AI quality materially decreased relative to an approved reference?

Conceptually:

`Approved Baseline + Current Evaluation → Regression Comparison`

The regression benchmark defines:

- Delta interpretation
- Regression thresholds
- Criterion degradation rules
- Critical-failure regression behavior

Those rules belong under:

`datasets/benchmark/regression/`

---

## Baseline Relationship to Cross-Platform Benchmarking

A baseline may also support comparison across platforms.

Conceptually:

`Equivalent Dataset + Equivalent Evaluation Configuration + Platform Results`

The cross-platform benchmark determines:

- Comparison validity
- Platform-level reporting
- Criterion-level comparison
- Interpretation of non-identical outputs

Those rules belong under:

`datasets/benchmark/cross-platform/`

---

## Recommended Baseline Lifecycle

The canonical lifecycle is:

`Generate → Evaluate → Score → Review → Approve → Freeze → Compare → Maintain`

### Generate

Execute the QA-AI capability against the controlled dataset.

### Evaluate

Apply canonical criteria and rubric.

### Score

Apply the selected scoring model.

### Review

Validate result quality and evidence.

### Approve

Accept the result as the benchmark reference.

### Freeze

Treat the approved baseline as stable.

### Compare

Use it for later benchmark evaluation.

### Maintain

Version or deprecate when material conditions change.

---

## Baseline Boundaries

The baseline benchmark must not:

- Redefine evaluation criteria.
- Redefine rubric levels.
- Change scoring formulas.
- Require byte-for-byte golden-output matching.
- Rank platforms.
- Define cross-platform winners.
- Define regression thresholds.
- Store uncontrolled runtime outputs as approved references.
- Automatically approve every passing result.

---

## Validation Checklist

Before approving a baseline, verify:

- Dataset exists and is approved.
- Artifact or capability is identified.
- Evaluation criteria are identified.
- Rubric is identified.
- Scoring model is identified.
- Evaluation profile is identified.
- Score calculation is valid.
- Critical failures are resolved.
- Evidence is available.
- Result meets the applicable quality gate.
- Baseline metadata is complete enough for comparison.
- Approval status is explicit.
- Baseline version is defined.

---

## Final Baseline Definition

A QA-AI baseline is:

> An approved, versioned, traceable, and reproducible evaluation result that serves as the stable quality reference for future comparable executions.

The canonical baseline model provides:

- Stable benchmark references
- Evaluation traceability
- Configuration awareness
- Version control
- Reproducibility
- Quality-gate enforcement
- Downstream support for cross-platform and regression benchmarking
