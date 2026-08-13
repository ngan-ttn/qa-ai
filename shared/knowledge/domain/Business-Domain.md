# Business Domain

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

A **business domain** is an area of business activity, knowledge, rules, terminology, actors, outcomes, and constraints that a software system supports. Domain understanding gives QA the context needed to judge whether behavior is merely technically valid or actually correct for the business.

A domain can span multiple products, teams, systems, channels, and jurisdictions. Its boundaries are therefore established from business responsibility and meaning, not automatically from application or database boundaries.

## Purpose

Provide a reusable foundation for identifying domain scope, stakeholders, capabilities, entities, processes, rules, events, risks, and authoritative evidence before deriving QA artifacts.

## Core Concepts

### Domain Scope
Defines which business problems and responsibilities are inside the area being analyzed and which are outside.

### Actors and Stakeholders
People, organizations, roles, or systems that initiate, perform, approve, receive, own, or govern domain activities.

### Business Capabilities
Stable abilities the organization must perform, such as fulfillment, account servicing, eligibility assessment, or reconciliation.

### Business Outcomes
Observable results the domain is expected to produce, such as a fulfilled order, approved permit, settled transaction, or completed return.

### Domain Rules
Policies and constraints that determine valid states, decisions, calculations, permissions, and transitions.

### Domain Language
Terms must be interpreted according to agreed business meaning, not assumed from everyday or technical usage.

### Sources of Authority
Requirements, policy, SME decisions, contracts, regulations, and approved operating procedures may carry different authority. Conflicts must be surfaced rather than silently resolved.

## How It Works

```text
Business objective
      ↓
Domain scope + stakeholders
      ↓
Capabilities + entities
      ↓
Processes + rules + events
      ↓
States + exceptions + controls
      ↓
Observable business outcomes
```

QA uses this model to connect individual requirements to business intent, identify missing context, and reason about impact beyond one screen or endpoint. Domain analysis should continuously separate confirmed project facts from reusable generic patterns.

## When to Use

Use when entering a new product area, reviewing requirements, analyzing business rules, designing scenarios, assessing regression impact, defining test data, or investigating defects with unclear business consequences.

## When Not to Use

Do not use generic domain knowledge to override project requirements, approved policy, legal or clinical advice, or authoritative subject-matter expertise. Do not infer organization-specific thresholds, permissions, formulas, or obligations from industry practice alone.

## Advantages

Domain framing improves requirement interpretation, risk identification, terminology consistency, cross-feature coverage, stakeholder communication, and business-focused defect assessment.

## Limitations

Domains vary by organization, product, jurisdiction, operating model, and time. Generic knowledge cannot supply project-specific rules, and even approved domain models can become stale or conflict with actual operations.

## Examples

### E-Commerce
Checkout may involve customer, cart, inventory, pricing, promotion, payment, order, fulfillment, cancellation, and refund concepts. A technically successful request is insufficient if the resulting order violates inventory or payment rules.

### Banking
A transfer can involve account eligibility, authorization, limits, posting state, external rails, reversal, reconciliation, auditability, and regulatory controls. The specific state model must come from the product and market.

### Enterprise Approval
A request may move across Requestor, Operations, Risk, and Regulatory roles. Domain analysis identifies who owns decisions, which data becomes authoritative, and which exceptions can reopen or cancel the process.

## Best Practices

- Establish domain scope and exclusions before analyzing details.
- Identify authoritative terminology, stakeholders, and source documents.
- Separate generic domain patterns from project-specific rules.
- Trace business outcomes to capabilities, entities, processes, rules, and exceptions.
- Record assumptions and ambiguity instead of inventing missing behavior.
- Verify cross-system ownership and source-of-truth boundaries.
- Revalidate domain assumptions when product, policy, or jurisdiction changes.
- Use domain knowledge to ask better questions, not to replace evidence.

## Related Knowledge

- `Domain-Terminology.md`
- `Domain-Knowledge.md`
- `Business-Context.md`
- `Domain-Driven-Thinking.md`
- `Business-Process-Fundamentals.md`
- `Business-Entity.md`
- `Business-Rule-Fundamentals.md`

## References

- Domain-driven design and business-analysis literature.
- Project requirements and approved business documentation.
