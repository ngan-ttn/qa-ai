# Commit and Rollback

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Commit** finalizes a database transaction according to the DBMS's durability and visibility guarantees. **Rollback** abandons uncommitted transactional changes. Together they define the primary success and failure boundaries of transactional work.

## Purpose

This article helps QA validate failure paths, partial-state prevention, transaction error handling, savepoints, and the difference between database rollback and compensation of external side effects.

## Core Concepts

### Commit
Commit marks a transaction as successfully completed. Other sessions observe its effects according to isolation and replication behavior.

### Rollback
Rollback reverses or discards transaction-local uncommitted changes according to engine semantics.

### Implicit Commit and Autocommit
Drivers or DBMSs may automatically commit statements. Some DDL can have special commit behavior.

### Savepoint
A savepoint allows rollback of part of a transaction where supported, without discarding all prior work.

### Abort-on-Error
Certain errors can mark a transaction as failed until rollback; details vary by DBMS and driver.

## How It Works

```text
BEGIN
  ↓
change A
  ↓
change B
  ├── success → COMMIT
  └── failure → ROLLBACK
```

The DBMS uses transaction metadata, logs, undo information, or row versions to finalize or discard work.

## When to Use

Use this knowledge for exception-path testing, transactional services, stored routines, batch processing, migrations, test-data setup, and concurrency failures.

## When Not to Use

Do not assume rollback reverses messages already published, notifications sent, remote API operations, or files written. Do not assume every database tool starts an explicit transaction automatically.

## Advantages

Commit and rollback semantics provide predictable success and recovery boundaries for database work.

## Limitations

Behavior differs for DDL, distributed transactions, nested transactions, savepoints, and connection failures. A lost client response after commit can create uncertainty about whether the write succeeded.

## Examples

### Mid-Transaction Failure
An update to record A succeeds, but update to record B violates a constraint. QA verifies rollback leaves both records in the expected original state if both operations share one transaction.

### Lost Response After Commit
The DB commits, but the application times out before receiving confirmation. Retrying an unsafe operation can duplicate effects, so QA evaluates reconciliation or idempotency behavior.

### Savepoint
A batch processes optional items and rolls back one failed item to a savepoint. This should be tested only if the design explicitly uses savepoints.

## Best Practices

- Confirm transaction and autocommit configuration in the actual application path.
- Test failures before and after critical operations.
- Verify complete persistent state after rollback.
- Treat unknown commit outcome as a retry and reconciliation risk.
- Avoid relying on rollback as the only safety mechanism for external effects.
- Use explicit transaction cleanup in automated tests.

## Related Knowledge

- `Transactions.md`
- `ACID-Properties.md`
- `Isolation-Levels.md`
- `Stored-Procedure-Testing.md`
- `../api/Idempotency.md`
- `../api/Retry-Strategy.md`

## References

- ISO/IEC 9075, transaction control.
- Target DBMS and driver transaction documentation.