# Performance Monitoring

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Database performance monitoring** collects and analyzes evidence about workload latency, throughput, resource use, waits, blocking, query behavior, storage, connections, and capacity over time.

## Purpose

This article helps QA distinguish database performance symptoms from causes and build evidence-based non-functional validation without inventing universal thresholds.

## Core Concepts

### Latency
Time required to complete an operation or query. Percentiles are often more informative than averages for variable workloads.

### Throughput
Amount of work completed per unit time, such as queries or transactions per second.

### Resource Utilization
CPU, memory, storage I/O, network, cache, temporary space, and connection usage can constrain performance.

### Waits and Blocking
Sessions can spend time waiting for locks, I/O, CPU scheduling, log flush, network, or other resources.

### Query-Level Metrics
Execution count, duration, rows, reads, writes, plan changes, and errors help isolate expensive workloads.

### Baseline
A baseline captures expected behavior under a defined environment and workload. Thresholds must come from approved SLOs, capacity goals, or benchmark criteria.

## How It Works

Monitoring combines DBMS telemetry, operating-system/platform metrics, query statistics, logs, traces, and application observations. Correlation across the same time window is essential.

## When to Use

Use performance monitoring for load/performance testing, regressions, timeout investigation, capacity planning, failover exercises, and production incident analysis where authorized.

## When Not to Use

Do not classify high CPU or a slow query as a defect without workload context and requirements. Do not apply arbitrary “healthy” thresholds from generic knowledge.

## Advantages

Monitoring reveals trends, contention, plan regressions, saturation, and intermittent issues that functional assertions alone cannot capture.

## Limitations

Telemetry can add overhead, be sampled, miss short spikes, or be inaccessible in managed environments. Correlation does not automatically prove causation.

## Examples

### Blocking Spike
API latency rises while database wait metrics show lock waits and one long transaction. This narrows investigation toward contention rather than CPU capacity.

### Plan Regression
The same query's latency increases after deployment while its execution plan and read volume change substantially.

### Capacity Trend
Connection usage approaches the configured pool or DB limit during peak load, producing queueing before CPU is saturated.

## Best Practices

- Define workload, environment, and success criteria before measurement.
- Compare percentiles and throughput, not averages alone.
- Correlate application and database timestamps.
- Capture query plans and waits for reproducible slow paths.
- Compare against a controlled baseline when assessing regression.
- Protect sensitive SQL text and parameter values in exported evidence.
- Treat thresholds as project-specific.

## Related Knowledge

- `Query-Optimization.md`
- `Execution-Plans.md`
- `Indexes.md`
- `Locking.md`
- `Database-Architecture.md`
- `../qa/Quality-Metrics.md`

## References

- Target DBMS monitoring and observability documentation.
- Performance engineering literature.