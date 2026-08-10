# Validation Pattern

## Purpose

The `Validation` pattern defines a reusable reasoning approach for verifying that information, artifacts, or outputs satisfy defined rules, criteria, or expectations.

Its purpose is to confirm correctness, completeness, consistency, and compliance before downstream activities are performed.

This pattern focuses on **verification** rather than evaluation or artifact generation.

---

## When To Use

Apply this pattern whenever AI needs to verify whether information satisfies predefined requirements or acceptance criteria.

Typical use cases include:

- Requirement validation
- Business rule validation
- Scenario validation
- Test case validation
- Output validation
- Rule compliance verification

---

## Core Principles

An effective validation should:

- Validate against explicit criteria.
- Produce objective verification results.
- Avoid subjective judgments.
- Preserve traceability to validation criteria.
- Clearly distinguish compliant and non-compliant items.

---

## Validation Process

A complete validation typically follows these activities.

### 1. Identify Validation Targets

Determine what should be validated.

Typical considerations include:

- Artifacts
- Information
- Outputs
- Business rules
- Requirements

---

### 2. Identify Validation Criteria

Determine the rules or expectations used during validation.

Typical considerations include:

- Standards
- Business rules
- Acceptance criteria
- Quality requirements
- Constraints

---

### 3. Verify Compliance

Evaluate each validation target against the applicable criteria.

Typical considerations include:

- Correctness
- Completeness
- Consistency
- Rule compliance

---

### 4. Identify Validation Results

Determine the outcome of each verification.

Typical considerations include:

- Passed validations
- Failed validations
- Missing information
- Rule violations

---

### 5. Produce Structured Validation Results

Organize validation outcomes into a structured representation suitable for downstream activities.

---

## Expected Outcome

A successful validation should produce:

- Verified artifacts
- Identified validation failures
- Structured validation results
- Traceable validation evidence
- Actionable verification outcomes

---

## Design Guidelines

The validation pattern should:

- Remain domain-independent.
- Validate only against defined criteria.
- Avoid unsupported assumptions.
- Preserve traceability between criteria and results.
- Produce objective validation outcomes.

---

## Relationships

This pattern is commonly used by:

- Requirement Review
- Scenario Review
- Test Case Review
- Regression Review
- Bug Report Review
- API Testing Review

It may also support other skills requiring rule-based verification before downstream activities.

---

## References

- `shared/standards/`
- `shared/templates/`
- `shared/glossary/`