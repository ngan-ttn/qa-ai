# Performance Testing

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-12

## Overview

**API performance testing** evaluates responsiveness, throughput, capacity, resource behavior, and stability under defined workloads. It can include load, stress, spike, endurance, and scalability testing depending on the objective.

## Purpose

This article helps QA reason about performance evidence without inventing targets or treating a single response-time measurement as a complete performance assessment.

## Core Concepts

### Response Time / Latency

Elapsed time between request initiation and completion from a defined observation point.

### Throughput

Amount of work completed per unit of time.

### Concurrency

Number of overlapping active users, sessions, connections, or operations.

### Load Test

Evaluates expected or planned workload.

### Stress Test

Pushes beyond expected capacity to understand limits and failure behavior.

### Spike Test

Evaluates sudden workload changes.

### Endurance Test

Evaluates sustained operation for leaks, degradation, or resource exhaustion.

### Percentiles

Percentiles such as p95 or p99 describe tail latency better than averages alone. Exact required percentiles must come from the service objective.

## How It Works

```text
Workload Model
      ↓
Generate controlled traffic
      ↓
Measure latency / throughput / errors / resources
      ↓
Compare with defined objectives
      ↓
Analyze bottlenecks and degradation
```

Performance tests should be run in an environment and with data volumes representative enough for the objective.

## When to Use

Use performance testing for high-volume APIs, latency-sensitive operations, batch endpoints, public integrations, capacity planning, major architectural changes, or explicit non-functional requirements.

## When Not to Use

Do not run disruptive performance tests in production or shared environments without authorization. Do not declare a performance defect without an agreed target or clear regression baseline.

## Advantages

Performance testing exposes bottlenecks, capacity limits, tail-latency problems, resource leaks, and unstable behavior under realistic demand.

## Limitations

Results depend heavily on environment, network, data volume, workload model, warm-up state, caching, and monitoring quality. Synthetic traffic may not match real consumer behavior.

## Examples

### Load Test

Simulate the agreed expected request mix while measuring p95 latency, throughput, and error rate against documented objectives.

### Spike

Increase traffic rapidly and observe autoscaling, queueing, rate limiting, and recovery.

### Endurance

Maintain sustained load long enough to detect connection leaks or gradual memory growth.

## Best Practices

- Define workload and success criteria before execution.
- Use representative request mix and data size.
- Monitor server-side resources and dependencies, not only client latency.
- Separate application errors from generator or network errors.
- Warm up systems consistently when caches or JIT behavior matter.
- Use percentiles and error rates, not averages alone.
- Coordinate tests to avoid disrupting unrelated teams.
- Compare results across equivalent environments when assessing regression.

## Related Knowledge

- `API-Test-Strategy.md`
- `Rate-Limiting.md`
- `Timeout-Handling.md`
- `Retry-Strategy.md`
- `Pagination.md`

## References

- Performance-testing practices from industry load-testing methodologies.
- Service-level objectives and performance thresholds must come from authoritative project or operational requirements.

No universal response-time target applies to all APIs.
