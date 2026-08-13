# Chaos Testing

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Chaos Testing** deliberately introduces controlled failures or adverse conditions to evaluate system resilience, recovery, observability, and degraded behavior. It is related to chaos engineering but this article focuses on the testing technique and QA reasoning boundary.

## Purpose

Validate resilience assumptions under realistic failure conditions without relying only on design claims or happy-path integration tests.

## Core Concepts

### Steady-State Hypothesis
A measurable expectation describing acceptable system behavior before, during, and after an experiment.

### Fault Injection
Controlled introduction of failures such as latency, dependency loss, process termination, resource pressure, network partition, or unavailable components.

### Blast Radius
The intentionally limited scope of possible impact.

### Abort Condition
A measurable threshold or signal requiring the experiment to stop.

### Recovery
Behavior after the fault is removed, including retry, failover, backlog processing, reconciliation, and state restoration.

### Observability
Metrics, logs, traces, alerts, and business indicators needed to understand impact and recovery.

## How It Works

```text
Define resilience hypothesis
      ↓
Choose authorized environment and blast radius
      ↓
Define fault + abort criteria
      ↓
Establish baseline
      ↓
Inject fault
      ↓
Observe behavior and recovery
      ↓
Reconcile data / side effects
      ↓
Capture learning and remediation
```

## When to Use

Use for distributed services, failover, queue processing, redundancy, retry/recovery, infrastructure dependencies, or critical workflows where resilience is an explicit requirement.

## When Not to Use

Do not perform chaos experiments in production or shared environments without explicit organizational authorization, safety controls, rollback plans, and observability. Do not use chaos testing to discover resilience requirements that were never defined.

## Advantages

- Tests real failure behavior.
- Validates recovery and observability.
- Reveals hidden dependency assumptions.
- Produces operational evidence beyond static architecture review.

## Limitations

- Can cause real disruption if poorly controlled.
- Results depend heavily on environment fidelity.
- Failure combinations are vast.
- Passing one experiment does not prove universal resilience.

## Examples

A controlled test pauses one non-production dependency and verifies timeout, retry, user-visible degradation, backlog recovery, and duplicate protection.

A queue consumer is restarted while messages are in flight; QA verifies eventual processing, ordering assumptions, duplicate handling, and reconciliation against defined guarantees.

## Best Practices

- Obtain explicit authorization.
- Start with small blast radius.
- Define steady state and abort criteria.
- Protect real customer/business data.
- Verify recovery and data integrity, not only service availability.
- Capture observations and follow-up actions.
- Increase experiment scope only after lower-risk tests are stable.

## Related Knowledge

- `../Experience-Based/Exploratory-Testing.md`
- `../../api/Retry-Strategy.md`
- `../../api/Timeout-Handling.md`
- `../../database/Backup-and-Recovery.md`
- `../../qa/Risk-Based-Testing.md`

## References

- Chaos engineering and resilience testing literature.
- Organization reliability and environment-safety policies.