# Requirement Review

> Version: 1.0.0  
> Status: Draft  
> Last Updated: 2026-08-14

## Overview

**Requirement Review** is the systematic evaluation of requirement information before or during implementation to identify defects, ambiguity, inconsistency, missing information, and testability problems.

Requirement Review is a preventive quality activity.

It aims to improve the quality of the test basis before defects propagate into design, implementation, and testing.

A generalized review flow is:

```text
Requirement
    │
    ▼
Understand Intent
    │
    ▼
Evaluate Quality
    │
    ▼
Identify Issues
    │
    ▼
Clarify / Resolve
    │
    ▼
Updated Requirement
```

Requirement Review may be formal or lightweight depending on project context.

---

## Purpose

The purpose of Requirement Review is to identify requirement defects early and establish a clearer basis for development and testing.

It helps QA practitioners:

- detect ambiguity before implementation;
- identify missing business rules and conditions;
- identify contradictory statements;
- evaluate whether expected behavior is testable;
- identify missing acceptance criteria;
- expose dependencies and assumptions;
- improve scenario and testcase quality;
- reduce downstream rework;
- support early risk identification.

Within QA-AI, Requirement Review knowledge supports requirement analysis, clarification generation, coverage review, and regression-impact reasoning.

The review should identify evidence-based issues without redefining product requirements.

---

## Core Concepts

### Clarity

A requirement is clear when its intended meaning can be understood without multiple reasonable interpretations.

Vague terms such as `quickly`, `normally`, `appropriate`, or `several` may require clarification when they affect observable behavior.

### Completeness

A requirement is sufficiently complete when the information required to understand the relevant behavior is present.

Completeness concerns may include:

- missing conditions;
- missing outcomes;
- missing exceptions;
- missing roles;
- missing state behavior;
- missing validation rules.

Completeness is evaluated relative to the feature scope, not an imaginary perfect specification.

### Consistency

Requirements are consistent when related statements do not contradict one another.

Example:

```text
Requirement: Field is optional
Acceptance Criteria: Field is mandatory
```

This is a conflict that should be resolved rather than silently normalized.

### Correctness

Correctness asks whether the requirement accurately represents the intended business or stakeholder need.

QA may identify suspicious behavior, but authoritative stakeholders determine intended product behavior.

### Testability

A requirement is testable when expected behavior can be observed or measured.

Untestable wording may include:

- subjective quality statements;
- undefined timing;
- invisible internal outcomes with no verification path;
- unspecified expected results.

### Feasibility

Feasibility considers whether the requirement appears implementable within known technical, operational, or regulatory constraints.

QA may raise feasibility risks but should not replace engineering analysis.

### Traceability

Traceability identifies the source and downstream relationships of a requirement.

Useful relationships include:

```text
Business Need
    │
    ▼
Requirement
    │
    ▼
Acceptance Criteria
    │
    ▼
Scenario / Testcase
```

### Atomicity

A requirement is easier to analyze when independent behaviors are separated clearly.

A statement containing multiple unrelated obligations may hide partial implementation or partial coverage.

### Verifiable Language

Requirement wording should describe observable conditions and outcomes where practical.

Example:

```text
Weak: The page should load quickly.
Better: The page should meet the approved response-time criterion.
```

The actual criterion must come from project requirements, not from the reviewer.

---

## How It Works

Requirement Review can follow a structured sequence.

### 1. Identify the Source

Confirm the artifact being reviewed and its relationship to other authoritative sources.

### 2. Understand the Intent

Identify the business objective, actors, scope, and primary behavior.

### 3. Evaluate Quality Characteristics

Review for:

- clarity;
- completeness;
- consistency;
- correctness concerns;
- testability;
- traceability;
- feasibility concerns.

### 4. Inspect Testing-Sensitive Areas

Look for:

- boundaries;
- state transitions;
- role differences;
- exception paths;
- calculations;
- validations;
- integration dependencies;
- timing behavior.

### 5. Record Findings

Classify each finding as a concrete issue, question, assumption, or investigation item.

### 6. Resolve and Recheck

When clarification is provided, verify that the updated requirement resolves the issue without creating new contradictions.

---

## When to Use

Requirement Review is valuable during:

### Backlog Refinement

To improve stories and acceptance criteria before implementation begins.

### Formal Specification Review

To identify quality defects in BRDs, functional specifications, or regulatory requirements.

### Change Requests

To assess whether changed requirements remain consistent with existing behavior.

### Test Preparation

To ensure the test basis is sufficiently clear before scenario and testcase design.

### Defect Disputes

To determine whether unexpected behavior reflects a product defect or requirement ambiguity.

### Integration Planning

To identify missing ownership, interface, or dependency behavior.

---

## When Not to Use

Requirement Review should not be used to:

- invent missing business rules;
- rewrite product intent based only on reviewer preference;
- reject valid requirements because they do not follow one preferred format;
- require unnecessary documentation for low-risk work;
- treat every technical unknown as a requirement defect;
- replace stakeholder approval or architecture review.

Avoid turning review into stylistic editing when wording is already clear and testable.

---

## Advantages

### Earlier Defect Detection

Requirement defects can be corrected before they become implementation defects.

### Lower Rework Risk

Clarifying behavior early reduces downstream changes to code, tests, and documentation.

### Better Test Coverage

Clear rules and conditions produce stronger scenarios and test cases.

### Better Collaboration

Structured findings make clarification more focused and actionable.

### Improved Traceability

Reviewed requirements provide a stronger source for downstream QA artifacts.

---

## Limitations

### Review Depends on Available Context

A reviewer cannot validate business correctness without sufficient domain or stakeholder information.

### Review Does Not Eliminate Change

Requirements may still evolve after review.

### Excessive Review Can Delay Feedback

The depth of review should match risk and complexity.

### Review Cannot Prove Completeness

Unknown future conditions or hidden stakeholder expectations may remain.

### Authority Remains External

QA identifies issues; project stakeholders resolve product decisions.

---

## Examples

### Example 1 — Undefined Threshold

Requirement:

> Lock the account after several failed attempts.

Finding:

- `several` is ambiguous;
- exact threshold is required for implementation and testing.

### Example 2 — Missing Exception

Requirement:

> Users can cancel an order before shipment.

Review questions may include:

- Which statuses count as `before shipment`?
- What happens if cancellation and shipment processing occur concurrently?

Only questions relevant to project context should be raised.

### Example 3 — Inconsistent Sources

A mockup marks a field optional while acceptance criteria require it.

The review should identify the conflict and request source-of-truth resolution.

### Example 4 — Untestable Outcome

Requirement:

> Search results should be user-friendly.

The phrase does not define observable acceptance behavior and requires measurable or reviewable criteria if it is release-significant.

---

## Best Practices

1. Review requirement meaning before grammar or formatting.
2. Use a consistent quality lens: clarity, completeness, consistency, testability, traceability, and risk.
3. Phrase findings specifically and reference the affected requirement.
4. Separate questions from confirmed defects in the requirement.
5. Avoid proposing arbitrary business values when data is missing.
6. Prioritize findings that can cause incorrect implementation or missing coverage.
7. Recheck updated requirements after clarification.
8. Preserve resolved decisions for downstream traceability.
9. Adapt review depth to business risk and complexity.
10. Keep the review focused on requirement quality rather than implementation preferences.

For QA-AI:

- identify evidence-backed gaps;
- preserve conflicting source statements instead of silently reconciling them;
- label uncertainty;
- generate concise, decision-oriented clarification questions;
- do not infer requirement precedence unless defined.

---

## Related Knowledge

### Requirement Engineering

`Requirement-Engineering.md` provides the broader requirement lifecycle.

### Requirement Analysis

`Requirement-Analysis.md` explains how requirement information is structured for downstream QA reasoning.

### Acceptance Criteria

`Acceptance-Criteria.md` provides deeper guidance on measurable acceptance conditions.

### Verification and Validation

`Verification-and-Validation.md` explains complementary quality perspectives relevant to requirement evaluation.

### Software Testing Life Cycle

`STLC.md` explains where requirement review contributes to early testing and defect prevention.

---

## References

This article is conceptually aligned with established requirements and testing guidance, including:

- ISO/IEC/IEEE 29148 — requirements engineering and requirements quality.
- ISTQB Certified Tester Foundation Level syllabus — static testing, reviews, test basis, early testing, and testability.
- ISO/IEC/IEEE 29119 — software testing processes.

Project-specific review roles, sign-off rules, requirement precedence, checklists, and approval workflows must come from authoritative project documentation.