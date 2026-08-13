# Locking

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Locking** is a concurrency-control mechanism in which a DBMS coordinates access to resources by granting and waiting on lock modes. Locks may apply to rows, keys, pages, tables, metadata, predicates, or other product-specific resources.

## Purpose

This article helps QA analyze blocking, deadlocks, lost responsiveness, transaction contention, and behavior under concurrent reads and writes.

## Core Concepts

### Shared or Read Lock
Allows compatible reading while restricting certain writes under lock-based implementations.

### Exclusive or Write Lock
Protects modifications from incompatible concurrent access.

### Lock Granularity
Fine-grained locks increase concurrency but require more lock management; coarse locks can increase blocking.

### Lock Duration
Some locks last for a statement, others until transaction end, depending on isolation and DBMS rules.

### Blocking
One transaction waits because another holds an incompatible lock.

### Deadlock
Transactions form a wait cycle. The DBMS typically detects the cycle and aborts one participant.

### Lock Escalation
Some products replace many fine-grained locks with a coarser lock under configured conditions.

## How It Works

```text
T1 acquires A
T2 acquires B
T1 waits for B
T2 waits for A
      ↓
Deadlock detector
      ↓
One transaction aborted
```

MVCC systems can reduce some read and write blocking but still use locks for writes, metadata, or other operations.

## When to Use

Use locking knowledge for concurrency defects, timeout investigation, batch processing, high-contention updates, migrations, DDL blocking, and deadlock testing.

## When Not to Use

Do not assume a slow query is blocked without evidence. Do not force locks or terminate sessions in shared environments unless operationally authorized.

## Advantages

Locks provide strong coordination and can enforce serial access to conflicting operations.

## Limitations

Poor lock ordering, long transactions, broad scans, or high contention can reduce throughput and create deadlocks. Lock behavior is highly product-specific.

## Examples

### Blocking Update
T1 updates a row and keeps the transaction open. T2 attempts to update the same row and waits until T1 commits, rolls back, or a timeout occurs.

### Deadlock
T1 updates object A then B; T2 updates B then A. Opposite acquisition order can form a cycle and cause one transaction to abort.

### DDL Lock
A schema change waits behind a long-running transaction or blocks application queries, depending on DBMS metadata-lock semantics.

## Best Practices

- Keep transactions short and predictable.
- Acquire resources in consistent order where application design allows.
- Capture blocking and deadlock diagnostics rather than relying on elapsed time alone.
- Test application behavior after lock timeout or deadlock victim errors.
- Consider indexes and query predicates because they can affect locked ranges and resources.
- Confirm MVCC and locking behavior from target documentation.

## Related Knowledge

- `Transactions.md`
- `Isolation-Levels.md`
- `Concurrency-Control.md`
- `Indexes.md`
- `Performance-Monitoring.md`

## References

- Database concurrency-control literature.
- Target DBMS locking and deadlock documentation.