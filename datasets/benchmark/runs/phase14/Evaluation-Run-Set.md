# Phase 14 Evaluation Run Set

## Run Set Metadata

- Run Set ID: `P14-RUNSET-001`
- Status: `Approved for Execution`
- Dataset: `REQ-AUTH-001`
- Complexity: `Simple`
- Artifact Under Evaluation: `Structured Test Case Model`
- Workflow: `workflows/testcase-generation`
- Platforms: `ChatGPT`, `Claude`, `Cursor`
- Evaluation Criteria: `EVAL-CRITERIA-001`
- Evaluation Rubric: `EVAL-RUBRIC-001`
- Scoring Model: `EVAL-SCORING-001`
- Evaluation Profile: canonical default artifact-quality profile
- Framework Version: `1.0.0`
- Roadmap Baseline: Phase 13 Frozen; Phase 14 execution branch

## Objective

Evaluate whether the same QA-AI testcase-generation workflow produces source-grounded, contract-compliant, traceable test-case artifacts across all three supported Phase 13 runtimes under the same controlled requirement input and evaluation configuration.

## Why REQ-AUTH-001

`REQ-AUTH-001` is selected because it:

- is an approved controlled requirement dataset;
- contains explicit account-level tracking behavior;
- defines the 1–4 lower boundary, fifth-attempt lock threshold, 15-minute duration, successful-login reset, locked-state rejection, and automatic unlock behavior;
- intentionally contains no known ambiguity;
- allows evaluation of requirement fidelity, boundary/state coverage, traceability, completeness, and assumption control without relying on hidden implementation details.

## Controlled Input

Each platform must receive the same authoritative dataset content from:

`datasets/requirements/simple/REQ-AUTH-001.md`

No additional product behavior may be supplied unless the run is invalidated and restarted under a new run-set version.

## Requested Deliverable

Each platform must generate the testcase-generation workflow output culminating in a `Structured Test Case Model`.

The run must preserve the canonical workflow order:

```text
Requirement Information
    ↓
Requirement Analyzer
    ↓
Structured Requirement Analysis
    ↓
Business Rule Extractor
    ↓
Structured Business Rule Model
    ↓
Scenario Generator
    ↓
Structured Test Scenario Model
    ↓
Testcase Generator
    ↓
Structured Test Case Model
```

The evaluated deliverable is the final Structured Test Case Model. Intermediate artifacts may be retained as supporting evidence when the runtime exposes them.

## Required Behavioral Coverage

The final test-case artifact should remain grounded in the dataset and provide appropriate coverage for confirmed behavior including:

- failed-attempt counter increments for incorrect passwords;
- account remains unlocked after attempts 1–4;
- fifth consecutive failed attempt locks the account;
- lock duration starts when the fifth failed attempt is recorded;
- all password-based login attempts are rejected while locked, including correct-password attempts;
- automatic unlock after 15 minutes;
- counter reset after automatic unlock;
- successful login before lock resets the counter;
- subsequent failed attempt after reset starts a new sequence at one;
- isolation of failed-attempt tracking between accounts.

Implementation mechanisms not defined by the dataset must not be invented.

## Evaluation Dimensions

Use the canonical scoring profile:

| Criterion | Dimension | Weight |
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

Rubric levels and scoring factors must come from `EVAL-RUBRIC-001` and `EVAL-SCORING-001`.

## Quality Gate

A platform result is baseline-eligible only when:

- Final Score ≥ 85;
- Result = PASS;
- no unresolved critical failure exists;
- runtime evidence and evaluation reasoning are traceable;
- the run used the approved controlled input and configuration.

Passing does not automatically approve a baseline record. Baseline approval remains a separate review step.

## Run Identity

Use one run per platform:

- `P14-RUN-CHATGPT-001`
- `P14-RUN-CLAUDE-001`
- `P14-RUN-CURSOR-001`

A rerun after material configuration or input change must use a new run ID.

## Controlled Variables

Keep constant where practical:

- repository branch/commit baseline;
- dataset content;
- requested artifact;
- workflow and skill contracts;
- evaluation criteria/rubric/scoring;
- runtime instructions installed from the Phase 13 adapter baseline.

Platform/model-specific differences must be recorded rather than normalized away.

## Outputs Required Per Run

1. Execution metadata.
2. Raw generated artifact.
3. Evaluator criterion levels with evidence.
4. Canonical score result.
5. Critical-failure list.
6. Reviewer notes.
7. Baseline eligibility decision.

## Completion Rule

`P14-RUNSET-001` is complete only after all three platform runs have actual captured output and evaluated results under the same controlled configuration.