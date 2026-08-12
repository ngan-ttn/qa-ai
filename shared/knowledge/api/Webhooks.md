# Webhooks

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-12

## Overview

A **webhook** is an event-notification pattern in which one system sends an HTTP request to a consumer-controlled endpoint when a defined event occurs. Unlike polling, the consumer does not repeatedly ask whether something changed.

## Purpose

Webhook knowledge helps QA validate event delivery, authentication, retries, duplicate handling, ordering assumptions, endpoint security, and eventual processing behavior.

## Core Concepts

### Producer

The system that detects an event and sends the webhook.

### Consumer Endpoint

The HTTP endpoint that receives the notification.

### Event Payload

The request body identifies the event and relevant data. Some designs send a complete snapshot; others send only identifiers requiring a follow-up API call.

### Delivery Acknowledgement

The consumer normally returns an HTTP response indicating whether the webhook request was accepted. This acknowledgement does not necessarily prove downstream business processing completed.

### Retry

Producers often retry delivery after transient failures. Exact retry schedules and limits are provider-specific.

### Duplicate Delivery

Webhook delivery is commonly at-least-once rather than exactly-once. Consumers should therefore tolerate duplicates where the provider contract says retries can occur.

### Ordering

Event delivery order may not be guaranteed. Consumers may need sequence numbers, timestamps, or current-state reconciliation.

### Authenticity

Webhook consumers should verify that incoming requests come from a trusted producer, often through signatures, secrets, certificates, or network controls.

## How It Works

```text
Business Event
      ↓
Webhook Producer
      ↓ HTTP POST
Consumer Endpoint
      ↓
Validate authenticity
      ↓
Acknowledge delivery
      ↓
Process / enqueue / reconcile
```

If delivery fails, the producer may retry according to policy.

## When to Use

Use webhook knowledge for payment callbacks, delivery status updates, external workflow notifications, event subscriptions, asynchronous integrations, or partner notifications.

## When Not to Use

Do not assume webhooks guarantee exactly-once delivery, strict ordering, or immediate processing unless the contract explicitly provides those guarantees.

## Advantages

Webhooks reduce polling, improve near-real-time integration, and allow providers to push important state changes to consumers.

## Limitations

They introduce public endpoint exposure, retry complexity, duplicate events, delivery delays, ordering uncertainty, and dependency on consumer availability.

## Examples

### Payment Completion

A payment provider sends `payment.completed`. QA validates signature, payload schema, duplicate handling, and final local payment state.

### Consumer Returns 500

The producer retries according to its documented policy. QA verifies the consumer does not create duplicate downstream side effects.

### Delayed Delivery

The webhook arrives after the consumer already learned the new state through polling or another API call. The consumer should reconcile safely.

## Best Practices

- Verify webhook authenticity before processing data.
- Acknowledge quickly and process asynchronously when appropriate.
- Design consumers for duplicate delivery.
- Do not rely on ordering unless guaranteed.
- Store event identifiers or equivalent deduplication context where needed.
- Test retries, timeouts, malformed signatures, stale events, and replay according to scope.
- Protect secrets in logs and test evidence.
- Reconcile with source-of-truth APIs when eventual consistency requires it.

## Related Knowledge

- `Event-Driven-APIs.md`
- `Idempotency.md`
- `Retry-Strategy.md`
- `Timeout-Handling.md`
- `Authentication.md`
- `Integration-Testing.md`

## References

- HTTP semantics defined by RFC 9110.
- Provider webhook specifications commonly define signature and retry behavior.
- CloudEvents may be used as a standardized event envelope in some systems.

Delivery guarantees and security mechanisms are provider-specific.
