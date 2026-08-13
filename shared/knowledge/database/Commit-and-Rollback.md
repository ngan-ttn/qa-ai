# Commit and Rollback

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview
Commit finalizes a transaction's changes; rollback abandons eligible uncommitted changes.

## Purpose
Support validation of success, cancellation, error recovery, and test-data cleanup.

## Core Concepts
### Commit Boundary
Defines which changes become finalized under the DBMS transaction model.
### Rollback
Restores transactional state to the start or a supported savepoint.
### Autocommit
Some clients commit each statement automatically unless configured otherwise.

## How It Works
The DBMS records transaction state and either completes persistence at commit or discards/reverses uncommitted work at rollback.

## When to Use
Use for error paths, multi-step writes, manual SQL testing, and cleanup.

## When Not to Use
Do not expect rollback to undo external side effects such as emails or calls already made outside the database transaction.

## Advantages
Explicit boundaries make failure behavior and test setup more controllable.

## Limitations
DDL and autocommit behavior vary by DBMS and client configuration.

## Examples
A failed second insert should allow rollback of the first insert when both belong to the same transaction.

## Best Practices
- Know the client's autocommit mode.
- Verify persisted state after commit and rollback.
- Use savepoints only where supported and relevant.

## Related Knowledge
- `Transactions.md`
- `Data-Manipulation-Language.md`

## References
- ISO/IEC 9075 transaction control.
- Target DBMS documentation.