# Manufacturing

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Manufacturing** software supports planning, production, material consumption, work orders, bills of material, routing, quality, equipment, inventory, and traceability from inputs to finished goods.

## Purpose

Give QA reusable manufacturing context without assuming one plant, process type, ERP, quality standard, or regulatory regime.

## Core Concepts

### Bill of Material (BOM)
Defines components and quantities needed for a product or assembly, often with version/effective-date semantics.

### Work Order
Authorizes or tracks production of a defined quantity under specific routing, material, and process conditions.

### Routing / Operation
Sequence or network of production steps, work centers, and resources.

### Material Consumption
Raw or intermediate inventory is issued, consumed, returned, or scrapped during production.

### Yield / Scrap
Actual output can differ from planned quantity; acceptable variance and handling are project-specific.

### Lot / Serial Traceability
Materials and products may require traceability through production and quality events.

### Quality Control
Inspection, hold, nonconformance, release, and rework may affect material or product status.

### Version / Effective Date
BOM, routing, specification, and process instructions can change over time.

## How It Works

Demand or plan creates work → materials are allocated/issued → operations execute → quality checks occur → output is received → variances and traceability are recorded.

## When to Use

Use for MES/ERP production, work orders, material tracking, quality, batch/lot processes, and manufacturing inventory.

## When Not to Use

Do not assume BOM consumption, scrap tolerance, backflush, quality release, or traceability requirements without approved process rules.

## Advantages

Manufacturing context highlights quantity, version, traceability, concurrency, material-status, and quality-state risks.

## Limitations

Processes vary widely between discrete, batch, continuous, configure-to-order, and other manufacturing models.

## Examples

A work order uses BOM version 3 effective today. QA verifies historical orders keep their intended component definition if the design snapshots versions.

A material lot is placed on quality hold after partial consumption. QA validates whether remaining stock and affected work orders are restricted according to approved rules.

## Best Practices

- Verify effective versions of BOM/routing/specifications.
- Reconcile planned, issued, consumed, produced, returned, and scrapped quantities.
- Test lot/serial traceability where required.
- Cover hold, reject, rework, and release states.
- Include concurrent material use and inventory updates.
- Preserve production history and auditability.
- Confirm tolerances and quality thresholds from authoritative sources.

## Related Knowledge

- `Master-Data.md`
- `Transaction-Data.md`
- `Process-Lifecycle.md`
- `Logistics.md`
- `../database/Data-Validation.md`

## References

- Manufacturing operations and quality-management literature.
- Approved production and quality specifications.
