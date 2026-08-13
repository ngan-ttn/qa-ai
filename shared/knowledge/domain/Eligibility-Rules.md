# Eligibility Rules

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

An **eligibility rule** determines whether a person, entity, transaction, product, or request qualifies for an action, benefit, process, or outcome under defined conditions.

## Purpose

Help QA model qualification logic, temporal scope, evidence, precedence, and re-evaluation behavior.

## Core Concepts

### Subject
The object being evaluated, such as customer, account, order, claim, or request.

### Criteria
Facts that must be satisfied or avoided.

### Required vs Optional Criteria
Some conditions are mandatory while others contribute to scoring or alternate pathways.

### Disqualifier
A condition that makes the subject ineligible even when other criteria pass.

### Effective Time
Eligibility can depend on status or facts at application time, decision time, transaction time, or another defined anchor.

### Evidence
Source data or documents used to prove eligibility.

### Re-evaluation
Eligibility may need to be checked again when data changes or before a later business step.

### Override / Exception
Authorized exceptions must be explicit and auditable.

## How It Works

Facts about the subject are evaluated against applicable criteria, disqualifiers, effective dates, and precedence. The output can be eligible, ineligible, pending evidence, or another project-defined state.

## When to Use

Use for promotions, benefits, account actions, permits, product access, approvals, membership, claims, and regulated processes.

## When Not to Use

Do not assume eligibility is permanent after one successful evaluation. Do not invent criteria from industry expectations.

## Advantages

Eligibility modeling supports clear positive, negative, boundary, stale-data, and exception tests.

## Limitations

Eligibility may depend on external sources, delayed data, manual evidence, or changing policies.

## Examples

A promotion requires active membership on transaction date, eligible product category, minimum amount, and no excluded payment method. QA tests each criterion, combinations, and exact effective-time boundary.

A permit action may be allowed only while the permit remains approved and within approved period; later state change may require re-evaluation.

## Best Practices

- Define subject, criteria, disqualifiers, and outcome explicitly.
- Identify authoritative data source for each criterion.
- Clarify the time at which eligibility is evaluated.
- Test stale and changed facts between evaluation and execution.
- Cover missing evidence and pending states.
- Verify override authorization and audit trail.
- Use decision tables for multi-condition eligibility.

## Related Knowledge

- `Decision-Rules.md`
- `Validation-Rules.md`
- `Rule-Exceptions.md`
- `Business-Context.md`

## References

- Business-rules and eligibility-policy literature.
- Approved eligibility requirements.
