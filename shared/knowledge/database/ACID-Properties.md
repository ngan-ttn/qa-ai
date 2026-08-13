# ACID Properties

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview
ACID summarizes four properties associated with reliable transactions: Atomicity, Consistency, Isolation, and Durability.

## Purpose
Give QA a precise framework for transaction-risk analysis without oversimplifying engine-specific guarantees.

## Core Concepts
### Atomicity
A transaction's changes are committed as a unit or not committed.
### Consistency
A committed transaction should preserve defined integrity rules; ACID consistency does not mean every business rule is automatically enforced.
### Isolation
Concurrent transactions are separated according to the configured isolation model.
### Durability
Committed changes survive failures within the DBMS's documented durability guarantees.

## How It Works
Logging, locking/MVCC, constraints, recovery, and storage mechanisms cooperate to provide these properties.

## When to Use
Use for transaction, failure, concurrency, and recovery testing.

## When Not to Use
Do not use ACID as proof that application-level workflows across services are globally consistent.

## Advantages
ACID provides a strong vocabulary for data correctness under failures and concurrency.

## Limitations
Exact guarantees depend on DBMS configuration, isolation, replication, and durability settings.

## Examples
A committed payment record should not disappear after a supported database restart if durability guarantees apply.

## Best Practices
- Test properties through observable behavior.
- Confirm engine configuration.
- Separate database consistency from domain correctness.

## Related Knowledge
- `Transactions.md`
- `Isolation-Levels.md`
- `Backup-and-Recovery.md`

## References
- Database transaction-processing literature.
- Target DBMS documentation.