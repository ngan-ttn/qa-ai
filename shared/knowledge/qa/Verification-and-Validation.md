# Verification and Validation

> Version: 1.0.0  
> Status: Draft  
> Last Updated: YYYY-MM-DD

## Overview

**Verification and Validation (V&V)** are complementary quality perspectives used to evaluate whether software work products conform to specified requirements and whether the delivered solution satisfies intended needs.

A common shorthand is:

```text
Verification
→ Are we building the product correctly?

Validation
→ Are we building the right product?
```

This shorthand is useful but simplified.

Verification and validation can occur throughout the lifecycle and may use both static and dynamic activities depending on the quality question being evaluated.

---

## Purpose

The purpose of Verification and Validation knowledge is to help QA practitioners distinguish conformance to defined requirements from satisfaction of intended use and stakeholder needs.

It helps teams:

- evaluate requirements and work products earlier;
- verify that implementation conforms to specifications;
- validate that delivered behavior supports intended outcomes;
- identify situations where technically correct software still fails the business need;
- select appropriate static and dynamic quality activities;
- improve requirement, design, and acceptance reasoning.

Within QA-AI, V&V knowledge supports requirement review, requirement analysis, scenario generation, coverage review, acceptance reasoning, and quality assessment.

V&V should not be reduced to fixed project phases unless the project explicitly defines them that way.

---

## Core Concepts

### Verification

Verification evaluates whether a work product satisfies specified requirements, rules, designs, or other defined criteria.

Verification may apply to:

- requirements;
- design;
- code;
- interfaces;
- test artifacts;
- implemented behavior.

Examples include reviewing whether a design reflects an approved requirement or checking whether implemented calculations match a specification.

### Validation

Validation evaluates whether the system or solution satisfies intended use, business need, or stakeholder expectations in the relevant context.

Validation may reveal that a correctly implemented requirement still does not solve the intended problem.

### Conformance

Conformance means alignment with defined criteria.

```text
Specified Requirement
      │
      ▼
Implemented Behavior
      │
      ▼
Compare
```

This perspective is central to verification.

### Intended Use

Intended use describes what users or stakeholders actually need to achieve.

Validation considers whether the delivered solution supports that purpose.

### Test Basis

Verification often depends on explicit artifacts such as requirements, acceptance criteria, designs, or contracts.

Validation may also require broader business, user, operational, or domain context.

### Static V&V Activities

V&V can begin before executable software exists.

Examples include:

- requirement review;
- design review;
- prototype evaluation;
- acceptance-criteria review;
- code review.

### Dynamic V&V Activities

Executable testing can also contribute to verification and validation.

Examples include:

- functional testing against specifications;
- acceptance testing against business needs;
- usability evaluation;
- system testing in representative conditions.

### Acceptance

Acceptance is a project or stakeholder decision that may use validation evidence.

The exact authority and acceptance process are project-specific.

### Relationship to Testing

Testing is one source of V&V evidence, but V&V is broader than test execution alone.

---

## How It Works

Verification and validation operate as complementary questions throughout the lifecycle.

```text
Business Need
      │
      ▼
Requirements
      │
      ├── Verify clarity and consistency
      │
      ▼
Design
      │
      ├── Verify against requirements
      │
      ▼
Implementation
      │
      ├── Verify against design / requirements
      │
      ▼
Delivered System
      │
      └── Validate against intended use
```

### Verification Flow

```text
Defined Criteria
      │
      ▼
Work Product / Behavior
      │
      ▼
Compare
      │
      ▼
Conformance Evidence
```

### Validation Flow

```text
User / Business Need
      │
      ▼
Delivered Capability
      │
      ▼
Evaluate in Relevant Context
      │
      ▼
Fitness Evidence
```

The two perspectives can reveal different quality problems.

---

## When to Use

### Requirement Review

Use verification to check requirement quality and consistency and validation thinking to question whether the requirement reflects the intended need.

### Design Review

Verify that design choices satisfy approved requirements and constraints.

### Test Design

Use requirements as conformance targets while preserving broader user and business objectives.

### Acceptance Testing

Use validation evidence to evaluate whether the solution supports intended use.

### Defect Analysis

Distinguish an implementation defect from a requirement that was implemented correctly but defined the wrong behavior.

### Product Improvement

Use user or production feedback to validate whether delivered behavior remains suitable over time.

---

## When Not to Use

Do not treat Verification and Validation as mutually exclusive or as rigid sequential phases.

Do not assume:

- verification is only static;
- validation is only dynamic;
- QA alone owns validation;
- passing all specification-based tests proves business success;
- user satisfaction overrides explicit regulatory or contractual requirements;
- a requirement is correct merely because it is implemented consistently.

The appropriate evidence depends on the product and decision being made.

---

## Advantages

### Broader Quality Perspective

V&V considers both conformance and intended usefulness.

### Earlier Defect Prevention

Verification can identify problems in requirements and design before implementation.

### Better Acceptance Reasoning

Validation keeps business and user objectives visible.

### Better Defect Classification

Teams can distinguish implementation failures from requirement or product-definition problems.

### Better Lifecycle Quality

V&V encourages quality evaluation at multiple stages rather than only during system testing.

---

## Limitations

### Intended Needs May Be Ambiguous

Stakeholders may disagree about what success means.

### Validation Context May Be Incomplete

Test environments may not fully represent real operational use.

### Conformance Does Not Guarantee Value

Correct implementation of the wrong requirement can still fail the product objective.

### Validation Does Not Replace Specification

User preference alone cannot redefine contractual, regulatory, or approved requirements.

### Terminology Varies

Organizations may use V&V terms differently in governance or regulated processes.

---

## Examples

### Example 1 — Correct Implementation, Wrong Need

Requirement:

> Users must enter ten fields before searching.

The implementation matches the requirement and verification passes.

User research later shows that the workflow prevents users from completing their intended task efficiently.

Validation reveals a product-need problem rather than an implementation-conformance defect.

### Example 2 — Calculation Verification

An approved rule defines a 10% discount for eligible users.

Testing verifies that the system applies exactly 10% under the defined conditions.

### Example 3 — Requirement Review

A requirement states two conflicting status rules.

Static review identifies the inconsistency before implementation, providing verification evidence at the requirement level.

### Example 4 — Acceptance Context

A mobile workflow behaves correctly in functional tests but is unusable on the supported device size used by the target users.

Validation identifies a gap between technical correctness and intended use.

---

## Best Practices

1. Keep the test basis and intended business need visible throughout the lifecycle.
2. Verify requirements before relying on them for implementation and testing.
3. Use static and dynamic evidence where appropriate.
4. Distinguish conformance defects from requirement-definition problems.
5. Make acceptance conditions observable where possible.
6. Include representative users or operational context when validation requires them.
7. Preserve regulatory and contractual requirements during validation decisions.
8. Avoid oversimplifying V&V into fixed tools or phases.
9. Trace important validation findings back to product decisions.
10. Revisit validation as user needs and operating conditions evolve.

For QA-AI:

- separate requirement conformance from intended-use reasoning;
- do not infer stakeholder intent when evidence is absent;
- identify when a passing implementation may still require validation context;
- preserve authoritative requirement and acceptance sources.

---

## Related Knowledge

### Requirement Engineering

`Requirement-Engineering.md` provides the lifecycle in which requirements are defined and validated.

### Requirement Review

`Requirement-Review.md` provides static evaluation of requirement quality.

### Acceptance Criteria

`Acceptance-Criteria.md` explains concrete conditions used for acceptance-oriented verification and validation.

### Static and Dynamic Testing

`Static-and-Dynamic-Testing.md` explains execution modes that can support V&V.

### Software Quality

`Software-Quality.md` provides the broader quality context for conformance and fitness for use.

### Functional and Non-Functional Testing

`Functional-and-Non-Functional-Testing.md` explains quality objectives that may contribute V&V evidence.

---

## References

This article is conceptually aligned with established software-engineering and testing guidance, including:

- ISO/IEC/IEEE 12207 — software lifecycle verification and validation processes.
- ISO/IEC/IEEE 29119 — software testing concepts and processes.
- ISTQB testing guidance — verification, validation, static testing, acceptance testing, and test basis concepts.

Project-specific V&V responsibilities, independence requirements, acceptance authorities, compliance evidence, and approval workflows must come from authoritative project documentation.