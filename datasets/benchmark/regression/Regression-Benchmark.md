# Regression Benchmark

## Benchmark Metadata

- Benchmark ID: `BENCH-REGRESSION-001`
- Benchmark Type: `Regression`
- Scope: `QA-AI Artifact Quality Regression`
- Status: `Approved`
- Purpose: Define how current QA-AI evaluation results are compared with approved baselines to identify meaningful quality degradation.

---

## Purpose

This document defines the canonical regression benchmark model for QA-AI.

Regression benchmarking compares a current QA-AI evaluation result against an approved and compatible baseline to determine whether previously validated quality has degraded.

It answers:

> Has the current QA-AI execution introduced a meaningful quality regression relative to the approved baseline?

Regression benchmarking may be used after changes to:

- Skills
- Workflows
- Prompts
- Shared knowledge
- Standards
- Adapters
- Framework behavior
- Supported execution platforms or models
- Other execution configuration that may affect QA artifact quality

The benchmark evaluates quality change.

It does not assume that changed wording, formatting, decomposition, or output structure is regression.

---

## Benchmark Position in the Evaluation Flow

The canonical regression flow is:

`Approved Baseline → Current Execution → Canonical Evaluation → Regression Comparison`

Conceptually:

`Baseline Evaluation ↔ Current Evaluation`

The regression benchmark consumes already evaluated results.

It does not replace:

- Source datasets
- Golden outputs
- Evaluation criteria
- Evaluation rubrics
- Scoring models
- Baseline approval

---

## Regression Objective

The purpose of regression benchmarking is to identify meaningful degradation in previously validated QA-AI quality.

Regression analysis may examine:

- Overall quality score
- Quality band
- Quality-gate result
- Criterion-level quality
- Critical failures
- Coverage characteristics
- Source fidelity
- Correctness
- Traceability
- Scope and assumption control
- Execution consistency

The benchmark should detect meaningful quality loss without treating harmless output variation as regression.

---

## Regression Comparison Unit

The smallest canonical regression comparison unit is:

`Approved Baseline + Comparable Current Evaluation`

for the same:

`Dataset + Artifact/Capability + Evaluation Configuration`

Example:

`BASE-REQ-AUTH-001-TC-001 + Current Test Cases Evaluation`

Each regression result must remain traceable to both:

- The approved baseline
- The current evaluation

A benchmark suite may aggregate multiple regression comparison units, but individual results must remain independently reviewable.

---

## Regression Eligibility

A regression comparison is valid only when the baseline and current result are sufficiently compatible.

### Required Compatibility

The following must be materially compatible:

1. Dataset
2. Dataset version or immutable dataset reference
3. Artifact type or evaluated capability
4. Evaluation criteria
5. Evaluation rubric
6. Scoring model
7. Evaluation profile

Relevant execution configuration should also be recorded when it may affect interpretation.

Examples include:

- Framework version
- Skill version
- Workflow version
- Prompt version
- Knowledge-pack version
- Adapter version
- Execution platform
- Model identifier when available

Configuration differences may be the reason for performing the regression benchmark.

They do not automatically invalidate comparison when the evaluation contract remains compatible.

---

## Dataset Compatibility

The current execution must use the same or materially equivalent source dataset as the approved baseline.

A material source change may invalidate direct regression comparison.

Examples include:

- Changed business rules
- New acceptance criteria
- Removed behavior
- Changed boundaries
- Changed role permissions
- Changed expected states or transitions

If source behavior changes materially, the old result may no longer represent the correct quality reference.

In that case, the dataset and baseline should be reviewed before regression comparison continues.

---

## Artifact Compatibility

The baseline and current result must evaluate the same artifact type or capability.

Valid comparison:

`Test Cases Baseline → Current Test Cases`

Invalid direct comparison:

`Test Scenarios Baseline → Current Test Cases`

Cross-artifact changes may be analyzed separately but must not be represented as direct artifact regression.

---

## Evaluation Compatibility

Regression scores are directly comparable only when the evaluation definitions remain compatible.

At minimum, verify:

- Criteria
- Rubric
- Scoring model
- Evaluation profile

If a material evaluation definition changes, direct score comparison may become invalid.

The correct action may be to:

- Re-evaluate the historical artifact using the new evaluation configuration, or
- Establish a new baseline.

Incompatible scores must not be silently compared.

---

## Non-Comparable Regression Results

A regression comparison must be classified as:

`Non-Comparable`

when material compatibility cannot be established.

Examples include:

- Materially changed source behavior
- Different artifact type
- Incompatible scoring model
- Materially different evaluation profile
- Unequal authoritative input
- Invalid baseline
- Insufficient baseline evidence
- Missing metadata that prevents defensible comparison

A `Non-Comparable` result is not:

- Regression
- Improvement
- Stable quality

It indicates that a defensible regression conclusion cannot be made from the available evidence.

---

## Regression Evidence Dimensions

Regression detection must consider multiple quality dimensions.

The canonical evidence dimensions are:

1. Critical failures
2. Quality-gate result
3. Criterion-level rubric changes
4. Final unrounded score
5. Quality band
6. Supporting evaluation evidence
7. Comparison compatibility

Overall score is therefore one regression signal, not the sole decision mechanism.

---

## Score Delta

For compatible baseline and current results:

`Score Delta = Current Unrounded Score - Baseline Unrounded Score`

Interpretation:

- Positive value → Current score increased
- Zero → No numeric change
- Negative value → Current score decreased

When the current result is lower:

`Score Drop = Baseline Unrounded Score - Current Unrounded Score`

### Example

Baseline:

`96.4`

Current:

`93.1`

Then:

`Score Delta = 93.1 - 96.4 = -3.3`

`Score Drop = 3.3`

Unrounded scores should be used when available.

---

## Score Delta Interpretation

Score delta is descriptive evidence.

A negative score delta indicates lower measured quality, but it does not automatically establish material regression.

The interpretation must consider:

- Which criteria changed
- Whether a critical failure appeared
- Whether the quality gate changed
- Whether the quality band changed
- Whether the difference is repeatable
- Whether the comparison configuration remains compatible

The canonical regression benchmark therefore does not define an arbitrary universal numeric regression threshold without supporting benchmark evidence.

---

## Regression Threshold Policy

Numeric regression tolerance may be introduced when sufficient benchmark history exists.

A threshold policy may later define values such as:

- Expected run-to-run variation
- Warning delta
- Material regression delta
- Severe regression delta

Any such threshold must be:

1. Evidence-based.
2. Explicitly documented.
3. Versioned.
4. Applied consistently.
5. Identified in the regression record.
6. Compatible with the evaluated artifact and benchmark context.

Until such a policy is approved, score delta remains supporting evidence rather than an independent regression decision rule.

---

## Criterion-Level Regression

Rubric levels are ordered as:

`L4 > L3 > L2 > L1 > L0`

A criterion regression occurs when the current result receives a lower rubric level than the approved baseline for the same applicable criterion.

Examples:

- `L4 → L3`
- `L4 → L2`
- `L3 → L1`

A criterion improvement occurs when the current level is higher.

Examples:

- `L3 → L4`
- `L2 → L3`

`N/A` is not part of the ordinal quality scale.

---

## High-Impact Criterion Regression

Regression in some quality dimensions may have greater practical significance.

High-impact criteria include:

- C01 — Requirement Fidelity
- C02 — Correctness
- C03 — Completeness
- C04 — Scope Control
- C05 — Assumption Control
- C06 — Traceability
- C12 — Internal Consistency

Degradation in these criteria requires explicit review because it may materially affect downstream QA reliability.

The benchmark does not assume that every one-level change has identical business impact.

Supporting evidence must be reviewed.

---

## Supporting Criterion Regression

Other criteria may expose meaningful quality degradation without necessarily invalidating the artifact.

Examples include:

- C07 — Clarity
- C08 — Testability
- C09 — Coverage Efficiency
- C10 — Boundary and State Coverage
- C11 — Risk Awareness

Their significance depends on:

- Artifact type
- Evaluation profile
- Degree of degradation
- Resulting QA impact
- Whether the weakness appears repeatedly

---

## N/A Regression Handling

If both baseline and current results validly mark a criterion:

`N/A`

there is no criterion-level regression for that criterion.

If applicability differs:

1. Review why the criterion changed applicability.
2. Verify the artifact contract.
3. Verify the evaluation profile.
4. Verify source behavior.

Do not automatically interpret:

`L4 → N/A`

or:

`N/A → L4`

as either regression or improvement.

A material applicability change may make the comparison non-comparable.

---

## Critical Failure Regression

Critical failures receive the highest regression attention.

### New Critical Failure

If:

- The approved baseline has no unresolved critical failure, and
- The current result introduces one or more critical failures

then a material regression exists.

Examples include:

- New source contradiction
- New fabricated business behavior
- New critical coverage omission
- New incorrect critical expected result
- New broken critical traceability
- New unsupported scope expansion
- New internal critical conflict

A new critical failure must not be hidden by a strong aggregate score.

### Baseline Critical Failure

Under the canonical baseline contract, an approved active baseline should not contain an unresolved critical failure.

If one is discovered:

- Review baseline validity.
- Do not silently use the baseline for regression comparison.
- Correct, invalidate, or replace the baseline as appropriate.

---

## Quality-Gate Regression

A quality-gate regression occurs when:

`Baseline Result = PASS`

and:

`Current Result = FAIL`

This represents a material regression because the current artifact no longer satisfies the approved QA-AI quality gate.

The underlying reason should be preserved.

Examples include:

- Critical failure
- Criterion degradation
- Aggregate quality degradation
- Combination of multiple weaknesses

---

## Quality-Band Regression

Quality-band movement provides additional regression evidence.

Examples:

- `Excellent → Good`
- `Good → Acceptable`
- `Acceptable → Weak`
- `Weak → Failed`

A lower quality band should be recorded.

However, band movement must be interpreted together with criterion-level and critical-failure evidence.

---

## Regression Classification

The canonical regression benchmark uses the following outcome classifications.

### No Regression

Use when:

- Comparison is valid.
- No meaningful quality degradation is identified.
- No new critical failure exists.
- Quality-gate result is preserved.
- Criterion-level changes do not indicate material degradation.

A small score decrease may still result in `No Regression` when no material quality evidence supports regression.

### Regression

Use when:

- Comparison is valid, and
- Meaningful quality degradation is supported by evaluation evidence.

Evidence may include:

- New critical failure
- PASS → FAIL transition
- Material criterion degradation
- Meaningful score decline supported by criterion evidence
- Repeated quality deterioration across controlled runs

The regression record should identify the specific evidence responsible for the classification.

### Improvement

Use when:

- Comparison is valid.
- Current quality is meaningfully better than the approved baseline.
- Improvement is supported by evaluation evidence.
- No material regression offsets the improvement.

Improvement may be supported by:

- Better criterion levels
- Higher quality band
- Stronger quality-gate performance
- Improved score
- Removal of previously observed non-critical weaknesses

A higher score alone does not automatically require an `Improvement` classification.

### Mixed Change

Use when:

- Comparison is valid.
- Meaningful improvements exist in some dimensions.
- Meaningful regressions exist in others.
- Neither a simple regression nor improvement label adequately represents the result.

Example:

- Traceability improves.
- Completeness degrades.
- Final score remains similar.

The benchmark should preserve both positive and negative evidence.

### Non-Comparable

Use when the compatibility requirements for regression analysis are not satisfied.

No regression conclusion should be made.

---

## Regression Severity

When a result is classified as `Regression`, severity may be recorded as:

- Minor
- Material
- Severe

Severity must be evidence-based.

### Minor

Use when:

- Degradation is limited.
- No critical failure exists.
- Quality gate remains PASS.
- The affected quality dimension does not materially compromise artifact reliability.

### Material

Use when:

- Quality degradation meaningfully affects artifact reliability, coverage, traceability, or usability.
- A high-impact criterion degrades materially.
- The quality gate changes from PASS to FAIL without a new critical failure.
- Multiple meaningful weaknesses appear.

### Severe

Use when:

- A new critical failure appears.
- Requirement Fidelity or Correctness becomes fundamentally unreliable.
- Multiple core quality dimensions degrade substantially.
- The artifact becomes unsafe or unreliable as a QA reference.

Severity must not be derived solely from an arbitrary score-delta threshold unless an approved threshold policy exists.

---

## Regression Decision Priority

When evidence points in different directions, review in the following order:

1. Comparison compatibility
2. New critical failures
3. Quality-gate change
4. High-impact criterion degradation
5. Other material criterion degradation
6. Score delta
7. Quality-band movement
8. Supporting quality changes

This ordering prevents aggregate score movement from hiding more important quality defects.

It is an evaluation priority, not a replacement for evidence-based judgment.

---

## Example A — No Regression

Baseline:

- Score = `96.0`
- Result = PASS
- Critical Failures = None

Current:

- Score = `95.2`
- Result = PASS
- Same material criterion levels
- Critical Failures = None

Score Delta:

`95.2 - 96.0 = -0.8`

Outcome:

`No Regression`

Reason:

The score is slightly lower, but no material criterion, quality-gate, or critical-failure evidence indicates meaningful degradation.

---

## Example B — Criterion Regression

Baseline:

- Score = `94`
- C03 Completeness = L4
- Result = PASS

Current:

- Score = `89`
- C03 Completeness = L2
- Result = PASS
- Critical Failures = None

Outcome:

`Regression`

Severity:

`Material`

Reason:

Completeness is a high-impact criterion and has materially degraded even though the current artifact still passes the quality gate.

---

## Example C — Quality-Gate Regression

Baseline:

- Score = `88`
- Result = PASS

Current:

- Score = `82`
- Result = FAIL
- Critical Failures = None

Outcome:

`Regression`

Severity:

`Material`

Reason:

The current execution no longer satisfies the approved quality gate.

---

## Example D — New Critical Failure

Baseline:

- Score = `95`
- Result = PASS
- Critical Failures = None

Current:

- Score = `49`
- Result = FAIL
- Critical Failures:
  - CF-01 — Source Contradiction

Outcome:

`Regression`

Severity:

`Severe`

Reason:

A new critical failure has been introduced.

---

## Example E — Improvement

Baseline:

- Score = `87`
- C03 Completeness = L3
- C06 Traceability = L3

Current:

- Score = `94`
- C03 Completeness = L4
- C06 Traceability = L4
- No criterion regression
- Critical Failures = None

Outcome:

`Improvement`

Reason:

The current result demonstrates meaningful criterion-level and overall quality improvement.

---

## Example F — Mixed Change

Baseline:

- C03 Completeness = L4
- C06 Traceability = L3
- Score = `91`

Current:

- C03 Completeness = L3
- C06 Traceability = L4
- Score = `91`

Outcome:

`Mixed Change`

Reason:

Traceability improves while completeness degrades.

The unchanged final score does not mean the quality profile is unchanged.

---

## Example G — Non-Comparable

Baseline:

- Dataset Version = `1.0`
- Requirement defines one approval workflow.

Current:

- Dataset Version = `2.0`
- Requirement introduces a materially different approval workflow.

Outcome:

`Non-Comparable`

Reason:

The underlying business behavior changed materially, so the old baseline no longer represents an equivalent evaluation target.

---

## Repeated-Run Regression

Some QA-AI executions may produce variable outputs across repeated runs.

When repeated execution is part of the benchmark, regression analysis may compare:

- Mean score
- Median score
- Minimum score
- Maximum score
- PASS rate
- Critical-failure rate
- Criterion-level degradation frequency

The comparison must identify:

- Number of baseline runs
- Number of current runs
- Execution configuration
- Aggregation method

Like-for-like statistics should be compared.

---

## PASS-Rate Regression

For repeated runs:

`PASS Rate = Passing Runs / Total Runs × 100`

Example:

Baseline:

`5 / 5 = 100%`

Current:

`4 / 5 = 80%`

The lower PASS rate is regression evidence even when average score remains relatively strong.

Its significance should be reviewed together with the failed-run evidence.

---

## Critical-Failure-Rate Regression

For repeated runs:

`Critical Failure Rate = Runs with ≥1 Critical Failure / Total Runs × 100`

Example:

Baseline:

`0 / 10 = 0%`

Current:

`2 / 10 = 20%`

A newly observed critical-failure rate is strong regression evidence.

The affected runs and failure categories must remain visible.

---

## Stability Regression

Quality consistency may regress even when average score remains similar.

Example:

Baseline scores:

`93, 94, 93, 94, 93`

Current scores:

`98, 82, 97, 81, 98`

The average alone does not represent the increased instability.

When repeated-run data exists, regression reporting should preserve:

- Score range
- Minimum score
- PASS rate
- Critical-failure rate
- Criterion-level variability

Formal statistical stability thresholds should not be invented without sufficient empirical benchmark evidence.

---

## Benchmark Suite Regression

A regression benchmark suite may contain multiple controlled datasets and artifact types.

Each comparison unit should first receive an independent regression result.

Suite-level reporting may then summarize:

- Total comparisons
- No Regression count
- Regression count
- Improvement count
- Mixed Change count
- Non-Comparable count
- Minor regression count
- Material regression count
- Severe regression count
- Mean score delta
- PASS-rate change
- Critical-failure-rate change

Individual severe regressions must remain visible and must not disappear inside aggregate metrics.

---

## Complexity-Aware Regression

When datasets are classified by complexity, regression results should remain identifiable by complexity level.

Example:

| Complexity | Baseline | Current | Result |
|---|---:|---:|---|
| Simple | 96 | 96 | No Regression |
| Medium | 94 | 91 | Review criterion evidence |
| Complex | 91 | 82 | Regression |

This can reveal degradation that appears primarily on more complex requirements.

The benchmark reports the observed pattern.

It must not infer technical root cause without evidence.

---

## Artifact-Level Regression

Different QA artifacts may regress independently.

Example:

| Artifact | Result |
|---|---|
| Requirement Analysis | No Regression |
| Business Rules | No Regression |
| Risk Analysis | Regression |
| Test Scenarios | Regression |
| Test Cases | Regression |
| Regression Analysis | No Regression |

Artifact-level results should remain visible before any framework-level aggregation.

This helps identify where quality degradation enters the QA-AI artifact chain.

---

## Regression Propagation

A downstream artifact may degrade because an upstream artifact degraded.

Example:

`Requirement Analysis → Business Rules → Test Scenarios → Test Cases`

If an upstream artifact loses a business rule, downstream scenario and test-case coverage may also decline.

Regression analysis should preserve traceability between affected artifacts when evidence exists.

It must not automatically assume causation solely from execution order.

---

## Change Attribution

Regression benchmarking detects quality change.

It does not automatically prove the root cause.

Potential change areas may include:

- Skill
- Workflow
- Prompt
- Shared knowledge
- Standard
- Adapter
- Platform
- Model
- Framework configuration

Known configuration changes should be recorded.

A specific cause should only be stated when supported by evidence.

---

## Regression Investigation

When regression is identified, investigation should focus on the evidence that caused the classification.

### Minor Regression

Review:

- Affected criterion
- Whether the issue repeats
- Whether it indicates an emerging trend

### Material Regression

Review:

- High-impact criterion changes
- Coverage loss
- Traceability loss
- Scope expansion
- Assumption leakage
- Relevant framework changes

### Severe Regression

Review immediately:

- Critical-failure evidence
- Requirement fidelity
- Correctness
- Current execution configuration
- Recent changes affecting the evaluated capability

The regression benchmark identifies quality degradation.

It does not define deployment, rollback, or release policy.

---

## Baseline Update After Improvement

A better current result does not automatically replace the approved baseline.

The lifecycle remains:

`Improved Result → Baseline Candidate → Review → Validate → Approve → New Baseline Version`

Baseline governance remains defined by:

`datasets/benchmark/baseline/`

This prevents uncontrolled baseline drift.

---

## Regression After Requirement Change

A material requirement change should not be reported as QA-AI regression merely because the current artifact differs from the old baseline.

The recommended flow is:

1. Review source compatibility.
2. Version the dataset when necessary.
3. Review affected golden outputs.
4. Re-evaluate the updated QA-AI artifacts.
5. Establish a compatible baseline.

Regression benchmarking should measure framework quality change, not intentional product-requirement evolution.

---

## Regression After Evaluation Model Change

If the evaluation model changes materially:

- Review compatibility.
- Do not directly compare incompatible scores.
- Re-evaluate the historical artifact under the new model when appropriate, or
- Establish a new baseline.

Relevant changes may include:

- Criteria
- Rubric
- Scoring factors
- Criterion weights
- Quality gate
- Critical-failure rules
- Evaluation profile

Evaluation changes must not silently create artificial regression.

---

## Recommended Regression Record

A regression comparison should preserve:

| Field | Description |
|---|---|
| Regression ID | Unique regression comparison identifier |
| Benchmark ID | Regression benchmark definition |
| Baseline ID | Approved baseline |
| Baseline Version | Baseline version |
| Current Evaluation ID | Current evaluation |
| Dataset ID | Controlled dataset |
| Dataset Version | Dataset version or immutable reference |
| Artifact Type | Evaluated artifact or capability |
| Framework Version | Current framework version |
| Evaluation Criteria | Criteria definition |
| Evaluation Rubric | Rubric definition |
| Scoring Model | Scoring definition |
| Evaluation Profile | Evaluation profile |
| Baseline Score | Baseline unrounded score |
| Current Score | Current unrounded score |
| Score Delta | Current minus baseline |
| Criterion Regressions | Degraded criteria |
| Criterion Improvements | Improved criteria |
| Critical Failure Changes | Critical-failure differences |
| Quality-Gate Change | PASS/FAIL relationship |
| Quality-Band Change | Quality-band movement |
| Classification | Regression outcome |
| Severity | Minor / Material / Severe when applicable |
| Evidence | Supporting regression evidence |
| Notes | Relevant comparison context |

---

## Example Regression Record

Example serialized representation:

    regression_id: REG-REQ-AUTH-001-TC-001
    benchmark_id: BENCH-REGRESSION-001

    baseline:
      id: BASE-REQ-AUTH-001-TC-001
      version: 1.0.0
      unrounded_score: 96.4
      final_score: 96
      quality_band: Excellent
      result: PASS

    current:
      evaluation_id: EVAL-RUN-042
      unrounded_score: 91.2
      final_score: 91
      quality_band: Good
      result: PASS

    comparison:
      score_delta: -5.2

      criterion_regressions:
        C03:
          from: L4
          to: L3

        C06:
          from: L4
          to: L3

      criterion_improvements: {}

      critical_failure_changes: []

      classification: Regression
      severity: Material

The record preserves the comparison result.

It does not replace:

- Baseline evidence
- Current evaluation evidence
- Criterion-level rubric evidence

---

## Regression Comparison Procedure

For each regression benchmark:

1. Select the approved baseline.
2. Verify baseline validity.
3. Identify the current evaluation.
4. Verify dataset compatibility.
5. Verify artifact compatibility.
6. Verify evaluation configuration compatibility.
7. Record relevant execution configuration.
8. Compare critical failures.
9. Compare quality-gate results.
10. Compare criterion levels.
11. Calculate score delta.
12. Review quality-band movement.
13. Review supporting evidence.
14. Apply regression decision priority.
15. Assign the regression classification.
16. Assign severity when regression exists.
17. Preserve the comparison record.
18. Include the result in suite or trend analysis when applicable.

---

## Regression Fairness Controls

Regression benchmarking should preserve the following controls.

### Same Business Truth

The baseline and current execution must represent materially equivalent source behavior.

### Same Evaluation Standard

Evaluation definitions must remain compatible.

### No Exact-Match Requirement

Different wording, ordering, formatting, or valid decomposition is not regression by itself.

### No Aggregate Masking

Critical failures and material criterion degradation must remain visible even when aggregate scores remain strong.

### No Score-Only Decisions

Numeric score changes must be interpreted with criterion and quality-gate evidence.

### No Unsupported Root Cause

Regression detection must not be converted into technical attribution without evidence.

### Transparent Configuration

Known changes that may affect execution should be recorded when available.

---

## Trend Analysis

Regression results may be tracked across framework versions.

Example:

`v1.0 → v1.1 → v1.2 → v1.3`

Trend analysis may examine:

- Score movement
- Criterion-level patterns
- PASS-rate movement
- Critical-failure frequency
- Artifact-specific regression
- Complexity-specific regression

Only compatible benchmark results should be combined into a trend.

Historical results should retain their original benchmark and evaluation versions.

---

## Regression Benchmark Versioning

Material changes to regression rules should be versioned.

Examples include changes to:

- Regression classifications
- Severity definitions
- Decision priority
- Compatibility rules
- Repeated-run aggregation
- Approved numeric threshold policies

Results produced using materially different regression benchmark definitions must not be presented as directly equivalent without compatibility assessment.

---

## Regression Benchmark Boundaries

This benchmark must not:

- Redefine canonical criteria.
- Redefine rubric levels.
- Redefine scoring formulas.
- Automatically replace approved baselines.
- Require exact golden-output matching.
- Treat every negative score delta as regression.
- Hide criterion degradation behind aggregate scores.
- Hide critical failures through averaging.
- Interpret intentional requirement changes as QA-AI regression.
- Invent numeric thresholds without benchmark evidence.
- Infer root cause without supporting evidence.
- Define deployment or rollback policy.
- Rank execution platforms.

Platform comparison remains the responsibility of the cross-platform benchmark.

---

## Validation Checklist

Before accepting a regression result, verify:

- Baseline exists and is approved.
- Baseline remains valid.
- Baseline version is identified.
- Dataset is compatible.
- Artifact or capability is compatible.
- Evaluation criteria are compatible.
- Rubric is compatible.
- Scoring model is compatible.
- Evaluation profile is compatible.
- Current result was independently evaluated.
- Relevant execution configuration is recorded.
- Unrounded scores are used when available.
- Score delta is calculated correctly.
- Criterion-level changes are reviewed.
- Critical-failure changes are reviewed.
- Quality-gate change is reviewed.
- Quality-band movement is reviewed.
- N/A applicability remains valid.
- Classification is supported by evidence.
- Severity is supported by evidence when applicable.
- Non-comparable cases are not forced into regression classifications.
- Supporting evidence is retained.

---

## Final Regression Benchmark Definition

A QA-AI regression benchmark is:

> A controlled, evidence-based comparison between an approved quality baseline and a compatible current QA-AI evaluation used to identify meaningful degradation in previously validated QA quality.

The canonical regression benchmark provides:

- Baseline-to-current comparison
- Compatibility validation
- Score-delta analysis
- Criterion-level regression detection
- Critical-failure regression detection
- Quality-gate regression detection
- Quality-band tracking
- Regression severity classification
- Improvement and Mixed Change handling
- Non-comparability protection
- Repeated-run quality analysis
- Stability regression visibility
- Benchmark-suite aggregation
- Complexity-aware regression analysis
- Artifact-level regression analysis
- Version-aware regression governance
- Protection against unsupported numeric thresholds

It enables QA-AI to detect meaningful quality loss while avoiding false regression signals caused by harmless output variation.
