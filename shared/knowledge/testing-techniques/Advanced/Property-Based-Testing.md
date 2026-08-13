# Property-Based Testing

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Property-Based Testing** generates many input examples and validates general properties or invariants that should hold across the generated space instead of asserting only a small set of handpicked examples.

## Purpose

Discover edge cases and broader behavioral inconsistencies by expressing rules as reusable properties and automatically exploring many valid or invalid inputs.

## Core Concepts

### Property
A statement expected to hold for a broad class of inputs, such as idempotency, round-trip consistency, ordering, conservation, or invariant preservation.

### Generator
Creates candidate inputs according to constraints.

### Shrinking
Reduces a failing generated example to a smaller, easier-to-understand counterexample.

### Invariant
A condition expected to remain true before and after operations.

### Assumptions / Preconditions
Constraints defining where a property is valid; overly restrictive assumptions reduce meaningful exploration.

## How It Works

```text
Define property + valid domain
      ↓
Generate many inputs
      ↓
Execute system behavior
      ↓
Check property
      ↓
Shrink failing counterexample
      ↓
Reproduce and add focused regression
```

## When to Use

Use for parsers, transformations, serialization, calculations, collections, sorting, APIs with invariants, idempotent operations, and data-processing logic.

## When Not to Use

Do not use vague properties as substitutes for precise business examples. Property-based testing is less suitable where expected outcomes are highly scenario-specific and no meaningful invariant can be stated.

## Advantages

- Explores many cases automatically.
- Finds unexpected edge cases.
- Shrinking improves failure diagnosis.
- Encourages explicit invariant thinking.

## Limitations

- Property design can be difficult.
- Bad generators create misleading coverage.
- Stateful/external systems require careful isolation.
- Passing properties do not prove all requirements.

## Examples

For a reversible encoding function, `decode(encode(x)) == x` may be a property across generated valid inputs.

For an idempotent API operation, repeating the same authorized request with the same idempotency context should preserve the defined business result.

For sorting, output should be ordered and contain the same multiset of items as input.

## Best Practices

- Derive properties from authoritative invariants.
- Keep generators representative and constraint-aware.
- Preserve random seeds and minimized failures.
- Separate universal properties from example-specific business rules.
- Add explicit examples for important known boundaries.
- Avoid inventing algebraic properties the system never promised.

## Related Knowledge

- `Fuzz-Testing.md`
- `Mutation-Testing.md`
- `../Specification-Based/Boundary-Value-Analysis.md`
- `../../api/Idempotency.md`
- `../../domain/Business-Rule-Fundamentals.md`

## References

- Property-based testing literature and framework documentation.