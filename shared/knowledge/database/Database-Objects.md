# Database Objects

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview
Database objects are named structures managed by a DBMS, such as tables, views, indexes, constraints, sequences, procedures, and triggers.

## Purpose
Provide a map of common object types so QA can identify what should be inspected when database behavior changes.

## Core Concepts
### Data Objects
Tables and views expose stored or derived data.
### Integrity Objects
Keys and constraints enforce structural rules.
### Programmable Objects
Procedures, functions, and triggers execute database-side logic.
### Performance Objects
Indexes and partitions influence access paths.

## How It Works
DDL creates or changes objects. Dependencies between objects affect deployment, validation, and regression scope.

## When to Use
Use during schema review, migration testing, stored-logic testing, and regression analysis.

## When Not to Use
Do not assume every DBMS supports identical object types or semantics.

## Advantages
Object-level reasoning makes schema changes and their impacts easier to trace.

## Limitations
Names alone do not reveal behavior; definitions, permissions, dependencies, and engine semantics matter.

## Examples
Changing a table column may affect a view, index, procedure, API mapping, and report.

## Best Practices
- Review dependencies before changing or testing objects.
- Validate permissions and object definitions in the target environment.
- Prefer source-controlled migrations where available.

## Related Knowledge
- `Tables.md`
- `Views.md`
- `Indexes.md`
- `Stored-Procedure-Testing.md`
- `Trigger-Testing.md`

## References
- ISO/IEC 9075, SQL.
- Target DBMS object documentation.