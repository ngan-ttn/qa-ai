# Pairwise Testing

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Pairwise Testing** selects test combinations so that every relevant pair of parameter values appears together in at least one test. It is a practical form of combinatorial interaction testing used to reduce large configuration or input spaces.

## Purpose

Achieve broad interaction coverage with fewer tests when exhaustive combination testing is too expensive and two-way interactions are a reasonable risk model.

## Core Concepts

### Parameter
A configurable dimension such as browser, role, payment type, locale, device, or feature flag.

### Value
One possible setting for a parameter.

### Pairwise Interaction
A specific pair of values from two different parameters.

### Covering Array
A generated set of rows that covers required value interactions according to the chosen strength.

### Constraints
Invalid, impossible, or forbidden combinations must be modeled explicitly so generated tests remain executable and meaningful.

## How It Works

```text
List parameters and values
      ↓
Remove or model invalid combinations
      ↓
Generate pairwise covering set
      ↓
Review business-critical combinations
      ↓
Execute and supplement with risk-specific cases
```

Pairwise generation optimizes coverage of pairs; it does not automatically cover higher-order or business-critical combinations.

## When to Use

Use for configuration matrices, browser/device coverage, permissions, feature flags, integration options, product variants, or forms with many mostly independent parameters.

## When Not to Use

Do not use pairwise as the sole technique when defects are known to depend on three-way or higher interactions, sequences, boundaries, or exact business-rule combinations.

## Advantages

- Reduces combinatorial explosion.
- Provides systematic interaction coverage.
- Often yields much smaller suites than exhaustive testing.
- Works well with automated generation tools.

## Limitations

- Two-way coverage may miss higher-order defects.
- Poor constraint modeling can generate invalid tests.
- Critical combinations can be omitted despite pairwise completeness.
- Parameter/value modeling quality strongly affects results.

## Examples

A web matrix contains browser × OS × role × locale. Pairwise generation can cover every two-factor value interaction with far fewer cases than the full Cartesian product.

A checkout configuration with payment type, currency, customer tier, and shipping mode may use pairwise tests plus explicitly added high-risk combinations from business rules.

## Best Practices

- Define parameters at comparable abstraction levels.
- Model impossible combinations explicitly.
- Add mandatory business-critical scenarios manually.
- Validate generated suites for realistic data dependencies.
- Use higher interaction strength when evidence justifies it.
- Do not confuse pairwise coverage with requirement coverage.

## Related Knowledge

- `Combinatorial-Testing.md`
- `Orthogonal-Array-Testing.md`
- `../Specification-Based/Equivalence-Partitioning.md`
- `../Specification-Based/Decision-Table-Testing.md`

## References

- Combinatorial interaction testing literature.
- NIST combinatorial testing research and covering-array concepts.