# Database Architecture

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Database architecture** describes the components and deployment relationships used to store, process, protect, and serve data. It includes logical layers such as clients, query processors, transaction managers, storage engines, logs, and catalogs, plus deployment patterns such as single-node systems, primary/replica topologies, clusters, partitions, and distributed databases.

## Purpose

This article helps QA reason about where database behavior occurs, which component may cause a failure, and how topology can affect consistency, latency, failover, recovery, and test observations.

## Core Concepts

### Client and Connection Layer

Applications connect through drivers, protocols, connection pools, gateways, or proxies. Authentication, session settings, timeouts, and routing can differ by connection path.

### Query Processor

The parser validates syntax; the optimizer chooses an execution plan; the executor performs the plan. Product implementations vary, but the separation is useful for performance reasoning.

### Transaction and Concurrency Manager

This component coordinates commit, rollback, locks or MVCC, isolation, and conflict handling.

### Storage Engine

The storage engine manages pages, records, indexes, caches, and durable media. Physical layout is product-specific and should not be assumed from logical schema alone.

### Transaction Log

Many systems record changes in a log used for recovery, replication, or durability. Exact guarantees depend on configuration and engine behavior.

### Metadata / Catalog

The system catalog stores schema definitions, object metadata, statistics, permissions, and related information.

### Deployment Topology

Architectures may include primary/replica, shared-nothing clusters, shards, managed cloud services, read replicas, or distributed consensus groups. A topology changes where reads and writes go and what consistency can be observed.

## How It Works

A generalized path is:

```text
Application
    ↓
Driver / Pool / Proxy
    ↓
DBMS Listener
    ↓
Parser → Optimizer → Executor
    ↓          ↓
Transaction   Storage
Manager       Engine
    ↓          ↓
Log / Cache / Data Files / Replicas
```

In replicated deployments, write traffic may go to a primary while some reads go to replicas. A recently committed change can therefore appear immediately on one connection and later on another if replica lag exists and the architecture permits it.

## When to Use

Use database architecture knowledge for environment design review, failover testing, replica consistency checks, performance analysis, connection issues, backup/recovery validation, sharding, migration, and diagnosing differences between read and write paths.

## When Not to Use

Do not infer a project's topology from generic terminology such as “database cluster” or “cloud database.” Do not assume replicas are synchronous, failover is automatic, or read-after-write consistency is guaranteed unless documented.

## Advantages

Architectural awareness improves defect localization, makes consistency expectations more precise, and prevents QA from treating every database observation as if it came from one authoritative node with immediate visibility.

## Limitations

Architecture can be hidden behind managed services or proxies. Operational settings can change behavior without schema changes. Many architecture details are vendor-specific and may require platform documentation or observability access.

## Examples

### Replica Lag

An API writes to the primary and a reporting query reads from a replica. The report temporarily misses the new row. QA must determine whether this delay is within the documented consistency model rather than immediately classifying it as persistence failure.

### Connection Routing

Two test tools use different connection endpoints. One reaches a read-only replica and cannot perform a mutation. The observed permission behavior is architectural, not necessarily a SQL defect.

### Failover

During a controlled failover, in-flight transactions may abort and clients may need to reconnect. QA validates behavior against the approved recovery and retry design instead of assuming zero interruption.

## Best Practices

- Document which endpoint or node test queries reach.
- Separate logical schema understanding from physical deployment assumptions.
- Confirm read/write routing and consistency guarantees.
- Include topology in concurrency, failover, and performance investigations.
- Use least-privilege credentials appropriate to the test purpose.
- Correlate application, database, and infrastructure timestamps when diagnosing distributed behavior.

## Related Knowledge

- `Database-Fundamentals.md`
- `Database-Objects.md`
- `Transactions.md`
- `Replication.md`
- `Partitioning.md`
- `Sharding.md`
- `Backup-and-Recovery.md`
- `Performance-Monitoring.md`

## References

- Database-system architecture literature.
- Target DBMS architecture documentation.
- Target platform documentation for deployment and consistency guarantees.