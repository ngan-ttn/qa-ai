# Reference Data

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Reference data** is a controlled set of values used to classify, constrain, or interpret other business data, such as country codes, status types, categories, reason codes, currencies, or business classifications.

## Purpose

Help QA validate allowed values, meaning, lifecycle, compatibility, localization, and propagation of controlled code sets.

## Core Concepts

### Code and Label
A stable code may have one or more display labels. Labels can change without changing identity.

### Allowed Set
The valid value population can be fixed, configurable, or effective-dated.

### Classification
Reference values categorize or qualify entities and transactions.

### Mapping
Different systems may use different code sets requiring explicit translation.

### Effective Dating
Values can become active, inactive, or replaced over time.

### Localization
Display labels can vary by language while canonical code remains stable.

### Unknown / Other
Some domains define explicit fallback values; they should not be invented generically.

## How It Works

Reference data is maintained by an authoritative source and consumed by validations, dropdowns, integrations, calculations, and reporting. Changes can affect many dependent features.

## When to Use

Use for status dictionaries, reason codes, geographic codes, product classifications, currency lists, and controlled business enumerations.

## When Not to Use

Do not assume UI dropdown options are the complete authoritative code set. Do not hard-code lists in tests when the product is intentionally configurable unless the expected snapshot is controlled.

## Advantages

Reference-data analysis improves validation and mapping coverage while reducing inconsistent classification across systems.

## Limitations

Code sets evolve; external standards and partner mappings can differ in version or timing.

## Examples

A `Cancellation Reason` code may be stored as `C01` while UI displays localized text. QA verifies code mapping and behavior when a reason becomes inactive for new transactions but remains visible historically.

Two partners may use different country codes. Integration mapping must be explicit rather than assuming label equality.

## Best Practices

- Identify authoritative code and display label separately.
- Test active, inactive, unknown, and deprecated values where applicable.
- Verify effective-date behavior.
- Validate cross-system mappings.
- Include localization and sorting only when requirements define them.
- Assess regression impact of reference-data changes.
- Preserve historical readability for old values.

## Related Knowledge

- `Master-Data.md`
- `Business-Entity.md`
- `Validation-Rules.md`
- `Domain-Terminology.md`

## References

- Data-governance and reference-data management literature.
- Approved code-set specifications.
