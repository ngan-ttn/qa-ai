# Artifact Quality Scoring

## Evaluation Metadata

- Evaluation ID: `EVAL-SCORING-001`
- Evaluation Type: `Scoring Model`
- Applies To:
  - `EVAL-CRITERIA-001`
  - `EVAL-RUBRIC-001`
- Scope: `QA-AI Generated Artifacts`
- Status: `Approved`
- Maximum Score: `100`
- Purpose: Convert criterion-level rubric results into consistent and measurable QA artifact quality scores.

---

## Purpose

This document defines the canonical scoring model used to convert QA-AI artifact rubric evaluations into measurable quality results.

It operates after:

`Criteria → Rubric → Scoring`

The resulting scores may be consumed by downstream evaluation activities such as:

- Baseline benchmarking
- Cross-platform comparison
- Framework regression evaluation
- Skill quality evaluation
- Workflow quality evaluation

The scoring model answers:

> How should criterion-level rubric results be converted into consistent and comparable quality scores?

It does not redefine:

- Quality criteria
- Rubric-level definitions
- Source requirements
- Golden outputs
- Benchmark baselines
- Cross-platform comparison rules
- Benchmark regression thresholds

Those responsibilities belong to their respective evaluation layers.

---

## Scoring Principles

### Criterion-Based

Scores are derived only from the applicable canonical quality criteria.

No score may be introduced for an undocumented quality dimension.

### Rubric-Driven

Qualitative evaluation occurs before numeric scoring.

The canonical sequence is:

`Evidence → Criterion → Rubric Level → Score Factor → Weighted Score`

The scoring model must not independently reinterpret artifact quality.

### Weighted

Not all quality dimensions have equal impact.

Source fidelity, correctness, completeness, and traceability receive greater weight because defects in these areas can materially affect downstream QA artifacts.

### Severity-Aware

A high aggregate score must not hide a critical quality failure.

Critical failures therefore affect both the maximum final score and the final quality-gate result.

### N/A-Aware

A genuinely non-applicable criterion must not reduce the artifact score.

Its weight is excluded and the remaining applicable weight is normalized.

### Reproducible

Given the same:

- Criterion applicability
- Rubric levels
- Scoring profile
- Critical failures

the scoring model must produce the same result.

### Comparable

Scores use a normalized `0–100` scale so they can be consumed consistently by downstream benchmark and regression processes.

---

## Canonical Rubric Score Factors

Rubric levels map to numeric score factors as follows:

| Rubric Level | Label | Score Factor |
|---|---|---:|
| L4 | Excellent | 1.00 |
| L3 | Good | 0.80 |
| L2 | Partial | 0.50 |
| L1 | Poor | 0.25 |
| L0 | Failed | 0.00 |

`N/A` does not have a score factor.

A valid `N/A` criterion is excluded from the active-weight calculation.

---

## Default Evaluation Profile

The canonical default artifact-quality profile uses the following criterion weights.

| Criterion | Quality Dimension | Weight |
|---|---|---:|
| C01 | Requirement Fidelity | 15 |
| C02 | Correctness | 15 |
| C03 | Completeness | 12 |
| C04 | Scope Control | 8 |
| C05 | Assumption Control | 8 |
| C06 | Traceability | 10 |
| C07 | Clarity | 5 |
| C08 | Testability | 7 |
| C09 | Coverage Efficiency | 5 |
| C10 | Boundary and State Coverage | 5 |
| C11 | Risk Awareness | 5 |
| C12 | Internal Consistency | 5 |
| **Total** |  | **100** |

The profile gives the greatest influence to:

1. Requirement Fidelity
2. Correctness
3. Completeness
4. Traceability
5. Scope and assumption control

Supporting quality dimensions remain measurable without outweighing source-grounded correctness.

---

## Criterion Weighted Score

For every applicable criterion:

`Criterion Weighted Score = Criterion Weight × Rubric Score Factor`

### Example

For `C01`:

- Weight = `15`
- Rubric Level = `L3`
- L3 Score Factor = `0.80`

Calculation:

`15 × 0.80 = 12.00`

Therefore, `C01` contributes `12.00` weighted points.

---

## Raw Weighted Score

The Raw Weighted Score is the sum of the weighted scores for all applicable criteria.

`Raw Weighted Score = Σ Criterion Weighted Scores`

When all canonical criteria are applicable:

- Active Weight = `100`
- Maximum Raw Weighted Score = `100`

Example:

| Criterion | Weight | Level | Factor | Weighted Score |
|---|---:|---|---:|---:|
| C01 | 15 | L4 | 1.00 | 15.00 |
| C02 | 15 | L4 | 1.00 | 15.00 |
| C03 | 12 | L3 | 0.80 | 9.60 |

The calculation continues for every applicable criterion.

---

## Active Weight

The Active Weight is the sum of the configured weights for all applicable criteria.

`Active Weight = Σ Applicable Criterion Weights`

If every criterion applies:

`Active Weight = 100`

If one or more criteria are validly marked `N/A`, their weights are excluded.

---

## N/A Normalization

A criterion may be excluded only when:

1. The canonical criteria allow contextual applicability.
2. The rubric permits `N/A`.
3. The criterion is genuinely irrelevant to the evaluated artifact.
4. The evaluator records a justification.

The normalized score is calculated as:

`Normalized Score = (Raw Weighted Score / Active Weight) × 100`

### Example

Assume:

- `C11` has weight `5`.
- `C11` is validly marked `N/A`.
- Every remaining criterion receives `L4`.

Then:

`Active Weight = 95`

`Raw Weighted Score = 95`

Therefore:

`Normalized Score = (95 / 95) × 100 = 100`

The artifact is not penalized for a criterion that genuinely does not apply.

---

## Invalid N/A Handling

`N/A` must not be used to hide poor or uncertain performance.

If a criterion applies but evidence is incomplete:

- Do not automatically mark it `N/A`.
- Record the evidence limitation.
- Obtain additional evaluation evidence when possible.
- Apply the evaluation process defined for the available evidence.

Core quality criteria should normally remain applicable:

- C01 — Requirement Fidelity
- C02 — Correctness
- C03 — Completeness
- C04 — Scope Control
- C05 — Assumption Control
- C06 — Traceability
- C07 — Clarity
- C12 — Internal Consistency

Context-dependent applicability is more likely for:

- C08 — Testability
- C10 — Boundary and State Coverage
- C11 — Risk Awareness

Applicability must remain consistent with the canonical criteria and rubric definitions.

---

## Pre-Cap Score

After N/A normalization:

`Pre-Cap Score = Normalized Score`

If no criteria are `N/A`:

`Pre-Cap Score = Raw Weighted Score`

The Pre-Cap Score represents aggregate quality before critical-failure controls are applied.

---

## Critical Failure Scoring

Critical failures are identified by the rubric layer.

The scoring model determines their numeric and quality-gate impact.

A critical failure must not be treated only as an ordinary point deduction because strong performance in unrelated criteria could otherwise hide a foundational defect.

---

### CF-01 — Source Contradiction

Maximum Final Score:

`49`

Reason:

An artifact that directly contradicts authoritative source behavior cannot be treated as a reliable QA artifact.

---

### CF-02 — Fabricated Business Behavior

Maximum Final Score:

`49`

Reason:

Unsupported business behavior presented as confirmed truth compromises source fidelity and downstream reliability.

---

### CF-03 — Critical Coverage Omission

Maximum Final Score:

`69`

Reason:

The artifact may contain substantial valid content but remains materially incomplete in a business-critical area.

---

### CF-04 — Incorrect Critical Expected Result

Maximum Final Score:

`49`

Reason:

An executable artifact containing a critical incorrect expected result may validate incorrect system behavior.

---

### CF-05 — Broken Critical Traceability

Maximum Final Score:

`69`

Reason:

Critical downstream behavior without defensible source traceability weakens auditability and artifact reliability.

---

### CF-06 — Unsupported Scope Expansion

Maximum Final Score:

`59`

Reason:

Unsupported architecture, API, database, role, dependency, or business behavior represented as confirmed may misdirect downstream QA work.

---

### CF-07 — Internal Critical Conflict

Maximum Final Score:

`49`

Reason:

An artifact containing materially incompatible definitions cannot serve as a reliable QA reference.

---

## Critical Failure Cap Summary

| Critical Failure | Description | Maximum Final Score |
|---|---|---:|
| CF-01 | Source Contradiction | 49 |
| CF-02 | Fabricated Business Behavior | 49 |
| CF-03 | Critical Coverage Omission | 69 |
| CF-04 | Incorrect Critical Expected Result | 49 |
| CF-05 | Broken Critical Traceability | 69 |
| CF-06 | Unsupported Scope Expansion | 59 |
| CF-07 | Internal Critical Conflict | 49 |

---

## Multiple Critical Failures

When multiple critical failures are confirmed:

`Applied Critical Failure Cap = Lowest Applicable Cap`

Caps are not added together.

### Example

Confirmed failures:

- CF-03 → Cap `69`
- CF-06 → Cap `59`

Applied cap:

`59`

This avoids arbitrary compound penalties while ensuring that the most severe confirmed defect controls the maximum score.

---

## Final Score Calculation

The canonical calculation order is:

1. Determine applicable criteria.
2. Assign rubric levels.
3. Convert rubric levels to score factors.
4. Calculate weighted criterion scores.
5. Sum the Raw Weighted Score.
6. Calculate Active Weight.
7. Normalize the score when valid `N/A` criteria exist.
8. Determine the Pre-Cap Score.
9. Identify confirmed critical failures.
10. Determine the lowest applicable critical-failure cap.
11. Apply the cap.
12. Round the Final Score.
13. Determine Quality Band.
14. Determine PASS or FAIL.

If at least one critical-failure cap applies:

`Final Unrounded Score = min(Pre-Cap Score, Applied Critical Failure Cap)`

Otherwise:

`Final Unrounded Score = Pre-Cap Score`

---

## Rounding Rule

Intermediate calculations should retain at least two decimal places.

The final score is rounded to the nearest whole number using conventional half-up rounding.

Examples:

- `92.40 → 92`
- `92.50 → 93`
- `84.49 → 84`
- `84.50 → 85`

Implementations should preserve the unrounded score internally when downstream benchmark comparison requires greater precision.

---

## Quality Bands

| Final Score | Quality Band | Interpretation |
|---|---|---|
| 95–100 | Excellent | High-quality artifact with no material defect preventing intended use |
| 85–94 | Good | Strong artifact with only limited improvement required |
| 70–84 | Acceptable | Meaningfully usable but requires correction before meeting the canonical quality gate |
| 50–69 | Weak | Significant quality problems require substantial revision |
| 0–49 | Failed | Artifact is unreliable for its intended QA purpose |

Quality Band describes artifact quality.

It does not independently determine the final quality-gate result.

---

## Default Quality Gate

The default QA-AI artifact score threshold is:

`PASS Threshold = 85`

Score-only interpretation:

| Final Score | Score Threshold Result |
|---|---|
| 85–100 | Meets score threshold |
| 0–84 | Does not meet score threshold |

However, the final result must also consider unresolved critical failures.

---

## Critical Failure Gate

Any unresolved confirmed critical failure forces the final result to:

`FAIL`

This applies to:

- CF-01
- CF-02
- CF-03
- CF-04
- CF-05
- CF-06
- CF-07

The artifact must be corrected and re-evaluated before it can pass.

---

## Final Result Rule

An artifact receives:

`PASS`

only when both conditions are true:

1. `Final Score ≥ 85`
2. `No unresolved critical failure exists`

Otherwise:

`FAIL`

Formally:

`PASS = (Final Score ≥ 85) AND (Critical Failure Count = 0)`

---

## Perfect Score Rule

A Final Score of `100` requires:

- Every applicable criterion receives `L4`.
- No unresolved critical failure exists.
- Every `N/A` classification is valid and justified.
- Sufficient evidence exists to evaluate all applicable criteria.

A score of `100` means:

> No material quality defect was identified against the active evaluation profile.

It does not mean:

- The artifact must exactly match the golden output.
- The artifact is the only valid interpretation.
- The source requirement itself is complete.
- The wording or formatting is perfect.
- Future requirements cannot change the expected artifact.

---

## Worked Example A — Perfect Artifact

Assume:

- All 12 criteria apply.
- Every criterion receives `L4`.
- No critical failure exists.

| Criterion | Weight | Level | Factor | Weighted Score |
|---|---:|---|---:|---:|
| C01 | 15 | L4 | 1.00 | 15.00 |
| C02 | 15 | L4 | 1.00 | 15.00 |
| C03 | 12 | L4 | 1.00 | 12.00 |
| C04 | 8 | L4 | 1.00 | 8.00 |
| C05 | 8 | L4 | 1.00 | 8.00 |
| C06 | 10 | L4 | 1.00 | 10.00 |
| C07 | 5 | L4 | 1.00 | 5.00 |
| C08 | 7 | L4 | 1.00 | 7.00 |
| C09 | 5 | L4 | 1.00 | 5.00 |
| C10 | 5 | L4 | 1.00 | 5.00 |
| C11 | 5 | L4 | 1.00 | 5.00 |
| C12 | 5 | L4 | 1.00 | 5.00 |
| **Total** | **100** |  |  | **100.00** |

Raw Weighted Score:

`100.00`

Active Weight:

`100`

Pre-Cap Score:

`100.00`

Critical Failures:

`None`

Final Score:

`100`

Quality Band:

`Excellent`

Result:

`PASS`

---

## Worked Example B — Minor Quality Weaknesses

Assume:

- C03 = `L3`
- C07 = `L3`
- All remaining criteria = `L4`
- No critical failure exists.

Calculations:

C03:

`12 × 0.80 = 9.60`

C07:

`5 × 0.80 = 4.00`

Full-score contribution from all remaining criteria:

`100 - 12 - 5 = 83`

Raw Weighted Score:

`83 + 9.60 + 4.00 = 96.60`

Pre-Cap Score:

`96.60`

Final Score:

`97`

Quality Band:

`Excellent`

Result:

`PASS`

---

## Worked Example C — Valid N/A

Assume:

- C10 = `N/A`
- C11 = `N/A`
- Both exclusions are valid and documented.
- Every remaining criterion receives `L4`.

Excluded Weight:

`5 + 5 = 10`

Active Weight:

`100 - 10 = 90`

Raw Weighted Score:

`90`

Normalized Score:

`(90 / 90) × 100 = 100`

Pre-Cap Score:

`100`

Critical Failures:

`None`

Final Score:

`100`

Quality Band:

`Excellent`

Result:

`PASS`

---

## Worked Example D — Critical Coverage Omission

Assume:

- Pre-Cap Score = `91`
- CF-03 is confirmed.

CF-03 cap:

`69`

Final Unrounded Score:

`min(91, 69) = 69`

Final Score:

`69`

Quality Band:

`Weak`

Result:

`FAIL`

The aggregate score cannot hide missing business-critical coverage.

---

## Worked Example E — Unsupported Scope Expansion

Assume:

- Pre-Cap Score = `88`
- CF-06 is confirmed.

CF-06 cap:

`59`

Final Unrounded Score:

`min(88, 59) = 59`

Final Score:

`59`

Quality Band:

`Weak`

Result:

`FAIL`

The artifact requires correction even when much of its remaining content is valid.

---

## Worked Example F — Multiple Critical Failures

Assume:

- Pre-Cap Score = `92`
- CF-03 is confirmed.
- CF-06 is confirmed.

Applicable caps:

- CF-03 → `69`
- CF-06 → `59`

Applied Critical Failure Cap:

`59`

Final Unrounded Score:

`min(92, 59) = 59`

Final Score:

`59`

Quality Band:

`Weak`

Result:

`FAIL`

The caps are not added or subtracted from the score.

The lowest applicable cap controls the result.

---

## Recommended Scoring Record

A scoring result should preserve sufficient information for audit, reproduction, and downstream comparison.

| Field | Description |
|---|---|
| Evaluation ID | Unique evaluation execution identifier |
| Dataset ID | Evaluated dataset |
| Artifact Type | Evaluated artifact type |
| Evaluator | Human, AI evaluator, or evaluation process |
| Evaluation Profile | Scoring profile used |
| Scoring Model | Scoring model identifier |
| Criterion Levels | L4–L0 or N/A for each criterion |
| Raw Weighted Score | Sum of weighted applicable criterion scores |
| Active Weight | Sum of applicable criterion weights |
| Normalized Score | Score normalized to 100 |
| Critical Failures | Confirmed critical-failure identifiers |
| Applied Cap | Lowest applicable critical-failure cap |
| Final Score | Rounded final score |
| Quality Band | Excellent / Good / Acceptable / Weak / Failed |
| Result | PASS / FAIL |
| Evidence | References supporting evaluation decisions |

---

## Example Scoring Record

Example serialized evaluation record:

    evaluation_id: EVAL-RUN-001
    dataset_id: REQ-AUTH-001
    artifact_type: Test-Cases
    evaluation_profile: default-artifact-quality
    scoring_model: EVAL-SCORING-001

    criterion_levels:
      C01: L4
      C02: L4
      C03: L3
      C04: L4
      C05: L4
      C06: L4
      C07: L4
      C08: L4
      C09: L4
      C10: L4
      C11: L4
      C12: L4

    raw_weighted_score: 97.6
    active_weight: 100
    normalized_score: 97.6

    critical_failures: []
    applied_cap: null

    final_score: 98
    quality_band: Excellent
    result: PASS

The serialized record stores the measurable evaluation result.

It does not replace the supporting rubric evidence.

---

## Artifact-Specific Scoring Profiles

The canonical weights define the default evaluation profile.

Future artifact-specific profiles may adjust weights when there is a justified evaluation need.

Examples may include:

- Requirement Analysis profile
- Business Rules profile
- Risk Analysis profile
- Test Scenarios profile
- Test Cases profile
- Regression Analysis profile

Any alternative profile must:

1. Reference the canonical criteria.
2. Reference the canonical rubric.
3. Define all configured criterion weights explicitly.
4. Sum configured weights to `100` before N/A handling.
5. Preserve the canonical rubric-level meanings.
6. Identify the scoring profile in every evaluation record.
7. Be versioned when changes affect comparability.

Alternative profiles must not silently modify the default profile.

---

## Scoring Model Versioning

Changes to any of the following may materially affect score comparability:

- Rubric score factors
- Criterion weights
- N/A normalization
- Quality bands
- PASS threshold
- Critical-failure caps
- Critical-failure gate behavior
- Rounding rules

Material scoring changes require a versioned scoring definition.

Results produced using materially different scoring models must not be treated as directly comparable without an explicit compatibility rule.

---

## Scoring Boundaries

The scoring model must not:

- Reinterpret source requirements.
- Override rubric evidence.
- Add undocumented quality criteria.
- Reward verbosity.
- Penalize harmless formatting differences.
- Require exact golden-output wording.
- Infer missing product behavior.
- Invent technical architecture.
- Rank platforms.
- Establish benchmark baselines.
- Define benchmark regression thresholds.

Scoring converts qualitative evaluation into a measurable result.

It does not replace QA judgment.

---

## Relationship to Evaluation Architecture

The canonical evaluation flow is:

`Evaluation Inputs → Criteria → Rubric → Scoring → Benchmark / Regression Comparison`

### Criteria

Defines what quality dimensions are evaluated.

### Rubric

Defines how quality is judged.

### Scoring

Defines how rubric judgments become measurable results.

This document belongs to this layer.

### Benchmark

Uses scored evaluation results to establish baselines, compare platforms, and detect quality regression.

---

## Final Scoring Definition

The canonical QA-AI artifact scoring model defines:

- Maximum normalized score: `100`
- Five rubric score factors:
  - L4 = `1.00`
  - L3 = `0.80`
  - L2 = `0.50`
  - L1 = `0.25`
  - L0 = `0.00`
- Twelve default criterion weights totaling `100`
- Valid `N/A` normalization
- Seven critical-failure score caps
- Critical-failure automatic FAIL behavior
- Five quality bands
- Default PASS threshold: `85`
- Deterministic rounding rules
- Evidence-preserving scoring records
- Version-aware score comparability

This scoring model provides the quantitative layer required for consistent QA-AI artifact evaluation and downstream benchmarking.
