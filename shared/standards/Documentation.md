# Documentation Standard

## Purpose

This document defines the documentation standards used throughout the repository.

The objective is to ensure that all documentation is consistent, readable, maintainable, and easy to navigate regardless of its purpose or complexity.

---

## Scope

This standard applies to all Markdown documents in the repository, including:

* Standards
* Templates
* Checklists
* Knowledge documents
* Prompt patterns
* Workflows
* Specifications
* Guides
* README files

---

## Documentation Principles

All documentation SHOULD follow these principles:

* **Consistency** — Follow the same structure and writing style.
* **Clarity** — Present information in a clear and unambiguous manner.
* **Maintainability** — Keep documents easy to update.
* **Reusability** — Write content that can be reused whenever possible.
* **Scalability** — Organize information to support future expansion.

---

## Document Structure

A document SHOULD be organized in the following order:

1. Title
2. Metadata
3. Overview or Purpose
4. Main Content
5. Examples (if applicable)

Not every document requires every section, but the structure SHOULD remain logical and predictable.

---

## Headings

Use hierarchical Markdown headings.

```text
# Document Title

## Major Section

### Subsection

#### Detail
```

Rules:

* A document MUST contain exactly one level-1 heading (`#`).
* Heading levels MUST NOT be skipped.
* Headings SHOULD be concise and descriptive.

---

## Paragraphs

Paragraphs SHOULD:

* Focus on a single idea.
* Be concise.
* Avoid unnecessary repetition.

Prefer short paragraphs over large blocks of text.

---

## Lists

Use bullet lists when presenting unordered information.

Use numbered lists when sequence or order is important.

Nested lists SHOULD be kept shallow whenever possible.

---

## Tables

Tables SHOULD be used for structured information such as:

* Comparisons
* Definitions
* Allowed values
* Reference data

Example:

| Field   | Description        |
| ------- | ------------------ |
| Version | Document version   |
| Status  | Document lifecycle |

Avoid using tables for lengthy explanations.

---

## Code Blocks

Code blocks SHOULD be used for:

* Examples
* Commands
* Configuration
* File structures
* Prompt samples

Specify the language whenever applicable.

Example:

````markdown
```yaml
version: 1.0.0
status: Draft
```
````

---

## File Structure

Directory structures SHOULD use fenced code blocks.

Example:

```text
shared/
├── standards/
├── templates/
└── knowledge/
```

---

## Emphasis

Use emphasis sparingly.

* **Bold** for important terms.
* *Italic* for emphasis.
* `Inline code` for filenames, commands, variables, and technical terms.

Avoid excessive formatting.

---

## References

When referring to another repository document:

* Use its filename.
* Keep references consistent.
* Avoid duplicating information across documents.

Whenever possible, reference the original source instead of copying content.

---

## Writing Style

Documentation SHOULD:

* Use professional English.
* Use active voice whenever practical.
* Prefer simple and direct language.
* Keep terminology consistent throughout the repository.

Avoid:

* Slang
* Informal expressions
* Ambiguous wording

---

## Examples

Include examples when they improve understanding.

Examples SHOULD:

* Be realistic.
* Be concise.
* Reflect repository conventions.

---

## Maintenance

Documentation SHOULD be reviewed periodically to ensure that:

* Content remains accurate.
* References remain valid.
* Examples are up to date.
* Obsolete information is removed.

---

## Best Practices

* Keep one primary topic per document.
* Prefer reusable content over duplication.
* Keep sections independent whenever possible.
* Use consistent terminology across documents.
* Prioritize readability over formatting complexity.
