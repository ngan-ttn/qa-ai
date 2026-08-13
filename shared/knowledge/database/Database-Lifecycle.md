# Database Lifecycle

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

The **database lifecycle** describes how a database solution moves from requirements and modeling through implementation, deployment, operation, evolution, migration, archival, and retirement. It is a conceptual lifecycle rather than a mandatory delivery methodology.

## Purpose

Lifecycle awareness helps QA participate before execution-only testing, identify migration and compatibility risk, and understand how database quality responsibilities change as schemas, data volumes, integrations, and operational requirements evolve.

## Core Concepts

### Requirements and Data Discovery

Teams identify business entities, relationships, data classifications, volume expectations, retention needs, consistency requirements, and integration boundaries.

### Modeling and Design

Logical models become physical schemas, keys, constraints, indexes, partitions, and access patterns. Design decisions should reflect authoritative requirements and expected workload.

### Implementation

DDL, migrations, routines, triggers, seed/reference data, and application mappings are developed and version-controlled according to project practices.

### Verification

QA validates schema compatibility, CRUD behavior, integrity, transactions, migration, performance-sensitive paths, and security-relevant data handling.

### Deployment

Database changes are applied through controlled migration or deployment processes. Order, rollback strategy, backward compatibility, and application-version coordination are important risks.

### Operation

Monitoring, backups, capacity, replication, maintenance, incident response, and data-quality feedback become primary sources of quality evidence.

### Evolution

Schemas and data models change as features evolve. Changes may require backfill, dual-read/write periods, compatibility windows, or data migration.

### Retirement

Obsolete objects, datasets, or entire databases are archived or removed according to approved retention, legal, security, and operational policies.

## How It Works

```text
Discover → Model → Implement → Verify → Deploy
   ↑                                 ↓
   └──── Feedback ← Operate ← Evolve
                         ↓
                    Archive / Retire
```

The lifecycle is iterative. Production incidents can lead to new constraints or indexes; domain changes can require migrations; security policy can alter retention or access.

## When to Use

Use lifecycle knowledge for schema-change review, migration planning, deployment readiness, rollback analysis, test environment refresh, archival, deprecation, and long-term data-quality planning.

## When Not to Use

Do not treat this lifecycle as a required sequence or approval process. Agile, continuous delivery, database-as-code, managed-service, and platform models can organize the same concerns differently.

## Advantages

Lifecycle thinking shifts database quality earlier, improves migration safety, encourages operational feedback, and makes retirement and retention considerations explicit rather than treating databases as static assets.

## Limitations

A generic lifecycle does not define ownership, release cadence, approval gates, backup schedules, retention duration, recovery objectives, or migration tooling. Those remain organization- and project-specific.

## Examples

### Additive Schema Change

A nullable column is introduced before application code begins using it. QA validates old and new application versions if coexistence is part of the rollout strategy.

### Data Backfill

A new derived field requires historical records to be populated. QA compares source and target populations, validates transformation rules, and checks restart/retry behavior of the backfill process.

### Retirement

An obsolete table is no longer read by supported applications. Removal still requires impact analysis for reports, integrations, jobs, audit obligations, and retention policy.

## Best Practices

- Include QA in schema and migration review before deployment.
- Version database changes and retain traceability to application changes.
- Plan backward/forward compatibility where multiple app versions can coexist.
- Test migration on representative data volumes and edge cases.
- Define rollback or roll-forward strategy explicitly.
- Use production incidents and data-quality findings to improve regression coverage.
- Treat archival and deletion as governed operations, not housekeeping assumptions.

## Related Knowledge

- `Database-Fundamentals.md`
- `Database-Architecture.md`
- `Data-Migration-Testing.md`
- `Backup-and-Recovery.md`
- `Performance-Monitoring.md`
- `../qa/Regression-Testing.md`
- `../qa/Continuous-Improvement.md`

## References

- Database change-management and migration practices.
- Target DBMS deployment and migration documentation.
- Organization retention, recovery, and release governance where applicable.