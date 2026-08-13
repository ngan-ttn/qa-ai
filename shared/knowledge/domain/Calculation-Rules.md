# Calculation Rules

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Calculation rules** define how business values are derived from inputs, formulas, rates, rounding, sequence, dates, and conditional logic.

## Purpose

Provide QA a model for validating derived amounts and quantities independently and reproducibly.

## Core Concepts

### Inputs
Authoritative values used by the formula.
### Formula
Defined mathematical or logical transformation.
### Precision and Rounding
Scale, rounding mode, and rounding stage affect results.
### Ordering
Applying discount, tax, fee, or conversion in different sequence can change output.
### Effective Rate
Rates can vary by date, product, tier, or context.

## How It Works

QA reconstructs the expected result from authoritative inputs and rules, then compares system output including intermediate values where observable.

## When to Use

Use for prices, tax, points, balances, fees, quantities, commissions, and thresholds.

## When Not to Use

Do not invent rounding modes, currency precision, or rate precedence.

## Advantages

Independent calculation detects subtle business defects.

## Limitations

Hidden intermediate precision and external rate sources can complicate reproduction.

## Examples

A 10% discount followed by tax may differ from tax followed by discount depending on policy; QA must use the specified sequence.

## Best Practices

- Identify authoritative inputs.
- Test zero, negative, min/max, fractional, and boundary values where valid.
- Confirm rounding stage and mode.
- Test effective-date changes.
- Reconcile totals to component values.

## Related Knowledge

- `Business-Rule-Fundamentals.md`
- `Decision-Rules.md`
- `Eligibility-Rules.md`

## References

- Approved calculation specifications and business-rule literature.