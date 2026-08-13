# Data Definition Language

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Data Definition Language (DDL)** is a common term for SQL statements that create, alter, or remove database structures such as tables, columns, constraints, indexes, views, and schemas.

## Purpose

This article helps QA review schema changes, migration scripts, compatibility risk, and structural side effects without assuming identical DDL behavior across DBMS products.

## Core Concepts

### CREATE
Creates a database object such as a table, view, index, or schema.

### ALTER
Changes an existing object's definition, for example adding a column or constraint.

### DROP
Removes an object and can be destructive to dependent structures or data.

### Dependency
Views, routines, constraints, indexes, applications, and reports may depend on a changed object.

### Online vs Blocking Change
Some schema changes can be applied with limited disruption while others acquire locks or rebuild data. Behavior depends on product, version, data size, and options.

### Transactional DDL
Some DBMSs allow certain DDL to participate in transactions; others implicitly commit or have special rules.

## How It Works

DDL updates system metadata and may also transform physical storage. For example, adding a nullable metadata-only column can be cheap in one system, while changing a data type can scan or rewrite a large table.

## When to Use

Use DDL knowledge for database migrations, release review, schema-diff validation, rollback planning, compatibility analysis, and test environment setup.

## When Not to Use

Do not execute DDL in shared or production environments merely to test syntax. Do not assume a rollback can reverse every DDL operation or restore lost data.

## Advantages

DDL makes schema evolution explicit and versionable and provides concrete artifacts for review before deployment.

## Limitations

DDL semantics vary significantly by DBMS. Structural changes may be expensive, lock data, invalidate dependencies, or require data conversion.

## Examples

### Add Column
A new nullable column is added before application code starts writing it. QA validates compatibility with older application versions if coexistence is required.

### Type Change
Changing a string column to numeric can fail or transform historical values. QA profiles existing data before migration and verifies rejected/converted cases.

### Drop Object
Dropping a view may break reports even if application code no longer references it.

## Best Practices

- Review DDL together with migration order and application-version compatibility.
- Validate existing data before tightening constraints or changing types.
- Identify dependent views, routines, jobs, and integrations.
- Test on representative data volume where lock/rewrite risk matters.
- Define rollback or roll-forward strategy explicitly.
- Avoid irreversible destructive changes without verified backup/recovery plan.

## Related Knowledge

- `SQL-Overview.md`
- `Database-Objects.md`
- `Constraints.md`
- `Indexes.md`
- `Data-Migration-Testing.md`
- `Database-Lifecycle.md`

## References

- ISO/IEC 9075, SQL schema definition.
- Target DBMS DDL and migration documentation.