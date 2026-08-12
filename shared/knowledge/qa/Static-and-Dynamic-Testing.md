# Static and Dynamic Testing

> Version: 1.0.0  
> Status: Draft  
> Last Updated: YYYY-MM-DD

## Overview

**Static Testing** evaluates work products without executing the software under test.

**Dynamic Testing** evaluates software by executing it and observing behavior.

Conceptually:

```text
Static Testing
→ Evaluate without executing the software

Dynamic Testing
→ Evaluate by executing the software
```

The two approaches are complementary. Static Testing can identify problems earlier in requirements, design, code, and other artifacts, while Dynamic Testing provides evidence about runtime behavior.

---

## Purpose

The purpose of Static and Dynamic Testing knowledge is to help QA practitioners select appropriate quality activities across the software lifecycle.

It helps teams:

- identify defects before executable software exists;
- understand the role of reviews and static analysis;
- understand what runtime testing can and cannot reveal;
- combine preventive and detection-oriented activities;
- improve shift-left testing;
- avoid treating executable testing as the only form of testing.

Within QA-AI, this knowledge supports requirement review, test planning, risk analysis, coverage review, defect prevention, and quality reasoning.

---

## Core Concepts

### Static Testing

Static Testing evaluates artifacts without running the software.

Possible targets include:

- requirements;
- acceptance criteria;
- design documents;
- source code;
- API contracts;
- test cases;
- configuration;
- documentation.

### Review

A review is a human evaluation of a work product.

Reviews may be informal or structured and may involve:

- requirement review;
- design review;
- code review;
- testcase review;
- walkthrough;
- inspection.

The exact review process is organization-specific.

### Static Analysis

Static analysis uses tools to examine software artifacts without executing the application behavior represented by those artifacts.

Examples may include checking source code for:

- rule violations;
- complexity;
- dependency issues;
- unreachable code;
- selected defect patterns.

Tool findings require interpretation and do not automatically represent confirmed product defects.

### Dynamic Testing

Dynamic Testing executes software and evaluates observed results.

Examples include:

- functional testing;
- integration testing;
- regression testing;
- performance testing;
- compatibility testing;
- exploratory testing.

### Defect Prevention

Static Testing may identify issues before they propagate into executable software.

```text
Requirement Defect
      │
      ▼
Static Review Detects Issue
      │
      ▼
Clarification Before Implementation
```

### Runtime Evidence

Dynamic Testing provides evidence about system behavior under tested runtime conditions.

It is necessary for issues that only appear through execution, timing, integration, state, or environment interaction.

### Complementary Coverage

Some problems are easier to detect statically, others dynamically.

Example:

```text
Ambiguous Requirement → Static Review
Incorrect Runtime Calculation → Dynamic Test
```

Effective quality practices use both where appropriate.

---

## How It Works

A lifecycle may combine static and dynamic activities as follows:

```text
Requirement
    │
    ├── Static Review
    │
    ▼
Design
    │
    ├── Static Review
    │
    ▼
Implementation
    │
    ├── Code Review / Static Analysis
    │
    ▼
Executable Build
    │
    └── Dynamic Testing
```

### Static Evaluation

The reviewer or tool examines the artifact against expected quality, standards, consistency, or correctness criteria.

### Dynamic Evaluation

The tester prepares conditions, executes the software, observes actual behavior, and compares it with expected behavior.

### Feedback

Findings from either approach may trigger requirement clarification, design changes, code changes, or additional test coverage.

---

## When to Use

### Requirement and Acceptance Review

Use Static Testing to detect ambiguity, gaps, and contradictions before implementation.

### Design and Interface Review

Use Static Testing to identify structural, contract, and consistency problems.

### Source-Code Quality Activities

Use reviews or static-analysis tools where relevant to the engineering process.

### Executable Feature Verification

Use Dynamic Testing to evaluate actual software behavior.

### Integration and State Behavior

Use Dynamic Testing when runtime interaction is essential to the question.

### Combined Quality Strategy

Use both approaches for important behavior where early prevention and runtime evidence provide complementary value.

---

## When Not to Use

Do not use Static Testing when the quality question can only be answered by runtime behavior.

Do not use Dynamic Testing as a substitute for reviewing ambiguous requirements or specifications.

Do not:

- treat tool warnings as confirmed defects without evaluation;
- assume static review can prove runtime behavior;
- assume passed dynamic tests prove the source or requirements are defect-free;
- require formal inspections for every low-risk artifact;
- classify a practice based only on whether a tool is used.

The distinction is based primarily on execution of the software under test.

---

## Advantages

### Earlier Feedback

Static Testing can identify issues before executable software exists.

### Lower Rework Potential

Early correction may prevent downstream design, code, and test changes.

### Broader Artifact Coverage

Requirements, design, code, and tests can all be evaluated.

### Runtime Confidence

Dynamic Testing provides direct evidence of actual software behavior.

### Complementary Detection

Combining both approaches increases the types of quality problems that can be identified.

---

## Limitations

### Static Testing Cannot Observe Runtime Behavior

Timing, state interaction, integration failures, and environment behavior may require execution.

### Dynamic Testing Requires Executable Software

It cannot detect requirement defects before a runnable implementation exists unless those artifacts are reviewed separately.

### Reviews Depend on Reviewer Knowledge

Important issues may be missed when relevant context or expertise is absent.

### Static Tools Can Produce Noise

Findings may include false positives or low-value warnings.

### Dynamic Coverage Is Incomplete

Only executed conditions provide direct evidence.

---

## Examples

### Example 1 — Requirement Review

Requirement:

> The system should respond quickly.

A static review identifies that the expected performance criterion is undefined.

### Example 2 — Code Review

A reviewer identifies that one error path does not close a resource correctly before the code is executed in system testing.

### Example 3 — Runtime Integration Failure

An API contract appears consistent during review, but Dynamic Testing reveals that production-like configuration causes timeout behavior.

### Example 4 — Testcase Review and Execution

Static review finds that a testcase lacks a measurable expected result. After correction, Dynamic Testing executes the testcase against the application.

---

## Best Practices

1. Apply quality activities as early as useful.
2. Review requirements before relying on them as a test basis.
3. Use static tools as evidence sources, not automatic defect classifiers.
4. Match review depth to artifact risk and importance.
5. Use Dynamic Testing for runtime behavior, interactions, timing, and state.
6. Combine static and dynamic findings when evaluating risk.
7. Preserve traceability from findings to corrected artifacts where valuable.
8. Avoid duplicating the same review without a clear purpose.
9. Use feedback from dynamic failures to improve upstream static reviews.
10. Keep project-specific review processes separate from generic testing concepts.

For QA-AI:

- distinguish artifact analysis from executable behavior;
- do not claim runtime correctness from static evidence alone;
- do not treat automated static findings as confirmed defects without context;
- recommend the evaluation mode that matches the quality question.

---

## Related Knowledge

### Requirement Review

`Requirement-Review.md` is a practical application of Static Testing to requirement artifacts.

### Software Testing Life Cycle

`STLC.md` provides the lifecycle context for static and dynamic testing activities.

### Functional and Non-Functional Testing

`Functional-and-Non-Functional-Testing.md` classifies testing by quality objective rather than execution mode.

### Verification and Validation

`Verification-and-Validation.md` explains broader evaluation perspectives that can use both static and dynamic activities.

### Testing Principles

`Testing-Principles.md` explains early testing and context-dependent test selection.

---

## References

This article is conceptually aligned with established testing guidance, including:

- ISTQB Certified Tester Foundation Level syllabus — static testing, reviews, static analysis, and dynamic testing concepts.
- ISO/IEC/IEEE 29119 — software testing processes.

Project-specific review types, static-analysis tools, coding rules, review responsibilities, and mandatory quality gates must come from authoritative project documentation.