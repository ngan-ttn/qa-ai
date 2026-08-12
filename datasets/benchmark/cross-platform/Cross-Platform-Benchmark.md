# Cross-Platform Benchmark

## Benchmark Metadata

- Benchmark ID: `BENCH-CROSS-PLATFORM-001`
- Benchmark Type: `Cross-Platform`
- Scope: `QA-AI Artifact Quality Across Execution Platforms`
- Status: `Approved`
- Purpose: Define how comparable QA-AI executions are evaluated and compared across supported execution platforms.

---

## Purpose

This document defines the canonical cross-platform benchmark model for QA-AI.

Cross-platform benchmarking compares QA-AI quality across different execution platforms while controlling the inputs and evaluation configuration used for each execution.

It answers:

> When equivalent QA-AI work is executed on different platforms, how should artifact quality be compared fairly and consistently?

The benchmark is designed to compare quality rather than textual similarity.

Supported comparisons may include platforms such as:

- ChatGPT
- Claude
- Future supported QA-AI execution platforms

A platform is included only when an implementation exists and the execution configuration is sufficiently documented for comparison.

This benchmark does not assume that different platforms must generate identical wording, structure, or reasoning paths.

---

## Benchmark Position in the Evaluation Flow

The canonical cross-platform flow is:

`Controlled Dataset → Equivalent QA-AI Execution → Platform Outputs → Canonical Evaluation → Scored Results → Cross-Platform Comparison`

Conceptually:

`Platform A Result ↔ Platform B Result`

under equivalent comparison conditions.

Cross-platform benchmarking consumes evaluated results.

It does not replace:

- Source datasets
- Golden outputs
- Evaluation criteria
- Evaluation rubrics
- Scoring models
- Approved baselines

---

## Comparison Objective

The purpose of cross-platform benchmarking is to determine whether supported platforms can execute the same QA-AI capability with materially comparable quality.

Comparison may examine:

- Overall artifact quality
- Criterion-level quality
- Critical failures
- Quality-gate result
- Coverage characteristics
- Source-grounding quality
- Traceability quality
- Artifact consistency

The benchmark should reveal meaningful quality differences without penalizing harmless implementation variation.

---

## Comparison Unit

The smallest canonical comparison unit is:

`Dataset + Artifact/Capability + Evaluation Configuration + Platform Results`

Example:

`REQ-AUTH-001 + Test Cases + EVAL-SCORING-001 + ChatGPT + Claude`

Each platform result remains independently traceable.

The comparison record references those results rather than replacing them.

---

## Comparison Eligibility

Two or more platform results may be directly compared only when the comparison conditions are sufficiently equivalent.

### Required Compatibility

The following should match:

1. Dataset ID
2. Dataset version or immutable dataset reference
3. Artifact type or evaluated capability
4. QA-AI framework contract
5. Evaluation criteria
6. Evaluation rubric
7. Scoring model
8. Evaluation profile

Where execution configuration can materially affect output, the comparison must also record:

- Skill version
- Workflow version
- Prompt version
- Knowledge-pack version
- Adapter version
- Framework version
- Model identifier when available

These fields do not always need to be identical across platforms.

Differences must be known and recorded so the benchmark result can be interpreted correctly.

---

## Controlled Inputs

Cross-platform comparison should use equivalent authoritative inputs.

Controlled inputs may include:

- Requirement dataset
- Supporting context
- Approved fixtures
- Upstream QA artifacts
- Skill input contract
- Workflow input contract

One platform must not receive materially richer business information than another unless the benchmark intentionally evaluates that difference.

If input differences materially affect expected output quality, the executions are not directly comparable under the standard cross-platform benchmark.

---

## Equivalent Execution Contract

Platforms may use different adapters or platform-native mechanisms.

They do not need identical internal implementations.

However, they must execute the same logical QA-AI contract.

Equivalent execution means that each platform receives materially equivalent:

- Task objective
- Skill or Workflow responsibility
- Input information
- Output contract
- Shared standards
- Applicable knowledge
- Evaluation target

The benchmark evaluates framework behavior, not whether each platform uses identical technical mechanics.

---

## Platform-Specific Adaptation

Platform adapters may translate QA-AI instructions into platform-compatible execution forms.

Acceptable differences may include:

- Instruction packaging
- Context injection
- File-loading mechanism
- Skill invocation mechanism
- Platform-native formatting
- Tool orchestration

These differences are allowed when they preserve the canonical QA-AI contract.

An adapter difference becomes benchmark-relevant when it materially affects artifact quality.

---

## Output Equivalence

Cross-platform outputs are not required to be textually identical.

Two outputs may be considered quality-equivalent even when they differ in:

- Wording
- Section ordering
- Explanation style
- Item decomposition
- Table formatting
- Identifier presentation
- Level of concise supporting detail

provided that both satisfy the applicable evaluation criteria.

The benchmark must therefore compare evaluated quality rather than raw text similarity.

---

## Material Output Differences

A difference is material when it affects one or more quality criteria.

Examples include:

- One platform omits a source-defined business rule.
- One platform invents unsupported behavior.
- One platform misses a critical boundary.
- One platform generates an incorrect expected result.
- One platform breaks traceability.
- One platform introduces unsupported implementation assumptions.

Material differences should appear through criterion-level evaluation and critical-failure evidence.

---

## Non-Material Output Differences

Differences should normally be treated as non-material when they do not affect the evaluation criteria.

Examples include:

- Different but equivalent wording
- Different Markdown formatting
- Different order of equivalent items
- Different naming of explanatory subsections
- Different valid decomposition of the same QA objective

Non-material differences must not be converted into artificial platform-quality gaps.

---

## Golden Output Usage

Golden outputs may support cross-platform evaluation as reviewed reference interpretations.

They must not be used as exact-match answer keys.

The benchmark must not prefer a platform merely because its output resembles the golden output more closely.

A platform output may differ substantially in wording and still achieve equivalent or better quality when evaluated against the canonical criteria and rubric.

---

## Baseline Usage

Cross-platform comparison may optionally reference an approved baseline.

A baseline can answer:

> How does each platform compare with an already approved quality reference?

Conceptually:

`Approved Baseline`

compared with:

`Platform A`

and:

`Platform B`

The baseline does not automatically determine the cross-platform winner.

Each platform result must still be evaluated independently.

---

## Evaluation Independence

Each platform output should be evaluated independently before comparison.

Recommended sequence:

1. Evaluate Platform A.
2. Record its criterion levels and score.
3. Evaluate Platform B.
4. Record its criterion levels and score.
5. Verify evaluation compatibility.
6. Compare the resulting evaluation records.

Evaluators should avoid lowering or increasing one platform's criterion rating merely because another platform performed differently.

---

## Comparison Dimensions

Cross-platform comparison uses multiple dimensions rather than final score alone.

### Final Score

Compare normalized artifact-quality scores produced by the same compatible scoring model.

### Quality Band

Compare resulting quality classifications.

### Quality-Gate Result

Compare whether each platform passes the applicable quality gate.

### Criterion Levels

Compare `C01–C12` results to identify where quality differences occur.

### Critical Failures

Compare confirmed critical-failure types and counts.

### N/A Applicability

Verify that criteria excluded as `N/A` are applied consistently across equivalent outputs.

---

## Score Delta

For two platform results:

`Score Delta = Platform A Unrounded Score - Platform B Unrounded Score`

The absolute difference is:

`Absolute Score Delta = |Platform A Unrounded Score - Platform B Unrounded Score|`

Unrounded scores should be preferred for comparison when available.

### Example

Platform A:

`94.6`

Platform B:

`92.8`

Then:

`Score Delta = 94.6 - 92.8 = +1.8`

`Absolute Score Delta = 1.8`

A positive signed delta means Platform A scored higher.

A negative signed delta means Platform B scored higher.

---

## Score Delta Interpretation

Score delta is descriptive evidence.

It must not be interpreted in isolation.

A small score difference may hide a material criterion difference.

A larger score difference may result from several non-critical weaknesses.

Therefore, cross-platform interpretation must consider:

1. Final score
2. Quality band
3. PASS/FAIL result
4. Criterion-level differences
5. Critical failures
6. Supporting evidence

The canonical cross-platform benchmark does not declare a universal winner solely from score delta.

---

## Criterion-Level Comparison

For each criterion, compare the rubric levels assigned to each platform.

Example:

| Criterion | Platform A | Platform B | Difference |
|---|---|---|---|
| C01 | L4 | L4 | Equivalent |
| C02 | L4 | L3 | A higher |
| C03 | L3 | L3 | Equivalent |
| C04 | L4 | L4 | Equivalent |

Criterion-level comparison helps identify the source of overall score differences.

It also prevents a final score from hiding meaningful quality behavior.

---

## Criterion Difference Representation

For comparison reporting, rubric levels may be ordered as:

`L4 > L3 > L2 > L1 > L0`

`N/A` is excluded from ordinal comparison.

When both platforms validly mark a criterion `N/A`, the criterion is:

`Not Applicable`

When only one equivalent execution marks a criterion `N/A`, the evaluator should verify whether applicability was handled consistently before treating the results as directly comparable.

---

## Critical Failure Comparison

Critical failures receive explicit comparison attention.

Example:

| Platform | Final Score | Critical Failure | Result |
|---|---:|---|---|
| Platform A | 91 | None | PASS |
| Platform B | 49 | CF-01 | FAIL |

The benchmark must not describe these results as approximately equivalent merely because other criteria are similar.

A critical failure represents a material reliability difference.

---

## Quality-Gate Comparison

Platform results may be classified as:

### Both Pass

Both results meet the canonical quality gate.

This means both satisfy the minimum approved quality standard.

It does not mean their quality is identical.

### One Passes, One Fails

The difference is material and should be investigated at criterion and evidence level.

### Both Fail

Neither platform currently meets the required quality gate.

The comparison should identify whether:

- They fail for the same reasons.
- They fail in different criteria.
- One has a critical failure.
- One is materially closer to passing.

---

## Cross-Platform Outcome Classification

The benchmark may classify a comparison using the following outcome labels.

### Comparable — Equivalent Quality

Use when:

- Results are comparison-compatible.
- Both satisfy the same quality-gate status.
- No material criterion difference changes the practical QA reliability conclusion.
- No asymmetric critical failure exists.

This classification does not require identical scores.

### Comparable — Platform A Higher Quality

Use when:

- Results are comparison-compatible.
- Platform A demonstrates a meaningful quality advantage supported by criterion-level evidence.

### Comparable — Platform B Higher Quality

Use when:

- Results are comparison-compatible.
- Platform B demonstrates a meaningful quality advantage supported by criterion-level evidence.

### Comparable — Mixed Strengths

Use when:

- Results are comparison-compatible.
- Platforms demonstrate materially different strengths and weaknesses.
- No single overall quality conclusion is sufficiently supported.

### Non-Comparable

Use when material compatibility conditions are not satisfied.

Examples:

- Different source dataset behavior
- Different artifact type
- Incompatible scoring model
- Materially different evaluation profile
- Unequal authoritative input
- Missing execution metadata that prevents defensible interpretation

---

## Meaningful Quality Advantage

A platform should not be declared higher quality solely because its numeric score is slightly higher.

A meaningful quality advantage should be supported by one or more of:

- Different quality-gate result
- Different quality band
- Material criterion-level improvement
- Absence of a critical failure present in the other platform
- Repeated advantage across controlled benchmark cases
- Better source fidelity, correctness, completeness, or other high-impact quality dimension

The benchmark intentionally avoids defining a universal score-delta threshold here.

A later benchmark policy may define statistical or operational significance when sufficient benchmark data exists.

---

## Single-Run Limitation

A single execution can reveal quality differences for a specific benchmark case.

It does not establish that one platform is universally better.

Cross-platform conclusions should distinguish:

- Case-level result
- Dataset-level pattern
- Benchmark-suite pattern

Broader platform conclusions require multiple controlled benchmark cases.

---

## Repeated Execution

When platform outputs are non-deterministic, repeated executions may be used.

A repeated benchmark should record:

- Number of runs
- Execution configuration
- Score for each run
- Criterion-level results
- Critical failures
- Aggregate summary

Possible aggregate statistics may include:

- Mean score
- Median score
- Minimum score
- Maximum score
- PASS rate
- Critical-failure rate

The benchmark record must identify when results are aggregated from repeated executions.

---

## Aggregate Score

For `n` comparable executions of the same platform:

`Mean Score = Sum of Unrounded Scores / n`

Example:

Scores:

- `92.0`
- `94.0`
- `91.0`

Then:

`Mean Score = (92 + 94 + 91) / 3 = 92.33`

Mean score alone must not replace critical-failure or criterion-level analysis.

---

## PASS Rate

For repeated executions:

`PASS Rate = Passing Runs / Total Runs × 100`

Example:

- Total runs = `5`
- PASS runs = `4`

Then:

`PASS Rate = 4 / 5 × 100 = 80%`

PASS rate may help evaluate execution consistency across platforms.

---

## Critical Failure Rate

For repeated executions:

`Critical Failure Rate = Runs with ≥1 Critical Failure / Total Runs × 100`

Example:

- Total runs = `10`
- Runs containing critical failures = `2`

Then:

`Critical Failure Rate = 2 / 10 × 100 = 20%`

This metric helps distinguish a platform that occasionally produces severe defects from one that produces only minor quality variation.

---

## Benchmark Suite Comparison

A cross-platform benchmark suite may contain multiple controlled datasets.

Example conceptual structure:

`Simple Dataset + Medium Dataset + Complex Dataset`

For each platform, retain individual case results before aggregation.

A suite-level comparison may summarize:

- Number of benchmark cases
- Mean score
- Median score
- Minimum score
- PASS rate
- Critical-failure rate
- Criterion-level distribution
- Outcome by complexity level

Suite aggregation must not erase individual critical failures.

---

## Complexity-Aware Reporting

If datasets are categorized by complexity, results should remain identifiable by complexity class.

Example:

| Complexity | Platform A | Platform B |
|---|---:|---:|
| Simple | 96 | 96 |
| Medium | 93 | 91 |
| Complex | 89 | 82 |

This may reveal that platform quality diverges as requirement complexity increases.

The cross-platform benchmark reports this pattern.

It does not infer the technical cause without supporting evidence.

---

## Recommended Comparison Record

A cross-platform comparison should preserve:

| Field | Description |
|---|---|
| Comparison ID | Unique comparison identifier |
| Benchmark ID | Cross-platform benchmark definition |
| Dataset ID | Controlled dataset |
| Dataset Version | Dataset version or immutable reference |
| Artifact Type | Evaluated artifact or capability |
| Framework Version | QA-AI framework version |
| Evaluation Criteria | Criteria definition |
| Evaluation Rubric | Rubric definition |
| Scoring Model | Scoring model |
| Evaluation Profile | Evaluation profile |
| Platform Results | Independent evaluated platform results |
| Score Delta | Signed score difference |
| Absolute Score Delta | Absolute score difference |
| Criterion Differences | Criterion-level comparison |
| Critical Failure Differences | Critical-failure comparison |
| Quality-Gate Comparison | PASS/FAIL relationship |
| Outcome | Cross-platform outcome classification |
| Evidence | Supporting comparison evidence |
| Notes | Relevant interpretation context |

---

## Example Comparison Record

Example serialized representation:

    comparison_id: CROSS-REQ-AUTH-001-TC-001
    benchmark_id: BENCH-CROSS-PLATFORM-001

    dataset:
      id: REQ-AUTH-001
      artifact_type: Test-Cases

    evaluation:
      criteria: EVAL-CRITERIA-001
      rubric: EVAL-RUBRIC-001
      scoring_model: EVAL-SCORING-001
      profile: default-artifact-quality

    platforms:
      chatgpt:
        final_unrounded_score: 96.4
        final_score: 96
        quality_band: Excellent
        result: PASS
        critical_failures: []

      claude:
        final_unrounded_score: 94.8
        final_score: 95
        quality_band: Excellent
        result: PASS
        critical_failures: []

    score_delta:
      chatgpt_minus_claude: 1.6
      absolute: 1.6

    outcome: Comparable — Equivalent Quality

The outcome is not determined from the `1.6` score delta alone.

Criterion-level evidence must support the interpretation.

---

## Comparison Procedure

For each cross-platform benchmark:

1. Select the controlled dataset.
2. Identify the artifact or capability.
3. Define the execution contract.
4. Confirm equivalent authoritative inputs.
5. Record relevant execution configuration.
6. Execute the QA-AI capability on each platform.
7. Preserve each platform output independently.
8. Evaluate each output independently.
9. Apply the same compatible scoring model.
10. Verify comparison compatibility.
11. Compare final scores.
12. Compare quality bands.
13. Compare quality-gate results.
14. Compare criterion levels.
15. Compare critical failures.
16. Review material output differences.
17. Assign the cross-platform outcome.
18. Preserve evidence and comparison metadata.

---

## Fairness Controls

Cross-platform benchmarking should control avoidable bias.

### Same Business Information

Platforms should receive equivalent requirement information.

### Same QA Objective

Platforms should execute the same logical QA-AI task.

### Same Evaluation Standard

Outputs should be judged using compatible criteria, rubric, and scoring.

### Independent Evaluation

One platform's output should not define the expected answer for another.

### No Style Preference

Platform-specific prose style should not affect quality unless it materially affects clarity or another canonical criterion.

### No Exact-Match Bias

Similarity to a golden output must not be treated as quality by itself.

### Transparent Configuration

Known execution differences that may affect interpretation should be recorded.

---

## Handling Missing Platform Metadata

Some platforms may not expose all execution metadata.

Missing metadata does not automatically invalidate a comparison.

The evaluator should determine whether the missing information materially prevents:

- Reproduction
- Compatibility verification
- Result interpretation

If it does, classify the comparison as:

`Non-Comparable`

If it does not, record the limitation and continue.

Unknown values must not be invented.

---

## Handling Platform Errors

If a platform fails to produce the requested artifact because of an execution or platform error, record the failure separately.

Examples:

- Invocation failure
- Context-loading failure
- Tool failure
- Output truncation
- Unsupported execution path

A platform execution failure should not automatically be converted into an artifact-quality `L0` unless the benchmark explicitly defines that failure as part of the evaluated capability.

The benchmark record should distinguish:

`Execution Failure`

from:

`Artifact Quality Failure`

---

## Cross-Platform Trend Analysis

Repeated benchmark suites may reveal quality trends over time.

Examples include:

- One platform improving after adapter changes
- Quality convergence across platforms
- Increased variance on complex requirements
- Recurring criterion weakness on one platform

Trend analysis should use compatible benchmark versions.

Results from materially different evaluation models must not be combined without an explicit compatibility rule.

---

## Relationship to Baseline Benchmark

Baseline benchmarking defines approved quality references.

Cross-platform benchmarking compares equivalent platform executions.

A cross-platform comparison may:

- Compare platforms directly.
- Compare each platform against the same baseline.
- Do both.

Conceptually:

`Baseline → Platform A`

`Baseline → Platform B`

and:

`Platform A ↔ Platform B`

Baseline governance remains defined by:

`datasets/benchmark/baseline/`

---

## Relationship to Regression Benchmark

Cross-platform benchmarking asks:

> How do equivalent platforms compare?

Regression benchmarking asks:

> Has quality decreased relative to a previous approved reference?

These are different questions.

A platform may outperform another platform while still regressing relative to its own approved baseline.

Regression rules belong under:

`datasets/benchmark/regression/`

---

## Benchmark Versioning

Material changes to cross-platform comparison rules should be versioned.

Examples include changes to:

- Compatibility requirements
- Outcome classification
- Aggregation rules
- Repeated-run metrics
- Platform comparison semantics

Results produced under materially different benchmark definitions must not be presented as directly equivalent without a compatibility assessment.

---

## Cross-Platform Benchmark Boundaries

This benchmark must not:

- Redefine canonical criteria.
- Redefine rubric levels.
- Redefine scoring weights or formulas.
- Replace artifact evaluation with text similarity.
- Require identical platform outputs.
- Assume platform-specific wording is a defect.
- Declare universal platform superiority from one case.
- Hide critical failures through aggregate scores.
- Invent missing platform metadata.
- Define regression thresholds.
- Automatically promote a platform result to baseline.

---

## Validation Checklist

Before accepting a cross-platform comparison, verify:

- Dataset is identical or materially equivalent across executions.
- Dataset version is known.
- Artifact or capability is the same.
- QA-AI execution objective is equivalent.
- Authoritative input is equivalent.
- Evaluation criteria are compatible.
- Rubric is compatible.
- Scoring model is compatible.
- Evaluation profile is compatible.
- Relevant execution configuration is recorded.
- Platform outputs were evaluated independently.
- Score comparison uses unrounded values when available.
- Criterion-level differences were reviewed.
- Critical failures were reviewed.
- `N/A` applicability is consistent.
- Material differences are distinguished from stylistic differences.
- Outcome is supported by evidence.
- Comparison limitations are documented.

---

## Final Cross-Platform Benchmark Definition

A QA-AI cross-platform benchmark is:

> A controlled, evidence-based comparison of independently evaluated QA-AI executions performed on equivalent inputs and judged using compatible evaluation standards.

The canonical cross-platform benchmark provides:

- Fair comparison conditions
- Platform-independent quality evaluation
- Criterion-level comparison
- Critical-failure visibility
- Score and quality-gate comparison
- Repeated-run consistency metrics
- Benchmark-suite aggregation
- Complexity-aware reporting
- Explicit non-comparability handling
- Protection against exact-output bias

It enables QA-AI to determine whether supported execution platforms deliver materially comparable QA quality without requiring them to produce identical artifacts.
