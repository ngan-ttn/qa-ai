# Manufacturing

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Manufacturing** systems support materials, bills of material, work orders, production operations, quality, inventory movement, traceability, and completion.

## Purpose

Give QA reusable context for production and traceability workflows.

## Core Concepts

### Material and BOM
Inputs and defined product structure.
### Work Order
Authorization/instruction to produce quantity under defined routing.
### Operation
Production step or station activity.
### Lot/Serial Traceability
Links inputs and outputs for quality and recall needs.
### Yield and Scrap
Produced, rejected, reworked, or lost quantities.

## How It Works

Demand drives work; materials are issued, operations executed, outputs recorded, quality decisions made, and finished inventory received.

## When to Use

Use for MES/ERP production, inventory consumption, quality, traceability, and shop-floor integrations.

## When Not to Use

Do not assume BOM, routing, tolerance, or quality policy.

## Advantages

Highlights quantity conservation, traceability, sequencing, and quality-state risks.

## Limitations

Processes vary significantly by manufacturing type.

## Examples

A lot is split across production outputs; QA verifies consumed quantity, produced quantity, scrap, and genealogy according to approved rules.

## Best Practices

- Validate quantity and unit conversions.
- Test lot/serial traceability.
- Cover rework and scrap paths.
- Verify effective BOM/routing versions.

## Related Knowledge

- `Transaction-Data.md`
- `Process-Lifecycle.md`
- `Audit-Trail.md`

## References

- Manufacturing operations and approved product documentation.