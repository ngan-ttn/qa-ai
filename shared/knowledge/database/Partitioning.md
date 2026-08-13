# Partitioning

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Partitioning** divides a large logical dataset into smaller physical or logical segments according to a partition key or rule while preserving a unified access model. Common strategies include range, list, hash, and composite partitioning.

## Purpose

This article helps QA reason about data placement, partition pruning, retention, migration, boundary conditions, and performance behavior without confusing partitioning with sharding.

## Core Concepts

### Partition Key
The column or expression that determines where a row belongs.

### Range Partitioning
Rows are assigned based on ranges such as dates or numeric intervals.

### List Partitioning
Rows are assigned from explicit value groups.

### Hash Partitioning
A hash function distributes rows across partitions.

### Partition Pruning
The optimizer can skip irrelevant partitions when predicates align with partition rules.

### Local / Global Structures
Indexes and constraints can be partition-local or span the logical object depending on DBMS capability.

## How It Works

```text
Incoming row
    ↓
Evaluate partition rule
    ↓
Partition A / B / C
```

Queries that filter on compatible partition keys may touch only selected partitions. Queries without useful predicates may still scan many or all partitions.

## When to Use

Use partitioning knowledge for very large tables, time-based retention, bulk load, archival, query-performance analysis, and partition-boundary testing.

## When Not to Use

Do not assume partitioning distributes data across separate servers; that is commonly associated with sharding or distributed architecture. Do not assume partitioning always improves performance.

## Advantages

Partitioning can improve manageability, pruning, maintenance, data lifecycle operations, and some large-scale query patterns.

## Limitations

Poor partition keys create skew or excessive partition scans. Constraints, unique keys, indexes, and migrations can become more complex.

## Examples

### Date Range
Transactions are partitioned monthly. QA tests records exactly at month boundaries to ensure they land in the correct partition.

### Retention
An old partition is detached or dropped as part of approved retention processing. QA verifies only eligible data is affected.

### No Pruning
A query filters only on a non-partitioned attribute and scans many partitions, causing unexpected latency.

## Best Practices

- Test partition-key boundaries explicitly.
- Confirm placement rules from the actual schema.
- Verify pruning with execution evidence rather than assumption.
- Include partition maintenance in migration and recovery testing.
- Monitor skew and uneven data growth.
- Distinguish partitioning from sharding and replication.

## Related Knowledge

- `Database-Architecture.md`
- `Sharding.md`
- `Indexes.md`
- `Query-Optimization.md`
- `Data-Migration-Testing.md`

## References

- Target DBMS partitioning documentation.
- Database physical-design literature.