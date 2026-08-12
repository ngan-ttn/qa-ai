# Software Development Life Cycle

> Version: 1.0.0  
> Status: Draft  
> Last Updated: YYYY-MM-DD

## Overview

The **Software Development Life Cycle (SDLC)** is a structured way to understand how software progresses from an initial business need through planning, requirements, design, implementation, testing, deployment, operation, maintenance, and eventual retirement.

SDLC is broader than testing.

It describes the overall lifecycle of software and the activities required to create, deliver, operate, change, and retire software systems.

A generalized lifecycle can be represented as:

```text
Business Need
      │
      ▼
Planning
      │
      ▼
Requirements
      │
      ▼
Design
      │
      ▼
Development
      │
      ▼
Testing
      │
      ▼
Deployment
      │
      ▼
Operation & Maintenance
      │
      ▼
Retirement
```

The exact stages, names, sequence, and responsibilities vary across organizations and development models.

SDLC should therefore be understood as a lifecycle concept rather than one mandatory implementation process.

---

## Purpose

The purpose of SDLC knowledge is to provide QA practitioners with a lifecycle-level understanding of where software quality is created, influenced, evaluated, and improved.

This knowledge helps QA practitioners:

- understand where quality risks may originate;
- participate in quality activities earlier;
- distinguish development lifecycle activities from testing lifecycle activities;
- understand how changes propagate across lifecycle stages;
- identify lifecycle-related dependencies;
- recognize that testing is only one contributor to software quality;
- reason about quality before and after formal test execution.

Within QA-AI, SDLC knowledge supports:

- requirement analysis;
- risk analysis;
- regression analysis;
- coverage review;
- change-impact reasoning;
- release-related quality reasoning.

SDLC knowledge should guide lifecycle reasoning without assuming that every project follows the same methodology.

---

## Core Concepts

### Lifecycle Perspective

Software development is not a single implementation activity.

It is a lifecycle involving multiple interconnected stages.

```text
Need
  ↓
Definition
  ↓
Design
  ↓
Implementation
  ↓
Evaluation
  ↓
Delivery
  ↓
Operation
  ↓
Change
```

A problem introduced in one stage may become visible in another.

For example:

```text
Ambiguous Requirement
        │
        ▼
Incorrect Design Assumption
        │
        ▼
Incorrect Implementation
        │
        ▼
Testing Detects Defect
```

The defect is detected during testing, but its origin may be earlier in the lifecycle.

---

### Planning

Planning establishes the high-level direction of the initiative.

Typical concerns may include:

- business objectives;
- project scope;
- stakeholders;
- constraints;
- dependencies;
- high-level risks;
- resources;
- delivery expectations.

From a QA perspective, planning may expose early quality considerations such as:

- critical business areas;
- integration dependencies;
- environment constraints;
- test-data needs;
- non-functional concerns.

---

### Requirements

Requirements define what the system is expected to achieve.

Sources may include:

- business requirements;
- user stories;
- business rules;
- acceptance criteria;
- functional requirements;
- non-functional requirements;
- regulatory requirements;
- process flows.

QA contributes by evaluating requirement quality, including:

- clarity;
- completeness;
- consistency;
- testability;
- traceability;
- observable expected behavior.

Detailed requirement practices belong to the Requirement Engineering knowledge area.

---

### Design

Design determines how the system is expected to satisfy its requirements.

Design may address:

- architecture;
- components;
- workflows;
- APIs;
- data models;
- integration behavior;
- security;
- error handling;
- user experience.

QA may identify design-level risks such as:

- missing workflow paths;
- integration gaps;
- authorization weaknesses;
- data-integrity concerns;
- poor failure handling;
- testability limitations.

---

### Development

Development transforms requirements and designs into working software.

Typical activities may include:

- coding;
- configuration;
- database changes;
- API implementation;
- unit testing;
- code review;
- static analysis;
- component integration.

From a QA perspective, this stage may include preparation for later testing and continuous clarification of expected behavior.

---

### Testing

Testing evaluates software behavior and provides quality evidence.

Testing may include:

- functional testing;
- integration testing;
- regression testing;
- API testing;
- database validation;
- non-functional testing;
- exploratory testing.

SDLC identifies testing as one stage or activity area within the broader lifecycle.

Detailed testing processes belong to `STLC.md`.

---

### Deployment

Deployment moves a software version into a target environment.

Deployment may involve:

- application deployment;
- configuration changes;
- database migration;
- feature activation;
- infrastructure updates;
- integration configuration.

QA may contribute through release verification and validation of critical functionality.

Exact deployment practices are project-specific.

---

### Operation and Maintenance

After release, software enters operational use.

Activities may include:

- monitoring;
- incident handling;
- defect correction;
- support;
- performance monitoring;
- security updates;
- enhancements;
- maintenance changes.

Production behavior provides additional quality evidence.

Examples include:

- incidents;
- user feedback;
- support requests;
- monitoring data;
- production defects.

This information can improve future lifecycle activities.

---

### Retirement

Software or functionality may eventually be removed or replaced.

Retirement may involve:

- decommissioning;
- data migration;
- archival;
- integration removal;
- access removal;
- infrastructure shutdown.

Retirement can introduce significant quality risks and should be treated as part of the lifecycle rather than as an administrative afterthought.

---

### SDLC Models

SDLC can be implemented using different development models.

Common examples include:

- Waterfall;
- V-Model;
- Iterative development;
- Incremental development;
- Agile;
- DevOps-oriented delivery.

These models organize lifecycle activities differently.

They do not redefine the underlying need for planning, requirements, design, implementation, evaluation, delivery, and feedback.

---

### SDLC vs STLC

SDLC and STLC have different scopes.

| Aspect | SDLC | STLC |
|---|---|---|
| Scope | Entire software lifecycle | Testing lifecycle |
| Primary objective | Create, deliver, operate, and maintain software | Organize testing activities |
| Includes development | Yes | No |
| Includes testing | Yes | Core focus |
| Includes deployment and operation | Yes | Only where testing support is relevant |

Conceptually:

```text
SDLC
│
├── Planning
├── Requirements
├── Design
├── Development
├── Testing
│      └── STLC
├── Deployment
└── Operation & Maintenance
```

STLC operates within or alongside SDLC.

---

### Shift-Left Quality

Shift-left means introducing quality-related activities earlier in the lifecycle.

Examples include:

- requirement review;
- acceptance-criteria review;
- early risk analysis;
- design review;
- API-contract review;
- static testing;
- early test design.

The objective is earlier feedback.

It does not mean moving all executable testing before development.

---

### Shift-Right Quality

Shift-right continues quality evaluation after release.

Examples may include:

- production monitoring;
- observability;
- incident analysis;
- user feedback;
- production verification.

Operational evidence can feed back into future lifecycle decisions.

---

## How It Works

SDLC works as a connected lifecycle rather than a set of completely isolated stages.

A generalized flow is:

```text
Business Need
      │
      ▼
Define Scope
      │
      ▼
Understand Requirements
      │
      ▼
Design Solution
      │
      ▼
Implement
      │
      ▼
Evaluate
      │
      ▼
Deploy
      │
      ▼
Operate
      │
      ▼
Collect Feedback
      │
      └──────────────► Future Change
```

Quality is influenced at every stage.

For example:

### Requirement-Level Problem

```text
Missing Business Rule
        │
        ▼
Implementation Assumption
        │
        ▼
Incorrect Behavior
```

### Design-Level Problem

```text
Incomplete Integration Design
        │
        ▼
Incorrect Data Mapping
        │
        ▼
Integration Failure
```

### Deployment-Level Problem

```text
Incorrect Configuration
        │
        ▼
Environment Difference
        │
        ▼
Production Failure
```

SDLC reasoning therefore helps QA identify not only **what failed**, but also **where the quality risk may have originated**.

Changes also propagate through the lifecycle.

```text
Requirement Change
        │
        ▼
Design Impact
        │
        ▼
Implementation Impact
        │
        ▼
Testing Impact
        │
        ▼
Deployment Impact
```

This relationship is important for regression and change-impact analysis.

---

## When to Use

SDLC knowledge is useful whenever QA needs to reason about quality beyond isolated test execution.

### Requirement Review

Use SDLC understanding to identify whether upstream requirement issues may create downstream implementation or testing problems.

### Risk Analysis

Use lifecycle thinking to identify risks associated with:

- requirements;
- design;
- integration;
- implementation;
- deployment;
- operation.

### Change Analysis

Use SDLC relationships to understand how a change may affect downstream artifacts or systems.

### Test Planning

Use lifecycle context to understand:

- development timing;
- environment dependencies;
- release constraints;
- integration availability.

### Release Preparation

Use SDLC knowledge to distinguish testing completion from broader release readiness.

### Production Feedback

Use operational findings to improve future requirements, testing, and risk analysis.

---

## When Not to Use

SDLC knowledge should not be used to impose one universal development process.

Do not assume:

- every project uses Waterfall;
- every project has identical lifecycle stages;
- testing always occurs after development;
- Agile projects do not have an SDLC;
- deployment ends the lifecycle;
- QA owns every lifecycle activity;
- a generic SDLC diagram defines project responsibilities.

Avoid:

```text
Generic SDLC Model
        │
        ✗
        ▼
Assume Project Process
```

Instead:

```text
Generic SDLC Knowledge
        │
        ▼
Understand Lifecycle Concepts
        │
        ▼
Check Actual Project Process
```

Project-specific lifecycle behavior must come from authoritative project information.

---

## Advantages

Applying SDLC knowledge provides several benefits.

### Earlier Quality Awareness

QA can identify problems before executable software exists.

### Better Change-Impact Analysis

Lifecycle relationships help identify downstream consequences of requirement or design changes.

### Better Risk Identification

Quality risks can be recognized across requirements, design, implementation, deployment, and operation.

### Better Collaboration

Understanding the lifecycle helps QA work effectively with business, development, architecture, DevOps, and operations teams.

### Better Test Preparation

Testing activities can begin earlier through requirement analysis, planning, environment preparation, and test design.

### Better Production Learning

Operational feedback can improve future development and testing cycles.

---

## Limitations

SDLC knowledge has several limitations.

### SDLC Models Differ

Organizations may use different stage names, workflows, and responsibilities.

### Lifecycle Boundaries May Overlap

In Agile and continuous-delivery environments, activities may occur simultaneously rather than sequentially.

### Generic SDLC Does Not Define Governance

It does not specify:

- mandatory approvals;
- release gates;
- documentation requirements;
- project roles;
- stage entry or exit criteria.

### Lifecycle Models Do Not Guarantee Quality

Following a defined lifecycle does not ensure that requirements, design, implementation, or testing are effective.

### SDLC Does Not Replace STLC

SDLC provides the broader lifecycle context but does not define detailed testing processes.

---

## Examples

### Example 1 — Requirement Defect Propagation

A requirement does not define duplicate-handling behavior.

```text
Missing Requirement
        │
        ▼
Developer Assumption
        │
        ▼
Duplicate Records
        │
        ▼
Testing Detects Defect
```

The visible defect appears during testing, but the original quality issue began during requirements.

---

### Example 2 — Change Impact

A business rule changes.

Possible lifecycle impact:

```text
Business Rule
      │
      ▼
Requirement
      │
      ▼
API Logic
      │
      ▼
Database Behavior
      │
      ▼
Test Coverage
      │
      ▼
Regression Scope
```

SDLC thinking helps identify that the change may affect more than one implementation artifact.

---

### Example 3 — Agile Lifecycle

An Agile iteration may look like:

```text
Backlog Refinement
       │
       ▼
Requirement Analysis
       │
       ▼
Design & Development
       │
       ▼
Continuous Testing
       │
       ▼
Review
       │
       ▼
Feedback
       │
       └────────► Next Iteration
```

The lifecycle activities still exist even though they overlap and repeat.

---

### Example 4 — Production Feedback

A production incident reveals a missing recovery scenario.

```text
Production Incident
        │
        ▼
Risk Identified
        │
        ▼
Requirement Clarification
        │
        ▼
Test Coverage Updated
        │
        ▼
Future Release
```

Operational evidence becomes input to a new lifecycle cycle.

---

## Best Practices

When applying SDLC knowledge:

1. Understand the actual development model used by the project.
2. Participate in quality activities as early as practical.
3. Review requirements before implementation where possible.
4. Identify lifecycle dependencies.
5. Consider quality risks beyond the testing stage.
6. Prepare testing activities before test execution begins.
7. Analyze downstream impact when requirements or designs change.
8. Use production feedback to improve future quality activities.
9. Distinguish lifecycle concepts from project-specific governance.
10. Adapt QA activities to actual project context.

For QA-AI:

- use SDLC knowledge to understand lifecycle relationships;
- distinguish generic lifecycle guidance from project facts;
- do not infer Waterfall, Agile, or DevOps without evidence;
- do not invent stage-specific responsibilities;
- do not invent entry or exit criteria;
- preserve traceability to actual project inputs.

---

## Related Knowledge

### Software Quality

`Software-Quality.md` explains the broader concept of software quality that is influenced throughout the SDLC.

### Quality Assurance vs Quality Control

`Quality-Assurance-vs-Quality-Control.md` explains how preventive and product-evaluation activities can occur across multiple SDLC stages.

### Software Testing Life Cycle

`STLC.md` provides the testing-specific lifecycle operating within or alongside SDLC.

### Requirement Analysis

`Requirement-Analysis.md` provides deeper guidance for understanding and validating requirements during the requirements stage.

### Test Planning

`Test-Planning.md` describes how testing activities are organized once lifecycle context and testing objectives are understood.

### Regression Testing

`Regression-Testing.md` addresses evaluation of existing behavior after lifecycle changes affect the system.

---

## References

This article is conceptually aligned with established software engineering and testing guidance, including:

- ISO/IEC/IEEE 12207 — Software life cycle processes.
- ISO/IEC/IEEE 29119 — Software testing processes.
- ISTQB Certified Tester Foundation Level syllabus — software development lifecycle and testing concepts.

Specific organizations may implement lifecycle processes differently.

Project-specific SDLC stages, responsibilities, approvals, quality gates, and workflows must come from authoritative project documentation.