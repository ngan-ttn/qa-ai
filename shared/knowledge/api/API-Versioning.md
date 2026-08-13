# API Versioning

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-12

## Overview

**API versioning** is the practice of managing contract evolution so providers can change an API while controlling compatibility impact on consumers. Versioning is one tool within broader compatibility management; not every change requires a new externally visible version.

## Purpose

This article helps QA identify breaking versus non-breaking changes, design compatibility scenarios, validate supported versions, and test migration or deprecation behavior.

## Core Concepts

### Backward Compatibility

A provider change is backward-compatible when supported existing consumers can continue operating according to their contract expectations.

### Breaking Change

Examples can include removing fields, changing field meaning or type, making optional input mandatory, removing accepted values, or changing endpoint semantics.

### Version Identifier

Versions may be expressed through URI paths, headers, media types, query parameters, or other governance mechanisms.

### Compatibility Policy

The organization should define what constitutes a breaking change, how long versions are supported, and how deprecation is communicated.

### Consumer Tolerance

Clients should often tolerate additive response changes, but actual tolerance depends on implementation and contract. QA should test rather than assume.

### Schema Evolution

Adding optional fields is usually less disruptive than removing or redefining fields, but compatibility must consider serialization libraries, validation rules, generated clients, and consumer behavior.

## How It Works

```text
Current Contract
      │
      ├── compatible change → evolve same version
      │
      └── incompatible change → new version / migration strategy
```

A versioning strategy normally includes overlap, migration, deprecation, and retirement decisions.

## When to Use

Use versioning knowledge during change-impact analysis, regression planning, consumer compatibility testing, API migrations, mobile-backend compatibility validation, and deprecation planning.

## When Not to Use

Do not create new versions for every implementation change. Internal refactoring that preserves contract behavior does not require consumer-visible versioning.

## Advantages

Versioning can provide controlled evolution, migration time, coexistence of old and new consumers, and clearer compatibility guarantees.

## Limitations

Supporting multiple versions increases code, testing, documentation, operational, and security maintenance costs. Versioning cannot compensate for unclear compatibility policy.

## Examples

### Additive Change

A new optional response field is added. QA validates existing clients or contract consumers continue to work.

### Breaking Schema Change

`amount` changes from integer minor units to decimal major units. This changes meaning and representation and requires explicit compatibility handling.

### Overlapping Versions

`v1` remains supported while `v2` is introduced. QA validates both versions independently plus migration-critical differences.

## Best Practices

- Classify changes by consumer impact, not implementation effort.
- Maintain regression coverage for every supported version.
- Test old clients against new providers when independent deployment exists.
- Document deprecation and retirement behavior.
- Avoid silent semantic changes to existing fields.
- Validate generated SDK/client compatibility if provided.
- Include authorization and security fixes across all supported versions as required by policy.

## Related Knowledge

- `API-Lifecycle.md`
- `Contract-Testing.md`
- `REST-Architecture.md`
- `Response-Structure.md`
- `Functional-API-Testing.md`

## References

- OpenAPI Specification for describing versioned API contracts.
- Semantic Versioning concepts may inform compatibility classification but do not define a universal API-versioning strategy.

The actual versioning policy must come from the provider's governance standard.
