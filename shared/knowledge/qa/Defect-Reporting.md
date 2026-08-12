# Defect Reporting

> Version: 1.0.0  
> Status: Draft  
> Last Updated: YYYY-MM-DD

## Overview

**Defect Reporting** is the practice of documenting unexpected software behavior so that the issue can be understood, reproduced, evaluated, resolved, and verified efficiently.

A defect report is both a communication artifact and a traceability record.

A generalized reporting flow is:

```text
Unexpected Behavior
        │
        ▼
Investigate
        │
        ▼
Collect Evidence
        │
        ▼
Describe Reproduction
        │
        ▼
Record Actual vs Expected
        │
        ▼
Submit for Review
```

The exact fields, workflow, and tooling vary by project.

---

## Purpose

The purpose of Defect Reporting is to communicate enough reliable information for others to understand and act on a software problem.

A strong defect report helps teams:

- reproduce the issue;
- understand the affected behavior;
- compare actual and expected results;
- assess impact and urgency;
- identify the tested environment and data;
- avoid duplicate investigation;
- verify the eventual fix;
- preserve evidence for later analysis.

Within QA-AI, Defect Reporting knowledge supports bug-report review, defect analysis, severity reasoning, retesting, regression analysis, and quality reporting.

Defect reports should reflect observed evidence rather than speculation presented as fact.

---

## Core Concepts

### Defect Summary

The summary should identify the affected area and observed problem concisely.

A useful summary often expresses:

```text
Affected Function + Condition + Incorrect Behavior
```

Example:

> Checkout total excludes the promotion discount when a premium coupon is applied.

### Environment

Environment information helps determine where the issue was observed.

Relevant information may include:

- application version or build;
- test environment;
- browser or device;
- operating system;
- configuration;
- feature flags;
- integration state.

Only relevant environment details should be included.

### Preconditions

Preconditions describe required state before reproduction begins.

Examples include:

- user role;
- account state;
- existing data;
- feature configuration;
- order status.

### Steps to Reproduce

Steps should be specific, ordered, and minimal enough to reproduce the issue without unrelated actions.

They should describe what the tester actually did.

### Test Data

Relevant input values, identifiers, account states, or entity data should be recorded when they affect reproduction.

Sensitive information should follow project data-handling requirements.

### Actual Result

The actual result describes what was observed.

It should avoid vague wording such as `not working` when a more precise observation is available.

### Expected Result

The expected result should come from an authoritative test basis such as:

- requirement;
- acceptance criteria;
- approved business rule;
- specification;
- established expected behavior.

When expected behavior is unclear, the issue may require clarification before classification as a defect.

### Evidence

Evidence may include:

- screenshots;
- video;
- logs;
- API request and response;
- database evidence;
- console output;
- timestamps;
- trace or correlation identifiers.

Evidence should support the report rather than replace a clear written description.

### Severity and Priority

Severity describes impact; priority describes urgency or ordering.

They are related but not identical.

Detailed guidance belongs to `Defect-Severity-and-Priority.md`.

### Reproducibility

Reproducibility describes whether the issue can be repeated under the same or similar conditions.

An intermittent issue can still be valid if sufficient evidence exists.

### Traceability

A defect may be linked to:

- requirement;
- scenario;
- testcase;
- release;
- related defect;
- affected component.

Traceability helps later retesting and analysis.

---

## How It Works

A practical defect-reporting process may follow these steps.

### 1. Confirm the Observation

Repeat the behavior where practical and verify that the issue is not caused by obvious test-data or environment mistakes.

### 2. Identify the Expected Behavior

Use authoritative sources.

If the expectation is unclear, record the ambiguity instead of inventing it.

### 3. Minimize Reproduction

Remove unnecessary steps to isolate the condition that triggers the issue.

### 4. Collect Evidence

Capture the information needed to support investigation.

### 5. Write the Report

Include the relevant context, reproduction, actual behavior, expected behavior, and impact information.

### 6. Review for Reproducibility

Ask:

```text
Can another person understand the state,
perform the steps,
and observe the reported behavior?
```

### 7. Submit and Maintain

Update the defect when new evidence, status, or retest results become available.

---

## When to Use

Defect Reporting should be used when observed software behavior requires structured tracking and resolution.

### Functional Failure

When actual behavior differs from a confirmed requirement.

### Integration Failure

When connected systems exchange incorrect data or behave inconsistently with the agreed interface.

### Data Integrity Issue

When persisted or calculated data differs from expected behavior.

### Intermittent Failure

When the issue is not consistently reproducible but evidence demonstrates a real failure pattern.

### Production or UAT Issue

When defects require traceable investigation outside normal QA execution.

### Regression Failure

When previously working behavior fails after a change.

---

## When Not to Use

Do not report every unexpected observation as a confirmed product defect without investigation.

Possible alternatives include:

- requirement clarification;
- environment incident;
- test-data issue;
- dependency outage;
- test-case correction;
- support request.

Do not:

- invent expected results;
- exaggerate impact;
- include unrelated steps;
- attach evidence without explanation;
- expose sensitive data unnecessarily;
- assign blame to individuals;
- create duplicate reports when an existing defect already captures the same issue.

---

## Advantages

### Faster Reproduction

Clear steps and context reduce investigation time.

### Better Communication

Actual and expected behavior are explicit.

### Better Prioritization

Impact information helps triage decisions.

### Better Retesting

The original failed condition can be reproduced after a fix.

### Better Traceability

Defect history can be connected to requirements, tests, and releases.

### Better Quality Learning

High-quality defect data supports trend and root-cause analysis.

---

## Limitations

### Reports Depend on Available Evidence

Intermittent or environment-sensitive issues may remain difficult to reproduce.

### More Detail Is Not Always Better

Excessive logs or unrelated steps can obscure the real problem.

### Severity Can Be Context-Dependent

The same technical failure may have different business impact in different products.

### Reporting Does Not Resolve the Defect

A high-quality report supports investigation but does not identify the root cause automatically.

### Tool Fields Vary

Required fields and workflows depend on the project and defect-tracking system.

---

## Examples

### Example 1 — Weak Report

```text
Title: Checkout broken
Steps: Try checkout
Actual: Doesn't work
Expected: Should work
```

This report does not identify the condition, state, or observable failure.

### Example 2 — Stronger Report

```text
Title: Checkout total omits premium coupon discount when payment page is opened

Precondition:
- Premium user has an eligible coupon.
- Cart contains an eligible product.

Steps:
1. Apply the premium coupon.
2. Continue to the payment page.

Actual:
The payment total is calculated without the coupon discount.

Expected:
The payment total includes the approved coupon discount according to the promotion rule.
```

Relevant evidence and exact test data may be attached separately.

### Example 3 — Requirement Ambiguity

If the specification does not define whether a refund should restore a coupon, QA should raise clarification rather than filing a defect based on personal expectation.

### Example 4 — Intermittent Issue

A timeout occurs in 3 of 20 attempts.

The report should preserve frequency, timestamps, environment, and relevant logs rather than state that the problem occurs every time.

---

## Best Practices

1. Investigate before reporting.
2. Write a specific, behavior-focused summary.
3. Include only relevant preconditions and reproduction steps.
4. Record exact actual behavior.
5. Base expected behavior on authoritative evidence.
6. Include test data when it affects reproduction.
7. Attach evidence that supports investigation.
8. Separate impact assessment from root-cause speculation.
9. Protect sensitive data in screenshots, logs, and payloads.
10. Update the report with retest evidence and meaningful lifecycle decisions.

For QA-AI:

- preserve supplied defect facts without embellishment;
- distinguish observation from inference;
- flag missing reproduction information;
- verify that expected behavior is traceable to a source when available;
- avoid inventing severity, priority, ownership, or root cause without context;
- identify sensitive information before reproducing it in generated reports.

---

## Related Knowledge

### Defect Lifecycle

`Defect-Lifecycle.md` explains how a reported defect progresses through resolution and verification.

### Defect Severity and Priority

`Defect-Severity-and-Priority.md` explains impact and urgency classifications.

### Defect Analysis

`Defect-Analysis.md` explains how defect information can be examined for patterns and quality insights.

### Retesting

`Retesting.md` explains verification of the original failed behavior after a fix.

### Requirement Analysis

`Requirement-Analysis.md` helps establish authoritative expected behavior before defect classification.

---

## References

This article is conceptually aligned with established software-testing guidance, including:

- ISO/IEC/IEEE 29119 — incident reporting and software testing processes.
- ISTQB testing guidance — defect management and defect-report content concepts.

Project-specific defect templates, mandatory fields, evidence rules, sensitive-data handling, severity scales, ownership, and workflow must come from authoritative project documentation.