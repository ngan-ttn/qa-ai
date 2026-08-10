# How To Use

> Version: 1.0.0
> Status: Draft
> Last Updated: YYYY-MM-DD

---

# 1. Purpose

## Overview

This document provides guidance on how to use the QA-AI framework.

It explains how to navigate the repository, locate resources, select appropriate Skills, and execute Workflows for common QA activities.

This guide is intended for end users rather than framework maintainers.

---

## Objectives

This guide aims to:

- Help new users get started
- Explain repository navigation
- Demonstrate common usage patterns
- Promote effective reuse of Skills and Knowledge
- Reduce onboarding time

---

# 2. Who Should Use This Guide?

This guide is intended for:

- QA Engineers
- Test Analysts
- Test Leads
- Automation Engineers
- AI Prompt Engineers
- Contributors who want to use existing Skills

---

# 3. Before You Begin

Before using the repository, it is recommended to read:

1. README.md
2. 01-Architecture.md
3. 02-Core-Concepts.md

These documents provide the foundation for understanding the framework.

---

# 4. Repository Overview

The repository is organized into the following main areas:

```text
docs/
shared/
skills/
workflows/
examples/
datasets/
output/
scripts/
```

Each folder serves a specific purpose as defined in the repository documentation.

---

# 5. Typical Usage Flow

A typical usage sequence is:

```text
Understand Requirement
        │
        ▼
Select Workflow
        │
        ▼
Prepare Input
        │
        ▼
Execute Skills
        │
        ▼
Review Output
        │
        ▼
Refine if Necessary
```

---

# 6. Finding the Right Skill

Choose a Skill based on the QA task.

Examples:

| QA Task | Recommended Skill |
|----------|-------------------|
| Requirement Review | Requirement Analyzer |
| Business Logic | Business Rule Extractor |
| Risk Assessment | Risk Analyzer |
| Scenario Creation | Scenario Generator |
| Test Case Design | Test Case Generator |
| API Validation | API Test Generator |
| Database Validation | SQL Validation |

Always reuse an existing Skill before creating a new one.

---

# 7. Using Knowledge

Before executing a Skill:

- Review related Knowledge documents.
- Understand applicable testing principles.
- Refer to relevant standards or best practices.

Knowledge provides context but does not execute tasks.

---

# 8. Using Workflows

For complex QA activities, use predefined Workflows instead of running Skills independently.

A Workflow coordinates multiple Skills into a structured process.

Example:

```text
Requirement
        │
        ▼
Requirement Analyzer
        │
        ▼
Business Rule Extractor
        │
        ▼
Risk Analyzer
        │
        ▼
Scenario Generator
        │
        ▼
Test Case Generator
```

---

# 9. Reviewing Outputs

After execution:

- Verify completeness
- Validate accuracy
- Check formatting
- Review against Checklists
- Confirm business coverage

Generated outputs should be reviewed before use.

---

# 10. Best Practices

Recommended practices include:

- Read the relevant documentation first.
- Reuse existing Skills.
- Reuse existing Knowledge.
- Follow predefined Workflows.
- Validate outputs before publishing.
- Keep generated artifacts organized.

---

# 11. Common Mistakes

Avoid the following:

- Skipping prerequisite documentation
- Using the wrong Skill for the task
- Ignoring existing Knowledge
- Modifying shared resources unnecessarily
- Duplicating Skills or Workflows
- Assuming AI outputs are always correct

---

# 12. Frequently Asked Questions

## Where should I start?

Begin with the README and Architecture documentation.

---

## Can I create my own Skill?

Yes.

Follow the guidance in:

```
05-Skill-Development-Guide.md
```

---

## How do I add Knowledge?

Refer to:

```
06-Knowledge-Management.md
```

---

## How do I build a Workflow?

Refer to:

```
07-Workflow-Design.md
```

---

## How do I contribute?

Refer to:

```
09-Contribution.md
```

---

# 13. Troubleshooting

If you encounter issues:

- Verify repository structure
- Confirm you are using the correct Skill
- Check references
- Review documentation
- Ensure the latest version is being used

If the issue persists, consult the maintainers or review the relevant documentation.

---

# 14. References

- README.md
- 01-Architecture.md
- 02-Core-Concepts.md
- 05-Skill-Development-Guide.md
- 06-Knowledge-Management.md
- 07-Workflow-Design.md
- 09-Contribution.md