# Locking

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview
Locking is a concurrency-control mechanism that restricts incompatible access to database resources.

## Purpose
Support analysis of blocking, deadlocks, lost updates, and concurrent-write behavior.

## Core Concepts
### Shared and Exclusive Intent
Lock modes represent compatible and incompatible access intentions; exact modes vary by DBMS.
### Granularity
Locks may apply to rows, pages, tables, metadata, or other resources.
### Deadlock
Transactions can wait cyclically until the DBMS selects a victim or resolves the cycle.

## How It Works
The lock manager grants, queues, converts, and releases locks according to compatibility and transaction state.

## When to Use
Use for contention, deadlock, concurrent update, and long-running transaction tests.

## When Not to Use
Do not assume an MVCC system has no locks or that all reads block writes.

## Advantages
Locks protect conflicting operations and help preserve consistency.

## Limitations
Contention can reduce throughput and create timeouts or deadlocks.

## Examples
Two transactions updating the same row may cause one to wait or fail depending on the engine and timing.

## Best Practices
- Observe blocking with approved monitoring tools.
- Keep transactions short.
- Test recovery after deadlock/timeout.
- Avoid relying on timing alone for concurrency tests.

## Related Knowledge
- `Isolation-Levels.md`
- `Concurrency-Control.md`
- `Performance-Monitoring.md`

## References
- Target DBMS concurrency-control documentation.