# Data Warehousing

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

A **data warehouse** is a data platform optimized for analytical, historical, reporting, and aggregation workloads rather than routine transactional processing. Warehouses commonly integrate data from multiple sources through ETL or ELT pipelines and often use dimensional or denormalized models.

## Purpose

This article helps QA validate warehouse data freshness, transformations, dimensions/facts, historical behavior, reconciliation, and reporting without applying OLTP assumptions to analytical systems.

## Core Concepts

### Source Systems
Operational databases, APIs, files, streams, and external systems feed warehouse data.

### ETL / ELT
Extract-transform-load or extract-load-transform pipelines move and reshape data for analysis.

### Fact Table
Stores measurable events or observations, often linked to dimensions.

### Dimension
Stores descriptive context such as customer, product, date, organization, or geography.

### Grain
The grain defines what one fact row represents and is fundamental to correct aggregation.

### Slowly Changing Dimension
Historical dimension changes can be modeled using different strategies; exact type and behavior are design-specific.

### Freshness / Latency
Warehouse data can intentionally lag source systems by minutes, hours, or longer according to pipeline schedules and requirements.

## How It Works

```text
Operational sources
       ↓
Extract / ingest
       ↓
Transform / cleanse
       ↓
Warehouse tables/models
       ↓
Semantic/reporting layer
       ↓
Dashboards / analytics
```

Each stage can introduce filtering, mapping, deduplication, late-arriving data, and timing differences.

## When to Use

Use warehouse knowledge for reports, dashboards, analytics migrations, ETL validation, reconciliation, historical metrics, and data-quality investigations.

## When Not to Use

Do not compare a warehouse directly to an operational database at arbitrary times and label differences as defects without accounting for pipeline freshness and transformation rules.

## Advantages

Warehouses centralize analytical data, preserve history, and support efficient large-scale aggregation across multiple sources.

## Limitations

They introduce pipeline latency, transformation complexity, duplicate/reprocessing risk, historical-model complexity, and differences from source-system schemas.

## Examples

### Grain Error
A fact table is intended to have one row per order item, but a report counts rows as orders and overstates totals.

### Late-Arriving Data
An event arrives after the daily load window. QA verifies whether it appears in the next processing cycle according to the pipeline contract.

### Dimension History
A customer's segment changes. Historical reports may preserve the old segment or use the current segment depending on the dimension strategy.

## Best Practices

- Define fact grain before validating counts or aggregates.
- Reconcile source and warehouse populations at comparable cut-off times.
- Validate transformation and deduplication rules independently.
- Test late, duplicate, missing, and corrected source records.
- Confirm timezone and business-date boundaries.
- Separate freshness SLA from data correctness.
- Trace report metrics through semantic layers to warehouse sources.

## Related Knowledge

- `Aggregation.md`
- `Data-Validation.md`
- `Data-Migration-Testing.md`
- `Normalization.md`
- `Views.md`

## References

- Data warehousing and dimensional-modeling literature.
- Target warehouse and pipeline documentation.