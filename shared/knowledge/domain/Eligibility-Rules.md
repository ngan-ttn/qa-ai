# Eligibility Rules

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Eligibility rules** determine whether an actor, entity, transaction, or request qualifies for a business action, benefit, product, or process.

## Purpose

Help QA test qualification decisions, boundary conditions, precedence, and changes in eligibility over time.

## Core Concepts

### Eligibility Criteria
Conditions that must be satisfied.
### Disqualifier
A condition that blocks qualification.
### Effective Period
Eligibility may depend on time.
### Segment or Tier
Different groups can have different criteria.
### Re-evaluation
Eligibility may change when facts change.

## How It Works

Current facts are evaluated against applicable criteria and exclusions to produce eligible, ineligible, or sometimes review-required outcomes.

## When to Use

Use for promotions, refunds, credit products, benefits, permissions, loyalty rewards, and regulated services.

## When Not to Use

Do not infer eligibility from UI availability alone.

## Advantages

Explicit eligibility logic supports strong boundary and combination testing.

## Limitations

Criteria can depend on external or delayed data.

## Examples

A reward may require active membership, sufficient points, eligible market, and non-expired campaign status.

## Best Practices

- Test each criterion independently.
- Cover just-inside/just-outside boundaries.
- Test conflicting qualifiers/disqualifiers.
- Verify re-evaluation after relevant state changes.

## Related Knowledge

- `Decision-Rules.md`
- `Rule-Exceptions.md`
- `Validation-Rules.md`

## References

- Business decision and policy literature.