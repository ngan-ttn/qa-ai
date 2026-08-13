# Reference Data

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Reference data** is controlled data used to classify, constrain, or interpret other business data, such as status codes, country codes, categories, or reason types.

## Purpose

Help QA validate allowed values, effective dates, mappings, localization, and downstream behavior driven by controlled lists.

## Core Concepts

### Code and Meaning
Machine-readable value maps to business meaning.
### Controlled Set
Allowed values are governed rather than freely entered.
### Effective Dating
Values can become valid or obsolete over time.
### Mapping
Different systems may use different codes for equivalent concepts.

## How It Works

Processes consume reference values to validate input, route behavior, classify records, or display business meaning.

## When to Use

Use for dropdowns, statuses, reason codes, countries, currencies, categories, and integration mappings.

## When Not to Use

Do not assume every configuration list is reference data or that codes are globally standardized.

## Advantages

Controlled values improve consistency and interoperability.

## Limitations

Stale caches, mismatched mappings, and effective-date differences cause subtle defects.

## Examples

A cancellation reason may be active for new requests but retained historically after retirement.

## Best Practices

- Validate code, label, status, and effective period.
- Test unknown/retired values.
- Verify cross-system mapping.
- Preserve historical interpretability.

## Related Knowledge

- `Master-Data.md`
- `Transaction-Data.md`
- `Validation-Rules.md`

## References

- Data governance and reference-data literature.