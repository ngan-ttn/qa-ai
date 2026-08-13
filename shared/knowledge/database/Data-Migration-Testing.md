# Data Migration Testing

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview
Data migration testing validates movement or transformation of data between schemas, systems, versions, or storage models.

## Purpose
Ensure migrated data is complete, accurate, transformed correctly, referentially valid, and operationally usable.

## Core Concepts
### Source-to-Target Mapping
Defines how fields and records transform.
### Reconciliation
Compares counts, keys, totals, and representative details.
### Cutover and Recovery
Migration must account for failure, restart, rollback, or restore according to the approved plan.

## How It Works
QA baselines source data, executes migration in a controlled environment, validates target schema/data, tests transformed business behavior, and reconciles discrepancies.

## When to Use
Use for upgrades, platform moves, schema redesigns, mergers, imports, and historical backfills.

## When Not to Use
Do not rely only on row counts when transformations or filtering occur.

## Advantages
Migration testing reduces corruption, omission, duplication, and compatibility risk.

## Limitations
Production-scale volume, sensitive data, and cutover timing may be difficult to reproduce exactly.

## Examples
A legacy status code may map to a new enum; QA validates every supported mapping plus unmapped-value handling.

## Best Practices
- Freeze mapping rules before reconciliation.
- Test nulls, duplicates, boundaries, and rejected records.
- Reconcile at multiple levels.
- Validate restart/idempotency when migration is rerunnable.
- Protect sensitive source data.

## Related Knowledge
- `Data-Validation.md`
- `Database-Lifecycle.md`
- `Backup-and-Recovery.md`

## References
- Approved migration specification and runbook.
- Target DBMS migration documentation.