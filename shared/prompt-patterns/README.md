# Prompt Patterns

## Purpose

The `prompt-patterns` module defines reusable prompting patterns that support consistent AI reasoning across QA capabilities.

Rather than providing task-specific prompts, this module establishes common reasoning approaches that can be shared by multiple skills and workflows.

Its goal is to improve consistency, maintainability, and reusability throughout the QA-AI framework.

---

## Scope

This module contains generic prompt patterns that describe how AI should approach different types of reasoning tasks.

It does not contain complete prompts for individual skills or workflows.

Instead, each pattern represents a reusable reasoning strategy that can be combined with domain knowledge, templates, and standards.

---

## Module Structure

```text
shared/
└── prompt-patterns/
    ├── README.md
    ├── Analysis.md
    ├── Comparison.md
    ├── Extraction.md
    ├── Generation.md
    ├── Review.md
    ├── Transformation.md
    └── Validation.md
```

---

## Prompt Patterns

### Analysis

Provides reasoning patterns for understanding information before making decisions.

Typical activities include:

- Understanding context
- Identifying objectives
- Determining scope
- Recognizing relationships
- Detecting missing information

---

### Comparison

Provides reasoning patterns for evaluating multiple items against defined criteria.

Typical activities include:

- Identifying similarities and differences
- Comparing alternatives
- Evaluating trade-offs
- Assessing impacts
- Supporting decision making

---

### Extraction

Provides reasoning patterns for identifying and organizing relevant information.

Typical activities include:

- Extracting entities
- Identifying business rules
- Capturing requirements
- Organizing structured information
- Separating facts from assumptions

---

### Generation

Provides reasoning patterns for producing new artifacts from structured inputs.

Typical activities include:

- Generating scenarios
- Generating test cases
- Producing summaries
- Creating reports
- Building structured outputs

---

### Review

Provides reasoning patterns for evaluating the quality of existing artifacts.

Typical activities include:

- Identifying issues
- Evaluating completeness
- Checking consistency
- Assessing quality
- Providing review findings

---

### Transformation

Provides reasoning patterns for converting information into different representations while preserving meaning.

Typical activities include:

- Restructuring information
- Converting formats
- Simplifying content
- Expanding structured information
- Adapting outputs for downstream processing

---

### Validation

Provides reasoning patterns for verifying correctness and compliance.

Typical activities include:

- Checking completeness
- Verifying correctness
- Validating consistency
- Confirming rule compliance
- Detecting conflicts

---

## Relationships

Prompt patterns are shared resources that may be used by multiple modules.

Typical usage includes:

- Skills
- Workflows
- Shared templates
- Shared standards

Prompt patterns do not replace templates or standards.

Instead, they define reusable reasoning approaches that complement those resources.

---

## Design Principles

Prompt patterns should:

- Be reusable across multiple capabilities.
- Remain independent of specific business domains.
- Focus on reasoning rather than output formatting.
- Encourage consistent AI behavior.
- Support maintainable prompt engineering.

---

## References

Related modules include:

- `shared/standards/`
- `shared/templates/`
- `shared/glossary/`
- `skills/`
- `workflows/`