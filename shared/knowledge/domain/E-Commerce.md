# E-Commerce

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**E-commerce** systems support digital discovery, cart, pricing, checkout, payment, order management, fulfillment, cancellation, return, and refund.

## Purpose

Give QA a reusable end-to-end model for commerce risks across multiple services and business states.

## Core Concepts

### Catalog and Offer
Product information, availability, price, and promotion.
### Cart
A mutable pre-order selection whose values can become stale.
### Checkout
Validates identity, address, inventory, price, payment, and policy.
### Order
Business record representing accepted purchase intent.
### Fulfillment and After-Sales
Shipment, delivery, cancellation, return, and refund lifecycles.

## How It Works

```text
Browse → cart → checkout → payment/order → fulfillment → delivery → return/refund
```

Steps can be asynchronous and partially fail.

## When to Use

Use for web/mobile commerce, marketplace, checkout, order, payment, and fulfillment features.

## When Not to Use

Do not assume payment success equals order success or displayed stock equals guaranteed allocation.

## Advantages

E-commerce framing supports strong cross-service E2E and concurrency coverage.

## Limitations

Marketplace, tax, payment, and fulfillment models vary widely.

## Examples

Two buyers attempt the last unit concurrently. QA verifies allocation policy, payment handling, final inventory, and loser-path recovery.

## Best Practices

- Revalidate price and inventory at defined checkpoints.
- Test duplicate checkout and retry behavior.
- Cover partial failures between payment and order.
- Validate cancellation/return/refund state rules.
- Reconcile totals and quantities.

## Related Knowledge

- `Retail.md`
- `Logistics.md`
- `Calculation-Rules.md`
- `Process-Exceptions.md`

## References

- Commerce platform and approved business-policy documentation.