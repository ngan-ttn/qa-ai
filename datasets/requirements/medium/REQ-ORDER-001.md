# Order Cancellation and Inventory Restoration

## Dataset Metadata

- Dataset ID: `REQ-ORDER-001`
- Complexity: `Medium`
- Domain: `E-commerce`
- Primary Evaluation Focus: Requirement analysis, business-rule extraction, state-transition identification, role-based behavior, dependency analysis, boundary identification, and test coverage

---

## Context

The application is an e-commerce platform where registered customers can place orders for physical products.

An order progresses through fulfillment statuses after it is created.

Customers may cancel eligible orders before fulfillment reaches a stage where cancellation is no longer allowed.

When a cancellation succeeds, the system must update the order, restore inventory reserved by the order, and handle payment according to the current payment state.

---

## Requirement

As a registered customer,

I want to cancel an eligible order before it is shipped,

So that I do not receive products I no longer want and any reserved inventory or captured payment is handled correctly.

### Order Status

An order can have one of the following statuses:

- `Pending`
- `Confirmed`
- `Processing`
- `Shipped`
- `Delivered`
- `Canceled`

A customer may cancel an order only when its current status is:

- `Pending`
- `Confirmed`
- `Processing`

An order in `Shipped`, `Delivered`, or `Canceled` status cannot be canceled by the customer.

Cancellation eligibility must be evaluated using the order's current status when the cancellation request is processed.

### Authorization

Only the customer who owns the order may cancel it.

A customer must not be able to cancel an order belonging to another customer, regardless of the order's status.

### Successful Cancellation

When an eligible cancellation request succeeds:

1. The order status changes to `Canceled`.
2. Inventory reserved for each order item is released back to available inventory.
3. Payment handling is performed according to the payment state.
4. The cancellation timestamp is recorded.

The order must not return to a fulfillment status after it has been successfully canceled.

### Inventory Restoration

When an order is created, the ordered quantity is reserved from available inventory.

When the order is successfully canceled, the full quantity reserved by that order must be released.

For an order containing multiple products, the reserved quantity for every order item must be released.

Inventory restoration must occur only once for a successfully canceled order.

A repeated cancellation request for an already canceled order must not increase available inventory again.

### Payment Handling

For this dataset, payment can have one of the following states:

- `Pending`
- `Captured`
- `Refunded`

A payment may already be in `Refunded` state because of a payment adjustment performed outside the order-cancellation flow.

Payment handling after successful cancellation follows these rules:

| Payment State at Cancellation | Required Result |
|---|---|
| `Pending` | No refund is created. The payment remains uncaptured. |
| `Captured` | A full refund is initiated for the captured order amount. |
| `Refunded` | No additional refund is initiated. |

When a refund is initiated because of cancellation, the payment state does not immediately change to `Refunded`.

Refund completion is outside the cancellation transaction and is not defined by this dataset.

### Failed or Ineligible Cancellation

If the cancellation request is rejected because the order is not eligible or the customer does not own the order:

- The order status must not change.
- Reserved inventory must not be released.
- No refund must be initiated.
- No cancellation timestamp must be recorded.

---

## Acceptance Criteria

1. The order owner can cancel an order in `Pending`, `Confirmed`, or `Processing` status.
2. The order owner cannot cancel an order in `Shipped`, `Delivered`, or `Canceled` status.
3. A customer cannot cancel an order owned by another customer, even when the order is otherwise eligible for cancellation.
4. Cancellation eligibility is determined from the current order status when the cancellation request is processed.
5. A successful cancellation changes the order status to `Canceled`.
6. A successful cancellation records a cancellation timestamp.
7. A successfully canceled order cannot return to `Pending`, `Confirmed`, `Processing`, `Shipped`, or `Delivered` through the cancellation flow.
8. A successful cancellation releases the full quantity reserved by the order back to available inventory.
9. For a multi-item order, a successful cancellation releases the reserved quantity for every order item.
10. Inventory is restored only once for an order, and another cancellation request against the already canceled order does not release inventory again.
11. If the payment state is `Pending`, successful cancellation does not create a refund and no payment capture occurs as part of cancellation.
12. If the payment state is `Captured`, successful cancellation initiates one full refund for the captured order amount.
13. If the payment state is `Refunded`, successful cancellation does not initiate another refund.
14. Initiating a refund does not immediately change the payment state to `Refunded`.
15. A rejected cancellation does not change the order status.
16. A rejected cancellation does not release reserved inventory.
17. A rejected cancellation does not initiate a refund.
18. A rejected cancellation does not record a cancellation timestamp.

---

## Constraints / Notes

- Only cancellation initiated by a registered customer is in scope.
- Administrative or support-agent cancellation is outside the scope of this dataset.
- Each order has exactly one owning customer.
- The cancellation flow operates on the entire order; partial item cancellation is not supported by this dataset.
- Inventory reservation already exists before cancellation is requested.
- Payment authorization, payment capture processing, payment adjustments, and refund completion are outside the scope of the cancellation flow.
- The technical transaction mechanism used to coordinate order, inventory, and payment updates is not defined by this dataset.

---

## Known Ambiguities

The following information is intentionally not specified:

1. The expected recovery behavior if an internal failure occurs after one cancellation operation succeeds but another fails, for example when the order is marked `Canceled` but inventory restoration fails.
2. The expected behavior when two cancellation requests for the same eligible order are processed concurrently.
3. Whether the customer receives a notification after a successful cancellation.
4. The expected retry behavior when refund initiation fails.

These gaps are intentionally retained so downstream QA analysis can identify clarification needs and risks without inventing missing business rules.
