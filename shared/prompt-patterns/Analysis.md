# Analysis Pattern

## Purpose

The `Analysis` pattern defines a reusable reasoning approach for understanding information before performing downstream activities.

Its purpose is to establish a structured analysis process that identifies objectives, context, scope, relationships, constraints, and uncertainties.

This pattern focuses on **understanding** rather than generating or validating artifacts.

---

## When To Use

Apply this pattern whenever AI needs to understand information before making decisions or producing outputs.

Typical use cases include:

- Requirement analysis
- Feature analysis
- Change analysis
- Impact analysis
- Business process analysis
- Document analysis

---

## Core Principles

An effective analysis should:

- Establish sufficient context before drawing conclusions.
- Distinguish facts from assumptions.
- Identify both explicit and implicit information.
- Preserve the original intent.
- Record uncertainties rather than guessing.

---

## Analysis Process

A complete analysis typically follows these activities:

### 1. Understand Context

Determine the overall purpose and background.

Typical considerations include:

- Business objective
- User objective
- Domain context
- Existing constraints

---

### 2. Identify Scope

Determine what is included and excluded.

Typical considerations include:

- Functional scope
- System boundaries
- Roles and responsibilities
- Dependencies

---

### 3. Identify Key Information

Extract information required for downstream activities.

Typical considerations include:

- Inputs
- Outputs
- Rules
- Relationships
- Constraints

---

### 4. Detect Gaps

Identify information that is incomplete, inconsistent, or ambiguous.

Typical considerations include:

- Missing requirements
- Conflicting statements
- Undefined behaviors
- Open questions

---

### 5. Produce Structured Understanding

Organize the analyzed information into a structured representation suitable for downstream processing.

---

## Expected Outcome

A successful analysis should produce:

- Clear understanding of the subject
- Defined scope
- Structured information
- Identified assumptions
- Identified uncertainties
- Reusable analysis outputs

---

## Design Guidelines

The analysis pattern should:

- Remain domain-independent.
- Avoid generating downstream artifacts.
- Avoid making unsupported assumptions.
- Preserve traceability to the source information.
- Produce outputs suitable for reuse.

---

## Relationships

This pattern is commonly used by:

- Requirement Analyzer
- Business Rule Extractor
- Scenario Generator
- Regression Impact

It may also support other skills requiring structured understanding before reasoning.

---

## References

- `shared/standards/`
- `shared/templates/`
- `shared/glossary/`