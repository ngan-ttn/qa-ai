# Requirement Analysis

> Version: 1.0.0  
> Status: Draft  
> Last Updated: 2026-08-14

## Overview

**Requirement Analysis** is the QA activity of examining requirement information to understand expected behavior, identify rules and constraints, detect gaps or ambiguity, assess testability, and prepare structured input for downstream testing activities.

Requirement Analysis converts raw requirement information into a clearer model of what must be verified.

A generalized flow is:

```text
Raw Requirement
      │
      ▼
Understand Scope
      │
      ▼
Identify Actors & Flows
      │
      ▼
Extract Rules & Conditions
      │
      ▼
Identify Gaps & Risks
      │
      ▼
Assess Testability
      │
      ▼
Structured Analysis
```

Requirement Analysis should preserve the distinction between what is explicitly defined, what can be safely derived, what is missing, and what requires investigation.

---

## Purpose

The purpose of Requirement Analysis is to create a reliable understanding of the feature before test scenarios and test cases are designed.

It helps QA practitioners:

- understand business intent and feature scope;
- identify primary actors and user flows;
- extract business rules and validations;
- identify states, boundaries, dependencies, and exceptions;
- detect missing or conflicting information;
- assess whether expected behavior is observable and testable;
- identify clarification questions;
- expose early testing risks;
- establish traceability for downstream artifacts.

Within QA-AI, Requirement Analysis is a foundational input to:

- business-rule extraction;
- risk analysis;
- scenario generation;
- testcase generation;
- coverage review;
- regression analysis.

Requirement Analysis should improve understanding without inventing unconfirmed behavior.

---

## Core Concepts

### Feature Summary

A feature summary explains the business objective and primary behavior in concise terms.

It should answer:

- What is changing?
- Why does the behavior exist?
- Who uses it?
- What outcome is expected?

The summary should not introduce behavior that is absent from the requirement.

### Actors

Actors are users, systems, roles, or external parties that interact with the behavior.

Actor analysis helps identify:

- role-specific behavior;
- permission differences;
- interaction boundaries;
- external dependencies.

### Scope

Scope separates what the supplied requirement defines from what it does not define.

Useful categories include:

```text
In Scope
Not Defined
Out of Scope — only if explicitly stated
```

`Not Defined` should not automatically be treated as `Out of Scope`.

### Functional Behavior

Functional behavior describes observable system responses to user actions, events, conditions, and states.

Examples include:

- create;
- update;
- submit;
- approve;
- reject;
- authenticate;
- calculate;
- transition between states.

### Business Rules

Business rules define conditions, constraints, decisions, calculations, eligibility, or behavior that govern the feature.

Requirement Analysis identifies rule candidates, while detailed classification belongs to business-rule analysis or extraction.

### Conditions and Boundaries

Conditions determine when behavior applies.

Boundaries identify thresholds where behavior changes.

Examples:

```text
Quantity < 10  → Standard Flow
Quantity >= 10 → Approval Required
```

Boundaries are important because defects frequently occur around transitions between valid behavior ranges.

### States and Transitions

Stateful behavior depends on the current condition of an entity or process.

```text
Draft
  │
  ▼
Submitted
  │
  ├── Approved
  └── Rejected
```

Requirement Analysis should identify defined states, triggers, and allowed transitions without inventing undocumented transitions.

### Dependencies

Dependencies are systems, services, data, roles, environments, or upstream conditions required for behavior to work.

Dependencies may affect:

- testability;
- environment preparation;
- test data;
- integration scope;
- regression impact.

### Ambiguity

Ambiguity occurs when requirement wording supports more than one reasonable interpretation.

An ambiguous requirement should be clarified rather than silently normalized.

### Missing Information

Missing information is behavior or context required for complete analysis but not supplied.

Missing information can be classified as:

```text
Business / Functional Gap
→ Clarification Required

Technical / System Context Gap
→ Investigation Required
```

### Assumptions

An assumption is an unconfirmed belief used temporarily to continue reasoning.

Assumptions should always be labeled.

They must not be converted into confirmed requirements without evidence.

### Testability

A requirement is testable when expected behavior can be observed, measured, or otherwise verified.

Testability concerns may include:

- vague outcomes;
- inaccessible state;
- undefined expected result;
- unobservable background behavior;
- missing timing criteria.

---

## How It Works

Requirement Analysis typically follows a progressive refinement process.

### 1. Establish Context

Identify the business objective, feature, actors, and authoritative sources.

### 2. Decompose Behavior

Break the requirement into:

- flows;
- actions;
- conditions;
- rules;
- validations;
- state changes;
- dependencies.

### 3. Separate Evidence Levels

```text
Explicitly Defined
        │
        ├── Confirmed
        │
Safely Derived
        │
        ├── Derived and Labeled
        │
Not Defined
        │
        └── Clarification / Investigation
```

### 4. Identify Testing-Sensitive Areas

Look for:

- thresholds;
- exceptions;
- role differences;
- state transitions;
- concurrency implications;
- integration points;
- persistence expectations;
- timing behavior.

### 5. Assess Gaps and Risks

Record missing, conflicting, or unclear information and determine its downstream impact.

### 6. Produce Structured Analysis

The output should be understandable by humans and reusable by AI capabilities without requiring hidden assumptions.

---

## When to Use

Requirement Analysis should be used whenever QA needs to transform requirement information into a testable understanding.

### New Features

Use it before scenario or testcase design.

### Requirement Changes

Use it to identify changed behavior and downstream impact.

### Defect Clarification

Use it when expected behavior is disputed or unclear.

### Integration Work

Use it to identify dependencies, ownership boundaries, and externally controlled behavior.

### Legacy Features

Use it to reconstruct current expected behavior from authoritative documentation and approved evidence.

### AI-Assisted QA

Use structured Requirement Analysis as a stable upstream artifact for downstream generation and review skills.

---

## When Not to Use

Requirement Analysis should not be used to replace authoritative product decisions.

Do not:

- invent missing values or business rules;
- treat common industry behavior as project fact;
- silently resolve requirement conflicts;
- convert technical guesses into expected behavior;
- generate detailed test cases before understanding the requirement;
- assume behavior because it exists in a similar feature;
- treat every unknown technical detail as a business clarification.

Avoid:

```text
Unknown Behavior
      │
      ✗
      ▼
Assume Expected Result
```

Instead:

```text
Unknown Behavior
      │
      ▼
Classify Gap
      │
      ▼
Clarify or Investigate
```

---

## Advantages

### Earlier Problem Detection

Ambiguities and missing rules can be identified before implementation or execution.

### Better Scenario Coverage

Structured rules, flows, boundaries, and states provide stronger inputs for scenario design.

### Better Traceability

Requirements can be connected to downstream rules, scenarios, and test cases.

### Better Risk Analysis

Dependencies and unclear behavior become visible earlier.

### Reduced Assumption Risk

Explicit separation of facts, derived behavior, and gaps reduces silent invention.

### Better Collaboration

Clarification questions become specific and actionable.

---

## Limitations

### Source Quality Limits Analysis

Incomplete or contradictory sources may prevent definitive conclusions.

### Analysis Can Become Overly Detailed

Excessive decomposition can add documentation cost without improving testing decisions.

### Technical Context May Be Missing

Some system-level risks cannot be evaluated without architecture, API, database, or environment information.

### Requirements Change

Analysis becomes stale when upstream requirements change and downstream artifacts are not updated.

### Analysis Does Not Guarantee Coverage

Good analysis improves inputs but still requires effective test design and review.

---

## Examples

### Example 1 — Threshold Rule

Requirement:

> Lock the account after five consecutive incorrect password attempts.

Analysis identifies:

- actor: registered user;
- threshold: 5;
- below-threshold behavior: account remains unlocked;
- threshold behavior: account becomes locked;
- sequence condition: failures must be consecutive;
- related question: what resets the sequence?

### Example 2 — Undefined State Behavior

Requirement:

> Users can edit an order while it is active.

If `active` is not defined, QA should identify the missing state definition rather than invent which statuses are editable.

### Example 3 — Dependency

Requirement:

> Send a confirmation email after successful payment.

Analysis identifies at least two observable areas:

```text
Payment Success
      │
      ▼
Confirmation Trigger
      │
      ▼
Email Delivery Dependency
```

Whether the email provider itself is in scope requires project context.

### Example 4 — Conflicting Sources

User story says a field is optional while acceptance criteria say it is mandatory.

The correct analysis outcome is a conflict requiring clarification, not automatic preference for one source unless source precedence is defined.

---

## Best Practices

1. Start with the business objective and actor before detailed rules.
2. Preserve original requirement identifiers where available.
3. Separate explicit behavior from assumptions and missing information.
4. Identify happy paths, alternatives, exceptions, boundaries, and states.
5. Record dependencies that affect testability or execution.
6. Phrase clarification questions so they lead to a specific decision.
7. Avoid duplicating business rules in multiple forms unless traceability requires it.
8. Re-run analysis when authoritative requirements change.
9. Keep analysis technology-independent unless technical context is explicitly part of the requirement.
10. Preserve uncertainty instead of hiding it.

For QA-AI:

- treat the requirement as authoritative evidence;
- distinguish confirmed, derived, ambiguous, and missing information;
- do not silently fill gaps;
- preserve traceability to requirement IDs or sections;
- keep outputs structured enough for downstream skills;
- avoid generating scenarios or test cases inside the analysis artifact unless explicitly requested.

---

## Related Knowledge

### Requirement Engineering

`Requirement-Engineering.md` provides the broader lifecycle for eliciting, specifying, validating, and managing requirements.

### Requirement Review

`Requirement-Review.md` focuses on evaluating requirement quality before downstream use.

### Acceptance Criteria

`Acceptance-Criteria.md` explains measurable conditions used to confirm expected behavior.

### Software Testing Life Cycle

`STLC.md` provides the testing lifecycle context in which requirement analysis is an early testing activity.

### Risk-Based Testing

`Risk-Based-Testing.md` explains how identified risks influence testing priority and depth.

### Testing Techniques

`../testing-techniques/` provides systematic methods for converting analyzed behavior into effective test coverage.

---

## References

This article is conceptually aligned with established software testing and requirements guidance, including:

- ISO/IEC/IEEE 29148 — Requirements engineering and requirements specification.
- ISTQB Certified Tester Foundation Level syllabus — test basis, test analysis, early testing, and testability concepts.
- ISO/IEC/IEEE 29119 — software testing processes.

Project-specific scope, requirement precedence, acceptance rules, traceability expectations, and clarification ownership must come from authoritative project documentation.