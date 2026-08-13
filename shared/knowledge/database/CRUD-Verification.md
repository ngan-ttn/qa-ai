# CRUD Verification

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**CRUD verification** checks the persistence effects of create, read, update, and delete operations. It connects observable application actions to expected database state and helps detect incorrect mappings, unintended updates, duplicate rows, and missing side effects.

## Purpose

This article gives QA a repeatable model for validating data-backed functional behavior without assuming that application CRUD maps directly to physical insert/select/update/delete statements.

## Core Concepts

### Create
Expected records, defaults, generated identifiers, relationships, and initial states are persisted.

### Read
Returned data reflects the correct authorized and current state from the intended data source.

### Update
Only intended records and fields change; immutable fields and unrelated records remain unchanged.

### Delete
Deletion can be physical, soft, cascaded, archived, status-based, or prohibited. The requirement and data model determine the expected behavior.

### Side Effects
CRUD actions can trigger audit rows, history, events, derived data, or child changes.

### Scope
An operation's target population must be verified using stable identifiers and affected-row evidence where possible.

## How It Works

```text
Known pre-state
    ↓
Execute through intended interface
    ↓
Observe response/result
    ↓
Query target + related state
    ↓
Compare expected changes and invariants
```

Direct database mutation should not replace the application action when the objective is to test the application path.

## When to Use

Use CRUD verification for forms, APIs, admin tools, imports, workflows, master data, profile changes, and regression of persistence behavior.

## When Not to Use

Do not assume every create inserts one row, every update changes one table, or every delete removes data physically. Do not tightly couple high-level tests to internal schema when that schema is intentionally opaque and unnecessary for the objective.

## Advantages

CRUD checks expose mapping and persistence defects that can remain hidden behind successful UI or API responses.

## Limitations

Asynchronous writes, caches, replicas, triggers, event processing, and denormalized read models can delay or relocate observable state.

## Examples

### Create
Create one record through the API. Verify one expected primary record, correct generated key, required child rows, and no duplicate creation.

### Update
Edit one allowed field. Compare before and after state and verify immutable identifiers, unrelated fields, and unrelated rows did not change.

### Delete
Delete a record whose design uses soft deletion. Verify the deletion marker/status, expected visibility behavior, and related-data handling rather than expecting row absence.

## Best Practices

- Capture pre-state and post-state for critical updates.
- Identify records using stable keys.
- Verify intended changes and unintended side effects.
- Include invalid, duplicate, concurrent, and boundary paths where relevant.
- Account for triggers and asynchronous downstream effects.
- Confirm deletion semantics explicitly.
- Keep DB verification read-only unless mutation is part of controlled setup.

## Related Knowledge

- `Data-Validation.md`
- `Transactions.md`
- `Trigger-Testing.md`
- `Constraints.md`
- `Rows.md`

## References

- Project persistence and API/UI contracts.
- Target DBMS documentation.