# Contract Testing

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-12

## Overview

**Contract testing** verifies that API providers and consumers remain compatible with an agreed interface contract. The contract may describe operations, schemas, status codes, required fields, events, or consumer-specific expectations.

## Purpose

Contract testing catches interface incompatibilities earlier than broad end-to-end testing and supports independently deployed services or clients.

## Core Concepts

### Provider Contract

The provider promises a defined interface and behavior.

### Consumer Expectation

Consumers depend on specific parts of the provider contract. Consumer-driven contract testing captures those actual expectations explicitly.

### Schema Compatibility

Field presence, data types, nullability, enumerations, and structural changes can affect consumers.

### Behavioral Compatibility

Compatibility includes more than schema. Status codes, required headers, semantics, and error behavior may be contractually significant.

### Breaking Change

A change breaks the contract when supported consumers can no longer interact as promised.

### Contract Artifact

Contracts may be represented in OpenAPI, AsyncAPI, Protocol Buffers, Pact-style consumer contracts, JSON Schema, or other formats.

## How It Works

```text
Consumer Expectation / Shared Contract
            ↓
   Automated Contract Checks
       ↙              ↘
 Consumer side      Provider side
       ↓              ↓
 detect mismatch before integration release
```

Contract checks are commonly executed in CI/CD pipelines.

## When to Use

Use contract testing for microservices, public APIs, partner APIs, mobile backends, event schemas, independent deployment, and version evolution.

## When Not to Use

Do not treat contract tests as a replacement for business-process, end-to-end, security, or performance testing. A provider can satisfy the contract while still implementing incorrect business logic.

## Advantages

Contract testing is fast, precise, automatable, and effective at detecting incompatible interface changes before broader integration testing.

## Limitations

Contract tests cover only what the contract expresses. Incomplete contracts create false confidence, and consumer-driven contracts may miss unsupported consumers or emergent cross-system behavior.

## Examples

### Removed Field

A provider removes `currency` from a payment response. Contract validation fails before deployment because a supported consumer requires the field.

### Enum Change

A new status value is added. QA validates whether consumers are tolerant of additive enum values or whether the change is breaking for generated clients.

### Error Contract

A consumer expects `404` plus a stable error code for an unknown resource; provider changes to a generic `200` envelope. Contract checks flag the incompatibility.

## Best Practices

- Keep contract artifacts versioned and reviewable.
- Validate both success and important error shapes.
- Distinguish provider schema validation from consumer-driven expectations.
- Run contract checks before broad integration suites.
- Include all supported consumer types or document known gaps.
- Treat compatibility failures as change-management signals, not merely test failures.
- Avoid embedding internal implementation details in public contracts.

## Related Knowledge

- `API-Versioning.md`
- `API-Lifecycle.md`
- `Integration-Testing.md`
- `Response-Structure.md`
- `API-Mocking.md`

## References

- OpenAPI Specification.
- JSON Schema.
- Pact contract-testing concepts.
- AsyncAPI Specification for asynchronous interfaces.

The authoritative contract format depends on the target integration.
