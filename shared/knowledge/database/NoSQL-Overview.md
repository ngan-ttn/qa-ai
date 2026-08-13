# NoSQL Overview

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview
NoSQL is a broad label for non-relational database models including document, key-value, wide-column, and graph systems.

## Purpose
Prevent QA-AI from applying relational assumptions to databases with different data, query, and consistency models.

## Core Concepts
### Document
Stores structured documents, often with flexible schemas.
### Key-Value
Retrieves values primarily by key.
### Wide-Column
Organizes sparse or distributed column-oriented records.
### Graph
Models nodes and relationships directly.
### Consistency Model
Distributed systems may expose tunable or eventual consistency semantics.

## How It Works
Each model optimizes particular access patterns and distribution needs; APIs, indexing, transactions, and constraints vary significantly.

## When to Use
Use when requirements explicitly involve non-relational storage or distributed data models.

## When Not to Use
Do not use this overview as product-specific testing guidance.

## Advantages
NoSQL systems can offer flexible models, horizontal scale, or specialized access patterns.

## Limitations
Trade-offs include weaker cross-record constraints, different query capabilities, and model-specific consistency behavior.

## Examples
A document store may embed order items inside an order document instead of normalizing them into a separate table.

## Best Practices
- Identify the exact database model and guarantees.
- Test access patterns, consistency, indexes, and schema evolution according to product behavior.
- Avoid assuming SQL transactions or joins exist.

## Related Knowledge
- `Database-Fundamentals.md`
- `Relational-Database-Concepts.md`
- `Sharding.md`

## References
- Official documentation for the selected NoSQL database.
- Distributed data-system literature.