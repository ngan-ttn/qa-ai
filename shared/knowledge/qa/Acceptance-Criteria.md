# Acceptance Criteria

> Version: 1.0.0  
> Status: Draft  
> Last Updated: YYYY-MM-DD

## Overview

**Acceptance Criteria** are explicit conditions used to determine whether a requirement, user story, feature, or change satisfies the expected business behavior for acceptance.

Acceptance Criteria translate product intent into observable outcomes that can be reviewed, implemented, and tested.

A generalized relationship is:

```text
Business Need
     │
     ▼
Requirement / User Story
     │
     ▼
Acceptance Criteria
     │
     ▼
Expected Observable Behavior
     │
     ▼
Verification
```

Acceptance Criteria do not replace the full requirement. They define important acceptance conditions within the requirement context.

---

## Purpose

The purpose of Acceptance Criteria is to create a shared and testable understanding of when expected behavior is satisfied.

Acceptance Criteria help teams:

- clarify intended behavior;
- reduce ambiguity between stakeholders, developers, and QA;
- define important conditions and outcomes;
- expose missing business rules;
- support implementation decisions;
- provide a direct input to test analysis;
- support traceability between requirements and test coverage;
- establish a basis for acceptance discussions.

Within QA-AI, Acceptance Criteria knowledge supports:

- requirement analysis;
- business-rule extraction;
- scenario generation;
- testcase generation;
- coverage review;
- clarification-question generation.

Acceptance Criteria should be interpreted together with authoritative requirement context rather than as isolated sentences.

---

## Core Concepts

### Acceptance Condition

An acceptance condition describes a specific state, action, rule, or result that must be satisfied.

A useful condition generally answers:

- Under what situation?
- What action or event occurs?
- What observable result is expected?

### Observable Outcome

Acceptance Criteria should describe behavior that can be observed or verified.

Examples include:

- a message is displayed;
- an order changes status;
- a calculation returns a defined result;
- access is denied for an unauthorized role;
- data is persisted;
- an event is triggered.

Criteria that rely on subjective terms may be difficult to verify.

### Preconditions

A precondition describes relevant state that must exist before the acceptance behavior applies.

Examples:

- user is authenticated;
- account is active;
- order is in `Draft` status;
- inventory is available.

Preconditions should only be included when they materially affect the behavior.

### Trigger

A trigger is the action or event that causes the system to evaluate the acceptance behavior.

Examples:

- user submits a form;
- payment succeeds;
- timer expires;
- administrator approves a request.

### Expected Result

The expected result is the observable outcome that demonstrates whether the criterion is satisfied.

It should be specific enough to distinguish correct from incorrect behavior.

### Business Rule Relationship

Acceptance Criteria often express business rules in executable or reviewable context.

```text
Business Rule
      │
      ▼
Acceptance Condition
      │
      ▼
Scenario / Testcase
```

The same business rule may affect multiple criteria.

### Positive and Negative Criteria

Positive criteria describe expected successful behavior.

Negative criteria describe behavior under invalid, prohibited, or exceptional conditions.

Both may be important when the requirement depends on validation, permissions, limits, or failure handling.

### Boundary Criteria

When behavior changes at a threshold, Acceptance Criteria should make the boundary explicit where it is important to acceptance.

Example:

```text
Attempts 1–4 → Account remains unlocked
Attempt 5    → Account becomes locked
```

### Format Independence

Acceptance Criteria may be written in different forms.

Common examples include:

- bullet statements;
- Given / When / Then;
- rule tables;
- examples;
- numbered conditions.

No single format is mandatory unless project standards require it.

---

## How It Works

Acceptance Criteria are derived from requirement intent and relevant business rules.

A generalized flow is:

```text
Understand Requirement
      │
      ▼
Identify Important Conditions
      │
      ▼
Identify Trigger
      │
      ▼
Define Observable Outcome
      │
      ▼
Check Ambiguity & Coverage
      │
      ▼
Review with Stakeholders
```

### Given / When / Then Example

```text
Given   a registered user has entered four consecutive incorrect passwords
When    the user enters an incorrect password for the fifth consecutive attempt
Then    the account becomes temporarily locked
```

The format helps separate state, trigger, and expected outcome.

### Rule-Oriented Example

```text
AC-01: Attempts 1–4 do not lock the account.
AC-02: The fifth consecutive incorrect attempt locks the account.
AC-03: A successful login before the fifth failure resets failed-attempt tracking.
```

Both forms can be valid if they clearly express expected behavior.

---

## When to Use

Acceptance Criteria are useful when a feature or change requires clear acceptance conditions.

### User Stories

To define the behavior that must be satisfied for the story to be accepted.

### Requirement Clarification

To make vague business expectations observable.

### Test Design

To identify direct coverage obligations and expected results.

### Business Rule Validation

To express important rules in concrete scenarios or outcomes.

### Change Requests

To define how changed behavior differs from existing behavior.

### UAT Preparation

To provide a shared acceptance basis between product stakeholders and delivery teams.

---

## When Not to Use

Acceptance Criteria should not be used as a substitute for all requirement information.

Do not:

- omit important context because a short criterion exists;
- duplicate the entire specification inside acceptance criteria;
- invent technical behavior not required for acceptance;
- use vague criteria such as `works correctly` or `looks good`;
- assume every testcase must map one-to-one to one acceptance criterion;
- treat absent criteria as proof that other requirement behavior is out of scope;
- use acceptance criteria to define project-specific architecture unless explicitly required.

Acceptance Criteria should remain focused on acceptance-significant behavior.

---

## Advantages

### Shared Understanding

Criteria reduce interpretation differences between business, development, and QA.

### Better Testability

Observable outcomes provide a stronger basis for verification.

### Earlier Gap Detection

Writing criteria can expose missing conditions, exceptions, or rules.

### Better Traceability

Criteria can be mapped to scenarios and test cases.

### Better Scope Control

Explicit acceptance conditions help clarify what is essential to the change.

### Better Reviewability

Stakeholders can review concrete behavior more easily than broad intent alone.

---

## Limitations

### Criteria Can Be Incomplete

A small set of acceptance criteria may not cover every relevant requirement behavior.

### Over-Specification Can Reduce Flexibility

Criteria that encode unnecessary implementation details can constrain design without business need.

### Poor Criteria Create False Confidence

A story may satisfy written criteria while still missing important requirement behavior.

### Context Still Matters

The meaning of a criterion may depend on business rules, role definitions, state models, or external specifications.

### Format Does Not Guarantee Quality

Given / When / Then syntax does not automatically make a criterion clear or correct.

---

## Examples

### Example 1 — Field Validation

Requirement:

> Email is required for registration.

Acceptance Criteria:

```text
Given the registration form is displayed
When the user submits the form without an email address
Then registration is rejected and the required-field validation is shown
```

### Example 2 — Role Restriction

```text
Given a user does not have the Approver role
When the user opens an approval-required request
Then the approval action is not available to that user
```

The exact UI behavior must match the authoritative requirement.

### Example 3 — Boundary

```text
AC-01: Quantity 1–99 follows standard approval.
AC-02: Quantity 100 or greater requires additional approval.
```

### Example 4 — Ambiguous Criterion

Weak:

> The report loads quickly.

Problem:

- `quickly` is not measurable.

Improved form should reference an approved performance criterion rather than inventing a threshold.

---

## Best Practices

1. Write acceptance criteria from the user's or business behavior perspective.
2. Make expected outcomes observable and verifiable.
3. Include important preconditions when state affects behavior.
4. Express relevant boundaries explicitly.
5. Include negative or exception behavior when it affects acceptance.
6. Avoid embedding unnecessary implementation details.
7. Keep criteria consistent with business rules and other authoritative sources.
8. Review criteria before implementation where practical.
9. Preserve identifiers when criteria are used for traceability.
10. Treat missing or conflicting criteria as clarification needs rather than assumptions.

For QA-AI:

- preserve acceptance-criteria IDs and exact values;
- distinguish explicit criteria from inferred scenarios;
- do not treat criteria as the complete feature specification unless the source explicitly does so;
- map scenarios back to relevant criteria where possible;
- surface conflicts between criteria and other requirements.

---

## Related Knowledge

### Requirement Engineering

`Requirement-Engineering.md` provides the broader process in which acceptance conditions are defined and maintained.

### Requirement Analysis

`Requirement-Analysis.md` explains how acceptance criteria are analyzed together with flows, rules, states, and dependencies.

### Requirement Review

`Requirement-Review.md` provides guidance for evaluating acceptance criteria for clarity, completeness, consistency, and testability.

### Testing Techniques

`../testing-techniques/` provides methods for expanding acceptance conditions into broader test coverage.

### Verification and Validation

`Verification-and-Validation.md` provides complementary perspectives for evaluating whether implemented behavior conforms to requirements and intended needs.

---

## References

This article is conceptually aligned with established requirements and testing guidance, including:

- ISO/IEC/IEEE 29148 — requirements engineering and specification quality.
- ISTQB Certified Tester Foundation Level syllabus — test basis, acceptance criteria, test analysis, and testability concepts.
- Agile requirements practices commonly using examples and Given / When / Then expressions.

Project-specific acceptance formats, ownership, sign-off rules, source precedence, and Definition of Done must come from authoritative project documentation.