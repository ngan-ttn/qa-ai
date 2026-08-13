# Concurrency Control

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Concurrency control** is the set of mechanisms used by a DBMS and application to coordinate simultaneous transactions while preserving required correctness. Common approaches include locking, multi-version concurrency control (MVCC), optimistic validation, serialization, and application-level conflict handling.

## Purpose

This article gives QA a broader framework than locking alone for analyzing races, conflicts, lost updates, retries, duplicate creation, and concurrent business operations.

## Core Concepts

### Pessimistic Control
Prevents conflicting work through locks or reservations before completion.

### Optimistic Control
Allows work to proceed and detects conflicts when validating or committing, often requiring retry.

### MVCC
Maintains multiple row versions so readers can access a consistent version while writers create newer versions.

### Compare-and-Set or Version Column
Applications can update only if a version or token still matches, preventing silent overwrite.

### Lost Update
Two actors read the same state and write changes so one update unintentionally overwrites another.

### Write Skew
Transactions update different rows based on a shared condition and collectively violate an invariant under some snapshot models.

### Retry
Conflict resolution can involve retry, but retries must be safe and bounded and may require idempotency.

## How It Works

```text
Application conflict rules
        ↓
Transaction isolation
        ↓
Locks / MVCC / validation
        ↓
Constraints / unique keys
        ↓
Final committed state
```

A unique constraint can prevent duplicate committed rows even when two requests race, while the application still needs to translate the losing transaction's error correctly.

## When to Use

Use concurrency-control knowledge for simultaneous edits, duplicate submissions, scheduling, allocation, counters, reservation-like workflows, and any requirement involving multiple actors or workers.

## When Not to Use

Do not model concurrency only by sending requests at roughly the same time. Precise race conditions often require controlled synchronization and knowledge of transaction boundaries.

## Advantages

Concurrency testing finds defects invisible in sequential execution and validates both database protection and application conflict handling.

## Limitations

Concurrency is timing-sensitive and environment-dependent. Locks, isolation, replicas, queues, retries, and caches can all influence outcomes.

## Examples

### Duplicate Creation Race
Two requests attempt to create the same unique business key. A database unique constraint allows one commit and rejects the other. QA validates both final state and user or API response.

### Lost Update
Two users load version 5 of a record. User A saves version 6, then User B writes stale data. An optimistic version check can reject B instead of silently overwriting A.

### Limited Resource
Two transactions observe one remaining allocatable unit. Correct design must prevent both from successfully claiming it if exclusivity is required.

## Best Practices

- Define the invariant being protected before designing the test.
- Synchronize concurrent steps explicitly where possible.
- Verify final database state and all participant responses.
- Test conflict, timeout, deadlock, and retry paths.
- Use unique constraints or version checks as evidence only when they actually exist.
- Separate database concurrency from distributed-service concurrency.
- Repeat and instrument race tests for reproducibility.

## Related Knowledge

- `Transactions.md`
- `Isolation-Levels.md`
- `Locking.md`
- `Constraints.md`
- `../api/Idempotency.md`
- `../qa/Risk-Based-Testing.md`

## References

- Database concurrency-control literature.
- Target DBMS MVCC, locking, and conflict documentation.