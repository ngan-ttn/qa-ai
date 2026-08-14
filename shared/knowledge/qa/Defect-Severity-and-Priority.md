# Defect Severity and Priority

> Version: 1.0.0  
> Status: Draft  
> Last Updated: 2026-08-14

## Overview

**Defect Severity and Priority** are complementary classification concepts used to communicate the impact of a defect and the urgency with which it should be addressed.

Severity answers:

> How serious is the effect of the defect on the product, user, business, data, or system?

Priority answers:

> How urgently should the defect be addressed relative to other work?

Conceptually:

```text
Defect
  │
  ├── Severity → Impact
  │
  └── Priority → Urgency / Ordering
```

Severity and priority may influence one another, but they are not interchangeable.

Exact scales, ownership, and decision rules vary by organization.

---

## Purpose

The purpose of Severity and Priority classification is to improve defect communication and support consistent triage decisions.

This knowledge helps QA practitioners:

- describe defect impact more precisely;
- distinguish technical or business impact from delivery urgency;
- avoid treating all defects as equally important;
- communicate release risk;
- support defect triage;
- identify when business context changes urgency;
- avoid assuming severity automatically determines priority.

Within QA-AI, this knowledge supports defect reporting, defect analysis, release-risk reasoning, retesting, regression prioritization, and quality reporting.

Generic severity or priority labels should never replace the project's authoritative definitions.

---

## Core Concepts

### Severity

Severity represents the degree of negative impact caused by a defect.

Impact may involve:

- inability to complete a critical business flow;
- data loss or corruption;
- security exposure;
- financial impact;
- incorrect calculation;
- system unavailability;
- major usability degradation;
- cosmetic inconsistency.

Severity should be based on observed or credible impact rather than emotional wording.

### Priority

Priority represents how urgently a defect should be addressed relative to other work.

Priority may be influenced by:

- severity;
- release timing;
- affected user population;
- regulatory deadlines;
- workaround availability;
- business commitments;
- frequency of occurrence;
- visibility;
- dependency on other work.

### Independence

A high-severity defect is often high priority, but not always.

Likewise, a low-severity defect may become high priority for business reasons.

Example:

```text
High Severity + Low Immediate Exposure
→ Priority may be lower than expected

Low Severity + Release-Critical Branding Issue
→ Priority may be elevated
```

The actual decision must follow project context.

### Impact Dimensions

Severity evaluation may consider multiple dimensions:

- functional impact;
- business impact;
- data impact;
- security impact;
- regulatory impact;
- availability impact;
- recoverability;
- scope of affected users.

No universal weighting exists.

### Workaround

A workaround can reduce operational impact without eliminating the defect.

A workaround may influence priority, but it does not automatically reduce the inherent severity of the defect.

### Frequency

Frequency describes how often the defect occurs under relevant conditions.

A severe failure that occurs rarely may still be severe.

Frequency is one input to prioritization, not a substitute for impact.

### Severity Scale

Projects may use scales such as:

```text
Critical
High
Medium
Low
```

or numeric levels.

Labels are meaningful only when definitions are agreed.

### Priority Scale

Projects may use values such as:

```text
P0 / P1 / P2 / P3
```

or:

```text
Urgent / High / Medium / Low
```

Again, the definitions are project-specific.

---

## How It Works

A practical classification process can be represented as:

```text
Defect Observed
      │
      ▼
Assess Product / Business Impact
      │
      ▼
Determine Severity
      │
      ▼
Assess Timing, Exposure, Workaround, Commitments
      │
      ▼
Determine Priority
      │
      ▼
Review During Triage
```

### Severity Assessment

Ask questions such as:

- Which business flow is affected?
- Can the user continue?
- Is data incorrect or lost?
- Is security or compliance affected?
- How broad is the impact?

### Priority Assessment

Ask:

- Is the defect release-blocking?
- Is there a practical workaround?
- How many users are affected?
- Is the issue customer-visible?
- Is another feature dependent on the fix?
- Are there contractual or regulatory deadlines?

### Reassessment

Priority may change as release context changes.

Severity may also be reassessed if new evidence reveals a different impact than originally understood.

---

## When to Use

Severity and priority concepts are useful during:

### Defect Reporting

To communicate impact and urgency consistently.

### Defect Triage

To compare defects and decide resolution order.

### Release Readiness

To understand the significance of unresolved defects.

### Regression Planning

To prioritize coverage around high-impact fixed defects.

### Production Incident Review

To distinguish operational impact from corrective-action urgency.

### Quality Reporting

To summarize defect distribution without treating raw defect counts as sufficient quality evidence.

---

## When Not to Use

Do not use generic severity or priority scales as if they are universal.

Do not:

- assume `Critical` has the same meaning across organizations;
- set priority solely from severity;
- lower severity merely because a workaround exists;
- exaggerate severity to force faster resolution;
- treat low-priority defects as unimportant quality information;
- infer business urgency without product context;
- use severity or priority as a measure of developer performance.

Avoid classification based only on personal preference.

---

## Advantages

### Better Defect Communication

Impact and urgency are expressed separately.

### Better Triage

Teams can compare defects using consistent decision dimensions.

### Better Release Risk Visibility

High-impact unresolved defects become easier to identify.

### Better Prioritization

Urgent work can be distinguished from important but less time-sensitive work.

### Better Trend Analysis

Severity distributions can provide more context than defect counts alone.

---

## Limitations

### Classification Is Context-Dependent

The same defect may have different impact in different systems.

### Scales Can Be Subjective

Without definitions, teams may classify similar defects inconsistently.

### Priority Changes Over Time

Release timing or business events can change urgency.

### Labels Can Oversimplify

A single severity value may not capture every impact dimension.

### Classification Does Not Replace Analysis

Severity and priority do not explain root cause or regression impact.

---

## Examples

### Example 1 — High Severity, High Priority

A production payment flow charges customers twice.

Potential impact includes financial loss and customer harm, and immediate action may be required.

### Example 2 — High Severity, Lower Immediate Priority

A critical failure exists in functionality that is disabled and not scheduled for release.

The defect remains severe, while immediate priority may depend on release plans.

### Example 3 — Low Severity, High Priority

A visible legal name is misspelled on a launch-day public page.

The functional impact may be low, but business urgency may be high.

### Example 4 — Workaround

A report export fails in one format, but another approved format is available.

The workaround may influence urgency but does not erase the product defect.

---

## Best Practices

1. Define severity using impact, not desired resolution speed.
2. Define priority using urgency and delivery context.
3. Use project-approved classification definitions.
4. Record the evidence supporting high-impact classifications.
5. Consider business, data, security, and user impact where relevant.
6. Consider workaround and exposure when prioritizing.
7. Reassess classifications when new evidence appears.
8. Avoid severity inflation.
9. Keep triage decisions traceable where they materially affect release risk.
10. Use classification to support decisions, not individual performance measurement.

For QA-AI:

- do not assign exact severity or priority without project definitions when those definitions matter;
- distinguish impact evidence from urgency inference;
- explain the reasoning behind recommendations;
- flag missing business context rather than guessing priority.

---

## Related Knowledge

### Defect Lifecycle

`Defect-Lifecycle.md` explains where severity and priority are used during defect review and resolution.

### Defect Reporting

`Defect-Reporting.md` explains the evidence needed to support classification.

### Defect Analysis

`Defect-Analysis.md` explains how defect patterns and impact can be analyzed across multiple reports.

### Risk-Based Testing

`Risk-Based-Testing.md` uses related impact and likelihood concepts to prioritize testing effort.

### Regression Testing

`Regression-Testing.md` explains how defect fixes and impact influence regression scope.

---

## References

This article is conceptually aligned with established defect-management and testing practices, including:

- ISTQB testing guidance — defect classification, defect management, impact, and priority concepts.
- ISO/IEC/IEEE 29119 — software testing and incident-reporting concepts.

Project-specific severity levels, priority levels, owners, triage rules, release-blocking thresholds, and escalation policies must come from authoritative project documentation.