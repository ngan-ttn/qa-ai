# Checklists

## Purpose

The `checklists` module defines the quality validation criteria used throughout the QA-AI framework.

It provides reusable validation checklists for assessing the quality, completeness, and consistency of structured QA artifacts.

The module establishes **what should be validated**, but does not define **how artifacts are generated** or **how workflows are executed**.

---

## Role In The Architecture

The `checklists` module serves as the validation layer of the shared resources.

Within the shared architecture:

- **Standards** define project-wide rules and conventions.
- **Templates** define the expected structure of QA artifacts.
- **Checklists** define the validation criteria used to review those artifacts.
- **Prompt Patterns** define reusable prompting techniques for AI capabilities.
- **Glossary** defines standardized terminology used across the repository.
- **Knowledge** provides reusable QA and domain knowledge that supports artifact generation and validation.

Together, these modules provide the reusable foundation consumed by skills and workflows.

---

## Scope

The module defines validation criteria for structured QA artifacts, including:

- Requirement Analysis
- Business Rules
- Test Scenarios
- Test Cases
- Coverage Assessment
- Regression Impact Analysis

Each checklist focuses on validating a single artifact type.

---

## Structure

```text
shared/
└── checklists/
    ├── README.md
    ├── Requirement-Analysis.md
    ├── Business-Rule.md
    ├── Scenario.md
    ├── Testcase.md
    ├── Coverage.md
    └── Regression.md
```

Each document defines the validation criteria for one QA artifact.

---

## Relationship With Other Modules

### Standards

Standards define the rules and conventions that QA artifacts should follow.

Checklists verify compliance with those standards.

---

### Templates

Templates define the expected structure of QA artifacts.

Checklists validate whether generated artifacts follow the required structure and contain the expected information.

---

### Prompt Patterns

Prompt patterns provide reusable prompting techniques for AI capabilities.

Checklists evaluate the quality of generated outputs independently of the prompting strategy.

---

### Glossary

The glossary defines standardized terminology used throughout the QA-AI framework.

Checklists should use glossary terms consistently to ensure clear and unambiguous validation criteria.

---

### Knowledge

The knowledge module provides reusable QA concepts, testing practices, and domain-specific information.

Checklists may reference knowledge resources where additional context is required, but should not duplicate their content.

---

### Skills

Skills produce structured QA artifacts.

Checklists provide reusable validation criteria for reviewing those artifacts.

---

### Workflows

Workflows may incorporate checklists as validation steps to ensure artifact quality before downstream activities.

---

## Design Principles

The `checklists` module follows these principles.

### Artifact-Oriented

Each checklist validates a single QA artifact.

Validation criteria should not span multiple artifact types.

---

### Objective Validation

Validation criteria should be specific, measurable, and unambiguous.

Different reviewers should reach consistent conclusions when applying the same checklist.

---

### Reusable Validation

Validation criteria should be reusable across different skills, workflows, and QA activities.

Validation logic should not be duplicated across multiple checklists.

---

### Standards Compliance

Validation criteria should align with the conventions defined by the `standards` module.

Checklists should reference standards rather than redefine them.

---

### Template Awareness

Validation should consider the expected structure defined by the corresponding template.

A checklist validates both the completeness and quality of an artifact.

---

### Knowledge Independence

Checklists define validation criteria only.

Business knowledge, domain knowledge, and implementation details belong to the `knowledge` module.

---

## Module Boundary

This module defines:

- Validation criteria
- Quality checkpoints
- Acceptance conditions
- Review guidance for QA artifacts

This module does not define:

- Documentation standards
- Output templates
- Prompt construction
- QA knowledge
- Business knowledge
- Skill implementations
- Workflow logic

These responsibilities belong to other modules within the QA-AI framework.

---

## Usage

Checklists are intended to be applied after QA artifacts have been generated.

They may be used by:

- QA engineers performing manual reviews
- AI skills performing quality assessment
- QA workflows requiring validation before downstream activities

The module provides a consistent validation approach across the entire QA-AI framework.