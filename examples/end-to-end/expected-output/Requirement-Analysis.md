# Requirement Input

## Purpose

This file defines the standard requirement input structure for the QA-AI end-to-end workflow.

It represents the primary information provided to QA-AI before requirement analysis and downstream QA artifact generation begin.

The structure is intentionally flexible.

A requirement does not need to contain every section defined in this template. QA-AI should analyze the information that is available, identify missing or ambiguous information, and avoid inventing unsupported business behavior.

---

## Usage

Replace the placeholder content in this file with the requirement to be analyzed.

The input may originate from sources such as:

- User stories.
- Business requirements.
- Functional specifications.
- Acceptance criteria.
- Feature descriptions.
- Change requests.
- Product requirements.
- Consolidated requirement notes.

The requirement may be complete, partial, structured, or unstructured.

QA-AI is responsible for interpreting the supplied information according to the applicable skills and workflows.

---

## Input Template

### Feature

`<Feature name or short description>`

---

## User Story

If available:

```text
As a <user / role>

I want <capability or action>

So that <business value or objective>
```

If the source requirement does not use the user-story format, provide the original requirement description instead.

---

## Background

Describe the business or functional context relevant to the requested change.

Include available information such as:

- Current behavior.
- Business problem.
- Reason for the change.
- Relevant workflow context.
- Existing limitations.

If this information is unavailable, the section may be omitted.

---

## Requirements

Provide the known functional requirements.

Example structure:

```text
1. <Requirement>

2. <Requirement>

3. <Requirement>
```

Requirements should preserve the meaning of the original source information.

Do not add assumed behavior only to make the requirement appear complete.

---

## Acceptance Criteria

Provide acceptance criteria when available.

They may use Given / When / Then:

```text
### AC-01 — <Acceptance Criterion Name>

Given <initial condition>

When <action or event>

Then <expected behavior>
```

or any other format supplied by the requirement source.

Acceptance criteria are optional when they are not available.

---

## Business Rules

Include explicitly provided business rules when available.

Example:

```text
- <Business rule>
- <Constraint>
- <Validation rule>
```

Do not derive additional rules in this input file.

Business-rule extraction is performed by the downstream QA-AI capability.

---

## Roles and Permissions

Provide known actors, roles, or permission constraints when applicable.

Example:

```text
Role:
<role>

Allowed Actions:
<known actions>

Restricted Actions:
<known restrictions>
```

This section may be omitted when role-specific behavior is not part of the requirement.

---

## Data and Validation Rules

Provide explicitly defined data requirements when applicable.

Examples include:

```text
Required fields
Optional fields
Allowed values
Validation rules
Minimum / maximum values
Supported formats
Uniqueness rules
```

Only source-defined rules should be included.

---

## State or Status Rules

Provide known states, statuses, or state transitions when the feature contains state-dependent behavior.

Example:

```text
Draft
    ↓
Submitted
    ↓
Approved
```

or:

```text
Status = Approved
→ Editing is not allowed
```

This section is optional.

---

## Error Handling

Provide known error conditions and expected error behavior when defined.

Example:

```text
Condition:
<error condition>

Expected Behavior:
<message or system response>
```

Do not invent error messages or error handling that are not present in the source requirement.

---

## Integration Context

Provide known integration information when the feature interacts with other systems or components.

Examples:

```text
External service
API
Database
Background process
Notification service
Payment provider
Partner system
```

This information is especially useful for impact and regression analysis.

If integration information is unknown, leave it unspecified.

---

## Existing System Context

Provide known information about existing behavior or dependencies when available.

Examples include:

- Existing workflow.
- Related modules.
- Upstream dependencies.
- Downstream dependencies.
- Existing APIs.
- Existing data behavior.
- Existing authentication or authorization behavior.

This information improves regression analysis.

However, it is optional.

When existing-system context is not provided, QA-AI must identify regression dependencies that require investigation rather than inventing them.

---

## Notes

Provide any additional information supplied with the requirement.

Examples:

- Design notes.
- Known limitations.
- Scope restrictions.
- References to mockups.
- Technical notes.
- Business decisions.

---

## References

List supporting requirement sources when available.

Example:

```text
- <Document>
- <Ticket>
- <Design>
- <API specification>
```

References are optional.

---

## Minimum Input

QA-AI should not require the complete template before beginning analysis.

At minimum, the input must provide enough information to identify the requested feature or change.

For example:

```text
Feature:
Account Lock

Requirement:
Lock a user's account after repeated failed login attempts.
```

QA-AI may begin analysis from this information but should identify missing details that prevent reliable downstream conclusions.

---

## Handling Incomplete Requirements

Missing information must remain visible throughout the workflow.

The expected behavior is:

```text
Information Available
        ↓
Analyze

Information Ambiguous
        ↓
Identify Ambiguity

Information Missing
        ↓
Clarification Required

System Dependency Unknown
        ↓
Investigation Required
```

The expected behavior is not:

```text
Information Missing
        ↓
Invent Assumption
        ↓
Treat as Requirement
```

---

## Input Principles

Requirement input should follow these principles:

1. Preserve the meaning of the source requirement.
2. Do not add unsupported business behavior.
3. Distinguish explicit information from contextual notes.
4. Preserve important constraints and acceptance criteria.
5. Include existing-system context when it is known.
6. Allow incomplete requirements to enter the analysis workflow.
7. Keep missing information visible for downstream QA analysis.

---

## Relationship to Sample Requirement

This file defines the generic requirement input structure.

The accompanying file:

```text
Sample-Requirement.md
```

provides a concrete example of a requirement that can be processed by the end-to-end workflow.

The relationship is:

```text
Requirement.md
      ↓
Generic Input Contract

Sample-Requirement.md
      ↓
Concrete Example Input

QA-AI Workflow
      ↓
Expected QA Artifacts
```

`Requirement.md` should therefore remain reusable and feature-independent, while `Sample-Requirement.md` may contain feature-specific example data.