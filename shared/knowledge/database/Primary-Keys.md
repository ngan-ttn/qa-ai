# Primary Keys

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

A **primary key** is the selected key used to uniquely identify each row in a relational table. It may consist of one column or a combination of columns and is normally unique and non-null.

## Purpose

Primary-key knowledge helps QA identify records reliably, validate duplicate prevention, trace relationships, and avoid using unstable descriptive fields as row identifiers.

## Core Concepts

### Candidate Key
A candidate key is a minimal set of attributes capable of uniquely identifying a row.

### Primary Key
One candidate key is designated as the table's primary key.

### Composite Key
A primary key can contain multiple columns when uniqueness depends on a combination.

### Surrogate Key
A generated technical identifier can serve as the primary key even when a separate business key exists.

### Business Key
A domain-meaningful identifier may be unique but should not be assumed to be the database primary key.

## How It Works

The DBMS enforces uniqueness and non-null semantics for the primary key according to its implementation. Foreign keys in other tables may reference it, making primary-key changes potentially high impact.

## When to Use

Use primary-key knowledge for row identification, joins, CRUD checks, migration mapping, duplicate analysis, foreign-key validation, and regression impact analysis.

## When Not to Use

Do not assume generated keys are gap-free or sequential. Do not expose internal surrogate identifiers as business identifiers unless the contract explicitly uses them.

## Advantages

A stable primary key provides deterministic record identity and supports referential integrity and efficient access patterns.

## Limitations

The primary key does not encode all business uniqueness. A table can require additional unique constraints, and poorly chosen mutable keys can complicate relationships.

## Examples

### Surrogate Key
`customer_id` is a generated numeric primary key while `email` has a separate unique rule. QA validates the two constraints independently.

### Composite Key
An enrollment table may use `(student_id, course_id)` as a composite key to prevent duplicate enrollment pairs.

### Rollback Gap
An identity value allocated inside a rolled-back transaction can create a gap. This is not automatically a defect.

## Best Practices

- Use the actual key definition for record lookup.
- Validate duplicate insert behavior where relevant.
- Separate primary-key uniqueness from business uniqueness.
- Treat key mutation as high-impact when foreign references exist.
- Avoid assumptions about key ordering or continuity.

## Related Knowledge

- `Foreign-Keys.md`
- `Constraints.md`
- `Rows.md`
- `Relationships.md`
- `Data-Migration-Testing.md`

## References

- Relational model literature.
- ISO/IEC 9075, SQL key constraints.