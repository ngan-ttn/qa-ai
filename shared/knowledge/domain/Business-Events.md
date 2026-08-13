# Business Events

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

A **business event** is a meaningful occurrence in the domain, such as an order being placed, a payment being authorized, or a permit expiring.

## Purpose

Help QA identify event-driven state changes, downstream obligations, timing, duplication, ordering, and observable business effects.

## Core Concepts

### Event Fact
An event describes something that occurred.
### Producer and Consumer
One actor/system records the occurrence; others may react.
### Event Data
Carries identifiers and facts needed to interpret the occurrence.
### Timing and Ordering
Business meaning can depend on when events occur and in what order.
### Duplicate Handling
The same event may be delivered or processed more than once in some architectures.

## How It Works

A business action or condition creates an event; domain rules determine state changes and downstream reactions. Technical delivery mechanics belong to API/event-driven knowledge.

## When to Use

Use for notifications, integrations, asynchronous workflows, audit reasoning, and event-storming analysis.

## When Not to Use

Do not assume every business event maps one-to-one to a message or technical event.

## Advantages

Event thinking clarifies causality and downstream impact.

## Limitations

Event definitions can be too technical or too broad if business meaning is not explicit.

## Examples

`Order Shipped` can trigger customer notification, inventory/accounting updates, and delivery tracking. QA validates business consequences according to scope.

## Best Practices

- Name events as completed business facts.
- Include stable identifiers and relevant context.
- Distinguish event occurrence from delivery.
- Test duplicates, late events, and ordering when architecture permits them.
- Trace events to expected business outcomes.

## Related Knowledge

- `Business-Workflow.md`
- `Event-Storming.md`
- `../api/Event-Driven-APIs.md`

## References

- Domain-driven design and event-driven architecture literature.