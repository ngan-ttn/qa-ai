# Constraints

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview
Constraints are declarative rules that restrict stored data to valid structural states.

## Purpose
Provide QA guidance for testing database-enforced integrity independently from application validation.

## Core Concepts
### NOT NULL
Requires a value.
### UNIQUE and PRIMARY KEY
Enforce uniqueness.
### FOREIGN KEY
Enforces eligible references.
### CHECK
Restricts values using a predicate where supported.

## How It Works
The DBMS evaluates applicable constraints during data changes and rejects operations that violate them.

## When to Use
Use for negative testing, integrity validation, schema review, and migrations.

## When Not to Use
Do not assume constraints encode every business rule.

## Advantages
Constraints protect integrity regardless of which application writes the data.

## Limitations
Complex cross-record or temporal business rules may require other mechanisms.

## Examples
A check constraint may prevent a negative quantity even if a client bypasses UI validation.

## Best Practices
- Test each constraint's valid and invalid boundaries.
- Verify constraint names/messages only when contractually relevant.
- Check existing data before adding stricter constraints.

## Related Knowledge
- `Primary-Keys.md`
- `Foreign-Keys.md`
- `Data-Validation.md`

## References
- ISO/IEC 9075, SQL.