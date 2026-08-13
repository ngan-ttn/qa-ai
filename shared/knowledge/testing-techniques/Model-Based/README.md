# Model-Based Testing Techniques

## Purpose

This category explains test derivation from explicit behavioral models.

## Scope

```text
Model-Based/
├── Model-Based-Testing.md
└── Finite-State-Machine-Testing.md
```

Model-Based Testing is the broader approach. Finite State Machine Testing is a specialization for finite state/event/transition behavior.

## Quality Boundary

A model is a test oracle only after its business meaning and abstraction are validated. Generated tests must not make an incorrect or stale model authoritative over approved requirements.

## Relationships

State Transition Testing provides specification-based state reasoning; FSM Testing provides a formal model-oriented extension; Domain Model knowledge provides business semantics but is not itself a test-generation contract.

## References

- `../Catalog.md`
- `../Specification-Based/State-Transition-Testing.md`
- `../../domain/Domain-Model.md`
- `../../../standards/Knowledge-Article.md`