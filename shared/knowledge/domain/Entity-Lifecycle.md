# Entity Lifecycle

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

An **entity lifecycle** describes how a business entity is created, activated, modified, suspended, closed, expired, archived, or otherwise evolves.

## Purpose

Help QA validate state-dependent entity behavior, historical integrity, and post-termination rules.

## Core Concepts

### Creation
Identity and initial valid state are established.
### Active Life
Permitted updates and relationships evolve.
### State Change
Business events alter availability or meaning.
### Termination
Closure, deletion, expiry, or deactivation.
### History
Prior states may need preservation for audit or business use.

## How It Works

Lifecycle transitions are governed by rules, actor permissions, time, and related process events.

## When to Use

Use for accounts, subscriptions, products, permits, orders, customers, and master records.

## When Not to Use

Do not assume deletion means physical removal or that closed entities can be recreated with the same identity.

## Advantages

Reveals stale-state, history, and reactivation defects.

## Limitations

Different systems may represent the same business lifecycle differently.

## Examples

A customer account may move from pending to active to suspended to closed; transaction permissions differ by state while history remains available.

## Best Practices

- Define state meanings and transition triggers.
- Test temporal boundaries.
- Verify historical and related data.
- Check reactivation/recreation rules explicitly.

## Related Knowledge

- `Business-Entity.md`
- `Process-Lifecycle.md`
- `Audit-Trail.md`
- `Data-Retention.md`

## References

- Domain lifecycle modeling literature.