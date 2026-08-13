# Data Migration Testing

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Data migration testing** validates movement or transformation of data between schemas, databases, versions, platforms, or storage models. It covers completeness, accuracy, transformation rules, relationships, restart behavior, compatibility, and post-migration usability.

## Purpose

This article gives QA a comprehensive model for validating high-risk data changes where defects can be silent, large-scale, or difficult to reverse.

## Core Concepts

### Source and Target
The migration has defined source populations and target representations. Both must be identified precisely.

### Mapping
Each source field/entity is mapped to a target field/entity or intentionally excluded according to approved rules.

### Transformation
Values can be normalized, converted, split, merged, defaulted, recalculated, or remapped.

### Reconciliation
Counts, keys, sums, hashes, or other independent checks compare source and target coverage.

### Reject / Error Handling
Invalid or unmappable records need defined handling, reporting, retry, and remediation.

### Idempotency / Restartability
A migration may need safe restart after interruption without duplicating or corrupting already processed data.

### Cutover and Compatibility
Application versions, writes during migration, dual-run periods, and rollback or roll-forward strategy affect correctness.

## How It Works

```text
Profile source data
      ↓
Apply mapping / transformation
      ↓
Load target
      ↓
Validate constraints and relationships
      ↓
Reconcile populations and values
      ↓
Application-level verification
```

Migration quality should be assessed using independent expected results rather than trusting the migration tool's success message alone.

## When to Use

Use migration testing for schema upgrades, platform changes, system consolidation, legacy replacement, data backfill, tenant movement, warehouse loads, and large reference/master-data changes.

## When Not to Use

Do not run destructive or irreversible migrations on shared or production data for exploratory testing. Do not treat equal row counts as sufficient proof of correctness when transformations or filtering exist.

## Advantages

Migration testing detects missing, duplicated, truncated, mis-mapped, corrupted, or incorrectly transformed data before business use.

## Limitations

Large datasets make full row-by-row comparison expensive. Historical data can already contain defects, and source/target models may intentionally differ.

## Examples

### Type Conversion
A text amount becomes decimal. QA identifies invalid legacy strings, precision/rounding rules, rejected rows, and target totals.

### Restart
The migration stops after 60%. On restart, already migrated rows must not be duplicated if restartability is required.

### Relationship Migration
Parent and child tables are migrated separately. QA checks key remapping and confirms no target orphans remain.

### Cutover
Writes continue briefly during migration. QA validates the approved synchronization or freeze strategy so late source changes are not lost.

## Best Practices

- Profile source quality before defining expected results.
- Build explicit source-to-target mapping coverage.
- Validate counts, keys, relationships, values, aggregates, and rejected records.
- Test boundaries, nulls, encoding, dates, precision, and large values.
- Use checksums or sampling only as part of a broader evidence strategy.
- Test restart, retry, rollback/roll-forward, and cutover paths.
- Compare application behavior after migration, not only database contents.
- Preserve audit evidence while protecting sensitive data.

## Related Knowledge

- `Data-Validation.md`
- `Database-Lifecycle.md`
- `Transactions.md`
- `Constraints.md`
- `Backup-and-Recovery.md`
- `Data-Warehousing.md`

## References

- Target migration design and mapping specification.
- Source and target DBMS documentation.
- Organization migration and recovery procedures.