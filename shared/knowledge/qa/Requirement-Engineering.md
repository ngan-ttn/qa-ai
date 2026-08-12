# Requirement Engineering

> Version: 1.0.0  
> Status: Draft  
> Last Updated: YYYY-MM-DD

## Overview

**Requirement Engineering** is the disciplined process of discovering, analyzing, documenting, validating, managing, and evolving the needs and constraints that a software system is expected to satisfy.

For QA, Requirement Engineering is important because test quality depends heavily on the quality of the information used as the test basis.

A generalized requirement lifecycle can be represented as:

```text
Business Need
      │
      ▼
Elicitation
      │
      ▼
Analysis
      │
      ▼
Specification
      │
      ▼
Validation
      │
      ▼
Baseline
      │
      ▼
Change Management
```

The exact activities, artifacts, roles, and approval steps vary across organizations and delivery models.

Requirement Engineering should therefore be understood as a lifecycle of requirement-related activities rather than one mandatory documentation process.

---

## Purpose

The purpose of Requirement Engineering knowledge is to help QA practitioners understand where requirements come from, how they evolve, and how requirement quality affects downstream design, implementation, testing, and release decisions.

This knowledge helps QA practitioners:

- understand business needs before testing behavior;
- distinguish requirements from assumptions and implementation details;
- identify missing, ambiguous, conflicting, or untestable requirements;
- understand relationships between business rules, acceptance criteria, and system behavior;
- preserve requirement traceability across QA artifacts;
- recognize the impact of requirement changes;
- avoid silently inventing behavior when information is incomplete.

Within QA-AI, Requirement Engineering knowledge supports:

- requirement analysis;
- business-rule extraction;
- clarification-question generation;
- risk analysis;
- scenario generation;
- testcase generation;
- coverage review;
- regression-impact analysis.

Requirement Engineering knowledge should guide requirement reasoning without replacing authoritative project requirements.

---

## Core Concepts

### Business Need

A business need describes the problem, opportunity, objective, or outcome that motivates a software change.

It answers questions such as:

- Why is this change needed?
- Who benefits from it?
- What outcome is expected?
- What problem should be solved?

The business need provides context but may not be directly testable until it is translated into more specific requirements.

### Requirement

A requirement describes a capability, behavior, quality, constraint, or condition that the system or solution is expected to satisfy.

Requirements may include:

- business requirements;
- stakeholder requirements;
- functional requirements;
- non-functional requirements;
- interface requirements;
- regulatory requirements;
- data requirements;
- operational constraints.

A requirement should be interpreted using authoritative project context rather than generic expectations.

### Elicitation

Elicitation is the activity of discovering requirement information from stakeholders and other sources.

Sources may include:

- stakeholder discussions;
- existing systems;
- process documents;
- business policies;
- user feedback;
- regulations;
- production behavior;
- data analysis;
- prototypes.

QA may contribute by asking questions that expose missing conditions, exceptions, and testability concerns.

### Analysis

Requirement Analysis examines requirement information to understand scope, behavior, dependencies, rules, risks, ambiguity, and testability.

Typical concerns include:

- actors;
- workflows;
- business rules;
- states;
- validations;
- boundaries;
- exceptions;
- dependencies;
- assumptions;
- missing information.

Detailed QA-oriented analysis belongs to `Requirement-Analysis.md`.

### Specification

Specification expresses requirements in a form that can be communicated and reviewed.

Possible forms include:

- user stories;
- acceptance criteria;
- use cases;
- business rules;
- functional specifications;
- process diagrams;
- interface contracts;
- prototypes.

Requirement Engineering does not require one universal specification format.

### Validation

Requirement validation evaluates whether requirements adequately represent the intended need and are suitable for downstream use.

Typical quality characteristics include:

- clarity;
- completeness;
- consistency;
- correctness;
- feasibility;
- testability;
- traceability.

Validation does not prove that every future implementation decision will be correct.

### Requirement Baseline

A baseline is an agreed version of requirement information used as a reference point for development and testing.

A baseline helps teams distinguish:

```text
Known Requirement
      │
      ▼
Subsequent Change
```

The exact approval and versioning process is project-specific.

### Requirement Change

Requirements may evolve because of:

- business changes;
- stakeholder feedback;
- technical constraints;
- regulatory changes;
- defects;
- production learning;
- scope decisions.

A requirement change may affect multiple downstream artifacts.

```text
Requirement Change
        │
        ▼
Business Rule Impact
        │
        ▼
Design / Implementation Impact
        │
        ▼
Scenario & Testcase Impact
        │
        ▼
Regression Impact
```

### Traceability

Traceability connects requirements to related artifacts and evidence.

A generalized QA traceability chain may be:

```text
Requirement
     │
     ▼
Business Rule
     │
     ▼
Test Scenario
     │
     ▼
Test Case
     │
     ▼
Test Result
```

Traceability supports coverage review and change-impact analysis.

---

## How It Works

Requirement Engineering works as an iterative information-refinement lifecycle.

```text
Need
 │
 ▼
Collect Information
 │
 ▼
Analyze Meaning
 │
 ▼
Resolve Gaps & Conflicts
 │
 ▼
Document Requirement
 │
 ▼
Validate
 │
 ▼
Use for Development & Testing
 │
 ▼
Manage Changes
```

QA involvement can occur throughout this lifecycle.

### During Elicitation

QA may identify questions about:

- alternative flows;
- invalid conditions;
- role differences;
- data constraints;
- integration behavior;
- error handling.

### During Analysis

QA separates:

```text
Explicitly Defined
        │
        ├── Confirmed Behavior
        │
Not Defined
        │
        ├── Clarification Required
        │
Assumption
        │
        └── Must Be Labeled
```

### During Validation

QA reviews whether expected behavior can be observed and verified.

### During Change

QA evaluates downstream impact instead of updating only the changed sentence or story.

Requirement Engineering is therefore connected to both defect prevention and regression reasoning.

---

## When to Use

Requirement Engineering knowledge is useful whenever software behavior must be understood before implementation or testing.

Use it during:

### New Feature Definition

To understand the business objective, expected behavior, constraints, and acceptance conditions.

### Requirement Review

To identify ambiguity, inconsistency, missing information, and testability problems.

### Test Design

To establish a reliable test basis before generating scenarios or test cases.

### Change Analysis

To determine whether a requirement change affects business rules, workflows, data, integrations, or existing coverage.

### Defect Investigation

To distinguish implementation defects from requirement ambiguity or misunderstanding.

### Regression Analysis

To identify downstream artifacts and behaviors affected by requirement changes.

---

## When Not to Use

Requirement Engineering knowledge should not be used to invent project behavior.

Do not:

- replace authoritative requirements with generic best practices;
- treat assumptions as confirmed rules;
- infer missing business behavior solely from similar systems;
- assume every project uses the same requirement artifacts;
- require formal specifications when the project uses another effective format;
- convert technical implementation choices into business requirements without evidence.

Avoid:

```text
Missing Requirement
      │
      ✗
      ▼
AI Invents Behavior
```

Instead:

```text
Missing Requirement
      │
      ▼
Identify Gap
      │
      ▼
Ask / Investigate
```

---

## Advantages

Requirement Engineering provides several benefits.

### Earlier Defect Prevention

Requirement problems can be detected before they become design or implementation defects.

### Better Testability

Clear expected behavior allows QA to design measurable verification.

### Better Coverage

Explicit rules, states, flows, and exceptions improve scenario completeness.

### Better Traceability

Requirements can be connected to downstream QA artifacts and evidence.

### Better Change Management

Requirement relationships help identify the impact of changes.

### Better Collaboration

A shared understanding reduces inconsistent interpretations across stakeholders, developers, and QA.

---

## Limitations

Requirement Engineering also has limitations.

### Requirements Can Remain Incomplete

Not every stakeholder knows all relevant behavior at the beginning of development.

### Requirements Evolve

A validated requirement may later change because of new information or constraints.

### Documentation Does Not Guarantee Understanding

A detailed specification can still be interpreted incorrectly.

### Formality Has Cost

Excessive documentation can slow feedback without improving clarity.

### Generic Knowledge Cannot Define Project Governance

Requirement approvals, ownership, templates, and baselines must come from project-specific sources.

---

## Examples

### Example 1 — Ambiguous Requirement

Requirement:

> The system should lock a user after several failed login attempts.

Problems include:

- number of attempts is undefined;
- lock duration is undefined;
- meaning of consecutive attempts is undefined;
- behavior during lock is undefined.

Requirement Engineering identifies these as clarification gaps rather than inventing values.

### Example 2 — Requirement Change

Original rule:

> Orders above $100 receive free shipping.

Changed rule:

> Premium members receive free shipping regardless of order value.

Possible impact:

```text
Requirement
   │
   ▼
Eligibility Rule
   │
   ▼
Checkout Logic
   │
   ▼
Scenario Coverage
   │
   ▼
Regression Scope
```

### Example 3 — Conflicting Requirements

One document states that a field is optional while acceptance criteria state that it is mandatory.

QA should record the inconsistency and request resolution rather than selecting one interpretation silently.

---

## Best Practices

When applying Requirement Engineering knowledge:

1. Start from the business objective before analyzing detailed behavior.
2. Separate explicit facts from assumptions and inferred behavior.
3. Review requirements for clarity, completeness, consistency, and testability.
4. Identify rules, conditions, states, boundaries, and exceptions explicitly.
5. Ask targeted clarification questions when behavior is undefined.
6. Maintain traceability for important requirements and downstream QA artifacts.
7. Reassess test coverage whenever requirements change.
8. Use the level of documentation appropriate to project risk and complexity.
9. Preserve authoritative wording where exact behavior matters.
10. Avoid duplicating requirement content across multiple artifacts without a clear purpose.

For QA-AI:

- treat supplied requirement information as authoritative input;
- label inferred or missing behavior explicitly;
- do not silently normalize conflicting requirements;
- preserve identifiers when available;
- propagate confirmed changes to downstream artifacts;
- distinguish clarification required from technical investigation required.

---

## Related Knowledge

### Software Development Life Cycle

`SDLC.md` provides the broader lifecycle context in which requirements influence design, implementation, testing, and change.

### Software Testing Life Cycle

`STLC.md` explains how requirement understanding becomes an input to testing activities.

### Requirement Analysis

`Requirement-Analysis.md` provides deeper QA-oriented guidance for structuring and evaluating requirement information.

### Requirement Review

`Requirement-Review.md` focuses on evaluating requirement quality before downstream use.

### Acceptance Criteria

`Acceptance-Criteria.md` explains measurable conditions used to determine whether expected behavior is satisfied.

### Verification and Validation

`Verification-and-Validation.md` explains complementary perspectives for evaluating conformance and intended need.

---

## References

This article is conceptually aligned with established requirements-engineering and software-engineering guidance, including:

- ISO/IEC/IEEE 29148 — Requirements engineering and requirements specification.
- ISO/IEC/IEEE 12207 — Software life cycle processes.
- ISTQB Certified Tester Foundation Level syllabus — test basis, requirements-related testing concepts, and early testing.

Specific organizations may implement Requirement Engineering differently.

Project-specific requirement types, ownership, approval processes, baselines, templates, traceability rules, and change workflows must come from authoritative project documentation.