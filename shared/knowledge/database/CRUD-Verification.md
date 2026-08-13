# CRUD Verification

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview
CRUD verification checks persistence effects of create, read, update, and delete operations.

## Purpose
Connect user/API actions to expected database state while detecting unintended side effects.

## Core Concepts
### Create
Expected records and defaults are persisted.
### Read
Returned data reflects authorized, valid stored state.
### Update
Only intended records and fields change.
### Delete
Deletion may be physical, soft, cascaded, or prohibited by design.

## How It Works
QA establishes a known state, performs the operation through the intended interface, then verifies affected records and relationships.

## When to Use
Use for data-backed functional features and regression checks.

## When Not to Use
Do not assume every delete physically removes a row.

## Advantages
CRUD checks expose mapping, persistence, and scope defects hidden by UI-only testing.

## Limitations
Direct state checks can miss asynchronous side effects if timing is not considered.

## Examples
Editing one profile should update intended fields while immutable identifiers and unrelated profiles remain unchanged.

## Best Practices
- Verify before/after state.
- Identify records with stable keys.
- Check audit fields only when part of the contract.
- Include duplicate and invalid-input paths.

## Related Knowledge
- `Data-Validation.md`
- `Transactions.md`
- `Trigger-Testing.md`

## References
- Project persistence contract.
- Target DBMS documentation.