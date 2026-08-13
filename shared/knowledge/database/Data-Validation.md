# Data Validation

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview
Data validation verifies that stored and derived data matches approved rules, mappings, relationships, and expected state transitions.

## Purpose
Provide a systematic approach for backend assertions beyond simply checking that a row exists.

## Core Concepts
### Completeness
Required data is present.
### Accuracy
Values match expected source or calculation.
### Consistency
Related representations agree according to the contract.
### Integrity
Keys and constraints remain valid.

## How It Works
Expected data is derived from requirements and controlled inputs, then compared with database results using deterministic queries or reconciliation rules.

## When to Use
Use for persistence, calculations, integrations, reporting, migrations, and defect investigation.

## When Not to Use
Do not expose or copy sensitive production data unnecessarily.

## Advantages
Direct validation can isolate backend defects and detect hidden corruption.

## Limitations
A database snapshot may be temporarily stale in asynchronous/eventual-consistency workflows.

## Examples
After a refund, QA verifies the transaction record, status, amount, relationship to the original transaction, and expected balance effect.

## Best Practices
- Define authoritative source and timing.
- Validate nulls, duplicates, boundaries, and relationships.
- Reconcile counts and totals where appropriate.
- Avoid assuming eventual updates are immediate.

## Related Knowledge
- `CRUD-Verification.md`
- `Constraints.md`
- `Aggregation.md`
- `Data-Migration-Testing.md`

## References
- Project data contracts and schema documentation.
- ISO/IEC 9075, SQL.