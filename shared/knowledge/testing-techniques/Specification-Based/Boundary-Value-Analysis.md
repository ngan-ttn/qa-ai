# Boundary Value Analysis

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Boundary Value Analysis (BVA)** focuses testing around the edges of ordered input or output domains because defects frequently occur where behavior changes from one class to another.

## Purpose

Systematically test minimums, maximums, transition points, and adjacent values that are more defect-prone than arbitrary interior values.

## Core Concepts

### Boundary
A point where expected behavior changes, such as a minimum, maximum, threshold, date cut-off, size limit, or capacity limit.

### On-Point and Off-Point Values
Tests commonly include the boundary itself and values immediately below or above it when the data type permits.

### Inclusive vs Exclusive Limits
`>= 18` and `> 18` have different boundary expectations. Requirement wording must be precise.

### Discrete vs Continuous Domains
The nearest adjacent value depends on granularity: integer, currency precision, timestamp resolution, string length, or business unit.

### Multiple Boundaries
A range can contain lower and upper boundaries; state or tier rules can contain many internal thresholds.

## How It Works

```text
Identify ordered domain
      ↓
Locate points where behavior changes
      ↓
Confirm inclusivity and granularity
      ↓
Select on-boundary and adjacent values
      ↓
Verify expected outcome at each transition
```

BVA complements, rather than replaces, Equivalence Partitioning.

## When to Use

Use for numeric ranges, lengths, dates, times, quantities, pagination limits, file sizes, thresholds, capacities, retry counts, or tier boundaries.

## When Not to Use

Do not force BVA onto unordered categories or rules whose risk is driven mainly by combinations, sequence, or state transitions.

## Advantages

- High defect-detection value with few tests.
- Makes inclusive/exclusive ambiguity visible.
- Works well with range-oriented business rules.
- Helps expose off-by-one and precision defects.

## Limitations

- Requires a meaningful ordered domain.
- Adjacent values may be unclear for continuous or business-defined units.
- Does not cover representative interior behavior or multi-condition logic by itself.

## Examples

### Quantity 1–100 Inclusive
Test `0`, `1`, `2`, `99`, `100`, `101` when integer granularity is correct for the rule.

### Password Length 8–64
Test lengths around 8 and 64, while separately covering character rules through other techniques.

### Date Eligibility
If an action is allowed through the end of a defined date, verify the final valid instant and the first invalid instant using the system's timezone and precision rules.

## Best Practices

- Confirm inclusivity explicitly.
- Use the business-relevant data granularity.
- Test both lower and upper boundaries.
- Include internal thresholds where behavior changes.
- Separate display rounding from authoritative precision.
- Combine with EP for representative partitions.
- Avoid inventing thresholds not present in requirements.

## Related Knowledge

- `Equivalence-Partitioning.md`
- `Decision-Table-Testing.md`
- `../Foundation/Black-Box-Testing.md`
- `../../domain/Calculation-Rules.md`

## References

- ISTQB Boundary Value Analysis guidance.
- Approved business rules defining ranges and thresholds.