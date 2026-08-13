# Data Validation

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Data validation** verifies that stored or transferred data is complete, accurate, consistent, correctly related, and aligned with authoritative requirements. Database validation can compare expected state to persisted state, reconcile populations, and detect anomalies hidden by UI-level testing.

## Purpose

This article gives QA a systematic approach to validating database data without conflating database structure with business truth.

## Core Concepts

### Completeness
Expected records and required fields are present, and no required population is missing.

### Accuracy
Stored values match authoritative inputs, calculations, transformations, or source data.

### Consistency
Related representations of the same fact agree where the design requires them to agree.

### Validity
Values satisfy schema and business rules applicable to the field or record.

### Uniqueness
Records are unique according to the actual business or technical key definition.

### Referential Integrity
Relationships point to valid referenced records where such integrity is required.

### Timeliness
Data freshness may matter for replicas, warehouses, reports, caches, and asynchronous flows.

## How It Works

A validation flow is:

```text
Authoritative expectation
       ↓
Identify keys and population
       ↓
Query actual data
       ↓
Compare value + relationship + count
       ↓
Investigate mismatches
```

Expected values should come from requirements, controlled input, independent calculations, or trusted source datasets rather than being reconstructed from the same implementation logic under test.

## When to Use

Use data validation for CRUD, imports, reports, migrations, reconciliation, audit data, transformations, integration, warehouse pipelines, and defect investigation.

## When Not to Use

Do not validate by merely comparing one derived system output against another derived from the same defective source. Do not expose sensitive data in screenshots or shared evidence unnecessarily.

## Advantages

Data validation can detect silent corruption, mapping errors, missing rows, duplicates, incorrect relationships, and transformation defects.

## Limitations

A database snapshot may be temporarily stale or incomplete under asynchronous systems. Queries can also be wrong, so validation logic itself must be reviewed and independently reasoned about.

## Examples

### Import Validation
For a 1,000-row import, QA verifies processed, successful, failed, and persisted populations reconcile according to documented handling rules.

### Field Mapping
An API field `approvedAt` is normalized to UTC in the database. QA compares equivalent instants rather than raw display strings.

### Duplicate Detection
Grouping by the true business key reveals duplicate active records while historical versions are excluded according to the data model.

## Best Practices

- Define the expected population before querying.
- Use stable keys and independent expected values.
- Validate counts, fields, relationships, and side effects together.
- Account for nulls, precision, timezone, soft delete, and history.
- Reconcile aggregates back to detail samples.
- Separate source-of-truth validation from replica or warehouse freshness.
- Keep validation SQL versioned and peer-reviewed for critical checks.
- Mask or omit sensitive values in test evidence.

## Related Knowledge

- `Database-Test-Strategy.md`
- `CRUD-Verification.md`
- `Joins.md`
- `Aggregation.md`
- `Constraints.md`
- `Data-Migration-Testing.md`

## References

- Data-quality and reconciliation practices.
- Target project data contract and schema documentation.