# Foundation Testing Approaches

## Purpose

This category establishes the three core testing perspectives used throughout the Testing Techniques knowledge domain.

## Scope

```text
Foundation/
├── Black-Box-Testing.md
├── White-Box-Testing.md
└── Gray-Box-Testing.md
```

- **Black Box** focuses on externally observable behavior.
- **White Box** uses internal implementation structure and coverage evidence.
- **Gray Box** combines behavior validation with partial internal knowledge.

## Learning Path

```text
Black Box ─┐
           ├── Gray Box
White Box ─┘
```

These are perspectives, not mutually exclusive project phases. A QA strategy may combine them according to risk and available observability.

## Relationships

Foundation concepts support every downstream category. Detailed specification-based techniques primarily build on Black-Box Testing; structure-based coverage primarily builds on White-Box Testing.

## Quality Boundary

The articles explain reusable testing knowledge. Project-specific coverage targets, access permissions, tooling, and execution gates remain authoritative project decisions.

## References

- `../Catalog.md`
- `../README.md`
- `../../../standards/Knowledge-Article.md`