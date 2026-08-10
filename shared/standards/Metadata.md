# Metadata Standard

## Purpose

This document defines the standard metadata format used throughout the repository.

Metadata provides essential information about a document, including its identity, ownership, lifecycle, and maintenance status. Consistent metadata improves discoverability, version tracking, and long-term maintainability.

---

## Scope

This standard applies to all documentation stored in this repository unless explicitly stated otherwise.

Examples include:

* Standards
* Templates
* Checklists
* Knowledge documents
* Prompt patterns
* Guides
* Specifications
* Workflows

---

## Metadata Schema

Documents should include the following metadata block at the beginning of the file.

```text
Version: 1.0.0
Status: Draft
Last Updated: YYYY-MM-DD
```

Additional metadata may be introduced when required by a specific project or workflow.

---

## Field Definitions

### Version

Identifies the current version of the document.

**Format**

```text
MAJOR.MINOR.PATCH
```

Example:

```text
1.0.0
```

---

### Status

Represents the current lifecycle stage of the document.

Allowed values:

| Status     | Description                                    |
| ---------- | ---------------------------------------------- |
| Draft      | Initial work in progress.                      |
| Review     | Under review and subject to change.            |
| Approved   | Reviewed and accepted as the current standard. |
| Deprecated | No longer recommended for future use.          |
| Archived   | Retained for historical reference only.        |

---

### Last Updated

Indicates the date of the most recent content change.

Format:

```text
YYYY-MM-DD
```

Example:

```text
2026-08-03
```

---

## Metadata Rules

### Required Fields

The following fields are mandatory for all repository documents:

* Version
* Status
* Last Updated

---

### Placement

Metadata should appear immediately after the main document title.

Example:

```markdown
# Naming Standard

Version: 1.0.0

Status: Draft

Last Updated: 2026-08-03
```

---

### Consistency

Metadata values must accurately reflect the current state of the document.

Whenever document content changes, update the metadata if required by the versioning rules.

---

## Versioning

This repository follows Semantic Versioning principles.

### Major

Increment when introducing breaking structural or conceptual changes.

Example:

```text
1.0.0 → 2.0.0
```

---

### Minor

Increment when adding new sections or expanding existing standards without breaking compatibility.

Example:

```text
1.1.0 → 1.2.0
```

---

### Patch

Increment when making corrections that do not significantly change the document.

Examples include:

* Grammar fixes
* Typographical corrections
* Formatting improvements
* Clarifications

Example:

```text
1.0.1 → 1.0.2
```

---

## Status Lifecycle

```text
Draft
   │
   ▼
Review
   │
   ▼
Approved
   │
   ├────────────► Deprecated
   │                   │
   │                   ▼
   └──────────────► Archived
```

---

## Example

```text
Version: 1.0.0
Status: Approved
Last Updated: 2026-08-03
```

---

## Best Practices

* Keep metadata concise and accurate.
* Update metadata whenever the document lifecycle changes.
* Follow Semantic Versioning consistently.
* Avoid introducing custom metadata unless it provides repository-wide value.
* Keep metadata consistent across all documents.
