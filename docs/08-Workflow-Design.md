# Versioning

> Version: 1.0.0
> Status: Draft
> Last Updated: YYYY-MM-DD

---

# 1. Purpose

## Overview

This document defines the versioning strategy used throughout the QA-AI framework.

Versioning enables contributors to track changes, maintain compatibility, and manage the evolution of the repository over time.

A consistent versioning policy helps users understand the impact of updates and supports long-term maintenance.

---

## Objectives

This document aims to:

- Standardize version management
- Define release policies
- Support backward compatibility
- Improve change traceability
- Simplify repository maintenance

---

# 2. Scope

This versioning policy applies to:

- Repository
- Documentation
- Skills
- Knowledge
- Workflows
- Templates
- Checklists

---

# 3. Version Format

QA-AI follows Semantic Versioning.

```
MAJOR.MINOR.PATCH
```

Example:

```
1.0.0
```

---

## MAJOR

Increment when introducing incompatible changes.

Examples:

- Repository restructuring
- Breaking architecture changes
- Removing supported components

---

## MINOR

Increment when adding new functionality without breaking compatibility.

Examples:

- New Skills
- New Knowledge
- New Workflows
- New Templates

---

## PATCH

Increment when making backward-compatible improvements.

Examples:

- Documentation updates
- Grammar fixes
- Bug fixes
- Minor clarifications

---

# 4. Repository Version

The repository has a single official version stored in:

```
VERSION
```

The same version should appear in:

- README
- Release Notes
- Git Tags

---

# 5. Document Version

Each document should include metadata.

Example:

```
Version: 1.0.0
Status: Draft
Last Updated: YYYY-MM-DD
```

Major document revisions should update the document version.

---

# 6. Skill Versioning

Each Skill maintains its own version.

Version updates should occur when:

- Input changes
- Output changes
- Logic changes
- Structure changes

Documentation-only changes may use PATCH increments.

---

# 7. Knowledge Versioning

Knowledge versions should change when:

- Concepts are added
- Definitions change
- Best practices are updated
- References are revised

Editorial corrections may use PATCH increments.

---

# 8. Workflow Versioning

Workflow versions should change when:

- Execution sequence changes
- Skills are added or removed
- Inputs change
- Outputs change

Minor documentation updates do not require a MAJOR version.

---

# 9. Release Types

QA-AI supports three release types.

## Major Release

Introduces significant architectural or functional changes.

Example:

```
2.0.0
```

---

## Minor Release

Introduces new capabilities while maintaining compatibility.

Example:

```
1.2.0
```

---

## Patch Release

Fixes defects or improves documentation.

Example:

```
1.2.3
```

---

# 10. Changelog

All notable changes should be recorded in:

```
CHANGELOG.md
```

Each release should include:

- Version
- Release date
- Summary
- Added
- Changed
- Fixed
- Removed (if applicable)

---

# 11. Backward Compatibility

Whenever possible:

- Existing Skills should continue to work.
- Existing Knowledge should remain valid.
- Existing Workflows should not break.

Breaking changes should only occur in MAJOR releases.

---

# 12. Deprecation Policy

Components should not be removed immediately.

Recommended lifecycle:

```
Active

↓

Deprecated

↓

Archived

↓

Removed
```

Deprecation should include:

- Reason
- Replacement (if available)
- Planned removal version

---

# 13. Release Process

Each release should follow this sequence.

```
Development

↓

Review

↓

Testing

↓

Documentation Update

↓

Version Update

↓

CHANGELOG Update

↓

Release

↓

Tag
```

---

# 14. Version Review Checklist

Before releasing a new version, verify:

- Version number is correct
- CHANGELOG is updated
- Documentation is synchronized
- References remain valid
- Repository builds successfully
- Deprecated items are documented

---

# 15. References

- README.md
- CHANGELOG.md
- VERSION
- 04-Repository-Convention.md
- 09-Contribution.md