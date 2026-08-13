# Decision Rules

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Decision rules** map combinations of business conditions to outcomes, actions, classifications, or routes.

## Purpose

Help QA make complex conditional logic explicit and test combinations systematically.

## Core Concepts

### Condition
A fact evaluated by the rule.
### Outcome
The result selected.
### Precedence
Which rule wins when multiple rules match.
### Completeness
All relevant input combinations have defined behavior.
### Exclusivity
Whether multiple outcomes can apply simultaneously.

## How It Works

Facts are evaluated against ordered or structured conditions; matching rules produce defined outcomes.

## When to Use

Use for approvals, routing, pricing categories, eligibility, fraud treatment, and status decisions.

## When Not to Use

Do not simplify continuous calculations or lifecycle behavior into decision tables when another model is clearer.

## Advantages

Makes gaps, overlaps, and contradictory conditions visible.

## Limitations

Large condition sets can create combinatorial explosion.

## Examples

Approval may depend on role, amount band, risk status, and document completeness; a decision table can expose undefined combinations.

## Best Practices

- Define condition domains.
- Check completeness and overlap.
- Clarify precedence.
- Use pairwise/risk-based reduction only after preserving critical combinations.
- Trace outcomes to rules.

## Related Knowledge

- `Eligibility-Rules.md`
- `Rule-Exceptions.md`
- `../testing-techniques/Specification-Based/Decision-Table-Testing.md`

## References

- Decision modeling and business-rule literature.