# Database Lifecycle

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview
The database lifecycle covers data requirements, modeling, implementation, migration, operation, evolution, backup, recovery, and retirement.

## Purpose
Show where QA can prevent and detect data defects throughout database evolution.

## Core Concepts
### Design
Business data and relationships are modeled.
### Build and Migration
Schemas and transformations are deployed.
### Operation
Data is created, changed, queried, monitored, backed up, and recovered.
### Evolution
Schemas and data change while compatibility and integrity must be preserved.

## How It Works
Lifecycle stages iterate as requirements change. Each schema or migration change can introduce data, compatibility, performance, and recovery risks.

## When to Use
Use for release planning, migration testing, regression analysis, and operational readiness.

## When Not to Use
Do not treat this conceptual lifecycle as a mandatory delivery methodology.

## Advantages
Lifecycle thinking encourages early validation and explicit migration/recovery coverage.

## Limitations
Ownership, gates, retention, and deployment practices are organization-specific.

## Examples
Adding a mandatory column may require a default or backfill strategy for existing rows before enforcing the constraint.

## Best Practices
- Review schema changes before deployment.
- Test forward migration and recovery paths.
- Protect production data and preserve auditability.
- Include compatibility impact in regression scope.

## Related Knowledge
- `Data-Migration-Testing.md`
- `Backup-and-Recovery.md`
- `Database-Test-Strategy.md`

## References
- Target DBMS migration and recovery documentation.
- Organization-specific data governance standards.