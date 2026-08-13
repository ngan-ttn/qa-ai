# Constraints

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

A **database constraint** is a rule enforced by the DBMS to restrict allowed table states. Common constraints include primary key, foreign key, unique, check, and not-null constraints.

## Purpose

Constraint knowledge helps QA separate structural integrity enforced by the database from validation performed only by applications or services.

## Core Concepts

### NOT NULL
Requires a column to contain a non-null value.

### UNIQUE
Prevents duplicate values or value combinations under DBMS-specific null semantics.

### PRIMARY KEY
Defines the principal unique row identifier.

### FOREIGN KEY
Requires valid references to an allowed parent key.

### CHECK
Evaluates a predicate over row values according to product semantics.

### Deferrable / Timing Behavior
Some DBMSs can defer certain constraint checks until transaction commit; others check immediately.

## How It Works

During data modification, the DBMS evaluates applicable constraints. A violating statement or transaction is rejected according to constraint timing and engine behavior.

## When to Use

Use constraints for negative data tests, schema review, migration validation, duplicate prevention, referential checks, and defect isolation.

## When Not to Use

Do not assume every business rule should or can be a database constraint. Cross-service, temporal, authorization, and workflow rules often live elsewhere.

## Advantages

Constraints provide centralized protection against invalid structural state regardless of which authorized application writes the data.

## Limitations

Constraints may be absent, disabled, deferred, or insufficient for business semantics. Product differences in nulls, expressions, and deferral matter.

## Examples

### Unique Constraint
A duplicate external reference is rejected even if two concurrent requests reach the database at nearly the same time.

### Check Constraint
A quantity column may be constrained to non-negative values; QA still verifies whether zero is allowed by the business rule.

### Foreign Key
A child row cannot reference a missing parent while the constraint is active.

## Best Practices

- Inspect actual constraint definitions before deriving expectations.
- Test boundary, null, duplicate, and reference violations.
- Validate application error handling when the DB rejects a write.
- Do not duplicate business-rule assumptions into database expectations.
- Include constraint changes in regression and migration review.

## Related Knowledge

- `Primary-Keys.md`
- `Foreign-Keys.md`
- `Columns.md`
- `Transactions.md`
- `Data-Validation.md`

## References

- ISO/IEC 9075, integrity constraints.
- Target DBMS constraint documentation.