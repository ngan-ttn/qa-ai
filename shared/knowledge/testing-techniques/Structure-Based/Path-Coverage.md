# Path Coverage

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Path Coverage** concerns execution of distinct control-flow paths through a unit or component. Because loops and combinations can create very large or infinite path spaces, practical path testing usually targets selected, bounded, or basis paths rather than every theoretical path.

## Purpose

Reason about sequence-dependent structural behavior beyond isolated statements or branches, especially where combinations of decisions create materially different execution routes.

## Core Concepts

### Control-Flow Path
A sequence of executed nodes and edges through the code.

### Feasible Path
A path that can actually occur for some valid program state/input.

### Infeasible Path
A syntactically apparent path that cannot occur because constraints make it unreachable.

### Loop Paths
Loops can create unbounded numbers of paths unless iterations are constrained.

### Basis / Selected Paths
Practical testing chooses representative independent or risk-significant paths rather than attempting exhaustive enumeration.

## How It Works

Build or inspect the control-flow structure, identify meaningful paths, constrain loops, select risk-significant routes, design inputs to traverse them, and verify both execution and outcomes.

## When to Use

Use for small critical algorithms, transaction logic, error/cleanup paths, safety logic, or functions where decision sequences materially affect correctness.

## When Not to Use

Do not pursue exhaustive path coverage for complex real-world code with loops, recursion, concurrency, or combinatorial branching. It quickly becomes infeasible.

## Advantages

- Captures interactions between successive decisions.
- Can reveal sequence-specific defects.
- Useful for critical compact logic.

## Limitations

- Path explosion is severe.
- Infeasible paths complicate measurement.
- Refactoring can change paths without changing business behavior.
- Full path coverage is rarely practical.

## Examples

A function with two independent binary decisions already has up to four straight-line outcome combinations; adding a loop multiplies possible paths dramatically.

A cleanup routine may execute only after one specific error path, making selected path analysis valuable even if global path coverage is impossible.

## Best Practices

- Define bounded path objectives.
- Focus on risk-significant and independent paths.
- Treat infeasible paths explicitly.
- Bound loop iteration cases using meaningful values.
- Combine with requirement-based tests.
- Avoid using path percentages as a universal quality threshold.

## Related Knowledge

- `Branch-Coverage.md`
- `Decision-Coverage.md`
- `Condition-Coverage.md`
- `../Foundation/White-Box-Testing.md`

## References

- Control-flow testing literature.
- Target static-analysis and coverage-tool documentation.