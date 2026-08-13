# Structure-Based Testing Techniques

## Purpose

This category covers implementation-aware techniques and coverage criteria used to evaluate which internal structures have been exercised.

## Scope

```text
Structure-Based/
├── Statement-Coverage.md
├── Branch-Coverage.md
├── Decision-Coverage.md
├── Condition-Coverage.md
├── Path-Coverage.md
└── Modified-Condition-Decision-Coverage-(MC-DC).md
```

## Progression

```text
Statement
   ↓
Branch / Decision
   ↓
Condition
   ↓
Selected Path Analysis
   ↓
MC/DC when specifically justified
```

Coverage strength is not a universal release-quality scale. Each metric answers a different structural question and must be interpreted with assertion quality and requirement coverage.

## Quality Boundary

No article defines a mandatory numeric coverage target. Tool semantics and project obligations remain authoritative.

## References

- `../Catalog.md`
- `../Foundation/White-Box-Testing.md`
- `../../../standards/Knowledge-Article.md`