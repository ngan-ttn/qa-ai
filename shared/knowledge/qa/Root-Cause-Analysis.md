# Root Cause Analysis

> Version: 1.0.0  
> Status: Draft  
> Last Updated: 2026-08-14

## Overview

**Root Cause Analysis (RCA)** is a structured approach for investigating why a defect, incident, or quality problem occurred and identifying contributing conditions that should be addressed to reduce recurrence.

RCA goes beyond the immediate symptom.

A generalized causal chain may be represented as:

```text
Observed Failure
      │
      ▼
Immediate Cause
      │
      ▼
Contributing Factors
      │
      ▼
Underlying Cause(s)
      │
      ▼
Corrective / Preventive Action
```

Root cause is not always a single event. Complex failures may result from several interacting technical, process, requirement, or operational factors.

RCA should therefore focus on evidence and system improvement rather than individual blame.

---

## Purpose

The purpose of Root Cause Analysis is to understand why a quality problem occurred deeply enough to select effective improvement actions.

It helps teams:

- distinguish symptoms from causes;
- identify recurring systemic weaknesses;
- reduce repeated defects;
- improve requirements, design, implementation, testing, or operations;
- identify missing controls or coverage;
- evaluate whether corrective actions address the real problem;
- convert production and defect evidence into organizational learning.

Within QA-AI, RCA knowledge supports defect analysis, regression improvement, continuous improvement, requirement review, risk analysis, and coverage review.

RCA should not claim causal certainty when available evidence supports only a hypothesis.

---

## Core Concepts

### Symptom

A symptom is the observable failure.

Example:

> An order total is incorrect after applying a coupon.

The symptom describes what was observed, not why it happened.

### Immediate Cause

The immediate cause is the direct mechanism that produced the failure.

Example:

> The calculation function used the pre-discount subtotal.

This may still not explain why the incorrect logic entered the system.

### Contributing Factor

A contributing factor increases the likelihood or impact of the problem but may not be sufficient by itself to produce the failure.

Examples include:

- ambiguous requirement;
- missing review;
- weak automated coverage;
- shared mutable configuration;
- insufficient production monitoring.

### Root Cause

A root cause is an underlying condition whose removal or control would materially reduce the likelihood of recurrence.

There may be more than one meaningful root cause.

### Causal Evidence

RCA should rely on evidence such as:

- logs;
- code changes;
- requirements;
- test results;
- timestamps;
- configuration;
- deployment history;
- reproduction data;
- stakeholder decisions.

### Five Whys

The **Five Whys** technique repeatedly asks why a condition occurred to move from symptom toward deeper causes.

The number five is not mandatory.

The investigation should stop when evidence no longer supports deeper claims or when an actionable causal level has been reached.

### Cause-and-Effect Analysis

Cause-and-effect or fishbone analysis groups possible causes into categories to support broader investigation.

Categories may include:

- people;
- process;
- technology;
- data;
- environment;
- requirements;
- external dependencies.

Categories should be adapted to the problem.

### Corrective Action

Corrective action addresses an existing cause or condition.

Example:

> Fix the incorrect calculation logic.

### Preventive Action

Preventive action reduces the likelihood of similar future problems.

Examples include:

- clarify the business rule;
- add decision-table coverage;
- strengthen code review;
- add monitoring;
- improve deployment validation.

### Verification of Action

An action is not automatically effective because it was completed.

Teams should evaluate whether recurrence or the relevant risk actually decreases.

---

## How It Works

A practical RCA process may follow these steps.

### 1. Define the Problem

Describe the observed failure precisely and establish scope.

### 2. Build the Timeline

Identify relevant events before, during, and after the failure.

### 3. Collect Evidence

Gather technical, requirement, process, and testing information.

### 4. Identify the Immediate Cause

Determine the direct mechanism that produced the failure.

### 5. Explore Contributing Factors

Use evidence, Five Whys, cause-and-effect analysis, or causal mapping.

### 6. Validate Causal Claims

Ask whether evidence supports the proposed relationship.

### 7. Define Actions

Separate immediate correction from longer-term prevention.

### 8. Verify Effectiveness

Monitor whether the same class of problem recurs.

```text
Problem
  │
  ▼
Evidence
  │
  ▼
Causal Analysis
  │
  ▼
Action
  │
  ▼
Effectiveness Check
```

---

## When to Use

RCA is useful for:

### Recurring Defects

When similar problems repeatedly return.

### High-Impact Incidents

When failures have significant business, security, financial, or operational impact.

### Production Escapes

When teams need to understand why existing controls did not detect or prevent a defect.

### Reopened Defects

When fixes repeatedly fail to resolve the reported problem.

### Quality Trends

When defect analysis identifies a persistent pattern requiring deeper investigation.

### Process Improvement

When the goal is to improve the system that produces quality outcomes rather than only fix one symptom.

---

## When Not to Use

Do not perform heavy RCA for every minor defect when the investigation cost exceeds the expected learning value.

Do not:

- stop at the first plausible explanation;
- force every issue into a single root cause;
- use Five Whys mechanically;
- assume correlation proves causation;
- write `human error` as the final explanation without examining system conditions;
- use RCA to assign blame;
- invent causes when evidence is missing.

If evidence is insufficient, record hypotheses and investigation gaps explicitly.

---

## Advantages

### Reduced Recurrence

Effective actions can address underlying conditions rather than symptoms alone.

### Better Quality Learning

Teams gain insight into how requirements, design, testing, and operations interact.

### Better Prevention

RCA can reveal missing controls or coverage.

### Better Risk Management

Known causal patterns can improve future risk analysis.

### Better Continuous Improvement

Evidence from RCA can guide focused process or engineering changes.

---

## Limitations

### Causality Can Be Complex

Multiple factors may interact and no single root cause may exist.

### Evidence May Be Incomplete

Logs, timelines, or historical decisions may be unavailable.

### Hindsight Bias

After a failure, causes may appear more obvious than they were beforehand.

### Analysis Can Become Too Broad

Without a clear problem statement, RCA may expand without producing actionable insight.

### Actions May Not Be Effective

Completing an action does not guarantee recurrence prevention.

---

## Examples

### Example 1 — Missing Validation

Observed problem:

> Invalid quantity was accepted.

Possible causal chain:

```text
Invalid Quantity Accepted
      │
      ▼
No Server Validation
      │
      ▼
Requirement Defined UI Validation Only
      │
      ▼
Integration Behavior Was Not Considered
```

The final RCA depends on evidence from requirements and implementation.

### Example 2 — Production Escape

A permission defect reaches production.

Investigation finds:

- implementation checked only one role;
- acceptance criteria defined multiple roles;
- regression suite covered only administrator behavior.

Possible actions may address both implementation and coverage.

### Example 3 — Five Whys

```text
Why did the report fail?
→ Required data was null.

Why was it null?
→ Migration did not populate the field.

Why did migration allow it?
→ Migration validation omitted the new constraint.
```

Further questions should continue only while supported by evidence.

---

## Best Practices

1. Define the problem before analyzing causes.
2. Build a fact-based timeline.
3. Separate symptoms, immediate causes, contributing factors, and underlying causes.
4. Use multiple evidence sources where practical.
5. Treat causal claims as hypotheses until supported.
6. Avoid blame-oriented language.
7. Define actions at the level of the identified cause.
8. Distinguish corrective actions from preventive actions.
9. Assign measurable effectiveness checks where appropriate.
10. Share relevant learning with future requirement, development, and testing activities.

For QA-AI:

- do not infer root cause solely from a defect description;
- label unsupported possibilities as hypotheses;
- preserve evidence links;
- distinguish immediate cause from systemic contributing factors;
- recommend further investigation when evidence is insufficient.

---

## Related Knowledge

### Defect Analysis

`Defect-Analysis.md` identifies patterns that may trigger deeper root-cause investigation.

### Defect Lifecycle

`Defect-Lifecycle.md` provides the defect history and resolution context used during RCA.

### Regression Testing

`Regression-Testing.md` may be improved when RCA reveals recurring coverage gaps.

### Requirement Review

`Requirement-Review.md` supports prevention when requirement defects are contributing factors.

### Continuous Improvement

`Continuous-Improvement.md` explains how RCA findings can be turned into controlled improvement actions.

---

## References

This article is conceptually aligned with established quality-improvement and causal-analysis practices, including:

- ISO 9001 quality-management principles related to corrective action and continual improvement.
- Common engineering RCA techniques such as Five Whys and cause-and-effect analysis.
- ISTQB testing guidance related to defect analysis and process improvement.

Project-specific RCA triggers, facilitators, templates, action ownership, and effectiveness criteria must come from authoritative organizational processes.