# Isolation Levels

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Transaction isolation** defines how concurrent transactions interact and what intermediate or changing state one transaction can observe from another. SQL commonly names levels such as Read Uncommitted, Read Committed, Repeatable Read, and Serializable, but real implementations can differ from simplified textbook anomaly tables.

## Purpose

This article helps QA design concurrency tests, interpret inconsistent observations correctly, and avoid assuming one isolation model from generic DBMS terminology.

## Core Concepts

### Dirty Read
A transaction observes another transaction's uncommitted change.

### Non-Repeatable Read
The same row read twice can change because another transaction commits an update between reads.

### Phantom
Repeating a predicate query can return a different set of matching rows after concurrent inserts or deletes.

### Serialization Anomaly
Concurrent transactions produce a result that cannot be explained by any serial ordering of those transactions.

### Snapshot and MVCC Behavior
Some DBMSs use multi-version concurrency control and expose snapshot semantics that do not map perfectly to traditional lock-based descriptions.

### Configured Level
Isolation can be configured globally, per session, or per transaction depending on the product.

## How It Works

Isolation is implemented through locks, versions, validation, conflict detection, or combinations. Stronger isolation generally restricts anomalies but may increase blocking, aborts, version retention, or retry needs.

## When to Use

Use isolation knowledge for concurrent edits, duplicate prevention, scheduling, reporting consistency, allocation, counters, and deadlock or retry analysis.

## When Not to Use

Do not derive expected anomalies only from a generic table of isolation levels. Confirm the target DBMS's documented semantics and application configuration.

## Advantages

Correct isolation reasoning exposes lost-update, stale-read, write-skew, phantom, and serialization risks that single-user testing misses.

## Limitations

Concurrency tests can be nondeterministic without controlled synchronization. Product-specific MVCC, locking, predicate locking, and conflict behavior vary significantly.

## Examples

### Read Committed
Transaction A reads a row. Transaction B commits an update. A second read by transaction A may see the new value under common Read Committed implementations.

### Snapshot Conflict
Two transactions read the same snapshot and update related rows. Depending on the DBMS, both may commit or one may be rejected; QA must validate documented semantics.

### Serializable Retry
Under Serializable isolation, the DBMS may abort one transaction to preserve serializable behavior. Application retry may therefore be an expected part of the design.

## Best Practices

- Record the exact isolation level used by the application path.
- Orchestrate concurrent steps with barriers or latches rather than timing guesses.
- Validate final state, not only intermediate responses.
- Repeat concurrency tests to expose race-dependent outcomes.
- Include retry and abort handling where the DBMS can reject conflicting work.
- Separate replica consistency from transaction isolation.

## Related Knowledge

- `Transactions.md`
- `ACID-Properties.md`
- `Locking.md`
- `Concurrency-Control.md`
- `Replication.md`

## References

- ISO/IEC 9075 transaction isolation concepts.
- Target DBMS isolation and MVCC documentation.