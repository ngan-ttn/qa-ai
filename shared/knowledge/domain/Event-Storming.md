# Event Storming

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Event Storming** is a collaborative discovery technique that explores a domain through business events, commands/actions, actors, policies, aggregates/concepts, and external systems.

## Purpose

Help QA use event-oriented discovery to uncover workflow, rules, boundaries, exceptions, and unanswered questions.

## Core Concepts

### Domain Event
A meaningful past-tense business fact.
### Command/Action
Intent that may cause an event.
### Actor
Person or system initiating action.
### Policy
Rule that reacts to facts and drives action.
### Hotspot
Question, conflict, risk, or uncertainty requiring resolution.

## How It Works

Participants lay out significant events in time order, then add causes, decisions, actors, dependencies, and problem areas to build shared understanding.

## When to Use

Use for complex workflows, new domains, cross-team discovery, and integration-heavy processes.

## When Not to Use

Do not treat workshop output as approved requirements without validation.

## Advantages

Rapidly surfaces hidden events, exceptions, terminology conflicts, and ownership boundaries.

## Limitations

Quality depends on participant knowledge and facilitation; outputs can be incomplete.

## Examples

For returns: `Return Requested → Return Approved → Item Received → Refund Issued`, with hotspots around partial return, failed refund, and eligibility expiry.

## Best Practices

- Use business-language past-tense events.
- Include domain experts and QA.
- Capture hotspots explicitly.
- Separate discovery from final specification.
- Convert findings into traceable requirements/questions/tests.

## Related Knowledge

- `Business-Events.md`
- `Business-Workflow.md`
- `Domain-Model.md`
- `Bounded-Context.md`

## References

- Alberto Brandolini, EventStorming literature.