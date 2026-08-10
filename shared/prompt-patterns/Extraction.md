# Extraction Pattern

## Purpose

The `Extraction` pattern defines a reusable reasoning approach for identifying and organizing relevant information from one or more information sources.

Its purpose is to transform unstructured or semi-structured content into structured information that can be consumed by downstream activities.

This pattern focuses on **identification and organization** rather than analysis, generation, or validation.

---

## When To Use

Apply this pattern whenever AI needs to identify and organize existing information.

Typical use cases include:

- Requirement extraction
- Business rule extraction
- Entity extraction
- Constraint extraction
- Input and output extraction
- Metadata extraction

---

## Core Principles

An effective extraction should:

- Preserve the original meaning.
- Extract only supported information.
- Avoid introducing assumptions.
- Maintain traceability to the source.
- Organize extracted information consistently.

---

## Extraction Process

A complete extraction typically follows these activities.

### 1. Identify Information Sources

Determine the content from which information should be extracted.

Typical considerations include:

- Requirement documents
- User stories
- Specifications
- API documentation
- Existing artifacts

---

### 2. Identify Target Information

Determine which information should be extracted.

Typical considerations include:

- Entities
- Business rules
- Actors
- Constraints
- Inputs
- Outputs
- Relationships

---

### 3. Extract Information

Identify information that is explicitly or implicitly supported by the source.

Typical considerations include:

- Relevant facts
- Structured attributes
- Supporting evidence

---

### 4. Organize Information

Arrange extracted information into a consistent and structured representation.

Typical considerations include:

- Logical grouping
- Classification
- Relationships
- Hierarchies

---

### 5. Preserve Traceability

Maintain the relationship between extracted information and its original source.

---

## Expected Outcome

A successful extraction should produce:

- Structured information
- Clearly identified entities
- Organized relationships
- Preserved source meaning
- Traceable outputs
- Reusable artifacts

---

## Design Guidelines

The extraction pattern should:

- Remain domain-independent.
- Preserve the original meaning.
- Avoid interpretation beyond the source.
- Avoid generating new information.
- Support downstream structured processing.

---

## Relationships

This pattern is commonly used by:

- Requirement Analyzer
- Business Rule Extractor
- Scenario Generator
- Regression Impact

It may also support other skills requiring structured information before reasoning.

---

## References

- `shared/standards/`
- `shared/templates/`
- `shared/glossary/`