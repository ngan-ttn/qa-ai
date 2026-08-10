# Generation Pattern

## Purpose

The `Generation` pattern defines a reusable reasoning approach for producing new artifacts from structured information.

Its purpose is to transform validated inputs into complete, consistent, and reusable outputs that support downstream activities.

This pattern focuses on **creating new artifacts** rather than analyzing, extracting, reviewing, or validating existing information.

---

## When To Use

Apply this pattern whenever AI needs to generate structured outputs from existing information.

Typical use cases include:

- Test scenario generation
- Test case generation
- Business rule generation
- Regression scope generation
- Documentation generation
- Report generation

---

## Core Principles

An effective generation should:

- Be based on validated input information.
- Preserve the original intent.
- Produce complete and internally consistent outputs.
- Avoid unsupported assumptions.
- Generate reusable artifacts.

---

## Generation Process

A complete generation typically follows these activities.

### 1. Understand Inputs

Determine the information required for generation.

Typical considerations include:

- Requirements
- Business rules
- Existing artifacts
- Constraints
- Generation objectives

---

### 2. Identify Generation Objectives

Determine what artifact should be produced.

Typical considerations include:

- Artifact type
- Intended audience
- Expected level of detail
- Output purpose

---

### 3. Apply Generation Rules

Generate the output according to applicable rules and constraints.

Typical considerations include:

- Completeness
- Consistency
- Traceability
- Reusability

---

### 4. Organize the Output

Arrange the generated information into a logical and structured representation.

Typical considerations include:

- Logical sequence
- Grouping
- Readability
- Maintainability

---

### 5. Preserve Traceability

Maintain clear relationships between generated content and supporting input information.

---

## Expected Outcome

A successful generation should produce:

- Complete artifacts
- Consistent outputs
- Structured information
- Traceable content
- Reusable deliverables

---

## Design Guidelines

The generation pattern should:

- Remain domain-independent.
- Generate outputs only from supported information.
- Avoid introducing unsupported assumptions.
- Preserve traceability to source information.
- Produce artifacts suitable for downstream activities.

---

## Relationships

This pattern is commonly used by:

- Scenario Generator
- Test Case Generator
- Business Rule Extractor
- Regression Impact

It may also support other skills requiring structured artifact generation.

---

## References

- `shared/standards/`
- `shared/templates/`
- `shared/glossary/`