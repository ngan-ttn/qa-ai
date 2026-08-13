# Event Storming

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Event Storming** is a collaborative discovery technique that explores a domain by identifying significant events, commands/actions, actors, policies, rules, external systems, and process hotspots. It is primarily a learning and modeling technique, not a software architecture mandate.

## Purpose

Help QA participate in domain discovery, uncover missing states and exceptions, and convert workshop findings into better clarification questions and test ideas.

## Core Concepts

### Domain Event
A past-tense business fact such as `Order Submitted` or `Permit Approved`.

### Command / Action
An intent that may cause an event, such as `Submit Order`.

### Actor
A role or system initiating an action.

### Policy / Rule
Logic that reacts to an event or determines a next action.

### Entity / Aggregate Candidate
A concept whose state is affected; whether it becomes a DDD aggregate is a later design decision.

### External System
A dependency outside the immediate domain boundary.

### Hotspot
An ambiguity, conflict, risk, unknown, or area needing investigation.

### Timeline
Events are often arranged in business sequence to expose lifecycle and causality.

## How It Works

```text
Identify important events
        ↓
Place in business timeline
        ↓
Add commands / actors / rules
        ↓
Identify entities + external systems
        ↓
Mark hotspots and exceptions
        ↓
Refine process / model / requirements
```

QA can use hotspots as clarification questions and derive state-transition, exception, integration, and end-to-end scenarios from the discovered flow.

## When to Use

Use for complex or poorly documented domains, cross-functional workshops, new product discovery, process redesign, and onboarding.

## When Not to Use

Do not treat workshop output as automatically approved requirements. Do not assume every identified event must become a technical event or message.

## Advantages

Event Storming quickly surfaces domain language, lifecycle, dependencies, exception paths, and disagreement among stakeholders.

## Limitations

Workshop quality depends on participant knowledge and facilitation. Outputs can be incomplete, biased, or overly high level.

## Examples

A commerce workshop identifies `Order Submitted`, `Payment Authorized`, `Inventory Reserved`, `Shipment Created`, and `Order Canceled`. A hotspot appears around payment success but inventory failure, prompting explicit compensation requirements.

A permit workflow reveals `Permit Approved` and later `UPN Added` as distinct business events, clarifying that extending coverage does not necessarily modify approval identity.

## Best Practices

- Include business and operational stakeholders, not only developers.
- Phrase events as business facts in past tense.
- Mark assumptions and unknowns visibly.
- Explore exception and recovery paths, not only happy path.
- Distinguish business events from technical implementation events.
- Convert hotspots into owned follow-up questions.
- Validate workshop output before using it as source of truth.
- Feed confirmed findings into domain models and QA scenarios.

## Related Knowledge

- `Business-Events.md`
- `Business-Workflow.md`
- `Domain-Model.md`
- `Bounded-Context.md`
- `Domain-Driven-Thinking.md`

## References

- Event Storming literature and facilitation guidance.
- Approved workshop outcomes and domain documentation.
