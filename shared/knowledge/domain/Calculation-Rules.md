# Calculation Rules

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

A **calculation rule** defines how one or more business values are derived from inputs, formulas, rates, units, rounding, thresholds, and timing semantics.

## Purpose

Help QA validate calculations precisely without inventing formulas, rounding rules, or effective rates that are not documented.

## Core Concepts

### Input Population
Which records or values participate in the calculation.

### Formula
The mathematical or logical derivation that produces the result.

### Unit / Currency
Inputs and outputs must use defined units and conversions.

### Precision
Stored and computed decimal precision can differ from display precision.

### Rounding
Rounding method, scale, and point in the calculation sequence affect results.

### Threshold / Cap / Floor
Rules may impose minimum, maximum, or band boundaries.

### Effective Rate
Rates can vary by date, segment, product, tier, or promotion.

### Aggregation Order
`round(each item) then sum` can differ from `sum then round`.

### Null / Missing Input
Rules must define how absent or invalid inputs are treated.

## How It Works

```text
Qualified inputs
   ↓
Normalize unit / precision
   ↓
Apply formula + rate + thresholds
   ↓
Rounding / cap / floor
   ↓
Final value + explanation/evidence
```

QA should independently reproduce expected results using the approved formula and test the exact boundaries where rates or outcomes change.

## When to Use

Use for prices, discounts, tax, loyalty points, balances, fees, commissions, quantities, scores, and derived reporting metrics.

## When Not to Use

Do not infer financial or regulatory calculation rules from generic industry practice. Do not compare display-rounded values to raw stored precision without understanding the contract.

## Advantages

Structured calculation testing catches precision, boundary, rate, order-of-operation, and stale-configuration defects.

## Limitations

Calculations can depend on external rates, effective dates, historical snapshots, and large data sets. Small rounding differences can accumulate materially.

## Examples

### Tier Boundary
A benefit rate changes at exactly 1,000 units. QA tests 999, 1,000, and 1,001 using the approved inclusive/exclusive rule.

### Rounding Sequence
Three line-item amounts are rounded individually before order total. QA confirms whether this differs from rounding only the final sum.

### Effective Rate
A promotion rate changes at midnight in a defined timezone. QA verifies which timestamp controls eligibility.

## Best Practices

- Obtain formula, units, precision, rounding method, and effective period explicitly.
- Recalculate independently from source inputs.
- Test zero, negative, min/max, and just-around thresholds.
- Verify order of operations.
- Include currency/unit conversion when applicable.
- Check configuration/version used by historical calculations.
- Reconcile aggregate calculations to detail.
- Record expected values with enough precision to explain differences.

## Related Knowledge

- `Business-Rule-Fundamentals.md`
- `Decision-Rules.md`
- `Eligibility-Rules.md`
- `Transaction-Data.md`
- `../database/Aggregation.md`

## References

- Approved calculation specifications and financial/business policy.
- Numerical-computing and accounting guidance applicable to the project.
