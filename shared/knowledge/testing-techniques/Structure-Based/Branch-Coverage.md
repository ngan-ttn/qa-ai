# Branch Coverage

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Branch Coverage** measures whether each possible branch outcome from control-flow decisions has been executed. It is stronger than statement coverage because executing all statements does not necessarily exercise all branch outcomes.

## Purpose

Reveal untested control-flow alternatives such as true/false outcomes, switch cases, loop exits, and exception branches.

## Core Concepts

### Branch
A possible control-flow edge leaving a decision or branching point.

### Decision Outcome
A branch can correspond to true/false, case selection, loop continuation/exit, or implementation-specific alternatives.

### Coverage Ratio
Commonly `executed branches / total branches`, with exact counting dependent on the language and tool.

### Partial Branch
Some tools flag lines where one branch was executed but another was not.

## How It Works

Coverage instrumentation records which control-flow edges execute during tests. QA then inspects unexecuted outcomes and designs additional cases when they represent reachable and meaningful behavior.

## When to Use

Use for conditional logic, validation, error handling, loops, feature flags, security decisions, routing logic, and implementation areas where alternative control paths matter.

## When Not to Use

Do not assume full branch coverage means all compound conditions or paths are covered. Condition coverage and path-oriented analysis may reveal additional gaps.

## Advantages

- Stronger structural signal than statement coverage.
- Exposes untested alternative outcomes.
- Useful for conditional and exception-heavy code.

## Limitations

- Does not prove every atomic condition influenced a decision both ways.
- Does not cover all path combinations.
- Tool definitions of branches may vary.
- Unreachable branches require engineering review rather than artificial tests.

## Examples

For `if (isActive) allow(); else reject();`, tests must execute both `allow` and `reject` branches.

For a loop, branch measurement may require tests that both enter the loop and exit without entering, depending on tool semantics.

## Best Practices

- Investigate each uncovered branch rather than chasing a number.
- Pair with requirement-based coverage.
- Include negative and exception outcomes.
- Confirm whether compiler-generated branches are being counted.
- Escalate unreachable logic for code/design review.

## Related Knowledge

- `Statement-Coverage.md`
- `Decision-Coverage.md`
- `Condition-Coverage.md`
- `Path-Coverage.md`
- `../Foundation/White-Box-Testing.md`

## References

- ISTQB structure-based coverage concepts.
- Target coverage-tool branch semantics.