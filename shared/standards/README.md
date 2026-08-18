# Standards

## Overview

The `shared/standards/` directory contains the core standards that define how documentation, prompts, knowledge, roadmap progress, operational workspaces, artifact exports, and AI-generated outputs are created and maintained across this repository.

These standards establish a consistent foundation for contributors and AI assistants so repository artifacts follow shared conventions regardless of domain or purpose.

This directory serves as the **single source of truth** for repository-wide standards.

---

## Objectives

The standards aim to:

- establish consistent conventions across the repository;
- improve readability and maintainability;
- encourage reusable documentation and prompts;
- standardize AI-generated outputs;
- define quality gates for reusable knowledge;
- keep roadmap progress tied to validated repository state;
- govern project workspace identity, provenance, lifecycle, revisions, dependencies, and freshness;
- preserve canonical artifact semantics across operational exports;
- support future expansion without introducing inconsistencies.

---

## Standards

| Document | Description |
|---|---|
| `Metadata.md` | Defines standard metadata, versioning, status, and maintenance information. |
| `Naming.md` | Defines naming conventions for directories, files, documents, prompts, workflows, and related assets. |
| `Documentation.md` | Defines writing and Markdown formatting standards. |
| `Output.md` | Defines quality and formatting standards for AI-generated outputs. |
| `Prompt.md` | Defines principles for reusable and maintainable prompts. |
| `Knowledge-Article.md` | Defines structure, depth, quality gates, ownership, and freeze criteria for knowledge articles. |
| `Roadmap-Progress.md` | Defines component status tracking, phase aggregation, roadmap synchronization, and the future automation contract. |
| `Workspace.md` | Defines canonical project/feature workspace structure, source/artifact identity, revision preservation, lifecycle, dependency, provenance, and freshness rules. |
| `Export.md` | Defines canonical-source preservation, normalized export models, XLSX/CSV rendering, provenance, freshness, profiles, and export-integrity validation. |

---

## Usage

Before creating or modifying repository artifacts:

1. identify the applicable standard or standards;
2. review the corresponding document;
3. follow the defined conventions and quality gates;
4. update the relevant source-of-truth metadata when tracked component status changes;
5. apply the standards consistently throughout the artifact.

For roadmap-tracked work, file creation alone must not be interpreted as completion. The component must satisfy its defined quality gate before its progress status is promoted.

Operational project artifacts under `workspace/` must additionally follow `Workspace.md`; lifecycle and freshness are separate dimensions and project artifact approval must not be inferred from AI generation/self-review.

Derived spreadsheet/CSV/import artifacts must follow `Export.md`; exported representations do not become canonical merely because they are easier to execute or import.

---

## Design Principles

All standards in this directory are based on:

- **Consistency** — apply the same conventions across the repository.
- **Clarity** — keep standards understandable and unambiguous.
- **Reusability** — design rules that apply across domains and workflows.
- **Maintainability** — keep standards easy to evolve intentionally.
- **Scalability** — support repository growth without major restructuring.
- **Traceability** — connect implementation state to the standards and progress records that govern it.
- **Quality before status** — do not promote an artifact or component merely because a physical file exists.

---

## Related Directories and Files

These standards are referenced by:

- `shared/templates/`
- `shared/checklists/`
- `shared/prompt-patterns/`
- `shared/knowledge/`
- `shared/glossary/`
- `skills/`
- `workflows/`
- `workspace/`
- `scripts/export/`
- `docs/11-Roadmap.md`
- `roadmap-status.json`

---

## Maintenance

Standards should be updated only when a repository-wide convention needs to be introduced, refined, or replaced.

Changes must preserve consistency across existing artifacts wherever possible. Changes to roadmap tracking semantics require corresponding review of `roadmap-status.json`, `docs/11-Roadmap.md`, and any automation that consumes them. Changes to workspace lifecycle/provenance semantics require corresponding review of `workspace/`, `shared/schemas/`, and `scripts/workspace/`. Changes to export semantics require corresponding review of `shared/schemas/` and `scripts/export/`.
