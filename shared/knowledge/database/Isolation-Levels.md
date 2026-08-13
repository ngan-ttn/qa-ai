# Isolation Levels

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview
Isolation levels define classes of visibility and concurrency behavior between transactions.

## Purpose
Help QA design reproducible concurrent tests and interpret anomalies correctly.

## Core Concepts
### Read Phenomena
Dirty reads, non-repeatable reads, and phantom-like changes are common conceptual phenomena.
### Serializable
A strong level intended to produce outcomes equivalent to some serial execution, though implementation mechanisms vary.
### MVCC and Locking
Engines may implement isolation through versioning, locks, or combinations.

## How It Works
The configured level controls what versions or locks a transaction observes and how conflicts are handled.

## When to Use
Use for concurrent updates, balances, inventory, duplicate prevention, and race-condition analysis.

## When Not to Use
Do not infer exact behavior solely from the isolation-level name; engine semantics differ.

## Advantages
Isolation provides controlled trade-offs between concurrency and anomaly prevention.

## Limitations
Stronger isolation may increase blocking, retries, or serialization failures.

## Examples
Two concurrent reservations for the last unit can expose lost-update or overselling risks if application and database controls are insufficient.

## Best Practices
- Record the actual DBMS and isolation setting.
- Synchronize concurrent test steps deliberately.
- Validate final state as well as intermediate observations.

## Related Knowledge
- `Transactions.md`
- `Locking.md`
- `Concurrency-Control.md`

## References
- ISO/IEC 9075 transaction isolation concepts.
- Target DBMS isolation documentation.