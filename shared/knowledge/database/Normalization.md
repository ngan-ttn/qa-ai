# Normalization

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview
Normalization organizes relational data to reduce harmful redundancy and update anomalies by separating facts according to dependencies.

## Purpose
Help QA understand why data may be split across tables and where integrity risks arise.

## Core Concepts
### Functional Dependency
One set of attributes determines another.
### Normal Forms
Common forms progressively reduce dependency anomalies.
### Denormalization
Intentional redundancy may be introduced for performance or analytical needs.

## How It Works
A model is decomposed so each relation represents coherent facts while keys preserve relationships.

## When to Use
Use during schema review, duplicate-data analysis, migration design, and join reasoning.

## When Not to Use
Do not demand normalization as an absolute rule; approved performance or analytical designs may denormalize intentionally.

## Advantages
Normalization can reduce inconsistent duplicate facts and simplify integrity enforcement.

## Limitations
Highly normalized models may require more joins and can be less convenient for some workloads.

## Examples
Customer contact details stored once in `customers` avoid repeating them in every order row.

## Best Practices
- Evaluate anomalies and dependencies, not table count alone.
- Distinguish deliberate denormalization from accidental duplication.
- Test synchronization when redundant values are intentionally stored.

## Related Knowledge
- `Relationships.md`
- `Joins.md`
- `Data-Warehousing.md`

## References
- Relational database normalization literature.