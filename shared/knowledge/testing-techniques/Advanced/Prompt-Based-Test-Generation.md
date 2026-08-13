# Prompt-Based Test Generation

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Prompt-Based Test Generation** uses structured natural-language instructions to guide an AI model in producing QA artifacts such as scenarios, test cases, edge cases, or coverage suggestions from supplied source material.

## Purpose

Provide a disciplined prompt-design approach that improves consistency, grounding, output structure, and reviewability of AI-generated testing artifacts.

## Core Concepts

### Task Definition
The prompt must state the intended QA objective clearly: analyze, generate scenarios, generate detailed cases, review coverage, or another bounded task.

### Source Context
Requirements, business rules, interfaces, constraints, and relevant knowledge should be provided or referenced explicitly.

### Output Contract
Expected sections, fields, terminology, prioritization, and formatting reduce ambiguity.

### Guardrails
Instructions should prohibit invented requirements, duplicate cases, vague expected results, unsafe actions, and unsupported assumptions.

### Iterative Review
Generation quality is improved by self-review or reviewer prompts that check traceability, gaps, duplication, and contradictions.

## How It Works

```text
Source material
    +
Task / role / constraints
    +
Output schema
    +
Quality guardrails
        ↓
AI generation
        ↓
Self-review / coverage review
        ↓
Human approval or downstream workflow
```

## When to Use

Use when AI is expected to transform requirements into structured QA artifacts or perform repeatable document analysis using explicit prompt contracts.

## When Not to Use

Do not rely on prompt wording to compensate for missing source information. Prompts cannot make unknown business rules authoritative.

## Advantages

- Fast to iterate.
- Portable across many AI systems.
- Can enforce consistent output structure.
- Makes task and guardrails explicit.

## Limitations

- Models may still ignore or misinterpret instructions.
- Prompt behavior can vary by model/version.
- Very large contexts can dilute important constraints.
- Overly prescriptive prompts can suppress useful reasoning.

## Examples

A test-case prompt states the requirement source, one-objective-per-case rule, mandatory columns, allowed priority values, traceability requirement, and instruction to list clarifications instead of inventing missing behavior.

A coverage-review prompt compares artifacts against extracted business rules and reports missing coverage without rewriting the requirement.

## Best Practices

- Separate source facts from instructions.
- Define the output contract explicitly.
- State assumption and clarification rules.
- Require measurable expected results.
- Avoid giant prompts that duplicate the knowledge base unnecessarily.
- Test prompts against representative datasets.
- Version prompts when used in production workflows.

## Related Knowledge

- `AI-Assisted-Test-Design.md`
- `../../../../shared/prompt-patterns/`
- `../../../../skills/`
- `../../../../workflows/`
- `../../qa/Requirement-Analysis.md`

## References

- `shared/prompt-patterns/`
- Repository skills, workflows, datasets, and evaluation rubrics.