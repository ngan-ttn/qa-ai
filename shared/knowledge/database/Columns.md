# Columns

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview
A column defines a named attribute of a relational table, including its data type and optional integrity rules.

## Purpose
Support precise validation of stored fields and schema-level requirements.

## Core Concepts
### Data Type
Controls the domain of representable values.
### Nullability
Determines whether absence represented by `NULL` is allowed.
### Default and Generated Values
Values may be supplied automatically by the database.

## How It Works
Each row contains a value or permitted null state for each column; the DBMS validates assignments against column definitions.

## When to Use
Use for field mapping, boundary validation, migrations, defaults, and data-quality checks.

## When Not to Use
Do not infer business validation solely from a database type; application rules may be stricter.

## Advantages
Column definitions provide enforceable structural contracts.

## Limitations
Types and limits vary across DBMSs, and semantic meaning is not fully captured by type alone.

## Examples
A quantity column may be integer and non-null, while a separate check constraint may require it to be positive.

## Best Practices
- Verify type, length/precision, nullability, default, and collation where relevant.
- Distinguish `NULL`, empty string, and zero.
- Check migration effects on existing values.

## Related Knowledge
- `Tables.md`
- `Constraints.md`
- `Data-Validation.md`

## References
- ISO/IEC 9075, SQL.
- Target DBMS data-type documentation.