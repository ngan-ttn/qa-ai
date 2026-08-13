# ACID Properties

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**ACID** summarizes four properties associated with reliable database transactions: **Atomicity, Consistency, Isolation, and Durability**. ACID is a reasoning framework, not a promise that every application workflow or distributed system is automatically correct.

## Purpose

This article helps QA reason precisely about failure and concurrency behavior while separating database guarantees from application-level business correctness.

## Core Concepts

### Atomicity
A transaction's participating database changes are committed as a unit or are not committed. Atomicity does not include external systems unless they participate in a supported distributed protocol.

### Consistency
A transaction moves the database between states that satisfy the integrity rules actually enforced or guaranteed by the system. ACID consistency does not mean every business rule is automatically enforced by the DBMS.

### Isolation
Concurrent transactions behave according to a defined isolation model. Lower isolation can permit anomalies; stronger isolation can increase contention or aborts.

### Durability
Once commit succeeds under the configured durability model, the DBMS preserves committed state through supported failures. Exact guarantees can depend on logging, storage, replication, acknowledgment policy, and configuration.

## How It Works

```text
Atomicity   ← transaction log / undo / versioning
Consistency ← constraints + transaction logic + application rules
Isolation   ← locks / MVCC / conflict detection
Durability  ← log flush / storage / replication policy
```

No single mechanism universally implements all four properties, and products differ substantially.

## When to Use

Use ACID when analyzing transaction failures, crash recovery, concurrent writes, rollback, migration, and data-integrity incidents.

## When Not to Use

Do not use “ACID compliant” as proof that application workflows across services are globally consistent, that replicas are immediately current, or that business calculations are correct.

## Advantages

ACID provides a compact vocabulary for reasoning about data correctness under failure and concurrency.

## Limitations

The labels are high level. Real behavior depends on isolation level, configuration, distributed architecture, autocommit, replication, storage guarantees, and application transaction boundaries.

## Examples

### Atomicity
A transaction inserts a header and lines. If one required line fails and the whole operation is one transaction, QA expects no committed partial object.

### Consistency
A foreign-key constraint prevents an invalid child reference, but it cannot by itself enforce a rule owned by an external service.

### Isolation
Two concurrent updates may serialize, block, overwrite, or cause one transaction to abort depending on concurrency control.

### Durability
After a successful commit and a supported database restart, the row should remain according to the configured durability guarantee.

## Best Practices

- Translate each ACID property into observable test expectations.
- Confirm actual transaction boundaries and DBMS configuration.
- Separate database integrity from domain correctness.
- Include crash/failure testing only in authorized environments.
- Pair ACID analysis with isolation, replication, and recovery knowledge.
- Do not infer distributed guarantees from local transaction guarantees.

## Related Knowledge

- `Transactions.md`
- `Commit-and-Rollback.md`
- `Isolation-Levels.md`
- `Concurrency-Control.md`
- `Replication.md`
- `Backup-and-Recovery.md`

## References

- Transaction-processing literature.
- Target DBMS transaction, durability, and recovery documentation.