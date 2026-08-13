# Sharding

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview
Sharding distributes different subsets of data across separate database nodes or instances according to a routing rule.

## Purpose
Explain cross-shard correctness, routing, skew, and operational risks relevant to QA.

## Core Concepts
### Shard Key
Determines data placement.
### Routing
Applications or middleware direct operations to the appropriate shard.
### Rebalancing
Data may move as capacity or topology changes.

## How It Works
A routing layer maps a record or query to one or more shards; cross-shard operations may require additional coordination.

## When to Use
Use for horizontally scaled datasets that exceed or intentionally distribute single-node capacity.

## When Not to Use
Do not confuse sharding with table partitioning inside one database system.

## Advantages
Sharding can increase storage and write scalability and isolate workloads.

## Limitations
Cross-shard joins/transactions, skew, rebalancing, and routing failures add complexity.

## Examples
Tenant-based sharding must keep each tenant's data on the intended shard and prevent cross-tenant leakage.

## Best Practices
- Test shard-key boundaries and routing.
- Validate rebalancing and failure behavior.
- Include cross-shard operations where supported.
- Monitor distribution skew.

## Related Knowledge
- `Partitioning.md`
- `Database-Architecture.md`
- `Replication.md`

## References
- Architecture and DBMS-specific sharding documentation.