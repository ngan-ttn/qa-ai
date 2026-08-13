# API Knowledge

## Purpose

The `shared/knowledge/api/` module provides reusable, technology-aware but implementation-independent knowledge about API architecture, HTTP communication, interface design, security, error handling, API testing, and modern API interaction patterns.

It supports both human QA work and QA-AI reasoning by providing modular concepts that can be retrieved independently and combined during requirement analysis, test generation, coverage review, regression analysis, and defect investigation.

This module is conceptual knowledge. It does not define project-specific endpoints, payloads, credentials, thresholds, roles, service-level objectives, or release rules.

---

## Scope

The API knowledge domain covers seven areas:

```text
API
├── Foundations
├── Communication
├── API Design
├── Security
├── Error Handling
├── API Testing
└── Advanced Topics
```

Knowledge owned by other domains remains outside this folder:

- generic QA lifecycle and management concepts → `../qa/`
- test-design techniques → `../testing-techniques/`
- database and SQL concepts → `../database/`
- industry-specific business concepts → `../domain/`

---

## Module Structure

```text
shared/knowledge/api/
├── README.md
├── Catalog.md
│
├── API-Fundamentals.md
├── Client-Server-Architecture.md
├── HTTP-Fundamentals.md
├── REST-Architecture.md
├── API-Lifecycle.md
│
├── HTTP-Methods.md
├── Request-Structure.md
├── Response-Structure.md
├── Headers.md
├── Cookies.md
├── Content-Negotiation.md
│
├── Resource-Design.md
├── URI-Design.md
├── API-Versioning.md
├── Idempotency.md
├── Pagination.md
├── Filtering-Sorting-and-Searching.md
│
├── Authentication.md
├── Authorization.md
├── OAuth-2.0.md
├── JWT.md
├── API-Keys.md
├── Rate-Limiting.md
├── API-Security-Best-Practices.md
│
├── HTTP-Status-Codes.md
├── Error-Response-Design.md
├── Retry-Strategy.md
├── Timeout-Handling.md
│
├── API-Test-Strategy.md
├── Functional-API-Testing.md
├── Contract-Testing.md
├── Integration-Testing.md
├── Performance-Testing.md
├── Security-Testing.md
├── API-Mocking.md
│
├── Webhooks.md
├── GraphQL.md
├── gRPC.md
├── WebSocket.md
└── Event-Driven-APIs.md
```

The folder contains **40 approved knowledge articles**, excluding `README.md` and `Catalog.md`.

---

## Knowledge Areas

### Foundations

Establish API, client-server, HTTP, REST, and lifecycle concepts required by the rest of the module.

### Communication

Explain request/response construction and HTTP communication metadata.

### API Design

Cover resource modeling, URI design, versioning, idempotency, pagination, filtering, sorting, and searching.

### Security

Explain identity, access control, delegated authorization, token/key mechanisms, rate limiting, and baseline API security practices.

### Error Handling

Explain protocol outcomes, structured errors, retries, and timeout behavior.

### API Testing

Provide reusable knowledge for functional, contract, integration, performance, security, and mocked API validation.

### Advanced Topics

Cover webhooks, GraphQL, gRPC, WebSocket, and event-driven APIs without forcing REST/HTTP assumptions onto different interaction styles.

---

## Standard Article Structure

Every knowledge article follows `../../standards/Knowledge-Article.md` and contains the 12 mandatory sections:

1. `Overview`
2. `Purpose`
3. `Core Concepts`
4. `How It Works`
5. `When to Use`
6. `When Not to Use`
7. `Advantages`
8. `Limitations`
9. `Examples`
10. `Best Practices`
11. `Related Knowledge`
12. `References`

Optional sections may be added only when they provide meaningful value.

---

## Design Principles

API knowledge articles must:

- keep one primary responsibility per article;
- explain concepts before implementation details;
- preserve protocol and security terminology accurately;
- distinguish general standards from project-specific contracts;
- avoid inventing endpoint behavior, status mappings, thresholds, roles, credentials, retry timing, or service objectives;
- separate transport-level behavior from domain business behavior;
- distinguish authentication from authorization;
- distinguish synchronous acknowledgement from eventual asynchronous completion;
- support both human readability and AI retrieval;
- cross-reference related articles instead of duplicating them.

---

## QA-AI Usage

The API knowledge domain can support:

- requirement analysis for API and integration features;
- API scenario and test-case generation;
- authentication and authorization coverage;
- negative and error-path analysis;
- regression impact analysis after API contract changes;
- compatibility and versioning review;
- integration, timeout, retry, and idempotency reasoning;
- security-focused functional coverage;
- analysis of GraphQL, gRPC, webhook, WebSocket, and event-driven requirements.

QA-AI must treat project-specific API documentation as authoritative when it conflicts with generic knowledge, provided the project behavior remains valid under applicable protocol or security constraints.

---

## Relationships

This module connects with:

- `../qa/` for test strategy, risk-based testing, regression, and quality-management concepts;
- `../testing-techniques/` for systematic test design;
- `../database/` for persistence and data-validation concepts;
- `../domain/` for domain rules and business entities;
- `../../checklists/API-Testing.md` for execution-oriented review checks;
- `../../glossary/API-Terms.md` for concise terminology;
- `../../../skills/` and `../../../workflows/` for AI capabilities that consume API knowledge.

---

## Maintenance and Freeze Policy

`Catalog.md` is the source of truth for the approved API knowledge baseline.

The current baseline is frozen after full cross-article review. `Frozen` is a repository baseline state, not a metadata lifecycle status. Article metadata uses the allowed lifecycle status `Approved`.

A frozen article may still be changed when:

- a technical error is identified;
- a referenced standard changes materially;
- cross-domain review finds a required correction;
- the API knowledge architecture is intentionally expanded;
- a new approved requirement requires stronger coverage.

Any change should preserve physical-file ↔ Catalog consistency and trigger appropriate cross-review of affected articles.

---

## References

- `Catalog.md` — authoritative article inventory and knowledge architecture.
- `../../standards/Knowledge-Article.md` — mandatory knowledge-article structure and quality requirements.
- `../../standards/Metadata.md` — document lifecycle metadata rules.
- `../../standards/Naming.md` — repository naming rules.
