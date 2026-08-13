# Decision Coverage

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Decision Coverage** evaluates whether each decision in the implementation has produced every relevant overall outcome, typically true and false. In many practical tools it is closely related to branch coverage, but terminology and counting can differ.

## Purpose

Ensure that control decisions are exercised across their possible overall outcomes while preserving clarity about the distinction between decision outcome and individual condition behavior.

## Core Concepts

### Decision
An expression or control point whose evaluated result determines subsequent execution.

### Outcome
The overall result of the decision, commonly true/false.

### Compound Decision
A decision can contain several atomic conditions connected by logical operators.

### Decision vs Condition
A decision may evaluate both true and false even if one atomic condition never independently takes both values.

## How It Works

Identify implementation decisions, design inputs that force each overall outcome, execute with coverage instrumentation, then confirm the resulting branches and assertions behave as expected.

## When to Use

Use where control-flow decisions drive important behavior, especially in validation, permissions, calculations, safety logic, or error handling.

## When Not to Use

Do not use decision coverage alone when risk depends on atomic condition independence, short-circuit behavior, or complex boolean combinations. Condition coverage or MC/DC may be more appropriate.

## Advantages

- Directly targets decision outcomes.
- Helps reveal one-sided logic tests.
- Provides a clear structural objective for conditional code.

## Limitations

- Does not prove each atomic condition was tested independently.
- Can be confused with branch coverage depending on tool terminology.
- Does not guarantee path completeness or business-rule completeness.

## Examples

For `if (age >= 18 && verified)`, one test can make the decision true and another false while never testing `verified = false` independently from the age condition.

A permission decision may produce both allow and deny while still leaving one internal condition unexercised due to short-circuit evaluation.

## Best Practices

- Define the tool's decision metric before using it.
- Pair structural coverage with meaningful behavior assertions.
- Inspect compound decisions for hidden condition gaps.
- Use MC/DC only where justified by risk or external standards.
- Avoid treating 100% decision coverage as proof of requirement completeness.

## Related Knowledge

- `Branch-Coverage.md`
- `Condition-Coverage.md`
- `Modified-Condition-Decision-Coverage-(MC-DC).md`
- `../Foundation/White-Box-Testing.md`

## References

- ISTQB decision coverage terminology.
- Target language and coverage-tool documentation.