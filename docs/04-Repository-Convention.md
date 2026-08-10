# Repository Convention

> Version: 1.0.0
> Status: Draft
> Last Updated: YYYY-MM-DD

---

# 1. Purpose

## Overview

This document defines the conventions and standards used throughout the QA-AI repository.

Repository conventions ensure that all documentation, Skills, Knowledge, Workflows, Templates, and supporting resources follow a consistent structure and style.

These conventions improve readability, maintainability, collaboration, and long-term scalability.

---

## Objectives

This document aims to:

- Standardize repository organization
- Define naming conventions
- Establish documentation standards
- Ensure consistency across all components
- Simplify repository maintenance

---

# 2. Scope

This document applies to every file and folder within the QA-AI repository, including:

- Documentation
- Skills
- Knowledge
- Workflows
- Templates
- Checklists
- Examples
- Datasets
- Scripts

---

# 3. Repository Structure Convention

The repository follows a fixed top-level structure.

```text
QA-AI/
│
├── README.md
├── LICENSE
├── CHANGELOG.md
├── VERSION
├── .gitignore
│
├── docs/
├── shared/
├── skills/
├── workflows/
├── examples/
├── datasets/
├── output/
└── scripts/
```

Top-level folders should not be renamed without an approved architectural change.

---

# 4. Folder Convention

Each folder has a single responsibility.

| Folder | Purpose |
|----------|---------|
| docs | Framework documentation |
| shared | Reusable resources |
| skills | AI Skills |
| workflows | Workflow definitions |
| examples | Sample inputs and outputs |
| datasets | Testing datasets |
| output | Generated artifacts |
| scripts | Utility scripts |

Folders should not contain unrelated content.

---

# 5. File Naming Convention

## Documentation

Documentation files follow the format:

```
NN-Document-Name.md
```

Examples:

```
01-Architecture.md
02-Core-Concepts.md
05-Skill-Development-Guide.md
```

---

## Skill

Skill folders use Pascal Case.

Examples:

```
Requirement-Analyzer
Scenario-Generator
Risk-Analyzer
```

---

## Knowledge

Knowledge documents use descriptive names.

Examples:

```
Boundary-Value-Analysis.md
Decision-Table.md
REST-API.md
OAuth.md
```

---

## Workflow

Workflow files describe business processes.

Examples:

```
Requirement-To-TestCase.md
Regression-Testing.md
API-Testing.md
```

---

# 6. Markdown Convention

Documentation should use consistent Markdown formatting.

## Heading Levels

```
# Document Title

## Major Section

### Subsection

#### Detail
```

Only one H1 (`#`) is allowed per document.

---

## Lists

Use unordered lists for collections.

```
- Item A
- Item B
- Item C
```

Use ordered lists only when sequence matters.

---

## Tables

Use tables for structured comparisons.

Example:

| Item | Description |
|------|-------------|
| Skill | Execute QA tasks |

---

## Code Blocks

Specify language whenever possible.

Example:

````text
```text
Repository Tree
```

---

## Diagrams

Use ASCII diagrams for simple flows.

Use Mermaid diagrams for complex workflows when supported.

---

# 7. Documentation Convention

Every document should follow a consistent structure.

Recommended sections:

1. Purpose
2. Scope
3. Main Content
4. References

Additional sections may be included if necessary.

---

Each document should include metadata.

Example:

```text
Version

Status

Last Updated
```

---

# 8. Cross-Reference Convention

Documents should reference related documents instead of duplicating information.

Example:

```
See:

02-Core-Concepts.md
```

Avoid copying definitions between documents.

---

# 9. Content Convention

Documentation should be:

- Clear
- Concise
- Consistent
- Platform-independent
- Reusable

Avoid:

- AI-specific instructions
- Personal notes
- Temporary comments
- Duplicate explanations

---

# 10. Versioning Convention

Repository versions follow Semantic Versioning.

```
MAJOR.MINOR.PATCH
```

Example:

```
1.0.0
```

Version history should be maintained in:

```
CHANGELOG.md
```

---

# 11. Contribution Convention

Contributors should:

- Follow repository standards
- Maintain document consistency
- Avoid duplicated content
- Reference existing documentation
- Update related documents when necessary

---

# 12. Review Convention

Before submitting changes, verify:

- Naming conventions
- Markdown formatting
- Internal references
- Grammar
- Broken links
- Duplicate content
- Consistency with repository standards

---

# 13. Repository Do's and Don'ts

## Do

- Follow naming conventions.
- Keep documents focused.
- Reuse shared resources.
- Reference existing documentation.
- Maintain consistent formatting.

---

## Don't

- Duplicate Knowledge.
- Combine multiple responsibilities.
- Break repository structure.
- Rename core folders.
- Introduce undocumented conventions.

---

# 14. References

- README.md
- 01-Architecture.md
- 02-Core-Concepts.md
- 03-Design-Decisions.md
- 05-Skill-Development-Guide.md