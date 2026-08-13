# Cause-Effect Graphing

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Cause-Effect Graphing** models logical relationships between input conditions (causes) and observable outcomes (effects). The graph helps expose dependencies, combinations, constraints, and logical relationships before tests are derived, often through a decision table.

## Purpose

Provide a structured technique for reasoning about complex boolean or rule interactions that are difficult to understand from prose alone.

## Core Concepts

### Cause
An input condition, event, state fact, or predicate.

### Effect
An expected output, decision, action, or state consequence.

### Logical Relationship
AND, OR, NOT, or equivalent business logic connecting causes to effects.

### Constraint
Rules that make combinations impossible, mutually exclusive, required, or dependent.

### Graph-to-Test Transformation
The graph is commonly converted into a decision table or a reduced set of logical test conditions.

## How It Works

```text
Requirement prose
     ↓
Extract causes and effects
     ↓
Connect logical relationships
     ↓
Add constraints / impossible combinations
     ↓
Review completeness and contradictions
     ↓
Convert to decision table / tests
```

The value of the graph is in making logic explicit before test selection.

## When to Use

Use for complex validation, eligibility, permissions, routing, business decisions, or rules containing nested logical expressions and dependent conditions.

## When Not to Use

Do not use it when a simple partition, boundary, or state model expresses the behavior more clearly. Avoid unnecessary graph complexity for straightforward rules.

## Advantages

- Visualizes logical dependency.
- Helps detect missing causes or effects.
- Identifies impossible combinations.
- Supports systematic conversion into decision coverage.

## Limitations

- Large graphs become difficult to maintain.
- Incorrect logical interpretation propagates into tests.
- Temporal and state-history behavior is not naturally represented.
- Specialized notation can reduce accessibility for stakeholders.

## Examples

A promotion applies when the campaign is active AND the customer is eligible AND either the amount threshold or an approved exception is satisfied. A cause-effect graph makes this grouping explicit before generating decision-table columns.

An upload is accepted only if format is valid, mandatory headers exist, and file size is within limit; virus detection or permission failure can independently force rejection.

## Best Practices

- Use atomic causes and observable effects.
- Capture mutually exclusive and impossible combinations.
- Confirm operator precedence explicitly.
- Keep business terminology from source requirements.
- Convert the graph into reviewable test conditions.
- Prefer a decision table when it communicates the same logic more simply.

## Related Knowledge

- `Decision-Table-Testing.md`
- `Equivalence-Partitioning.md`
- `State-Transition-Testing.md`
- `../../domain/Decision-Rules.md`

## References

- Classical cause-effect graphing literature.
- ISTQB specification-based technique references.