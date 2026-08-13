# Master Data

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Master data** is relatively stable, shared business data describing core entities used across processes, such as products, customers, suppliers, locations, organizational units, or devices.

## Purpose

Help QA reason about authority, synchronization, identity, lifecycle, quality, and downstream impact of shared business data.

## Core Concepts

### Shared Business Object
Master data is reused by multiple transactions or systems.

### System of Record
One source may be authoritative for a data set or attribute, but ownership can be distributed.

### Golden Record
Some architectures reconcile multiple sources into a preferred representation; this is a design choice, not a universal property.

### Reference Synchronization
Copies can be propagated to downstream systems with delay or transformation.

### Data Quality
Completeness, uniqueness, validity, consistency, and timeliness matter because defects propagate widely.

### Stewardship
Business or operational owners may approve or correct master data.

### Effective Dating
Attributes or relationships can change over time without rewriting history.

## How It Works

Master data is created or maintained in an authoritative process and then consumed by transactional or analytical systems. QA validates source ownership, propagation, and impact on dependent features.

## When to Use

Use for product masters, customer profiles, device catalogs, supplier/location data, code mappings, and shared configuration with business identity.

## When Not to Use

Do not classify every configuration value as master data. Do not assume one system is authoritative for all attributes without evidence.

## Advantages

Master-data awareness helps detect high-impact defects whose effects spread across many features and integrations.

## Limitations

Copies may be eventually consistent, historical values may be required, and duplicate/merge rules can be complex.

## Examples

A Product Master changes a device name. New screens may show the updated value while historical records retain prior snapshots depending on approved design.

A customer address update in CRM may propagate to another system asynchronously. QA distinguishes propagation delay from permanent synchronization failure.

## Best Practices

- Identify ownership per entity and critical attribute.
- Test duplicate, merge, and deactivation behavior.
- Verify downstream propagation and freshness expectations.
- Preserve historical semantics where required.
- Validate effective dates and reference integrity.
- Assess regression impact broadly for master-data changes.
- Protect sensitive master data in test environments.

## Related Knowledge

- `Business-Entity.md`
- `Reference-Data.md`
- `Transaction-Data.md`
- `Entity-Lifecycle.md`
- `../database/Data-Validation.md`

## References

- Master data management and data-governance literature.
- Approved system-of-record documentation.
