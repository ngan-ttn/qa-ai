# REST Architecture

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-12

## Overview

**REST (Representational State Transfer)** is an architectural style for network-based systems. It defines constraints intended to improve properties such as scalability, visibility, simplicity, and independent evolution. REST is not a wire protocol and is not synonymous with any API that uses JSON over HTTP.

## Purpose

Understanding REST helps QA reason about resource-oriented interfaces, HTTP semantics, stateless interactions, caching, uniform interfaces, and compatibility. It also prevents incorrect assumptions such as treating every HTTP endpoint as automatically RESTful.

## Core Concepts

### Client-Server

Client and server concerns are separated so each can evolve independently within the contract.

### Stateless Interaction

Each request should contain the information needed to understand that request. Server-side application state still exists; statelessness concerns request context rather than absence of data or business state.

### Cacheability

Responses define whether they may be reused by caches. Correct cache semantics can improve performance but incorrect caching can expose stale or sensitive data.

### Uniform Interface

REST emphasizes consistent interaction through resources, representations, standardized semantics, and hypermedia constraints.

### Layered System

A client need not know whether it communicates directly with an origin server or through intermediaries such as gateways, proxies, or caches.

### Code on Demand

REST optionally allows servers to extend client functionality by transferring executable code. This constraint is optional and uncommon in API-testing discussions.

### Resource and Representation

A resource is an identifiable conceptual entity. A representation is a transmitted description of a resource state, such as JSON or XML.

## How It Works

A REST-oriented HTTP API typically identifies resources through URIs and uses HTTP methods according to their standardized semantics.

```text
Client
  │ GET /orders/123
  ▼
Resource Interface
  │
  ▼
Representation of Order 123
```

State transitions occur through interactions with resources. The protocol response communicates the result, while representations communicate data. Good REST design uses HTTP semantics rather than hiding every operation behind arbitrary action endpoints.

## When to Use

Use REST knowledge when:

- reviewing resource-oriented HTTP APIs;
- validating method and URI consistency;
- testing cacheability and stateless behavior;
- assessing API design quality;
- reviewing versioning and compatibility approaches;
- distinguishing resource representations from backend models.

## When Not to Use

Do not force REST terminology onto APIs intentionally using RPC, GraphQL, gRPC, event-driven messaging, or other styles. Do not classify an API as fully REST-conformant simply because it exposes HTTP endpoints and JSON payloads.

## Advantages

REST constraints can support:

- loose coupling;
- scalable intermediary use;
- standardized semantics;
- broad HTTP-tool compatibility;
- independent client/server evolution;
- cacheable interactions;
- clear resource-oriented models.

## Limitations

REST may be a poor fit for:

- strongly RPC-oriented operations;
- streaming use cases;
- extremely low-latency binary communication;
- complex client-driven query requirements;
- event-first asynchronous architectures.

Real-world APIs also commonly implement only a subset of REST constraints.

## Examples

### Resource-Oriented Retrieval

```text
GET /customers/42
GET /customers/42/orders
```

The URI identifies resources rather than embedding implementation details.

### Update

```text
PUT /profiles/42
```

If PUT semantics are used, repeated equivalent requests should have the intended idempotent effect.

### Non-RESTful Action Pattern

```text
POST /doSomething?action=deleteOrder&id=42
```

This may still be a valid HTTP API, but its design is action/RPC-oriented rather than strongly resource-oriented.

## Best Practices

- Use HTTP method semantics consistently.
- Model stable business resources rather than database tables.
- Keep URIs understandable and implementation-independent.
- Treat statelessness correctly; do not confuse it with absence of server-side data.
- Define cache behavior deliberately.
- Return meaningful status codes and structured error information.
- Preserve compatibility when evolving representations.
- Test the published contract, not an idealized REST interpretation when the actual API intentionally differs.

## Related Knowledge

- `HTTP-Fundamentals.md` explains the protocol commonly used to implement REST APIs.
- `Resource-Design.md` and `URI-Design.md` provide deeper design guidance.
- `HTTP-Methods.md` and `Idempotency.md` cover operation semantics.
- `API-Versioning.md` addresses evolution and compatibility.
- `GraphQL.md` and `gRPC.md` describe alternative API approaches.

## References

- Roy T. Fielding, **Architectural Styles and the Design of Network-based Software Architectures**.
- RFC 9110, **HTTP Semantics**.

The term REST is frequently used loosely in industry. QA should evaluate the documented interface and actual architectural expectations rather than relying on labels alone.
