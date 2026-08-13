# Rule Exceptions

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

A **rule exception** defines a controlled situation in which a normal business rule does not apply, is modified, or is overridden. Exceptions are part of the business model and require explicit scope and authority.

## Purpose

Help QA distinguish legitimate exceptions from defects, identify precedence, and validate authorization, evidence, and downstream effects.

## Core Concepts

### Base Rule
The normal rule that applies when no exception is active.

### Exception Condition
Specific facts that activate alternate behavior.

### Scope
The exception may be limited by actor, product, market, amount, period, or transaction type.

### Authority
Some exceptions require a role or approval to invoke.

### Precedence
The relationship between base rule, multiple exceptions, and overrides must be defined.

### Duration
An exception can be one-time, temporary, effective-dated, or persistent.

### Evidence / Reason
Overrides may require a reason, document, approval, or audit record.

## How It Works

```text
Base rule applies?
   ↓
Check exception condition
   ↓
Authorized + in scope?
   ↓
Apply alternate outcome
   ↓
Record evidence / effects
```

QA verifies that exceptions are narrow: they should modify only intended behavior and should not accidentally bypass unrelated controls.

## When to Use

Use for manual override, special customer handling, regulatory exemptions, approval bypasses, rework flows, recovery, and policy exceptions.

## When Not to Use

Do not label undocumented inconsistent behavior as an exception. Do not assume administrators can override every rule.

## Advantages

Explicit exception modeling prevents both over-restriction and unauthorized bypass.

## Limitations

Exceptions can accumulate and become difficult to govern. Overlapping exceptions can produce unclear precedence or hidden complexity.

## Examples

A record normally cannot be edited after allocation, but a defined exception permits adding new UPN coverage while existing UPNs and approval fields remain locked. QA verifies the exception does not reopen unrestricted editing.

A manager may waive one validation under approved policy but still cannot bypass compliance screening. Authorization scope must be precise.

## Best Practices

- Trace every exception to an authoritative source.
- Define triggering condition, scope, authority, and duration.
- Test base rule and exception side by side.
- Verify unrelated controls remain enforced.
- Check precedence between multiple exceptions.
- Require and validate audit evidence when applicable.
- Test exception expiry and stale sessions.

## Related Knowledge

- `Business-Rule-Fundamentals.md`
- `Validation-Rules.md`
- `Decision-Rules.md`
- `Process-Exceptions.md`
- `Audit-Trail.md`

## References

- Business-rules and policy-governance literature.
- Approved exception and override policy.
