# WebSocket

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-12

## Overview

**WebSocket** is a protocol that establishes a persistent, full-duplex communication channel between endpoints after an opening handshake. Unlike ordinary HTTP request-response interactions, either side can send messages after the connection is established.

## Purpose

WebSocket knowledge helps QA test connection lifecycle, authentication, message ordering, reconnection, heartbeat behavior, concurrency, and real-time event delivery.

## Core Concepts

### Opening Handshake

The connection commonly begins through an HTTP upgrade handshake and then switches to WebSocket framing.

### Full Duplex

Client and server can send messages independently.

### Frames and Messages

Data is transmitted through frames that form text or binary messages.

### Persistent Connection

The connection remains open across multiple messages until closed or interrupted.

### Ping / Pong

Control frames can support liveness checks.

### Close Handshake

Endpoints communicate close codes and reasons according to protocol rules.

### Reconnection

Automatic reconnection is an application concern, not a guarantee of the WebSocket protocol.

## How It Works

```text
Client ── handshake ──> Server
Client <== persistent full-duplex channel ==> Server
Client/Server exchange messages
      ↓
close / network failure / reconnect logic
```

## When to Use

Use WebSocket knowledge for chat, live dashboards, collaborative applications, market feeds, device telemetry, multiplayer updates, or other low-latency bidirectional interactions.

## When Not to Use

Do not assume WebSocket guarantees message persistence, replay, exactly-once delivery, or automatic reconnection. Those are application-level concerns.

## Advantages

WebSocket avoids repeated request setup for ongoing bidirectional communication and supports low-latency server-to-client messages.

## Limitations

Persistent connections complicate scaling, load balancing, connection recovery, authorization refresh, observability, and state synchronization.

## Examples

### Authentication Expiry

A token expires while a connection remains open. QA validates whether the server disconnects, refreshes authorization context, or follows another documented policy.

### Network Drop

The client loses connectivity and reconnects. QA verifies whether missed messages are replayed, reconciled, or intentionally lost according to the application contract.

### Multiple Messages

Rapid inbound and outbound messages are tested for ordering, duplication, and state consistency.

## Best Practices

- Test handshake success and rejection.
- Validate authentication and authorization throughout connection lifetime.
- Test abrupt disconnects and clean close handshakes.
- Verify message schema and invalid message handling.
- Test reconnection and missed-event reconciliation according to requirements.
- Include concurrency and connection-limit scenarios where relevant.
- Protect sensitive data in persistent channels and logs.
- Distinguish protocol guarantees from application guarantees.

## Related Knowledge

- `Event-Driven-APIs.md`
- `Authentication.md`
- `Authorization.md`
- `Performance-Testing.md`
- `Integration-Testing.md`

## References

- RFC 6455, **The WebSocket Protocol**.

Application-level message guarantees and reconnection policy must come from the target system design.
