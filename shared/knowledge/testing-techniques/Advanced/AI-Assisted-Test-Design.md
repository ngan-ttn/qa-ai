# AI-Assisted Test Design

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**AI-Assisted Test Design** uses AI systems to support analysis, scenario ideation, test generation, coverage review, prioritization, transformation, or quality checking while keeping authoritative requirements and human review as control points.

## Purpose

Improve speed and breadth of test-design work without allowing generated content to silently invent requirements, business rules, expected results, or risk assumptions.

## Core Concepts

### Source Grounding
Generated tests should be traceable to supplied requirements, rules, interfaces, domain knowledge, and approved repository knowledge.

### Human Review
AI output is a draft or reasoning aid until validated against project context and quality gates.

### Coverage Expansion
AI can suggest edge cases, combinations, states, risks, and missing clarifications but should distinguish source-supported items from hypotheses.

### Hallucination Risk
AI can produce plausible but unsupported behavior, thresholds, permissions, statuses, or technical details.

### Repeatability
Prompts, model/version context, source artifacts, and review criteria should be captured when reproducibility matters.

## How It Works

```text
Authoritative inputs
      ↓
Select task + relevant knowledge
      ↓
AI analysis / generation
      ↓
Traceability + assumption check
      ↓
Human / automated quality review
      ↓
Approved QA artifact
```

## When to Use

Use for requirement decomposition, scenario generation, edge-case ideation, test-data ideas, test-case drafting, coverage review, regression impact analysis, and document quality checks.

## When Not to Use

Do not treat AI output as authoritative expected behavior. Avoid autonomous production actions, legal/clinical conclusions, security exploitation, or irreversible test execution without appropriate controls.

## Advantages

- Accelerates repetitive analysis and drafting.
- Can surface overlooked dimensions.
- Supports consistent use of reusable knowledge.
- Helps transform unstructured inputs into structured QA artifacts.

## Limitations

- Can hallucinate unsupported rules.
- Quality depends on source completeness and prompt/task design.
- Model behavior can vary over time.
- Sensitive data and tool permissions require governance.
- Generated volume can hide duplicate or low-value tests.

## Examples

An AI system reads a requirement and proposes scenarios categorized by business rule, boundary, state, permission, integration, and error path, while marking missing information as clarification questions rather than assumptions.

A coverage reviewer compares generated test cases with extracted rules and identifies untested conditions without creating new acceptance criteria.

## Best Practices

- Ground generation in explicit sources.
- Require assumption and clarification handling.
- Preserve traceability from source to output.
- Use deterministic templates where artifact consistency matters.
- Review duplicates, contradictions, and unsupported expected results.
- Protect sensitive project data according to policy.
- Evaluate output against golden datasets and quality rubrics where available.

## Related Knowledge

- `Prompt-Based-Test-Generation.md`
- `../Experience-Based/Exploratory-Testing.md`
- `../Specification-Based/Decision-Table-Testing.md`
- `../../qa/Requirement-Analysis.md`
- `../../../prompt-patterns/`
- `../../../../skills/`

## References

- Repository AI/QA standards, prompts, datasets, and evaluation guidance.
- Current model/provider documentation when a specific AI system is used.