# API Mocking

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-12

## Overview

**API mocking** simulates an API provider or dependency so consumers and tests can execute without relying on the real system. A mock can return predefined, rule-based, stateful, delayed, or error responses according to a controlled model.

## Purpose

Mocking helps QA test early, reproduce rare dependency conditions, isolate systems, and reduce reliance on unstable or costly external environments.

## Core Concepts

### Stub vs Mock

Terminology varies. A stub usually returns predefined responses; a mock may also verify expected interactions. In API testing, tools often use the term mock broadly.

### Contract-Based Mock

A mock generated from OpenAPI, AsyncAPI, schema, or consumer contract can stay closer to the defined interface.

### Stateful Mock

A stateful mock changes responses based on prior interactions, enabling workflow testing.

### Fault Simulation

Mocks can simulate timeouts, invalid responses, rate limits, server errors, or delayed processing that are difficult to reproduce in real dependencies.

### Fidelity

A mock is useful only to the degree that its behavior represents the dependency aspects relevant to the test objective.

## How It Works

```text
System Under Test
      ↓ request
Mock Dependency
      ↓ configured behavior
Response / delay / error
      ↓
System Under Test reaction
```

The mock replaces one boundary while the rest of the system remains under test.

## When to Use

Use mocking when a dependency is unavailable, expensive, nondeterministic, rate-limited, difficult to seed, not yet implemented, or unable to produce required error states.

## When Not to Use

Do not rely exclusively on mocks for release confidence. Real integration tests remain necessary for protocol, configuration, mapping, authentication, and behavior that the mock cannot faithfully reproduce.

## Advantages

Mocks improve determinism, speed, isolation, early testing, and coverage of rare failures.

## Limitations

Mocks can drift from reality, hide integration defects, oversimplify timing, and create false confidence if behavior is hand-coded incorrectly.

## Examples

### Partner Error

Mock a partner response with `503` and delay to verify timeout and retry behavior without disrupting the real sandbox.

### Contract-First Development

A frontend team uses a mock generated from the agreed API schema before the backend implementation is complete.

### Rare State

A mock returns a specific downstream decline code that is difficult to generate through the real provider.

## Best Practices

- Derive mocks from authoritative contracts where possible.
- Keep mocked behavior minimal and objective-specific.
- Version mocks with contract changes.
- Include error and latency behavior, not only happy paths.
- Maintain a separate real-integration suite.
- Detect mock drift through contract tests or periodic comparison with the real service.
- Clearly label evidence produced from mocks versus real dependencies.

## Related Knowledge

- `Contract-Testing.md`
- `Integration-Testing.md`
- `API-Test-Strategy.md`
- `Retry-Strategy.md`
- `Timeout-Handling.md`

## References

- OpenAPI and AsyncAPI specifications for contract-driven mocks.
- Service virtualization and test-double practices in software testing literature.

Mock fidelity requirements depend on the specific integration risk.
