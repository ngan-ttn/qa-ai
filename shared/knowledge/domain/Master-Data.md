# Master Data

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Master data** represents relatively stable, shared business entities used across processes, such as customers, products, suppliers, locations, or organizational units.

## Purpose

Help QA reason about authoritative ownership, identity, synchronization, lifecycle, and downstream impact of shared business data.

## Core Concepts

### Source of Truth
The authoritative owner for a master concept.
### Identity and Deduplication
Records must represent intended real-world/business identities.
### Distribution
Master data may be replicated to consuming systems.
### Governance
Creation and changes often require controlled rules and ownership.

## How It Works

Master data is created or maintained in an authoritative process and distributed or referenced by operational transactions.

## When to Use

Use for product catalogs, customer masters, reference ownership, supplier/location data, and cross-system synchronization.

## When Not to Use

Do not classify all long-lived data as master data; business role and reuse matter.

## Advantages

Clear master-data ownership reduces inconsistency across systems.

## Limitations

Synchronization delay, duplicate identities, and conflicting sources can create complex defects.

## Examples

A product master supplies code, name, status, and category to ordering and inventory processes; a stale consumer may reject a newly activated product.

## Best Practices

- Identify authoritative source.
- Test duplicate and merge behavior.
- Verify propagation and effective dates.
- Cover inactive/retired master records.
- Avoid inventing synchronization SLAs.

## Related Knowledge

- `Reference-Data.md`
- `Transaction-Data.md`
- `Business-Entity.md`

## References

- Master data management literature.