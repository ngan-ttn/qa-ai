# Retail

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Retail** software supports selling goods or services through stores, digital channels, or mixed commerce models. Common capabilities include product/catalog management, pricing, promotions, inventory, checkout, payment, returns, fulfillment, and customer service.

## Purpose

Give QA reusable retail context for analyzing cross-capability behavior without assuming one retailer's commercial rules.

## Core Concepts

### Product / SKU
A sellable item can have variants, identifiers, units, assortment, and lifecycle.

### Price
List, sale, channel, customer, location, or effective-dated prices may coexist.

### Promotion
Discounts, bundles, coupons, thresholds, or loyalty offers can interact and require precedence rules.

### Inventory
Stock can be available, reserved, damaged, in transit, or unavailable depending on the operating model.

### Cart / Basket
A temporary selection of items with quantities, prices, and promotions subject to revalidation.

### Checkout
Final validation of product, price, inventory, payment, delivery/pickup, and customer information.

### Return / Refund
Physical return, financial refund, exchange, and inventory disposition can be separate processes.

### Omnichannel
Store, web, mobile, pickup, and delivery channels can share or diverge in data and rules.

## How It Works

```text
Catalog / price / inventory
        ↓
Selection / cart
        ↓
Promotion + eligibility
        ↓
Checkout + payment
        ↓
Fulfillment
        ↓
Return / exchange / refund
```

Changes in price or inventory between selection and checkout often require revalidation.

## When to Use

Use for POS, e-commerce retail, inventory-backed sales, promotions, fulfillment, returns, store operations, and omnichannel experiences.

## When Not to Use

Do not assume promotion stacking, return periods, tax behavior, reservation policy, or inventory availability rules without current retailer requirements.

## Advantages

Retail context exposes cross-feature dependencies among price, stock, payment, fulfillment, and customer-facing totals.

## Limitations

Commercial policies can change frequently and differ by market, channel, product category, or campaign.

## Examples

A product is added to cart at one price but promotion expires before payment. QA validates the approved reprice behavior and user communication.

Two customers attempt to buy the last unit concurrently. QA tests reservation/commit semantics according to the retailer's inventory design.

A returned item receives a financial refund but is marked damaged and must not increase sellable stock.

## Best Practices

- Separate product identity, price, promotion, and inventory state.
- Test effective-date and campaign boundaries.
- Verify totals across line, order, tax/charge, and payment layers as defined.
- Cover concurrent stock changes and stale cart data.
- Test return, exchange, refund, and inventory disposition independently.
- Validate cross-channel consistency only where requirements promise it.
- Recheck configuration-driven rules during regression.

## Related Knowledge

- `E-Commerce.md`
- `Logistics.md`
- `Master-Data.md`
- `Transaction-Data.md`
- `Calculation-Rules.md`

## References

- Retail operations and commerce literature.
- Approved retailer product and commercial policy.
