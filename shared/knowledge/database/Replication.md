# Replication

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Replication** copies or propagates database changes from one node or storage location to another to support availability, read scaling, disaster recovery, geographic distribution, or downstream processing. Replication does not imply immediate consistency or automatic failover unless the architecture explicitly provides those guarantees.

## Purpose

This article helps QA reason about replica lag, read routing, failover, consistency, recovery, and test observations across replicated database architectures.

## Core Concepts

### Primary and Replica
A primary commonly accepts writes while replicas receive propagated changes. Other architectures may support multi-primary or consensus-based writes.

### Synchronous Replication
Commit acknowledgment can depend on one or more replicas confirming persistence, increasing durability/consistency at the cost of latency and availability trade-offs.

### Asynchronous Replication
The primary can acknowledge before replicas apply the change, allowing lag and temporary stale reads.

### Replica Lag
The delay between source commit and replica visibility.

### Read Routing
Applications may send reads to replicas, which changes read-after-write expectations.

### Failover
A replica may be promoted after primary failure. Client reconnection, transaction loss, and consistency guarantees depend on topology and policy.

### Conflict
Multi-writer systems need mechanisms for write conflict prevention or resolution.

## How It Works

```text
Write to source
     ↓
Commit / log change
     ↓
Replication transport
     ↓
Replica apply
     ↓
Read-visible on replica
```

The time and guarantees between these stages depend on replication mode, network conditions, and system design.

## When to Use

Use replication knowledge for stale-read defects, read-after-write testing, failover, disaster recovery, reporting replicas, geographic systems, and performance architecture.

## When Not to Use

Do not assume replicas are exact real-time copies. Do not use a replica result as evidence of primary persistence without understanding the routing and lag model.

## Advantages

Replication can improve availability, read scalability, geographic resilience, and recovery options.

## Limitations

It introduces lag, operational complexity, failover uncertainty, conflict handling, additional storage/network cost, and potentially weaker read consistency.

## Examples

### Read-After-Write Lag
An API writes to the primary, then a reporting read routed to a replica temporarily returns the old value. QA compares behavior with the documented consistency expectation.

### Failover
The primary becomes unavailable and a replica is promoted. QA verifies reconnection, allowed recovery time, final committed data, and handling of in-flight transactions.

### Replica-Only Defect
A report is stale while direct primary data is current. Investigation focuses on replication/apply lag rather than the original write path.

## Best Practices

- Know which node or endpoint each test reads and writes.
- Measure lag when freshness matters.
- Test failover with approved procedures and explicit recovery expectations.
- Reconcile final state after promotion/failback.
- Separate replication consistency from transaction isolation.
- Validate read-routing assumptions in application configuration.
- Do not infer synchronous durability from topology names alone.

## Related Knowledge

- `Database-Architecture.md`
- `Transactions.md`
- `Isolation-Levels.md`
- `Backup-and-Recovery.md`
- `Performance-Monitoring.md`

## References

- Target DBMS replication and failover documentation.
- Distributed-systems consistency literature.