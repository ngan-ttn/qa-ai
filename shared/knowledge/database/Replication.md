# Replication

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview
Replication maintains copies of database data across nodes or locations using engine- or platform-specific mechanisms.

## Purpose
Support QA reasoning about read consistency, failover, lag, and topology changes.

## Core Concepts
### Primary/Replica and Multi-Writer Models
Topologies determine where writes are accepted.
### Replication Lag
Copies may not reflect a write immediately.
### Failover
Roles may change after failure.

## How It Works
Changes are transferred and applied to replicas synchronously or asynchronously according to the configured system.

## When to Use
Use for high availability, read scaling, disaster recovery, and geo-distributed systems.

## When Not to Use
Do not assume replication is a backup or that all replicas are strongly consistent.

## Advantages
Replication can improve availability, locality, and read capacity.

## Limitations
Lag, conflicts, failover gaps, and operational complexity can affect correctness.

## Examples
A write followed immediately by a read from an asynchronous replica may return older state within documented consistency behavior.

## Best Practices
- Identify read/write routing.
- Measure lag under representative load.
- Test failover and recovery when in scope.
- Validate consistency expectations explicitly.

## Related Knowledge
- `Database-Architecture.md`
- `Backup-and-Recovery.md`
- `Concurrency-Control.md`

## References
- Target DBMS replication documentation.