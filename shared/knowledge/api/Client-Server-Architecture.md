# Client-Server Architecture

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-12

## Overview

**Client-server architecture** separates requesters of capabilities from providers of those capabilities. A client initiates an interaction; a server receives the request, applies relevant logic, and returns a response or otherwise coordinates the requested operation.

This separation is fundamental to web applications, mobile applications, service integrations, and many API-based systems.

## Purpose

Understanding client-server architecture helps QA determine where behavior is initiated, where validation and state changes occur, which failures belong to the client or server layer, and how network or dependency conditions can affect user-visible behavior.

## Core Concepts

### Client

A client is a software component that consumes a service. Examples include browsers, mobile apps, backend services, scripts, and partner systems.

### Server

A server exposes capabilities, validates requests, applies business logic, communicates with dependencies, and returns results.

### Separation of Concerns

Clients usually focus on interaction, presentation, or orchestration, while servers centralize shared business behavior and data access. The exact boundary is implementation-specific.

### Network Boundary

Remote client-server communication crosses a network boundary. This introduces latency, transport errors, timeouts, retries, security controls, and serialization concerns that do not exist in a simple local function call.

### Multi-Tier Architecture

A visible client may communicate with an API gateway, which communicates with multiple backend services and databases. The term client-server therefore describes an interaction pattern, not necessarily a two-machine topology.

### Trust Boundary

The server should not assume a client is trustworthy. Client-side validation improves usability but does not replace authoritative server-side validation and authorization.

## How It Works

A typical interaction is:

```text
User
 │
 ▼
Client Application
 │  HTTP/API request
 ▼
Server / API Layer
 │
 ├── authentication
 ├── validation
 ├── authorization
 ├── business logic
 └── dependency calls
 │
 ▼
Database / Services
 │
 ▼
Server Response
 │
 ▼
Client Rendering / Next Action
```

Failures can occur at any boundary. A client may construct an invalid request, the network may fail, the server may reject the action, a dependency may time out, or the response may be valid but rendered incorrectly by the client.

## When to Use

Use this knowledge when:

- isolating UI versus API defects;
- designing integration tests;
- validating client-side and server-side validation boundaries;
- analyzing network-related failures;
- testing mobile or browser applications backed by APIs;
- tracing data flow through multiple service layers.

## When Not to Use

Do not assume every system follows a classic client-server topology. Peer-to-peer, event-driven, embedded, batch, and local-only systems may use different interaction models. Even in client-server systems, project-specific responsibilities must be confirmed from architecture documentation.

## Advantages

Client-server separation can provide:

- centralized business logic;
- reusable services for multiple clients;
- independent client and server evolution;
- centralized security and data controls;
- scalability through distributed deployment;
- clearer testing boundaries.

## Limitations

Common limitations include:

- network dependency;
- additional latency;
- distributed failure modes;
- compatibility management between client and server versions;
- increased observability needs;
- server or dependency bottlenecks;
- complex retry and partial-failure behavior.

## Examples

### Web Application

A browser displays an order form. The browser validates required fields for usability, then sends the order to the server. The server repeats authoritative validation, checks permissions, persists the order, and returns the created resource.

### Mobile Application with Old Client Version

An older mobile client calls a newer server. Compatibility testing verifies that server changes do not break still-supported client versions.

### Backend-to-Backend Integration

Service A acts as a client of Service B. Although no human-facing UI exists, the same concerns apply: contract validation, authorization, timeout behavior, error mapping, and retry safety.

## Best Practices

- Test authoritative behavior at the server boundary, not only through the UI.
- Verify that invalid or manipulated client input cannot bypass server validation.
- Distinguish client rendering defects from server response defects.
- Include network failure, timeout, and reconnection scenarios where relevant.
- Validate compatibility expectations when clients and servers can be deployed independently.
- Use logs, correlation IDs, traces, or equivalent evidence to follow multi-tier requests.
- Avoid assuming a successful client message means the server completed the business operation.

## Related Knowledge

- `API-Fundamentals.md` defines the interface concepts used between clients and servers.
- `HTTP-Fundamentals.md` describes the protocol commonly used for web client-server communication.
- `Timeout-Handling.md` and `Retry-Strategy.md` cover common network-failure responses.
- `Integration-Testing.md` explains validation across component boundaries.
- `Authentication.md` and `Authorization.md` cover trust and access boundaries.

## References

- IETF HTTP specifications describe standardized client-server communication semantics for HTTP.
- Distributed-systems literature documents latency, partial failure, and independent-component behavior.

Actual responsibilities between client and server must be derived from the target system architecture and requirements.
