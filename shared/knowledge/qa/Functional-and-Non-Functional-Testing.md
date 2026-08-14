# Functional and Non-Functional Testing

> Version: 1.0.0  
> Status: Draft  
> Last Updated: 2026-08-14

## Overview

**Functional Testing** evaluates what a system does against specified or expected behavior.

**Non-Functional Testing** evaluates quality characteristics describing how well the system behaves under relevant conditions.

Conceptually:

```text
Functional Testing
→ What does the system do?

Non-Functional Testing
→ How well does the system behave?
```

The categories are complementary. A feature can be functionally correct while still being too slow, unreliable, inaccessible, incompatible, or otherwise unsuitable for its intended context.

---

## Purpose

The purpose of this knowledge is to help QA practitioners distinguish functional correctness from broader quality characteristics and plan appropriate coverage for both.

It helps teams:

- identify functional behavior requiring verification;
- recognize relevant non-functional quality risks;
- avoid treating functional test completion as proof of overall quality;
- connect requirements to appropriate test types;
- identify missing measurable quality criteria;
- reason about coverage across product behavior and quality characteristics.

Within QA-AI, this knowledge supports requirement analysis, risk analysis, test planning, scenario generation, coverage review, and quality reasoning.

Non-functional expectations should not be invented when project criteria are absent.

---

## Core Concepts

### Functional Testing

Functional Testing evaluates behavior such as:

- input validation;
- calculations;
- business rules;
- workflows;
- state transitions;
- permissions;
- integrations;
- data processing;
- error handling.

Expected behavior should come from an authoritative test basis.

### Non-Functional Testing

Non-Functional Testing evaluates quality characteristics and constraints.

Common areas include:

- performance;
- reliability;
- usability;
- security;
- compatibility;
- accessibility;
- scalability;
- recoverability.

The exact set depends on product context and quality requirements.

### Functional Correctness

Functional correctness asks whether the system produces the expected result under defined conditions.

### Performance

Performance concerns may include response time, throughput, resource utilization, and behavior under load. Thresholds must come from approved requirements or objectives.

### Reliability

Reliability concerns the system's ability to perform consistently over time and under defined conditions.

### Usability

Usability concerns how effectively and efficiently intended users can achieve goals.

### Security

Security concerns protection of confidentiality, integrity, availability, authentication, authorization, and related risks.

### Compatibility

Compatibility concerns behavior across relevant operating systems, browsers, devices, versions, interfaces, or environments.

### Accessibility

Accessibility evaluates whether the product can be used by people with relevant disabilities and assistive technologies according to applicable requirements or standards.

### Interaction Between Categories

Functional and non-functional concerns often intersect.

```text
Login Functionally Works
       │
       ├── But response time may be unacceptable
       ├── But authorization may be inadequate
       └── But interface may be inaccessible
```

---

## How It Works

Coverage begins by identifying expected behavior and relevant quality characteristics.

```text
Requirement & Risk Context
       │
       ▼
Identify Functional Behavior
       │
       ▼
Identify Quality Characteristics
       │
       ▼
Select Test Types & Techniques
       │
       ▼
Prepare Environment / Data / Tools
       │
       ▼
Execute & Evaluate
```

Functional expected results are often discrete behaviors. Non-functional expected results may require measurements, thresholds, standards, or comparative evaluation.

Quality decisions should consider both categories where relevant.

---

## When to Use

Use this distinction during:

### Requirement Analysis

To detect when functional behavior is defined but important quality characteristics are missing.

### Test Planning

To select appropriate test types, environments, tools, and expertise.

### Risk Analysis

To identify quality risks beyond functional correctness.

### Release Readiness

To avoid quality conclusions based only on functional pass results.

### Production Learning

To identify operational concerns such as latency, reliability, compatibility, or accessibility that require future coverage.

---

## When Not to Use

Do not treat Functional and Non-Functional Testing as completely isolated categories.

Do not:

- assume every quality characteristic must be tested for every feature;
- invent performance or availability thresholds;
- assume functional correctness means business suitability;
- classify a test only for taxonomy when the classification adds no decision value;
- assume manual testing is functional and automation is non-functional or vice versa.

Testing type should follow the quality question being evaluated.

---

## Advantages

### Broader Quality Coverage

The distinction encourages teams to consider more than functional correctness.

### Better Planning

Specialized environments, tools, or expertise can be identified early.

### Better Requirement Review

Missing quality criteria become easier to identify.

### Better Risk Alignment

High-impact quality characteristics can receive appropriate attention.

### Better Release Decisions

Evidence can include both behavior and quality characteristics.

---

## Limitations

### Categories Can Overlap

Quality concerns such as usability or reliability may involve observable functional behavior as well as non-functional characteristics.

### Non-Functional Criteria May Be Missing

Without measurable targets, evaluation can be ambiguous.

### Specialized Testing Can Be Expensive

Some quality characteristics require dedicated tools, environments, or expertise.

### Generic Lists Do Not Define Scope

Not every quality characteristic is relevant to every product.

### Passing Tests Do Not Prove Overall Quality

Only selected behaviors and conditions are evaluated.

---

## Examples

### Example 1 — Login

Functional tests may verify valid authentication, invalid-password handling, and account-lock behavior.

Non-functional tests may evaluate response time, compatibility, accessibility, or reliability when those concerns are relevant and defined.

### Example 2 — Search

Functional:

> Correct items are returned for a valid query.

Non-functional:

> Search responds within an approved performance target under specified load.

### Example 3 — Mobile Application

Functional coverage may pass on one device while compatibility testing reveals a failure on another supported device.

### Example 4 — Data Import

An import may process records correctly under normal conditions but fail reliability expectations during large or repeated workloads.

---

## Best Practices

1. Start from product requirements and risk rather than a generic checklist of test types.
2. Separate functional behavior from quality-characteristic expectations during analysis.
3. Make non-functional targets measurable where acceptance depends on them.
4. Identify specialized environment and tooling needs early.
5. Evaluate interactions between functional and non-functional risks.
6. Preserve supported platforms and conditions explicitly for compatibility testing.
7. Avoid claiming non-functional compliance without appropriate evidence.
8. Use production evidence to refine future quality-characteristic testing.
9. Keep specialist testing within qualified scope and expertise.
10. Communicate untested quality characteristics as residual risk where material.

For QA-AI:

- do not invent performance, accessibility, or reliability thresholds;
- distinguish requirement-backed criteria from recommended investigation;
- map test recommendations to actual product risk;
- preserve uncertainty when non-functional context is missing.

---

## Related Knowledge

### Software Quality

`Software-Quality.md` provides the broader quality perspective behind functional and non-functional evaluation.

### Test Strategy

`Test-Strategy.md` explains how test types are selected according to product risk and quality objectives.

### Risk-Based Testing

`Risk-Based-Testing.md` helps prioritize quality characteristics according to impact and likelihood.

### Verification and Validation

`Verification-and-Validation.md` provides complementary perspectives on conformance and intended use.

### Testing Principles

`Testing-Principles.md` explains why testing scope must be context-dependent and cannot be exhaustive.

---

## References

This article is conceptually aligned with established software-quality and testing guidance, including:

- ISO/IEC 25010 — software product quality characteristics.
- ISTQB testing guidance — functional and non-functional testing concepts and test types.
- ISO/IEC/IEEE 29119 — software testing processes.

Project-specific non-functional requirements, supported platforms, quality thresholds, compliance obligations, and specialized test scope must come from authoritative project documentation.