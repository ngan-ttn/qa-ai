# Retesting

> Version: 1.0.0  
> Status: Draft  
> Last Updated: YYYY-MM-DD

## Overview

**Retesting** is the testing activity used to verify whether a specific previously observed defect has been corrected.

Retesting focuses on the original failed condition and the expected behavior associated with that defect.

A generalized flow is:

```text
Defect Reported
      │
      ▼
Fix Implemented
      │
      ▼
Fix Available for Testing
      │
      ▼
Repeat Relevant Condition
      │
      ▼
Compare Actual vs Expected
      │
      ├── Pass → Verify / Close according to workflow
      │
      └── Fail → Reopen / Continue Investigation
```

Retesting is narrower than regression testing.

It answers whether the specific reported problem has been resolved, not whether other existing behavior remains unaffected.

---

## Purpose

The purpose of Retesting is to provide evidence that a reported defect fix satisfies the expected behavior under the relevant failed condition.

Retesting helps QA practitioners:

- verify a specific fix;
- reproduce the original defect condition consistently;
- compare behavior before and after the fix;
- determine whether a defect should be reopened or verified;
- preserve fix-verification evidence;
- separate direct fix verification from broader regression coverage.

Within QA-AI, Retesting knowledge supports defect lifecycle reasoning, bug-report review, regression analysis, test monitoring, and closure decisions.

Retesting should use authoritative expected behavior and should not be treated as proof that related functionality is unaffected.

---

## Core Concepts

### Original Failure Condition

The original failure condition is the state, input, action, and environment under which the defect was observed.

A reliable retest should reproduce the relevant condition closely enough to verify the fix.

### Fix Version

Retesting should identify the build, version, commit, or deployed environment containing the fix where such information is available.

Testing the wrong build can produce misleading results.

### Expected Behavior

The expected result should come from the same authoritative test basis used to classify the original behavior as defective, unless the requirement itself has changed.

### Confirmation Testing

Retesting is also commonly referred to as **confirmation testing**.

Both terms describe verification that a specific defect has been corrected.

### Pass Result

A retest passes when the previously failing behavior now satisfies the expected result under the relevant conditions.

A pass does not prove absence of related regression defects.

### Failed Retest

A retest fails when:

- the original failure still occurs;
- the fix only partially satisfies expected behavior;
- another behavior prevents verification of the fix.

The resulting lifecycle action depends on project workflow.

### Changed Requirement

If the expected behavior changed after the original defect was reported, retesting should use the current authoritative requirement and record the change.

The defect may need reclassification rather than simple pass/fail verification.

### Regression Relationship

Retesting and regression testing are complementary.

```text
Fix
 │
 ├── Retesting → Did the reported defect get fixed?
 │
 └── Regression → Did the change affect existing behavior?
```

---

## How It Works

A practical retesting process may follow these steps.

### 1. Review the Defect

Understand:

- original steps;
- preconditions;
- test data;
- actual result;
- expected result;
- environment;
- resolution notes.

### 2. Confirm Fix Availability

Verify that the tested build contains the intended fix.

### 3. Recreate the Relevant State

Prepare the same or equivalent data and preconditions required to reproduce the original issue.

### 4. Execute the Failed Condition

Repeat the minimum relevant flow needed to verify the reported defect.

### 5. Compare Results

```text
Current Result
      │
      ├── Matches Expected → Retest Pass
      │
      └── Does Not Match   → Retest Fail
```

### 6. Record Evidence

Update the defect or test evidence according to project practice.

### 7. Perform Regression Where Needed

Use change-impact analysis to determine related behavior requiring additional verification.

---

## When to Use

Retesting is appropriate when:

### A Defect Is Fixed

To verify the original failure no longer occurs.

### A Previously Failed Test Is Ready for Re-execution

To confirm whether the specific failure condition now passes.

### A Defect Is Reopened and Fixed Again

To verify the latest corrective change.

### A Configuration or Data Correction Claims to Resolve the Issue

To verify the specific observed behavior even when no source-code change was required.

### A Requirement Clarification Changes the Expected Result

To verify current behavior against the newly confirmed expectation where relevant.

---

## When Not to Use

Retesting should not be used as a substitute for regression testing.

Do not assume:

- a passed retest means no regression exists;
- every fixed defect requires the entire product to be retested;
- a retest should use new random data if the original condition is data-specific;
- the defect is fixed merely because development marked it resolved;
- a failed retest always means the same root cause remains.

Retesting may be unnecessary for administrative defect resolutions such as duplicate or invalid reports, depending on project workflow.

---

## Advantages

### Direct Fix Verification

Retesting provides focused evidence about the reported defect.

### Efficient Feedback

The tester can quickly determine whether the specific failure condition changed.

### Better Defect Lifecycle Control

Retest results support reopen or closure decisions.

### Better Evidence

Before-and-after behavior can be compared clearly.

### Clear Separation of Objectives

Retesting keeps fix verification distinct from regression-risk evaluation.

---

## Limitations

### Narrow Scope

Retesting does not evaluate all consequences of the fix.

### Environment Differences Can Affect Results

A fix may behave differently if the retest environment does not match the relevant original conditions.

### Original Report Quality Matters

Poor steps, missing data, or unclear expected results make reliable retesting harder.

### Fixes Can Change Requirements

If product behavior was redefined, the original defect expectation may no longer be valid.

### Passing Does Not Prove Root Cause Removal

The observed symptom may disappear even if a broader underlying issue remains.

---

## Examples

### Example 1 — Calculation Defect

Original failure:

> A 10% discount is displayed as 5%.

Retest:

```text
Prepare Original Eligibility State
      │
      ▼
Apply Same Discount Condition
      │
      ▼
Verify Approved 10% Result
```

### Example 2 — Role Permission Defect

A user without approval permission could previously approve a request.

Retesting should recreate the same role and request state and verify that the unauthorized action is no longer allowed.

### Example 3 — Retest Pass, Regression Fail

The original checkout calculation is fixed, but a different promotion type now calculates incorrectly.

The retest passes while regression testing identifies a new problem.

This demonstrates why the two activities are distinct.

### Example 4 — Requirement Changed

A defect was reported because a timeout occurred after 30 seconds. Later, the approved requirement changes the timeout to 20 seconds.

Retesting should use the current approved behavior and preserve the requirement change in the defect context.

---

## Best Practices

1. Read the original defect before retesting.
2. Confirm that the fix is actually deployed in the tested environment.
3. Reuse the original failed condition when it materially affects reproduction.
4. Use current authoritative expected behavior.
5. Record the tested build, environment, and relevant data.
6. Capture evidence for failed retests and important passed retests where required.
7. Reopen with clear evidence when the defect persists.
8. Perform impact-based regression separately.
9. Avoid expanding a focused retest into unrelated exploratory work without a clear objective.
10. Preserve traceability between the defect, fix, retest result, and regression evidence.

For QA-AI:

- distinguish retesting from regression;
- do not mark a defect verified from status text alone;
- use original defect evidence and current requirements;
- flag missing build, data, or reproduction context when they block reliable verification.

---

## Related Knowledge

### Defect Lifecycle

`Defect-Lifecycle.md` explains where retesting fits between resolution and closure or reopening.

### Defect Reporting

`Defect-Reporting.md` explains the reproduction information required for effective retesting.

### Regression Testing

`Regression-Testing.md` explains how related existing behavior is evaluated after a change.

### Defect Analysis

`Defect-Analysis.md` can reveal patterns in failed retests or recurring defects.

### Test Monitoring and Control

`Test-Monitoring-and-Control.md` uses retest status as one input to testing progress and risk evaluation.

---

## References

This article is conceptually aligned with established software-testing guidance, including:

- ISTQB Certified Tester Foundation Level syllabus — confirmation testing and regression testing concepts.
- ISO/IEC/IEEE 29119 — software testing processes.

Project-specific retest ownership, evidence requirements, defect transitions, pass criteria, and closure workflow must come from authoritative project documentation.