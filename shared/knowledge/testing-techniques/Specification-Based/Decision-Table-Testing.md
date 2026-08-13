# Decision Table Testing

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Decision Table Testing** models combinations of conditions and the actions or outcomes that should result. It is particularly effective when business behavior depends on several independent or interacting rules.

## Purpose

Expose missing, contradictory, unreachable, or incorrectly implemented condition combinations while creating traceable tests for complex business logic.

## Core Concepts

### Conditions
Facts or predicates that influence the decision.

### Actions / Outcomes
Expected result when a rule column matches.

### Rule Column
One unique combination of condition values and corresponding actions.

### Don't-Care Value
A condition that does not affect a particular rule and can be marked as irrelevant only when that irrelevance is justified.

### Completeness and Consistency
A strong table covers relevant combinations and avoids conflicting outcomes for the same combination unless precedence is explicitly defined.

## How It Works

```text
Business rules
     ↓
List decision conditions
     ↓
List possible condition values
     ↓
Enumerate / reduce meaningful combinations
     ↓
Map each combination to expected action
     ↓
Review gaps, conflicts, precedence
     ↓
Derive tests from rule columns
```

Large tables may be simplified using don't-care conditions, rule equivalence, or combinatorial reasoning without losing business-significant combinations.

## When to Use

Use for eligibility, approvals, pricing, discounts, permissions, routing, validation, fraud/risk outcomes, feature availability, or any logic driven by multiple conditions.

## When Not to Use

Do not use a decision table as the primary technique for long sequential workflows, lifecycle transitions, continuous numeric boundaries, or exploratory objectives.

## Advantages

- Makes condition interactions explicit.
- Exposes missing and contradictory rules.
- Supports traceable business-rule coverage.
- Converts complex prose into reviewable logic.

## Limitations

- Combination counts grow quickly.
- Incorrect condition decomposition produces misleading tables.
- Temporal order and state history may require State Transition Testing.
- Rule precedence must come from authoritative sources.

## Examples

### Refund Eligibility
Conditions: transaction state, elapsed period, payment type, and exception approval. Each relevant combination maps to `Allow`, `Reject`, or `Manual Review`.

### Feature Permission
Conditions: authenticated, role authorized, object ownership, and record state. The table helps verify that authorization is not reduced to role alone.

### Discount Logic
Conditions for customer tier, promotion active, and minimum amount reveal whether discounts stack, conflict, or require precedence clarification.

## Best Practices

- Keep conditions atomic and unambiguous.
- Confirm rule precedence and defaults.
- Include negative and no-match outcomes.
- Review impossible combinations instead of silently deleting them.
- Trace every rule column to source requirements.
- Use BVA inside condition values where thresholds apply.
- Revisit the table when any dependent rule changes.

## Related Knowledge

- `Cause-Effect-Graphing.md`
- `State-Transition-Testing.md`
- `Equivalence-Partitioning.md`
- `../../domain/Decision-Rules.md`
- `../../domain/Rule-Exceptions.md`

## References

- ISTQB Decision Table Testing guidance.
- Business-rule and decision-modeling literature.