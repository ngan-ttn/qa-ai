# Sharding

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Sharding** distributes portions of a logical dataset across multiple database nodes or groups, typically according to a shard key. Unlike local table partitioning, sharding commonly places data on separate infrastructure and introduces routing and cross-shard coordination concerns.

## Purpose

This article helps QA reason about shard routing, data distribution, hot spots, cross-shard operations, resharding, tenant isolation, and failure scope.

## Core Concepts

### Shard Key
The attribute or function used to determine the shard responsible for a record.

### Routing
Applications, proxies, or database middleware route operations to one or more shards.

### Horizontal Distribution
Rows are divided across shards rather than every node storing the entire dataset.

### Cross-Shard Query
Queries spanning multiple shards require fan-out, aggregation, or distributed execution and can have different performance and consistency properties.

### Rebalancing / Resharding
Data may move when capacity changes or shard strategy evolves.

### Hot Shard
Uneven key distribution can overload one shard while others remain lightly used.

### Failure Domain
A shard failure may affect only part of the logical dataset, depending on replication and routing design.

## How It Works

```text
Request with shard key
        ↓
Router / shard map
   ↙      ↓      ↘
Shard A  Shard B  Shard C
```

Cross-shard operations may contact multiple nodes and then merge results. Distributed transactions are not automatically available or desirable.

## When to Use

Use sharding knowledge for high-scale data systems, tenant distribution, geographically partitioned data, routing defects, uneven capacity, resharding, and cross-shard reporting.

## When Not to Use

Do not use “partition” and “shard” interchangeably without confirming architecture. Do not assume globally unique constraints or transactions behave like a single-node relational database.

## Advantages

Sharding can scale storage and throughput horizontally and isolate some failure/capacity domains.

## Limitations

It increases routing, operational, migration, consistency, cross-shard query, and uniqueness complexity. Poor shard keys can create severe skew.

## Examples

### Tenant Routing
Tenant ID determines the shard. QA verifies requests for one tenant never resolve to another tenant's shard and that cross-tenant administrative queries behave according to design.

### Hot Shard
A small number of high-volume keys all map to one shard, creating latency despite spare capacity elsewhere.

### Resharding
Records move from shard A to B. QA validates no missing/duplicate records, correct routing during transition, and behavior for in-flight operations.

## Best Practices

- Identify the real shard key and routing layer.
- Test boundary and invalid-routing cases.
- Monitor distribution and hot-shard risk.
- Validate cross-shard aggregation separately from single-shard queries.
- Include resharding and failover in high-risk architecture tests.
- Do not assume global constraints exist unless explicitly implemented.
- Protect tenant/data isolation during routing tests.

## Related Knowledge

- `Partitioning.md`
- `Database-Architecture.md`
- `Replication.md`
- `Data-Migration-Testing.md`
- `Performance-Monitoring.md`

## References

- Distributed database architecture literature.
- Target platform sharding documentation.