# Functional API Testing

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-12

## Overview

**Functional API testing** verifies that an API behaves according to its functional requirements and contract for valid and invalid interactions. It covers data validation, business rules, state transitions, calculations, response behavior, and relevant side effects.

## Purpose

This article provides a reusable framework for converting API requirements into executable functional coverage without conflating functional testing with contract, performance, or security testing.

## Core Concepts

### Positive Testing

Verify valid requests produce correct outcomes.

### Negative Testing

Verify invalid requests are rejected safely and consistently.

### Boundary Testing

Validate limits such as minimum/maximum values, lengths, dates, quantities, and collection sizes.

### State-Based Behavior

The same request may be valid or invalid depending on resource or business-process state.

### Business Rules

API behavior often includes eligibility, calculations, duplicate rules, ownership, status transitions, and conditional fields.

### Side Effects

A correct response may require persistence, audit logs, events, emails, inventory changes, or downstream calls.

### Data Integrity

Created or updated values should remain correct across subsequent reads and dependent systems when verification is in scope.

## How It Works

```text
Requirement / Rule
      ↓
Identify API input and precondition
      ↓
Execute request
      ↓
Verify status + headers + body
      ↓
Verify state / side effects
```

Test design techniques such as equivalence partitioning, boundary value analysis, decision tables, and state-transition testing can be applied to API inputs and rules.

## When to Use

Use functional API testing for CRUD operations, workflows, calculations, validation rules, search/filter behavior, uploads, batch operations, state transitions, and domain actions.

## When Not to Use

Do not use functional testing alone to claim security, performance, or compatibility quality. These require dedicated objectives and evidence.

## Advantages

Functional API tests are usually faster and more focused than UI tests, isolate backend behavior, and provide strong regression value.

## Limitations

They may miss frontend integration defects, browser-specific behavior, infrastructure issues, or full cross-system outcomes unless side effects and dependencies are explicitly validated.

## Examples

### Required Field

POST an order without a mandatory `customerId`; verify the documented validation response and no resource creation.

### State Transition

Attempt to approve an already canceled request; verify the transition is rejected according to business rules.

### Boundary

Test quantity values at minimum, maximum, just below minimum, and just above maximum.

## Best Practices

- Trace tests to business rules and contract conditions.
- Validate one primary objective per detailed test where practical.
- Verify both response and persistent side effects.
- Apply systematic test-design techniques.
- Include unauthorized or invalid-state cases when functional permissions affect behavior.
- Reuse deterministic test data and reset state cleanly.
- Avoid coupling expected results to undocumented implementation details.

## Related Knowledge

- `API-Test-Strategy.md`
- `Request-Structure.md`
- `Response-Structure.md`
- `HTTP-Status-Codes.md`
- `../testing-techniques/Specification-Based/Equivalence-Partitioning.md`
- `../testing-techniques/Specification-Based/Boundary-Value-Analysis.md`
- `../testing-techniques/Specification-Based/State-Transition-Testing.md`

## References

- ISO/IEC/IEEE software testing concepts for functional testing foundations.
- OpenAPI Specification for contract-level request/response definitions.

Expected business behavior must be derived from authoritative requirements.
