# Core Concepts

> Version: 1.0.0  
> Status: Draft  
> Last Updated: YYYY-MM-DD

---

# 1. Purpose

## Overview

This document defines the core concepts used throughout the QA-AI framework.

Every document, Skill, Workflow, Template, and Knowledge module must use the terminology defined here.

The purpose of this document is to establish a common language that ensures consistency across the repository.

---

## Objectives

This document aims to:

- Define the core concepts of QA-AI
- Eliminate ambiguous terminology
- Standardize communication
- Provide a common vocabulary
- Serve as the single source of truth for repository terminology

---

# 2. Scope

This document defines conceptual models only.

It does **not** describe:

- Architecture
- Repository structure
- Implementation details
- Development guidelines

Those topics are covered in other documentation.

---

# 3. Concept Relationship

The concepts in QA-AI are related as follows:

```

User
│
▼
Workflow
│
▼
Skill
│
├──────────────┐
│              │
▼              ▼
Knowledge   Template
│              │
└──────┬───────┘
▼
Output

```

Workflow coordinates Skills.

Skills consume Knowledge and Templates.

Outputs are generated according to Templates using Knowledge.

---

# 4. Core Concepts

## 4.1 Repository

### Definition

The Repository is the complete collection of documentation, knowledge, reusable resources, workflows, skills, and supporting assets that together form the QA-AI framework.

### Responsibilities

- Organize project assets
- Provide version control
- Maintain documentation
- Store reusable resources

---

## 4.2 Knowledge

### Definition

Knowledge represents reusable domain expertise that can be consumed by multiple Skills.

Knowledge contains facts, principles, methodologies, standards, or reference information.

Knowledge does not execute tasks.

---

### Characteristics

- Reusable
- Platform independent
- Version controlled
- Execution independent

---

### Examples

- Boundary Value Analysis
- Equivalence Partitioning
- Decision Table Testing
- HTTP Status Codes
- SQL JOIN Types
- OAuth Concepts
- RBAC Principles

---

### Does NOT include

- Prompt instructions
- Workflow logic
- AI behavior
- Generated outputs

---

## 4.3 Skill

### Definition

A Skill is a reusable execution capability that performs a single QA task.

Each Skill transforms an input into an output using predefined Knowledge, Templates, and Standards.

---

### Characteristics

- Single Responsibility
- Reusable
- Stateless
- Predictable
- Testable

---

### Examples

- Requirement Analyzer
- Scenario Generator
- Test Case Generator
- Risk Analyzer
- SQL Validator

---

### Does NOT include

- Business knowledge
- Repository rules
- Multiple unrelated tasks

---

## 4.4 Workflow

### Definition

A Workflow defines the sequence in which multiple Skills are executed to achieve a complete QA objective.

A Workflow coordinates Skills but does not replace them.

---

### Characteristics

- Sequential
- Reusable
- Modular
- Extensible

---

### Example

Requirement

↓

Requirement Analysis

↓

Business Rule Extraction

↓

Scenario Generation

↓

Test Case Generation

---

## 4.5 Template

### Definition

A Template defines the expected structure and formatting of generated outputs.

Templates ensure consistency regardless of the AI platform.

---

### Examples

Requirement Analysis Template

Scenario Template

Test Case Template

Bug Report Template

---

### Purpose

- Standardize outputs
- Improve readability
- Simplify validation

---

## 4.6 Checklist

### Definition

A Checklist defines validation criteria used to verify completeness and quality.

A Checklist does not generate content.

It verifies content.

---

### Examples

Requirement Checklist

API Testing Checklist

Regression Checklist

Bug Report Checklist

---

### Purpose

- Reduce omissions
- Improve quality
- Support review

---

## 4.7 Standard

### Definition

A Standard defines repository-wide rules and conventions.

Standards ensure consistency across all components.

---

### Examples

Naming Convention

Markdown Style

Versioning Rules

Documentation Rules

Output Formatting Rules

---

## 4.8 Example

### Definition

An Example demonstrates how inputs are transformed into outputs.

Examples are reference materials.

They are not reusable Knowledge.

---

### Purpose

- Demonstration
- Learning
- Testing
- Validation

---

## 4.9 Dataset

### Definition

A Dataset is a collection of sample data used for testing, demonstrations, or Skill validation.

Datasets are not Knowledge.

---

### Examples

Sample Requirements

API Specifications

SQL Scripts

Existing Test Cases

---

## 4.10 Output

### Definition

Output is the final artifact produced by a Skill or Workflow.

---

### Examples

Requirement Analysis

Business Rules

Test Scenarios

Test Cases

Regression Reports

Coverage Reports

---

# 5. Concept Comparison

| Concept | Purpose | Produces Output | Reusable |
|----------|----------|----------------|-----------|
| Knowledge | Provide expertise | No | Yes |
| Skill | Execute a task | Yes | Yes |
| Workflow | Coordinate Skills | Yes | Yes |
| Template | Define structure | No | Yes |
| Checklist | Validate quality | No | Yes |
| Standard | Define rules | No | Yes |
| Example | Demonstrate usage | No | Yes |
| Dataset | Provide sample data | No | Yes |
| Output | Final artifact | Yes | No |

---

# 6. Concept Dependencies

```

Workflow
│
▼
Skill
│
├───────────────┐
│               │
▼               ▼
Knowledge   Template
│               │
├───────────────┤
▼
Checklist
│
▼
Standard
│
▼
Output

```

Concepts should only interact through defined relationships.

---

# 7. Terminology Guidelines

To maintain consistency:

- Use the defined terminology in all documentation.
- Avoid introducing synonyms for existing concepts.
- Do not redefine concepts in other documents.
- Reference this document whenever terminology clarification is required.

---

# 8. Common Misconceptions

### Knowledge is not a Skill.

Knowledge stores information.

Skills perform actions.

---

### Workflow is not a Skill.

A Workflow orchestrates Skills.

A Skill performs work.

---

### Template is not an Output.

A Template defines structure.

An Output is generated content.

---

### Checklist is not a Template.

A Checklist validates.

A Template structures.

---

### Dataset is not Knowledge.

Datasets provide sample data.

Knowledge provides reusable expertise.

---

# 9. References

- README.md
- 01-Architecture.md
- 03-Design-Decisions.md
- 04-Repository-Convention.md