# Comparison Pattern

## Purpose

The `Comparison` pattern defines a reusable reasoning approach for evaluating two or more items against a common set of criteria.

Its purpose is to identify similarities, differences, impacts, strengths, weaknesses, and trade-offs while preserving objective reasoning.

This pattern focuses on **evaluation** rather than generation or validation.

---

## When To Use

Apply this pattern whenever AI needs to compare multiple items before making a decision or producing recommendations.

Typical use cases include:

- Requirement comparison
- Feature comparison
- Current vs. expected behavior analysis
- Alternative solution evaluation
- Impact comparison
- Regression comparison
- Output quality comparison

---

## Core Principles

An effective comparison should:

- Compare items using consistent criteria.
- Evaluate comparable information only.
- Distinguish objective observations from interpretations.
- Identify both similarities and differences.
- Explain significant impacts where applicable.

---

## Comparison Process

A complete comparison typically follows these activities.

### 1. Identify Comparison Targets

Determine the items to be compared.

Typical considerations include:

- Objects
- Documents
- Features
- Behaviors
- Outputs

---

### 2. Establish Comparison Criteria

Define consistent evaluation dimensions.

Typical considerations include:

- Functionality
- Behavior
- Scope
- Quality
- Risk
- Performance
- Constraints

---

### 3. Compare Information

Evaluate each item using the same criteria.

Typical considerations include:

- Similarities
- Differences
- Missing information
- Conflicting information

---

### 4. Assess Impact

Determine the significance of identified differences.

Typical considerations include:

- Business impact
- Technical impact
- Testing impact
- User impact

---

### 5. Produce Structured Comparison

Organize comparison results into a structured representation suitable for downstream reasoning.

---

## Expected Outcome

A successful comparison should produce:

- Clearly identified similarities
- Clearly identified differences
- Structured comparison results
- Identified impacts
- Objective evaluation
- Reusable comparison outputs

---

## Design Guidelines

The comparison pattern should:

- Remain domain-independent.
- Use consistent comparison criteria.
- Avoid subjective judgments without evidence.
- Preserve traceability to the compared sources.
- Support downstream decision making.

---

## Relationships

This pattern is commonly used by:

- Regression Impact
- Coverage Reviewer
- Requirement Analyzer
- Test Case Reviewer

It may also support other skills requiring structured comparison before reasoning.

---

## References

- `shared/standards/`
- `shared/templates/`
- `shared/glossary/`