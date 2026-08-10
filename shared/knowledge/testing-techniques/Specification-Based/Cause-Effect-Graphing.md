# Cause-Effect Graphing

> Version: 1.0.0
> Status: Draft
> Last Updated: YYYY-MM-DD

---

# Overview

Cause-Effect Graphing is a Specification-Based Test Design Technique used to analyze logical relationships between input conditions (causes) and resulting system behaviors (effects).

Unlike techniques that focus on input values, boundaries, or business rule combinations, Cause-Effect Graphing models the logical dependencies that determine how different conditions influence system outcomes.

The technique represents these relationships using a Boolean graph composed of logical operators such as AND, OR, and NOT.

By visualizing the logical structure of a requirement, testers can identify missing conditions, conflicting logic, impossible combinations, and incomplete specifications before implementation begins.

Cause-Effect Graphing is particularly valuable for systems containing complex validation rules, eligibility criteria, calculation logic, authorization rules, and regulatory requirements.

---

# Purpose

The primary purpose of Cause-Effect Graphing is to transform complex logical requirements into a structured model that can be systematically analyzed and converted into executable test cases.

Its objectives include:

- Identify logical relationships.
- Validate cause-and-effect dependencies.
- Detect missing logical conditions.
- Detect contradictory requirements.
- Improve logical coverage.
- Support systematic test case generation.

---

# Learning Objectives

After completing this article, readers should be able to:

- Explain why Cause-Effect Graphing exists.
- Identify causes and effects from requirements.
- Apply Boolean logic to software requirements.
- Construct a Cause-Effect Graph.
- Convert a graph into a Decision Table.
- Generate effective test cases from logical models.

---

# Knowledge Map

```
Black-Box Testing
        │
        ▼
Cause-Effect Graphing
        │
        ▼
Decision Table Testing
        │
        ▼
Test Cases
```

Cause-Effect Graphing focuses on logical modeling, while Decision Table Testing focuses on business rule representation.

---

# Why Cause-Effect Graphing Exists

Consider the following requirement:

> Approve a loan if the applicant has a valid identity **AND** a sufficient credit score **OR** a government guarantee.

Although the requirement is relatively short, the underlying logic is more complex than it first appears.

Questions immediately arise:

- Does the guarantee replace the credit score?
- Must identity always be verified?
- What happens if only one condition is satisfied?
- Are some combinations impossible?

As the number of logical conditions increases, reasoning about every possible outcome becomes increasingly difficult.

Cause-Effect Graphing exists to make these logical relationships explicit, visual, and testable.

---

# History and Background

Cause-Effect Graphing was introduced to help testers analyze requirements containing complex logical dependencies.

The technique applies concepts from Boolean algebra and graph theory to software testing.

Rather than describing business rules only in text, testers construct a graph that represents how input conditions combine to produce specific system behaviors.

This graph can then be transformed into a Decision Table and ultimately into executable test cases.

Today, Cause-Effect Graphing is recognized as an advanced Specification-Based Testing technique and is particularly useful for systems with sophisticated validation logic.

---

# Core Concepts

---

## Cause

A cause is an input condition or circumstance that influences system behavior.

Examples:

- Customer is VIP
- Credit Score ≥700
- Identity Verified
- Coupon Applied
- User has Administrator Role

Each cause represents one logical input to the system.

---

## Effect

An effect is an observable system behavior that occurs when specific logical conditions are satisfied.

Examples:

- Apply Discount
- Approve Loan
- Grant Access
- Reject Request
- Display Error Message

Effects should always represent externally observable outcomes.

---

## Logical Relationship

Causes rarely operate independently.

They are connected using Boolean operators.

Examples:

```
Cause A

AND

Cause B
```

```
Cause A

OR

Cause B
```

```
NOT Cause A
```

These logical relationships determine when an effect should occur.

---

## Boolean Operators

Cause-Effect Graphing commonly uses:

- AND
- OR
- NOT

More complex requirements may involve nested logical expressions.

Correct interpretation of these operators is essential for accurate graph construction.

---

## Cause-Effect Graph

A Cause-Effect Graph visually represents the logical relationship between causes and effects.

Example:

```
Identity Verified ─┐
                   AND ─────► Approve Loan
Credit Score Pass ─┘

Government Guarantee ───────►
```

The graph makes complex requirements easier to understand and review before implementation.

---

## Constraints

Not every combination of causes is meaningful.

Examples include:

- Mutually exclusive conditions.
- Mandatory conditions.
- Impossible combinations.
- One-and-only-one selections.

Constraints prevent invalid or unrealistic combinations from being converted into unnecessary test cases.

---

# Testing Philosophy

Cause-Effect Graphing is based on one guiding principle.

> **Complex system behavior is best understood by modeling the logical relationships between causes and effects before designing test cases.**

Rather than starting directly with test cases, testers first model the underlying logic.

This approach improves requirement analysis, exposes hidden assumptions, and produces more systematic test coverage.
# How Cause-Effect Graphing Works

Cause-Effect Graphing transforms logical business requirements into a visual model that systematically represents how input conditions influence system behavior.

Instead of designing test cases directly from textual requirements, testers first model the logical relationships between causes and effects.

The overall workflow is shown below.

```
Business Requirement
        │
        ▼
Identify Causes
        │
        ▼
Identify Effects
        │
        ▼
Identify Logical Relationships
        │
        ▼
Build Cause-Effect Graph
        │
        ▼
Apply Constraints
        │
        ▼
Convert to Decision Table
        │
        ▼
Generate Test Cases
```

---

# Step 1 — Understand the Requirement

Begin by understanding the complete business logic.

Example:

```
Approve Loan when

Identity Verified

AND

(Credit Score Pass

OR

Government Guarantee)
```

Before modeling the graph, QA engineers should clarify:

- Which inputs influence the result?
- Which outputs are observable?
- Are all logical operators explicitly defined?
- Are there hidden assumptions?
- Are exceptional cases documented?

Cause-Effect Graphing depends on logical precision.

---

# Step 2 — Identify Causes

A cause is an independent input condition.

Example:

| ID | Cause |
|----|-------|
| C1 | Identity Verified |
| C2 | Credit Score Pass |
| C3 | Government Guarantee |

Each cause should represent one independent logical condition.

Avoid combining multiple ideas into a single cause.

Incorrect:

```
Customer is VIP and Order >100
```

Correct:

```
C1 Customer is VIP

C2 Order >100
```

---

# Step 3 — Identify Effects

Effects describe observable system behavior.

Example:

| ID | Effect |
|----|--------|
| E1 | Loan Approved |
| E2 | Loan Rejected |

Effects should always be externally verifiable.

Avoid describing internal implementation details.

---

# Step 4 — Identify Logical Relationships

Connect causes using Boolean operators.

Example:

```
Identity Verified

AND

(Credit Score Pass

OR

Government Guarantee)
```

Logical relationships define **when** an effect should occur.

Incorrect interpretation at this stage leads directly to incorrect test cases.

---

# Step 5 — Build the Cause-Effect Graph

Represent the requirement visually.

Example:

```
C2 ───┐
       │
       OR ───┐
C3 ───┘      │
             AND ─────► E1
C1 ──────────┘
```

The graph makes logical dependencies explicit.

It is often easier to review than textual requirements.

---

# Step 6 — Apply Constraints

Not every theoretical combination is valid.

Typical constraints include:

## Mutually Exclusive

Example:

```
Customer Type

VIP

Regular
```

A customer cannot be both simultaneously.

---

## Requires

Example:

```
Loan Approval

requires

Identity Verification
```

Without identity verification, approval is impossible.

---

## One-and-Only-One

Example:

```
Payment Method

Credit Card

Bank Transfer

Cash
```

Exactly one option may be selected.

---

## At-Least-One

Example:

```
Contact Method

Phone

Email

SMS
```

At least one method must be provided.

Applying constraints eliminates unrealistic combinations before test generation.

---

# Step 7 — Convert the Graph into a Decision Table

The graph itself is not the final testing artifact.

It is transformed into a Decision Table.

Example:

| C1 | C2 | C3 | E1 |
|----|----|----|----|
| Y | Y | N | Y |
| Y | N | Y | Y |
| Y | N | N | N |
| N | Y | Y | N |

The Decision Table provides a structured representation suitable for deriving test cases.

---

# Step 8 — Generate Test Cases

Each meaningful decision rule becomes one or more executable test cases.

Example:

Rule:

| Identity | Credit | Guarantee | Result |
|-----------|----------|------------|--------|
| Y | N | Y | Approve |

Possible test case:

**Preconditions**

- Applicant identity verified.

**Input**

- Credit Score = Fail
- Government Guarantee = Yes

**Expected Result**

- Loan approved.

Traceability between requirement, graph, decision table, and test case remains clear.

---

# Common Boolean Patterns

## AND

```
A

AND

B

↓

Effect
```

All causes must be true.

---

## OR

```
A

OR

B

↓

Effect
```

Any cause may trigger the effect.

---

## NOT

```
NOT A

↓

Effect
```

The effect occurs only when the cause is absent.

---

## Nested Logic

```
(A AND B)

OR

(C AND D)
```

Nested expressions are common in enterprise systems.

Modeling them graphically greatly improves readability.

---

# Worked Example 1 — Banking

Requirement:

```
Approve Loan if

Identity Verified

AND

(Credit Score Pass

OR

Government Guarantee)
```

Graph:

```
Identity

──────────┐

           AND

Credit ─┐  │

         OR ─────► Approve

Guarantee┘
```

---

# Worked Example 2 — E-Commerce Promotion

Requirement:

```
Apply Promotion when

VIP Customer

AND

Order ≥100

AND

Coupon Not Used
```

Causes:

- VIP
- Order ≥100
- Coupon Not Used

Effect:

- Promotion Applied

---

# Worked Example 3 — RBAC

Requirement:

```
Delete Record if

Admin

OR

Manager with Delete Permission
```

Graph:

```
Admin ───┐

          OR ───► Delete

Manager

AND

Delete Permission
```

---

# Worked Example 4 — Import Permit

Requirement:

```
Edit Permit when

Permit Approved

AND

Remaining Qty Available

AND

RA Role
```

The graph clearly separates:

- Permission
- Business Status
- Quantity Constraint

before creating a Decision Table.

---

# Worked Example 5 — Warehouse Cycle Count

Requirement:

```
Generate Gap Report when

Scanning Completed

AND

Inventory Snapshot Saved
```

Graph:

```
Scanning Completed

AND

Snapshot Saved

↓

Generate Report
```

Testing focuses on validating the logical dependency rather than only workflow execution.

---

# Visualizing Cause-Effect Thinking

```
Requirement
        │
        ▼
Causes
        │
        ▼
Boolean Logic
        │
        ▼
Effects
        │
        ▼
Cause-Effect Graph
        │
        ▼
Decision Table
        │
        ▼
Test Cases
```

Cause-Effect Graphing introduces an intermediate modeling step that improves both requirement analysis and systematic test design.
# Advantages

Cause-Effect Graphing provides a systematic approach for analyzing complex logical requirements before designing test cases.

Instead of reasoning about business logic mentally, testers build an explicit logical model that improves both requirement quality and testing effectiveness.

---

## Improves Requirement Understanding

Many requirements appear simple until their logical dependencies are analyzed.

Example:

```
Approve Loan if

Identity Verified

AND

(Credit Score Pass

OR

Government Guarantee)
```

A Cause-Effect Graph exposes the exact logical relationship, reducing misunderstanding between Business Analysts, Developers, and QA Engineers.

---

## Detects Missing Logical Conditions

While constructing the graph, testers often discover missing conditions.

Example:

```
Identity Verified

AND

Credit Score Pass
```

Questions naturally arise:

- Is age verification required?
- Is customer status relevant?
- Are there regulatory exceptions?

The graph encourages deeper requirement analysis before implementation begins.

---

## Detects Contradictory Logic

Logical conflicts become much easier to identify.

Example:

```
Condition A

↓

Approve Request
```

Another requirement states:

```
Condition A

↓

Reject Request
```

Representing both in the same graph immediately exposes the inconsistency.

---

## Simplifies Complex Requirements

Large textual requirements can be difficult to understand.

Graphical representation makes logical dependencies much easier to review.

This is particularly valuable in:

- Banking
- Insurance
- Healthcare
- ERP
- Regulatory Systems

---

## Provides a Foundation for Decision Tables

A Cause-Effect Graph is not the final testing artifact.

Instead, it provides a structured foundation for constructing a Decision Table.

This improves:

- Requirement traceability
- Rule completeness
- Test case consistency

---

# Limitations

Although Cause-Effect Graphing is powerful, it is not appropriate for every feature.

---

## Not Suitable for Simple Requirements

Example:

```
Age

18–60
```

The requirement contains a simple range rather than complex logical dependencies.

Boundary Value Analysis and Equivalence Partitioning are more suitable.

---

## Graph Complexity

As the number of causes increases, the graph may become difficult to read.

Example:

```
10 Causes

↓

Hundreds of logical paths
```

Large graphs should be divided into smaller logical units where appropriate.

---

## Does Not Model Workflow

Cause-Effect Graphing explains logical relationships.

It does not represent:

- Business lifecycle
- Workflow progression
- State changes

State Transition Testing should be used when behavior depends on the current system state.

---

# Decision Guide

Use the following guide when selecting Cause-Effect Graphing.

```
Requirement
      │
      ▼
Does behavior depend on multiple logical conditions?
      │
      ├── No
      │      │
      │      ▼
      │  Consider another technique
      │
      └── Yes
             │
             ▼
Are logical relationships (AND / OR / NOT) important?
             │
             ├── No
             │      │
             │      ▼
             │  Decision Table may be sufficient
             │
             └── Yes
                    │
                    ▼
          Apply Cause-Effect Graphing
```

---

## Typical Scenarios

Cause-Effect Graphing is particularly suitable for:

- Eligibility rules
- Validation logic
- Pricing calculations
- Discount policies
- Authorization rules
- Regulatory compliance
- Financial calculations
- Medical decision support
- Rule engine validation

---

# QA Review Checklist

Before completing Cause-Effect Graphing, verify the following.

## Requirement Analysis

- □ Have all causes been identified?
- □ Have all observable effects been identified?
- □ Are logical operators explicitly defined?
- □ Have assumptions been validated?

---

## Graph Review

- □ Does every cause contribute to at least one effect?
- □ Are Boolean relationships modeled correctly?
- □ Are nested expressions represented accurately?
- □ Have constraints been documented?

---

## Decision Table Review

- □ Has the graph been converted into a Decision Table?
- □ Are impossible combinations excluded?
- □ Are redundant rules eliminated?
- □ Are all meaningful logical paths represented?

---

## Test Case Review

- □ Is every decision rule covered by at least one test case?
- □ Are expected effects measurable?
- □ Is traceability maintained from requirement → graph → decision table → test case?

---

# Common Mistakes

## Confusing Causes with Effects

Incorrect:

```
Approve Loan
```

as a cause.

Correct:

```
Credit Score Pass
```

Cause = input condition.

Effect = observable system behavior.

---

## Ignoring Boolean Precedence

Example:

```
A AND B OR C
```

may be interpreted differently from:

```
A AND

(B OR C)
```

Operator precedence should always be clarified before constructing the graph.

---

## Modeling Implementation Instead of Requirements

The graph should represent business logic—not implementation details.

Focus on observable behavior rather than internal algorithms.

---

## Skipping the Decision Table

The graph itself is rarely sufficient for systematic test design.

Converting the graph into a Decision Table provides a clearer basis for deriving executable test cases.

---

# Frequently Asked Questions

## Is Cause-Effect Graphing the same as Decision Table Testing?

No.

Cause-Effect Graphing models logical relationships.

Decision Table Testing represents business rule combinations.

In many workflows, the graph is constructed first and then converted into a decision table.

---

## Should every graph become a Decision Table?

Generally, yes.

Decision Tables provide a more structured representation for test case generation.

---

## Can Cause-Effect Graphing handle nested logic?

Yes.

Nested Boolean expressions are one of the primary reasons for using this technique.

---

## Is Cause-Effect Graphing useful for APIs?

Yes.

It is particularly effective for APIs containing complex validation logic or multiple interacting request parameters.

---

# AI Perspective

AI can assist in identifying candidate causes, effects, and logical operators from structured requirements.

It may also generate an initial Cause-Effect Graph and propose corresponding Decision Tables.

However, AI cannot reliably infer undocumented business assumptions or implicit logical precedence.

Human review remains essential to confirm that the graph accurately reflects business intent.

Within the QA-AI framework, Cause-Effect Graphing supports Requirement Analyzer, Business Rule Extractor, Scenario Generator, and Test Case Generator by providing an intermediate logical model between requirements and executable tests.

---

# Summary

Cause-Effect Graphing is a Specification-Based Testing technique that models the logical relationships between input conditions and system behavior.

By explicitly representing causes, effects, Boolean operators, and constraints, testers can analyze complex requirements, detect logical defects, and systematically generate Decision Tables and test cases.

The technique is particularly valuable for systems where correctness depends on logical relationships rather than simple input validation or workflow progression.

---

# Related Knowledge

## Prerequisites

- Black-Box Testing

## Related Techniques

- Decision Table Testing
- State Transition Testing
- Equivalence Partitioning
- Boundary Value Analysis
- Use Case Testing

## Advanced Topics

- Boolean Algebra
- Rule Engine Testing
- Model-Based Testing
- Formal Specification Techniques

---

# References

## Standards

- ISTQB® Certified Tester Foundation Level (CTFL) Syllabus
- ISO/IEC/IEEE 29119 Software Testing

## Books

- Foundations of Software Testing — Dorothy Graham, Erik van Veenendaal, Rex Black
- Software Testing: Principles and Practices — Srinivasan Desikan, Gopalaswamy Ramesh

## Further Reading

- Lessons Learned in Software Testing — Cem Kaner, James Bach, Bret Pettichord
- Introduction to Boolean Algebra and Logic Design