# Defect Lifecycle

> Version: 1.0.0  
> Status: Draft  
> Last Updated: 2026-08-14

## Overview

The **Defect Lifecycle** describes how a reported software defect progresses from identification through investigation, resolution, verification, and closure.

It provides a structured view of defect states and transitions so teams can understand what has happened to a defect, what action is expected next, and whether the reported problem has been resolved.

A generalized lifecycle can be represented as:

```text
Defect Identified
      │
      ▼
Reported
      │
      ▼
Reviewed / Triaged
      │
      ▼
Assigned
      │
      ▼
Resolved
      │
      ▼
Retested
      │
      ├── Pass ──► Closed
      │
      └── Fail ──► Reopened
```

Actual state names and transitions vary across organizations and tools.

The lifecycle should therefore be understood as a conceptual model rather than one mandatory workflow.

---

## Purpose

The purpose of Defect Lifecycle knowledge is to help QA practitioners understand how defects are managed after discovery.

It helps teams:

- maintain clear ownership and status;
- distinguish discovery from confirmation and resolution;
- track whether a fix is ready for verification;
- separate retesting from broader regression testing;
- communicate unresolved quality risk;
- preserve defect history for analysis and learning;
- avoid premature closure.

Within QA-AI, Defect Lifecycle knowledge supports:

- bug-report review;
- defect analysis;
- retesting reasoning;
- regression analysis;
- test monitoring;
- release-risk reasoning;
- root-cause analysis.

Generic lifecycle knowledge must not override project-specific defect workflows.

---

## Core Concepts

### Defect Identification

A defect candidate begins when observed behavior appears to differ from expected behavior.

Before reporting, the tester may need to investigate whether the issue is caused by:

- product behavior;
- incorrect test data;
- environment problems;
- dependency failure;
- requirement ambiguity;
- test-design error.

### Reported State

Once sufficient evidence exists, the issue is recorded so it can be reviewed and tracked.

A reported defect should contain enough information to support reproduction and decision making.

Detailed reporting practices belong to `Defect-Reporting.md`.

### Review or Triage

A defect may be reviewed to determine:

- validity;
- severity;
- priority;
- ownership;
- affected scope;
- release impact;
- duplicate relationship.

The exact triage process is project-specific.

### Assigned / In Progress

A confirmed defect may be assigned for investigation and resolution.

The state name may vary, but the conceptual meaning is that corrective work is being performed or owned.

### Resolution

Resolution indicates that a decision or corrective action has been recorded.

Possible outcomes may include:

- fixed;
- duplicate;
- cannot reproduce;
- not a defect;
- deferred;
- accepted limitation.

These outcomes are not universal and must follow the project workflow.

### Retest

When a defect is reported as fixed, QA retests the specific failed behavior.

```text
Original Failure
      │
      ▼
Fix Available
      │
      ▼
Retest Same Condition
      │
      ▼
Compare Result
```

Detailed practices belong to `Retesting.md`.

### Reopen

If the original defect remains reproducible or the fix does not satisfy the expected behavior, the defect may be reopened.

Reopening should include updated evidence and the relevant build or environment context.

### Closure

A defect may be closed after the applicable verification or resolution criteria have been satisfied.

Closure should not hide unresolved impact.

For example, a deferred defect is not equivalent to a verified fix even if the workflow considers the issue administratively complete.

### Defect History

A defect record should preserve meaningful lifecycle history such as:

- status changes;
- comments;
- assignments;
- resolution decisions;
- evidence;
- verification results.

This history supports traceability and later analysis.

---

## How It Works

A generalized defect flow may proceed as follows.

### 1. Observe Unexpected Behavior

QA identifies behavior that appears inconsistent with the test basis.

### 2. Investigate

Reproduce the problem and eliminate obvious environment, data, or test issues.

### 3. Report

Create a defect with clear evidence and expected behavior.

### 4. Review and Prioritize

The team evaluates impact, urgency, ownership, and release relevance.

### 5. Resolve

Development or the responsible team investigates and records a resolution.

### 6. Retest

QA verifies the specific failure condition against the fix.

### 7. Regress as Needed

If the change may affect related behavior, appropriate regression testing is performed.

### 8. Close or Reopen

```text
Retest Result
     │
     ├── Expected Behavior Observed → Close
     │
     └── Failure Persists          → Reopen
```

The exact workflow must follow project rules.

---

## When to Use

Defect Lifecycle knowledge is useful whenever defects require structured tracking and communication.

Use it during:

### Test Execution

To understand how newly identified defects should progress after reporting.

### Defect Triage

To identify the current decision point and next action.

### Retesting

To determine whether a defect is ready for verification and what result should be recorded.

### Regression Planning

To evaluate whether fixes require related regression coverage.

### Test Monitoring

To understand unresolved defect status and testing risk.

### Release Discussions

To distinguish verified fixes, deferred defects, accepted limitations, and unresolved issues.

---

## When Not to Use

Do not use a generic Defect Lifecycle to invent project-specific states or transitions.

Do not assume:

- every project uses `New`, `Open`, `Fixed`, `Closed`;
- QA always owns closure;
- every reported defect must be fixed;
- every fix can be closed without retesting;
- `Rejected` always means the report was poor;
- `Deferred` means the defect has no quality impact.

Avoid:

```text
Generic Workflow
      │
      ✗
      ▼
Assume Project Statuses
```

Instead, use generic lifecycle knowledge to interpret the actual project workflow.

---

## Advantages

### Clear Ownership

Lifecycle states make the next expected action visible.

### Better Traceability

The defect history records decisions and verification evidence.

### Better Communication

Teams can distinguish reported, resolved, retested, and closed defects.

### Better Release Risk Visibility

Unresolved or deferred defects remain visible during quality discussions.

### Better Learning

Historical defect data can support root-cause and trend analysis.

---

## Limitations

### Workflows Differ

State names, transitions, and ownership vary significantly across teams.

### Status Can Be Misleading

A status label alone may not explain the actual resolution or remaining risk.

### Administrative Closure Is Not Quality Proof

A closed defect does not prove that related behavior is defect-free.

### Lifecycle Data Depends on Discipline

Incomplete comments, evidence, or resolution details reduce the value of defect history.

### Tooling Can Shape Behavior

Issue-tracking tools may impose workflows that do not perfectly represent the conceptual lifecycle.

---

## Examples

### Example 1 — Verified Fix

```text
New
 ↓
Confirmed
 ↓
Assigned
 ↓
Fixed
 ↓
Retest Passed
 ↓
Closed
```

The exact labels may differ, but the defect moves from discovery to verified resolution.

### Example 2 — Failed Retest

```text
Fixed
 ↓
Retest
 ↓
Original Failure Still Occurs
 ↓
Reopened
```

The reopened defect should include the new evidence and tested build.

### Example 3 — Duplicate

Two reports describe the same underlying defect.

One may be linked to the primary defect and resolved as duplicate according to project workflow.

The duplicate classification should preserve traceability rather than simply deleting the report.

### Example 4 — Deferred Defect

A low-priority defect may be deferred to a later release.

The defect remains a known product risk even if no immediate fix is planned.

---

## Best Practices

1. Investigate unexpected behavior before reporting a product defect.
2. Keep status changes consistent with actual defect state.
3. Preserve reproduction evidence and tested build information.
4. Distinguish resolution decisions from verified fixes.
5. Retest the original failed condition before closing a fixed defect where project practice requires verification.
6. Reopen defects with clear new evidence when the failure persists.
7. Link duplicates and related defects rather than losing history.
8. Keep deferred or accepted defects visible as remaining risk.
9. Use lifecycle data for trend and root-cause analysis, not individual blame.
10. Follow the authoritative project workflow for exact states and ownership.

For QA-AI:

- interpret statuses using project-specific definitions when available;
- do not invent unsupported transitions;
- distinguish `resolved` from `verified`;
- preserve defect history and evidence;
- treat deferred or accepted defects as known risk rather than fixed behavior.

---

## Related Knowledge

### Defect Reporting

`Defect-Reporting.md` explains how defects should be documented for effective reproduction and communication.

### Defect Severity and Priority

`Defect-Severity-and-Priority.md` explains impact and urgency concepts used during triage.

### Defect Analysis

`Defect-Analysis.md` explains how defect information is examined for patterns and quality insights.

### Root Cause Analysis

`Root-Cause-Analysis.md` addresses deeper causal investigation beyond the immediate symptom.

### Retesting

`Retesting.md` explains verification of a specific defect fix.

### Regression Testing

`Regression-Testing.md` explains evaluation of related existing behavior after a change.

---

## References

This article is conceptually aligned with established software-testing and defect-management practices, including:

- ISTQB testing guidance — defect management, confirmation testing, and regression testing concepts.
- ISO/IEC/IEEE 29119 — software testing processes and incident reporting concepts.

Project-specific defect states, ownership, triage rules, resolution values, closure criteria, and workflow automation must come from authoritative project documentation.