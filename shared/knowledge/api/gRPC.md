# gRPC

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-12

## Overview

**gRPC** is a remote procedure call framework commonly using Protocol Buffers for interface definition and serialization and HTTP/2 for transport. Services define strongly typed methods and messages from which client and server code can be generated.

## Purpose

gRPC knowledge helps QA validate service contracts, serialization, status handling, deadlines, metadata, streaming, compatibility, and service-to-service integrations.

## Core Concepts

### Service Definition

A `.proto` definition describes services, RPC methods, request/response messages, and field identifiers.

### Unary RPC

One request produces one response.

### Server Streaming

One request produces a stream of responses.

### Client Streaming

A stream of requests produces one response.

### Bidirectional Streaming

Both client and server exchange message streams concurrently.

### Metadata

Metadata carries request or response context such as credentials or tracing information.

### Deadline and Cancellation

Clients can set deadlines and cancel calls. Servers should observe deadlines and propagate them where appropriate.

### Status

gRPC defines its own status-code model distinct from HTTP status codes.

### Field Compatibility

Protocol Buffer field numbers and types have compatibility rules. Reusing removed field numbers or making incompatible changes can break consumers.

## How It Works

```text
.proto contract
      ↓
generated client/server interfaces
      ↓
client invokes RPC
      ↓
HTTP/2 + protobuf message exchange
      ↓
response / stream / gRPC status
```

## When to Use

Use gRPC knowledge for internal service meshes, low-latency service calls, strongly typed contracts, streaming integrations, or systems explicitly built on gRPC.

## When Not to Use

Do not test gRPC as if it were a normal JSON REST API. HTTP status, URI, and body expectations differ because gRPC defines application semantics through its own protocol conventions.

## Advantages

Strong contracts, code generation, efficient binary serialization, multiplexed HTTP/2 transport, and native streaming make gRPC effective for many service-to-service systems.

## Limitations

Human inspection is less convenient than JSON, browser support may require gRPC-Web or gateways, and compatibility errors in protobuf schemas can be subtle.

## Examples

### Unary Call

`GetOrder(GetOrderRequest) returns (Order)` is tested for valid ID, unknown ID, permission denial, deadline exceeded, and malformed metadata.

### Streaming

QA verifies message ordering, cancellation, partial stream failure, backpressure assumptions, and consumer reconnection according to the contract.

### Schema Evolution

A field is removed. Its protobuf field number should not be reused for a different meaning in later versions.

## Best Practices

- Treat `.proto` files as contract artifacts.
- Validate gRPC status and error details, not HTTP status alone.
- Test deadlines and cancellation.
- Verify metadata propagation and authentication.
- Include streaming-specific lifecycle and disconnect scenarios.
- Review protobuf compatibility during contract changes.
- Use generated clients or protocol-aware tools to avoid invalid assumptions about wire format.

## Related Knowledge

- `API-Fundamentals.md`
- `Contract-Testing.md`
- `Integration-Testing.md`
- `Timeout-Handling.md`
- `WebSocket.md`
- `API-Versioning.md`

## References

- gRPC documentation and protocol specifications.
- Protocol Buffers language and compatibility guidance.
- HTTP/2 specification for underlying transport concepts.

Service-specific deadlines, metadata, and status mappings are contract-specific.
