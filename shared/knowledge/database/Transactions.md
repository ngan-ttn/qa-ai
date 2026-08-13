# Transactions

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

A **database transaction** is a unit of work whose operations are coordinated under defined commit, rollback, isolation, and durability semantics. Transactions protect related changes from being left in unintended partial states and control how concurrent work interacts.

A transaction is a database boundary, not automatically a business-process boundary. A workflow that calls multiple services, queues, or external systems can span several independent transactions.

## Purpose

This article gives QA and QA-AI a practical reasoning model for multi-step persistence, failure injection, rollback verification, concurrency, visibility, and defect isolation.

## Core Concepts

### Transaction Boundary
A transaction begins explicitly or implicitly and ends with commit, rollback, or failure handling. Exact autocommit behavior depends on driver, framework, and DBMS settings.

### Atomic Work Unit
Changes inside one transaction are intended to become committed together or not become committed, subject to the engine's transaction guarantees.

### Commit
Commit requests that the transaction's changes become durable and visible according to the DBMS's rules.

### Rollback
Rollback abandons transactional changes that have not been committed. It cannot generally undo external side effects already performed outside the transaction.

### Isolation
Isolation determines what one transaction can observe about concurrent changes and which anomalies are possible.

### Transaction State
Transactions can be active, committed, rolled back, aborted, waiting, or in product-specific error states.

### Savepoint
Some DBMSs allow partial rollback to a savepoint inside a larger transaction.

## How It Works

```text
BEGIN
  ↓
Read / validate
  ↓
Write A
  ↓
Write B
  ↓
Constraint / conflict checks
  ↓
COMMIT or ROLLBACK
```

The DBMS coordinates locks or MVCC metadata, transaction logs, constraint checks, and recovery information. Visibility to other sessions depends on isolation and commit state.

For QA, key questions are: which operations share the transaction, which state is visible before commit, what remains after failure, and which side effects sit outside rollback scope.

## When to Use

Use transaction knowledge for multi-table updates, order creation, status transitions, batch processing, concurrency tests, stored procedures, migration, rollback scenarios, and failure recovery.

## When Not to Use

Do not assume a web request maps to exactly one transaction. Do not assume external notifications, messages, HTTP calls, or file writes are rolled back with database state. Do not assume autocommit settings are identical across tools and application code.

## Advantages

Transactions reduce partial-update risk, provide controlled concurrency, and give a clear unit for commit/rollback reasoning.

## Limitations

Long transactions can hold locks or old row versions, increase contention, delay cleanup, and complicate failure recovery. Distributed workflows require additional patterns; those are not provided automatically by one local transaction.

## Examples

### Multi-Table Create
Creating an order inserts a header and several items. If a required item insert fails, QA verifies that no unintended partial order remains when both writes are documented to share one transaction.

### External Side Effect
A transaction writes a record and then calls an external service. If the service succeeds but the DB transaction rolls back, database rollback alone cannot undo the external effect.

### Visibility
Session A updates a row but does not commit. Session B may or may not observe the new value depending on isolation and DBMS behavior.

### Deadlock Victim
Two transactions acquire resources in conflicting order. The DBMS aborts one transaction. QA verifies application retry/error handling and final data consistency.

## Best Practices

- Identify transaction boundaries from code/configuration or authoritative design.
- Verify successful commit and failure rollback paths.
- Check all related tables and side effects after rollback.
- Confirm isolation level and autocommit behavior.
- Test concurrency with deterministic orchestration where possible.
- Keep test transactions short and targeted.
- Distinguish local database atomicity from distributed business consistency.
- Capture correlation IDs, timestamps, and transaction context for defects.

## Related Knowledge

- `ACID-Properties.md`
- `Commit-and-Rollback.md`
- `Isolation-Levels.md`
- `Locking.md`
- `Concurrency-Control.md`
- `Stored-Procedure-Testing.md`
- `../api/Idempotency.md`

## References

- ISO/IEC 9075, SQL transaction concepts.
- Transaction-processing literature.
- Target DBMS and application-framework transaction documentation.