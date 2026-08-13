# Combinatorial Testing Techniques

## Purpose

This category addresses interaction coverage when many parameters create a large Cartesian product of possible configurations or inputs.

## Scope

```text
Combinatorial/
├── Pairwise-Testing.md
├── Orthogonal-Array-Testing.md
└── Combinatorial-Testing.md
```

## Relationships

Pairwise Testing covers two-way interactions. General Combinatorial Testing supports configurable `t-way` strength and constraints. Orthogonal Array Testing uses mathematically balanced designs when the factor structure fits.

## Quality Boundary

Interaction coverage does not replace boundary, sequence, state, or exact business-rule coverage. Critical combinations should be seeded explicitly instead of assuming a generated array will contain them.

## References

- `../Catalog.md`
- `../Specification-Based/Equivalence-Partitioning.md`
- `../../../standards/Knowledge-Article.md`