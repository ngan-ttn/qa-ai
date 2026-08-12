# API Catalog

## Purpose

The **API Catalog** defines the approved knowledge architecture for API concepts, communication, design, security, failure handling, testing, and modern integration patterns within the QA-AI framework.

Its objectives are to:

- define the authoritative set of API knowledge articles in `shared/knowledge/api/`;
- organize API knowledge into clear, reusable categories;
- expose conceptual prerequisites and learning order;
- support API reasoning across QA skills and workflows;
- prevent duplication with QA, testing-techniques, database, and domain knowledge;
- keep the physical folder and knowledge roadmap synchronized.

This catalog is the source of truth for the current API knowledge baseline.

---

## Scope

This catalog covers:

- API fundamentals and client-server interaction;
- HTTP communication;
- REST and resource-oriented design;
- API security and access control;
- error, retry, timeout, and rate behavior;
- API testing practices;
- webhooks, GraphQL, gRPC, WebSocket, and event-driven APIs.

The following topics are intentionally owned by other domains.

| Topic | Knowledge Domain |
|---|---|
| Test Planning and generic Test Strategy | `../qa/` |
| Risk-Based Testing | `../qa/` |
| Equivalence Partitioning | `../testing-techniques/` |
| Boundary Value Analysis | `../testing-techniques/` |
| Decision Table / State Transition Testing | `../testing-techniques/` |
| SQL and Database Validation | `../database/` |
| Industry-Specific Rules | `../domain/` |

---

## Knowledge Architecture

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

Each category owns a distinct responsibility while remaining connected to the wider QA-AI knowledge graph.

---

## Knowledge Map

### Foundations

```text
Foundations
├── API Fundamentals
├── Client-Server Architecture
├── HTTP Fundamentals
├── REST Architecture
└── API Lifecycle
```

### Communication

```text
Communication
├── HTTP Methods
├── Request Structure
├── Response Structure
├── Headers
├── Cookies
└── Content Negotiation
```

### API Design

```text
API Design
├── Resource Design
├── URI Design
├── API Versioning
├── Idempotency
├── Pagination
└── Filtering, Sorting and Searching
```

### Security

```text
Security
├── Authentication
├── Authorization
├── OAuth 2.0
├── JWT
├── API Keys
├── Rate Limiting
└── API Security Best Practices
```

### Error Handling

```text
Error Handling
├── HTTP Status Codes
├── Error Response Design
├── Retry Strategy
└── Timeout Handling
```

### API Testing

```text
API Testing
├── API Test Strategy
├── Functional API Testing
├── Contract Testing
├── Integration Testing
├── Performance Testing
├── Security Testing
└── API Mocking
```

### Advanced Topics

```text
Advanced Topics
├── Webhooks
├── GraphQL
├── gRPC
├── WebSocket
└── Event-Driven APIs
```

---

## Article Catalog

The table below defines the current approved API knowledge baseline.

| Article | File | Category | Level | Prerequisites | Priority | Status |
|---|---|---|---|---|---|---|
| API Fundamentals | `API-Fundamentals.md` | Foundations | Foundation | None | High | Approved |
| Client-Server Architecture | `Client-Server-Architecture.md` | Foundations | Foundation | API Fundamentals | High | Approved |
| HTTP Fundamentals | `HTTP-Fundamentals.md` | Foundations | Foundation | Client-Server Architecture | High | Approved |
| REST Architecture | `REST-Architecture.md` | Foundations | Intermediate | HTTP Fundamentals | High | Approved |
| API Lifecycle | `API-Lifecycle.md` | Foundations | Intermediate | API Fundamentals | Medium | Approved |
| HTTP Methods | `HTTP-Methods.md` | Communication | Foundation | HTTP Fundamentals | High | Approved |
| Request Structure | `Request-Structure.md` | Communication | Foundation | HTTP Fundamentals | High | Approved |
| Response Structure | `Response-Structure.md` | Communication | Foundation | HTTP Fundamentals | High | Approved |
| Headers | `Headers.md` | Communication | Foundation | HTTP Fundamentals | Medium | Approved |
| Cookies | `Cookies.md` | Communication | Intermediate | Headers | Medium | Approved |
| Content Negotiation | `Content-Negotiation.md` | Communication | Intermediate | Headers | Medium | Approved |
| Resource Design | `Resource-Design.md` | API Design | Intermediate | REST Architecture | Medium | Approved |
| URI Design | `URI-Design.md` | API Design | Intermediate | REST Architecture | Medium | Approved |
| API Versioning | `API-Versioning.md` | API Design | Intermediate | API Fundamentals | High | Approved |
| Idempotency | `Idempotency.md` | API Design | Advanced | HTTP Methods | High | Approved |
| Pagination | `Pagination.md` | API Design | Intermediate | Request Structure | Medium | Approved |
| Filtering, Sorting and Searching | `Filtering-Sorting-and-Searching.md` | API Design | Intermediate | Request Structure | Medium | Approved |
| Authentication | `Authentication.md` | Security | Foundation | HTTP Fundamentals | High | Approved |
| Authorization | `Authorization.md` | Security | Foundation | Authentication | High | Approved |
| OAuth 2.0 | `OAuth-2.0.md` | Security | Intermediate | Authentication, Authorization | High | Approved |
| JWT | `JWT.md` | Security | Intermediate | Authentication | High | Approved |
| API Keys | `API-Keys.md` | Security | Foundation | Authentication | Medium | Approved |
| Rate Limiting | `Rate-Limiting.md` | Security | Intermediate | HTTP Fundamentals | Medium | Approved |
| API Security Best Practices | `API-Security-Best-Practices.md` | Security | Advanced | Authentication, Authorization | High | Approved |
| HTTP Status Codes | `HTTP-Status-Codes.md` | Error Handling | Foundation | HTTP Fundamentals | High | Approved |
| Error Response Design | `Error-Response-Design.md` | Error Handling | Intermediate | HTTP Status Codes | High | Approved |
| Retry Strategy | `Retry-Strategy.md` | Error Handling | Intermediate | HTTP Status Codes, Idempotency | Medium | Approved |
| Timeout Handling | `Timeout-Handling.md` | Error Handling | Intermediate | HTTP Fundamentals | Medium | Approved |
| API Test Strategy | `API-Test-Strategy.md` | API Testing | Intermediate | REST Architecture | High | Approved |
| Functional API Testing | `Functional-API-Testing.md` | API Testing | Foundation | API Test Strategy | High | Approved |
| Contract Testing | `Contract-Testing.md` | API Testing | Intermediate | API Test Strategy | High | Approved |
| Integration Testing | `Integration-Testing.md` | API Testing | Intermediate | Functional API Testing | High | Approved |
| Performance Testing | `Performance-Testing.md` | API Testing | Advanced | API Test Strategy | Medium | Approved |
| Security Testing | `Security-Testing.md` | API Testing | Advanced | API Security Best Practices | High | Approved |
| API Mocking | `API-Mocking.md` | API Testing | Intermediate | Contract Testing | Medium | Approved |
| Webhooks | `Webhooks.md` | Advanced Topics | Intermediate | HTTP Fundamentals, Retry Strategy | Medium | Approved |
| GraphQL | `GraphQL.md` | Advanced Topics | Advanced | API Fundamentals | Medium | Approved |
| gRPC | `gRPC.md` | Advanced Topics | Advanced | API Fundamentals | Medium | Approved |
| WebSocket | `WebSocket.md` | Advanced Topics | Advanced | Client-Server Architecture | Medium | Approved |
| Event-Driven APIs | `Event-Driven-APIs.md` | Advanced Topics | Advanced | API Fundamentals | Medium | Approved |

---

## Category Summary

| Category | Articles | Status | Purpose |
|---|---:|---|---|
| Foundations | 5 | Approved | Establish core API and protocol concepts. |
| Communication | 6 | Approved | Explain HTTP request/response composition and metadata. |
| API Design | 6 | Approved | Model stable, compatible, usable API interfaces. |
| Security | 7 | Approved | Establish identity, access, abuse, and protection concepts. |
| Error Handling | 4 | Approved | Explain failures, errors, retries, and timeouts. |
| API Testing | 7 | Approved | Provide reusable API validation approaches. |
| Advanced Topics | 5 | Approved | Cover modern non-traditional API interaction styles. |
| **Total** | **40** | **Approved** | Current API knowledge baseline. |

The catalog count must match the physical `.md` knowledge articles in `shared/knowledge/api/`, excluding `README.md` and `Catalog.md`.

---

## Knowledge Levels

### Foundation

Introduces concepts needed for routine API reasoning and requires minimal prerequisite knowledge.

### Intermediate

Combines foundational concepts into design, integration, security, or testing practices.

### Advanced

Requires multiple prerequisite concepts or deeper reasoning about distributed behavior, compatibility, security, or asynchronous systems.

Knowledge level describes conceptual dependency, not job seniority.

---

## Priority Definitions

### High

Required for core API analysis, generation, and quality reasoning in common QA workflows.

### Medium

Important for broader coverage, specialized integrations, or advanced API contexts but not required for every API task.

Priority is a knowledge-development and retrieval signal, not a project defect priority.

---

## Dependency Flow

```text
API Fundamentals
      ↓
Client-Server Architecture
      ↓
HTTP Fundamentals
      ├── Communication
      ├── REST Architecture → API Design
      ├── Authentication → Authorization → Security
      └── Status Codes → Error Handling

API Test Strategy
      ├── Functional API Testing
      ├── Contract Testing
      ├── Integration Testing
      ├── Performance Testing
      ├── Security Testing
      └── API Mocking

Foundation + Design + Security + Failure Handling
      ↓
Advanced Topics
```

This is a recommended conceptual path, not a mandatory reading sequence.

---

## Cross-Domain Relationships

API knowledge should reference, rather than duplicate:

- `../qa/Risk-Based-Testing.md` for risk prioritization;
- `../qa/Regression-Testing.md` for generic regression concepts;
- `../testing-techniques/` for detailed test-design techniques;
- `../database/` for SQL, transactions, persistence, and database validation;
- `../domain/` for business entities, workflows, and industry rules.

---

## Quality and Freeze Criteria

The API baseline is considered complete when:

- all 40 cataloged articles physically exist;
- no cataloged article is empty;
- every article follows the 12 mandatory sections in `../../standards/Knowledge-Article.md`;
- article metadata uses an allowed lifecycle status;
- terminology is consistent across HTTP, REST, authentication, authorization, error, and testing concepts;
- cross-references point to real repository knowledge;
- no article duplicates another article's primary responsibility;
- project-specific rules are not presented as universal API rules;
- all categories pass cross-article review;
- Catalog count matches the physical baseline.

---

## Baseline Status

```text
Folder: shared/knowledge/api/
Physical Knowledge Articles: 40
Cataloged Knowledge Articles: 40
Catalog Status: Approved
Baseline State: Frozen
Freeze Date: 2026-08-12
```

`Frozen` describes the repository baseline. It is not a document metadata lifecycle value.

Future changes should trigger targeted review of affected articles and a new cross-domain consistency check when relationships change.

---

## References

- `README.md`
- `../../standards/Knowledge-Article.md`
- `../../standards/Metadata.md`
- `../../standards/Naming.md`
- `../../glossary/API-Terms.md`
