# Validation Rules

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

A **validation rule** determines whether data, an action, or a state is acceptable before a business operation proceeds. Validation can apply to syntax, completeness, relationship, state, permission, timing, or domain constraints.

## Purpose

Help QA distinguish validation types, ordering, scope, error behavior, and bypass risks while deriving precise positive and negative tests.

## Core Concepts

### Presence Validation
Required information must be provided when the rule applies.

### Format / Type Validation
Input must match an approved representation, type, precision, or structure.

### Range / Boundary Validation
Values must fall within allowed limits.

### Relationship Validation
Input must be consistent with related entities, states, or ownership.

### State Validation
An action is permitted only from eligible lifecycle states.

### Authorization-Dependent Validation
The same action can be valid for one role and invalid for another.

### Cross-Field Validation
Validity depends on combinations of fields rather than one field independently.

### Validation Timing
Rules can run on entry, save, submit, approval, import, or downstream processing. Timing affects observable behavior.

## How It Works

```text
Input / action
   ↓
Applicable validation set
   ↓
field + relationship + state + role checks
   ↓
valid → continue
invalid → block / reject / flag according to contract
```

QA should verify not only that invalid input is rejected but also that no unintended partial side effects occur and that alternate entry points apply equivalent rules when required.

## When to Use

Use for forms, APIs, uploads, imports, state transitions, business operations, and integrations where invalid data or action must be controlled.

## When Not to Use

Do not treat client-side UI validation as proof of business validation. Do not assume all channels intentionally share identical error wording or timing.

## Advantages

Systematic validation testing catches data-quality, bypass, state, and boundary defects early.

## Limitations

Validation logic can be duplicated across layers and become inconsistent. Some rules require external data or asynchronous checks.

## Examples

A UPN must be selected from an approved product master, must not duplicate an existing UPN on the record, and may be editable only during a defined workflow state.

An amount can be syntactically numeric yet invalid because currency precision, account status, or transaction limit rules fail.

## Best Practices

- Classify validation by field, relationship, state, role, and timing.
- Test null, empty, malformed, min/max, just-inside, and just-outside boundaries.
- Verify cross-field combinations.
- Compare behavior across UI/API/import channels when equivalence is required.
- Confirm error handling and side-effect rollback.
- Test duplicate and stale-state submissions.
- Trace validation back to authoritative rule source.

## Related Knowledge

- `Business-Rule-Fundamentals.md`
- `Decision-Rules.md`
- `Rule-Exceptions.md`
- `Process-States.md`
- `../testing-techniques/Specification-Based/Boundary-Value-Analysis.md`

## References

- Business-analysis and validation-design literature.
- Approved input and workflow requirements.
