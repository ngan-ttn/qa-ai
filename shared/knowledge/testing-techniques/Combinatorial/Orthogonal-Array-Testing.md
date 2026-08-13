# Orthogonal Array Testing

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Orthogonal Array Testing (OAT)** uses mathematically structured arrays to select balanced combinations of factor levels. Orthogonal arrays aim to distribute level combinations systematically and can support efficient experimentation or software configuration testing under suitable factor structures.

## Purpose

Provide a disciplined combination-reduction method when available orthogonal-array structures fit the problem and balanced interaction representation is valuable.

## Core Concepts

### Factor
A parameter or variable under study.

### Level
A possible value of a factor.

### Orthogonal Array
A matrix with mathematical balance properties such that selected level combinations occur uniformly for the covered interaction strength.

### Strength
The number of factors whose combinations receive the defined balance property.

### Fit
Real software factors often have unequal numbers of values or constraints, so a textbook orthogonal array may not map naturally to the system.

## How It Works

QA identifies factors and levels, selects an appropriate orthogonal array, maps software values to array symbols, validates constraints and feasibility, then supplements the array with business-critical cases not guaranteed by the design.

## When to Use

Use for controlled configuration experiments, parameter sets that match known array structures, or environments where balanced factor representation matters.

## When Not to Use

Do not force orthogonal arrays onto irregular value counts, heavy constraints, stateful flows, or business logic better modeled with decision tables or general covering arrays.

## Advantages

- Provides mathematically balanced combination selection.
- Reduces test count compared with exhaustive testing.
- Can support analysis of factor interactions at the designed strength.

## Limitations

- Array availability constrains factor/level structures.
- Mapping real software values can be awkward.
- Constraints can break orthogonality.
- The method can be harder to explain and maintain than pairwise generation.

## Examples

A controlled compatibility study with several factors each having the same number of levels may map cleanly to an orthogonal array.

A product matrix with unequal option counts and many forbidden combinations may be better served by constrained combinatorial generation instead.

## Best Practices

- Confirm the mathematical array fits the factor structure.
- Document factor-to-level mapping.
- Validate constraints before execution.
- Add high-risk combinations not guaranteed by the design.
- Prefer simpler pairwise/covering-array methods when they communicate and fit the problem better.

## Related Knowledge

- `Pairwise-Testing.md`
- `Combinatorial-Testing.md`
- `../Specification-Based/Equivalence-Partitioning.md`

## References

- Design-of-experiments and orthogonal-array literature.
- Combinatorial software testing research.