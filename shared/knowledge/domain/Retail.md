# Retail

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Retail** systems support products, prices, promotions, inventory, stores/channels, customers, sales, returns, and fulfillment.

## Purpose

Provide reusable QA context for omnichannel retail behavior.

## Core Concepts

### Product and Assortment
Items can vary by channel/location.
### Price and Promotion
Effective dates, eligibility, stacking, and rounding matter.
### Inventory
Availability can differ from physical stock due to reservation or latency.
### Sale and Return
Transactions have payment, receipt, tax, and reversal implications.

## How It Works

Retail processes connect catalog and pricing to inventory, checkout, payment, fulfillment, return, and reconciliation.

## When to Use

Use for POS, store operations, inventory, promotions, returns, and omnichannel features.

## When Not to Use

Do not assume promotion precedence, tax, or return policy.

## Advantages

Retail context exposes cross-channel pricing and inventory risks.

## Limitations

Policies differ by market, channel, and retailer.

## Examples

A promotion active online may not apply in store; QA validates channel, effective period, eligibility, and final price independently.

## Best Practices

- Test effective dates and price precedence.
- Cover inventory concurrency.
- Validate return/refund lifecycle.
- Reconcile receipt/order totals.

## Related Knowledge

- `E-Commerce.md`
- `Logistics.md`
- `Calculation-Rules.md`

## References

- Retail operations and approved product policy.