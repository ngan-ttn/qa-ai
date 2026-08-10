# Condition Coverage

> Version: 1.0.0
> Status: Draft
> Last Updated: YYYY-MM-DD

---

# Overview

Condition Coverage is a Structure-Based Test Design Technique that measures whether every individual condition within a decision has been evaluated to both **True** and **False** during testing.

Unlike Statement Coverage, Branch Coverage, and Decision Coverage, which evaluate code execution or overall decision outcomes, Condition Coverage examines each condition independently.

The technique answers one fundamental question:

> **Has every individual condition been evaluated to both True and False at least once?**

Condition Coverage is particularly valuable when decisions contain compound Boolean expressions, where multiple conditions work together to determine the program's behavior.

Although a decision may evaluate to both True and False, some individual conditions may never change their values during testing.

Condition Coverage addresses this limitation by ensuring that every condition is exercised independently.

---

# Purpose

The primary purpose of Condition Coverage is to verify that every individual condition within each decision has been evaluated to both True and False.

Its objectives include:

- Measure individual condition evaluation.
- Detect untested conditions.
- Improve logical verification.
- Strengthen confidence in compound decisions.
- Prepare for advanced techniques such as MC/DC.

---

# Learning Objectives

After completing this article, readers should be able to:

- Explain why Condition Coverage exists.
- Identify individual conditions within compound decisions.
- Calculate Condition Coverage.
- Distinguish Decision Coverage from Condition Coverage.
- Interpret Condition Coverage reports.
- Understand the relationship between Condition Coverage and MC/DC.

---

# Knowledge Map

```
White-Box Testing
        │
        ▼
Decision Coverage
        │
        ▼
Condition Coverage
        │
        ▼
Modified Condition/
Decision Coverage
```

Condition Coverage extends Decision Coverage by focusing on the evaluation of each individual condition rather than only the overall decision outcome.

---

# Why Condition Coverage Exists

Consider the following code.

```java
if(A && B){

    process();

}
```

Suppose only the following test cases are executed.

| A | B | Decision |
|---|---|----------|
| T | T | True |
| F | F | False |

Decision Coverage:

```
100%
```

because both decision outcomes have occurred.

However, imagine another set of tests.

| A | B | Decision |
|---|---|----------|
| T | T | True |
| T | F | False |

Again:

```
Decision=True

Decision=False
```

Decision Coverage is still:

```
100%
```

But:

```
A

never becomes False.
```

One individual condition has never been fully evaluated.

Condition Coverage exists to detect this situation.

---

# History and Background

As software systems evolved, developers recognized that evaluating only the overall outcome of a decision was insufficient for validating complex Boolean expressions.

A decision may produce both True and False outcomes while some individual conditions remain only partially exercised.

Condition Coverage was introduced to ensure that every condition within a decision contributes to testing by being evaluated to both True and False.

This concept later became the foundation for more advanced coverage techniques such as Modified Condition/Decision Coverage (MC/DC), which additionally verifies the independent effect of each condition.

---

# Core Concepts

## Condition

A condition is an individual Boolean expression within a decision.

Example:

```java
if(age >=18 && member){
```

Conditions:

```
C1

age >=18
```

```
C2

member
```

Each condition can independently evaluate to:

- True
- False

---

## Compound Decision

A compound decision contains two or more individual conditions.

Examples:

```java
A && B
```

```java
A || B
```

```java
(A && B) || C
```

Compound decisions require stronger testing than simple decisions.

---

## Condition Evaluation

Condition evaluation refers to the Boolean result of an individual condition.

Example:

```java
age >=18
```

Possible evaluations:

```
True
```

```
False
```

Each evaluation should occur during testing.

---

## Condition Coverage

Condition Coverage measures whether every individual condition has evaluated to both True and False.

Coverage answers:

> **Has every individual condition been evaluated under both possible Boolean values?**

---

## Coverage Percentage

Condition Coverage is calculated as:

```
Executed Condition Outcomes
-----------------------------------
Total Condition Outcomes

×

100%
```

Example:

Two conditions:

```
A

B
```

Possible evaluations:

```
A=True

A=False

B=True

B=False
```

Executed:

```
3
```

Total:

```
4
```

Coverage:

```
75%
```

---

# Decision Coverage vs Condition Coverage

Decision Coverage verifies:

```
Decision=True

Decision=False
```

Condition Coverage verifies:

```
A=True

A=False

B=True

B=False
```

Decision Coverage measures the outcome of the entire decision.

Condition Coverage measures the evaluation of every individual condition within that decision.

---

# Testing Philosophy

Condition Coverage is based on one central principle.

> **Every individual condition should be evaluated to both True and False, regardless of the overall decision outcome.**

By verifying every condition independently, testers gain stronger confidence that compound logical expressions have been exercised more thoroughly than with Decision Coverage alone.
# How Condition Coverage Works

Condition Coverage measures whether every individual condition within a decision has been evaluated to both **True** and **False** during testing.

Instead of focusing on the final outcome of a decision, the technique analyzes each Boolean condition separately.

The overall workflow is shown below.

```
Source Code
      │
      ▼
Identify Decisions
      │
      ▼
Identify Individual Conditions
      │
      ▼
Execute Test Cases
      │
      ▼
Record Condition Evaluations
      │
      ▼
Calculate Coverage
      │
      ▼
Analyze Missing Evaluations
      │
      ▼
Improve Test Suite
```

---

# Step 1 — Identify Decisions

Begin by identifying every decision in the source code.

Example:

```java
if(age >=18 && member){

    approve();

}
```

The `if` statement represents one decision.

---

# Step 2 — Identify Individual Conditions

Break the decision into its individual Boolean conditions.

Example:

```java
if(age >=18 && member){
```

Conditions:

| ID | Condition |
|----|-----------|
| C1 | age >=18 |
| C2 | member |

Each condition must be evaluated independently.

---

# Step 3 — Execute Test Cases

Execute test cases that produce different evaluations for each condition.

Example:

| Test | age | member |
|------|-----|---------|
| T1 | 20 | true |
| T2 | 16 | true |
| T3 | 20 | false |

Condition evaluations:

| Condition | True | False |
|-----------|------|-------|
| age >=18 | ✓ | ✓ |
| member | ✓ | ✓ |

Coverage:

```
100%
```

---

# Step 4 — Record Condition Evaluations

Coverage tools record the evaluation history of every condition.

Example report:

| Condition | True | False |
|-----------|------|-------|
| age >=18 | ✓ | ✓ |
| member | ✓ | ✗ |

This report immediately shows that one condition has not yet evaluated to **False**.

---

# Step 5 — Calculate Condition Coverage

Condition Coverage is calculated using the following formula.

```
Executed Condition Outcomes
-----------------------------------
Total Condition Outcomes

×

100%
```

Example:

Two conditions:

```
A

B
```

Possible evaluations:

```
A=True

A=False

B=True

B=False
```

Executed:

```
3
```

Total:

```
4
```

Coverage:

```
75%
```

Each True and False evaluation contributes equally.

---

# Step 6 — Analyze Missing Evaluations

Coverage reports identify conditions that have not yet been evaluated under both Boolean values.

Possible causes include:

- Missing test cases
- Constant conditions
- Defensive programming
- Incomplete business scenarios

Every missing evaluation should be reviewed before finalizing the test suite.

---

# Step 7 — Improve the Test Suite

Design additional test cases to exercise uncovered condition evaluations.

Example:

Current tests:

| age | member |
|-----|---------|
| 20 | true |
| 16 | true |

Missing:

```
member = false
```

Additional test:

| age | member |
|-----|---------|
| 20 | false |

Coverage becomes complete.

---

# Coverage Example 1 — AND Expression

```java
if(A && B){

    process();

}
```

Test cases:

| Test | A | B |
|------|---|---|
| T1 | T | T |
| T2 | F | T |
| T3 | T | F |

Condition evaluations:

| Condition | True | False |
|-----------|------|-------|
| A | ✓ | ✓ |
| B | ✓ | ✓ |

Coverage:

```
100%
```

---

# Coverage Example 2 — OR Expression

```java
if(A || B){

    process();

}
```

Test cases:

| Test | A | B |
|------|---|---|
| T1 | T | F |
| T2 | F | T |
| T3 | F | F |

Condition evaluations:

| Condition | True | False |
|-----------|------|-------|
| A | ✓ | ✓ |
| B | ✓ | ✓ |

Coverage:

```
100%
```

---

# Coverage Example 3 — Nested Expression

```java
if((A && B) || C){

    process();

}
```

Individual conditions:

- A
- B
- C

Coverage analysis focuses on each condition independently.

The complexity of the overall decision does not change the evaluation objective.

---

# Coverage Example 4 — Enterprise Authorization

```java
if(userActive && hasPermission){

    access();

}
```

Conditions:

- userActive
- hasPermission

Testing should verify:

| Condition | True | False |
|-----------|------|-------|
| userActive | ✓ | ✓ |
| hasPermission | ✓ | ✓ |

---

# Coverage Example 5 — Loan Approval

```java
if(identityVerified && creditApproved){

    approveLoan();

}
```

Both conditions should independently evaluate to:

- True
- False

This ensures that each prerequisite has been exercised.

---

# Coverage Reports

Modern coverage tools provide condition-level information such as:

- Individual conditions
- True evaluations
- False evaluations
- Missing evaluations
- Source code locations

Some tools combine Condition Coverage with Decision Coverage in a single report.

Others require specialized plugins or safety-critical toolchains.

---

# Coverage Interpretation

Higher Condition Coverage indicates that more individual conditions have been exercised under both Boolean values.

However:

```
100% Condition Coverage

≠

100% Decision Coverage

≠

100% MC/DC

≠

100% Software Quality
```

Condition Coverage verifies individual evaluations.

It does not prove that:

- Each condition independently affects the decision.
- Every execution path has been tested.
- Every business rule has been verified.
- Every assertion is correct.

---

# Comparing Decision Coverage and Condition Coverage

| Characteristic | Decision Coverage | Condition Coverage |
|----------------|-------------------|--------------------|
| Focus | Decision outcomes | Individual conditions |
| Unit of measurement | Decision | Condition |
| Requires True and False decision outcomes | Yes | No |
| Requires each condition to evaluate True and False | No | Yes |
| Prepares for MC/DC | Limited | Strong |

Condition Coverage provides deeper insight into compound Boolean expressions than Decision Coverage.

---

# Visualizing Condition Coverage

```
Decision
      │
      ▼
Identify Conditions
      │
      ▼
Condition A
 │         │
 T         F

Condition B
 │         │
 T         F
      │
      ▼
Coverage Report
      │
      ▼
Additional Test Cases
```

Condition Coverage strengthens logical testing by ensuring that every individual condition within a decision has been evaluated under both possible Boolean values.
# Advantages

Condition Coverage provides a deeper level of logical verification than Decision Coverage by ensuring that every individual condition within a compound decision has been evaluated to both **True** and **False**.

It is particularly valuable when software contains complex Boolean expressions that combine multiple conditions.

---

## Verifies Every Individual Condition

Decision Coverage verifies the overall outcome of a decision.

Condition Coverage verifies every Boolean condition separately.

Example:

```java
if(age >=18 && member){

    approve();

}
```

Both conditions:

- `age >=18`
- `member`

must independently evaluate to:

- True
- False

This provides greater confidence that every condition has been exercised.

---

## Improves Testing of Compound Decisions

Enterprise applications often contain decisions such as:

```java
if(userActive && hasPermission && accountVerified){

    access();

}
```

Testing only the final decision outcome may leave individual conditions only partially exercised.

Condition Coverage reduces this risk.

---

## Detects Missing Condition Evaluations

Coverage reports clearly indicate when a condition has never evaluated to one of its Boolean values.

Example:

| Condition | True | False |
|-----------|------|-------|
| userActive | ✓ | ✓ |
| hasPermission | ✓ | ✗ |
| accountVerified | ✓ | ✓ |

The report immediately identifies that `hasPermission` has never evaluated to **False**.

---

## Provides a Foundation for MC/DC

Condition Coverage introduces the concept of evaluating individual conditions.

MC/DC extends this concept further by verifying that each condition can independently influence the overall decision outcome.

For this reason, Condition Coverage is an essential prerequisite for understanding MC/DC.

---

## Strengthens Logical Verification

By exercising every condition under both Boolean values, testers gain stronger confidence that compound decision logic has been explored more thoroughly than with Decision Coverage alone.

---

# Limitations

Although Condition Coverage improves logical verification, it still has important limitations.

---

## Does Not Prove Independent Influence

Consider:

```java
if(A && B){

    process();

}
```

Condition Coverage verifies:

- A = True
- A = False
- B = True
- B = False

However, it does **not** prove that changing **A** alone changes the decision outcome.

MC/DC addresses this limitation.

---

## Does Not Guarantee Decision Coverage

It is possible to achieve high Condition Coverage while some overall decision outcomes remain untested.

Both metrics should therefore be considered together.

---

## Does Not Guarantee Path Coverage

Complex software often contains many execution paths.

Condition Coverage verifies individual condition evaluations—not complete execution paths.

---

## Executing Conditions Does Not Verify Correctness

Condition evaluations only confirm that values occurred.

They do not verify:

- Correct calculations
- Correct business behavior
- Correct assertions
- Correct side effects

Coverage remains an execution metric.

---

# Decision Guide

Use the following guide when selecting Condition Coverage.

```
Requirement
      │
      ▼
Does the decision contain multiple conditions?
      │
      ├── No
      │      │
      │      ▼
      │  Decision Coverage may be sufficient
      │
      └── Yes
             │
             ▼
Do you need to verify every condition individually?
             │
             ├── No
             │      │
             │      ▼
             │  Decision Coverage may be acceptable
             │
             └── Yes
                    │
                    ▼
             Apply Condition Coverage
```

---

## Typical Scenarios

Condition Coverage is particularly suitable for:

- Business Rule Validation
- Authorization Logic
- Security Checks
- Financial Validation
- Eligibility Rules
- API Validation Logic
- Unit Testing
- Service Layer Testing

---

# QA Review Checklist

Before accepting Condition Coverage results, verify the following.

## Condition Identification

- □ Have all individual conditions been identified?
- □ Are compound Boolean expressions decomposed correctly?
- □ Are nested conditions included?

---

## Coverage Review

- □ Has every condition evaluated to both True and False?
- □ Are missing evaluations understood?
- □ Are constant conditions investigated?
- □ Are unreachable conditions documented?

---

## Test Suite Review

- □ Does the test suite exercise each condition independently?
- □ Are positive and negative scenarios included?
- □ Do assertions verify the observed behavior?

---

## Reporting Review

- □ Has the Condition Coverage report been reviewed?
- □ Are project coverage goals achieved?
- □ Are coverage trends monitored?

---

# Common Mistakes

## Confusing Conditions with Decisions

A decision may contain multiple conditions.

Example:

```java
if(A && B){
```

Decision:

```
A && B
```

Conditions:

```
A

B
```

Coverage should be measured at the correct level.

---

## Assuming Condition Coverage Equals MC/DC

Condition Coverage verifies:

```
A=True

A=False
```

MC/DC additionally verifies that changing **A alone** changes the final decision.

These techniques have different objectives.

---

## Ignoring Compound Expressions

Complex Boolean expressions should always be decomposed into individual conditions before coverage analysis.

---

## Treating Coverage as a Quality Goal

High Condition Coverage improves confidence.

It does not replace:

- Functional testing
- Business validation
- Code review
- Meaningful assertions

---

# Frequently Asked Questions

## Is Condition Coverage stronger than Decision Coverage?

Yes.

Condition Coverage verifies every individual condition rather than only the overall decision outcome.

---

## Is 100% Condition Coverage sufficient?

No.

It does not guarantee:

- Independent condition influence
- Complete path coverage
- Correct implementation
- Complete business verification

---

## Does Condition Coverage replace MC/DC?

No.

MC/DC builds upon Condition Coverage by proving that each condition independently affects the decision.

---

## Should every project use Condition Coverage?

Not necessarily.

Projects with simple decision logic may obtain sufficient confidence using Decision Coverage.

Systems containing complex Boolean expressions benefit significantly from Condition Coverage.

---

# AI Perspective

AI can assist in decomposing compound Boolean expressions into individual conditions, estimating Condition Coverage, identifying missing evaluations, and generating additional test inputs.

AI may also recommend test cases to improve coverage reports.

However, AI cannot determine whether each condition independently affects the final decision without applying MC/DC analysis.

Within the QA-AI framework, Condition Coverage provides the conceptual bridge between Decision Coverage and Modified Condition/Decision Coverage (MC/DC).

---

# Summary

Condition Coverage is a Structure-Based Testing technique that measures whether every individual condition within a decision has been evaluated to both **True** and **False**.

Compared with Decision Coverage, it provides stronger confidence in compound Boolean expressions by focusing on individual conditions rather than only the final decision outcome.

Although valuable, Condition Coverage should be combined with functional testing and, where appropriate, MC/DC to achieve more comprehensive logical verification.

---

# Related Knowledge

## Prerequisites

- White-Box Testing
- Statement Coverage
- Branch Coverage
- Decision Coverage

## Related Techniques

- Modified Condition/Decision Coverage (MC/DC)
- Path Coverage

## Advanced Topics

- Boolean Algebra
- Safety-Critical Software Testing
- Code Coverage Analysis
- Mutation Testing

---

# References

## Standards

- ISTQB® Certified Tester Foundation Level (CTFL) Syllabus
- ISO/IEC/IEEE 29119 Software Testing

## Books

- Foundations of Software Testing — Dorothy Graham, Erik van Veenendaal, Rex Black
- Software Testing: Principles and Practices — Srinivasan Desikan, Gopalaswamy Ramesh

## Further Reading

- Code Complete — Steve McConnell
- Clean Code — Robert C. Martin