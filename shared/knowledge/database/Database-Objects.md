# Database Objects

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Database objects** are named structures managed by a DBMS to store data, expose derived data, enforce rules, execute logic, or support access and performance. Common relational objects include tables, views, indexes, sequences, constraints, procedures, functions, triggers, schemas, and materialized structures.

## Purpose

This article gives QA a map of the object types that may influence observable application behavior. It helps prevent over-focusing on tables when defects can originate from views, triggers, procedures, sequences, indexes, or metadata configuration.

## Core Concepts

### Tables

Tables store rows under a defined column structure and are the primary persistence object in many relational systems.

### Views

Views expose the result of a query as a reusable logical object. Some systems also support materialized views that persist results and refresh on a schedule or event.

### Indexes

Indexes are auxiliary structures that improve access paths and sometimes enforce uniqueness. They do not define business truth by themselves.

### Constraints

Primary keys, foreign keys, unique constraints, checks, and nullability rules enforce structural integrity.

### Sequences / Identity Generators

These generate identifiers. Gaps can be normal due to rollback, caching, allocation strategies, or concurrent use.

### Procedures and Functions

Stored routines execute database-side logic. They may validate input, transform data, perform transactions, or return result sets.

### Triggers

Triggers execute automatically in response to configured data or schema events. They can create side effects that are not obvious from the original SQL statement.

### Schemas / Namespaces

Schemas organize objects and can affect resolution and permissions. The same object name may exist in multiple schemas.

## How It Works

A user operation may involve several objects:

```text
INSERT into table
      ↓
Constraint checks
      ↓
Sequence / identity allocation
      ↓
Trigger execution
      ↓
Index maintenance
      ↓
Transaction commit
      ↓
View / report later reads resulting state
```

This means a defect seen in a table can originate from another object in the path.

## When to Use

Use this knowledge when reviewing schemas, tracing side effects, validating stored routines, investigating unexpected data changes, checking permissions, or explaining why application-visible results differ from direct table contents.

## When Not to Use

Do not assume every DBMS supports the same object types or semantics. Do not modify production objects or disable triggers/constraints to simplify testing unless explicitly authorized.

## Advantages

Understanding database objects improves traceability and helps QA select the correct validation point. It also makes migration and regression review more complete because schema changes often affect multiple object types.

## Limitations

Object definitions can be complex, generated, encrypted, or managed by frameworks. Some application behavior may reside outside the database entirely. Naming conventions alone do not prove an object's responsibility.

## Examples

### Trigger Side Effect

Updating an order row automatically inserts an audit record through a trigger. A test that checks only the updated row misses part of the intended persistence behavior.

### View Logic

A report reads from a view that excludes soft-deleted rows. The base table still contains the row, but the report correctly omits it according to the view definition.

### Sequence Gap

An insert obtains identifier `101` but rolls back. The next successful row receives `102`. QA should not assume sequential identifiers must be gap-free unless that is a business requirement.

## Best Practices

- Identify all objects involved in a critical data path.
- Review object definitions rather than inferring behavior from names.
- Distinguish logical objects from persisted storage.
- Include triggers, routines, and views in migration/regression analysis.
- Treat generated identifier gaps as implementation behavior unless requirements state otherwise.
- Verify object permissions with least privilege.

## Related Knowledge

- `Tables.md`
- `Views.md`
- `Indexes.md`
- `Constraints.md`
- `Stored-Procedure-Testing.md`
- `Trigger-Testing.md`
- `Database-Architecture.md`

## References

- ISO/IEC 9075, SQL object concepts.
- Target DBMS documentation for supported objects and semantics.