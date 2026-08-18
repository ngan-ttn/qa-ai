# Export Standard

> Version: 1.0.0  
> Status: Draft  
> Last Updated: 2026-08-18

## Purpose

This standard defines how canonical QA-AI Markdown artifacts are converted into operational spreadsheet, CSV, and test-management import representations without changing the canonical artifact semantics.

The canonical Markdown artifact remains the source of truth. Every export is a derived representation.

---

## Core Contract

```text
Canonical Markdown Artifact
        ↓ strict parser
Normalized Export Model
        ↓ renderer/profile
Derived Export
```

An edited export MUST NOT silently replace or redefine the canonical Markdown source.

Phase 17 baseline supports:

- `Test-Cases.md`;
- `Coverage-Review.md`;
- `Regression-Analysis.md`;
- generic XLSX/CSV export.

Vendor-specific profiles may be added only when the external import contract is verified. QA-AI MUST NOT invent a vendor schema.

---

## Normalized Models

Normalized models remove presentation-only Markdown syntax while preserving semantic fields, IDs, ordering, traceability, and status/tier semantics.

For Test Cases, numbered steps represented with `<br>` in Markdown are normalized into an ordered list. Renderers may convert that list into real line breaks for XLSX/CSV.

Unknown or unresolved values remain explicit. Export tooling MUST NOT manufacture missing values.

---

## Strict Parsing

Parsers MUST consume the canonical artifact representation. They MUST fail rather than silently reinterpret noncanonical structures when required headers or inventory representations are missing.

For Test Cases:

- the source inventory is the single table under `## Test Cases`;
- each `TC-*` appears exactly once;
- section-per-testcase content is not a supported canonical input;
- the canonical column names and order are preserved.

---

## Export Integrity

Every export MUST preserve, where applicable:

- unique record IDs;
- record count;
- field values;
- ordered steps;
- expected results;
- priority/status/tier semantics;
- traceability references.

Equal row counts alone are insufficient. A duplicate ID plus a missing ID is a validation failure even when total counts match.

Presentation-equivalent transformations such as Markdown `<br>` to an XLSX line break are allowed when normalized semantics remain equal.

---

## Export Metadata

Each generated export SHOULD have a sidecar `<artifact>.export.json` recording at least:

- schema version;
- artifact type;
- canonical source path;
- source SHA-256;
- export path and format;
- export profile;
- normalized record count;
- export timestamp;
- framework Git revision when available.

The source checksum is the deterministic freshness baseline for the export.

---

## Export Freshness

Export freshness is separate from artifact lifecycle.

```text
Current — source checksum matches export metadata
Stale   — source checksum differs from export metadata
```

Exports do not use the canonical artifact Draft/Review/Approved lifecycle.

---

## XLSX Rules

Generic spreadsheets SHOULD:

- preserve canonical column order;
- use one primary record per row;
- freeze the header row;
- enable filters;
- wrap multiline content;
- render ordered test steps with real line breaks;
- avoid merged cells that impair filtering/import;
- preserve UTF-8 text and identifiers.

Styling is operational only and MUST NOT encode new QA semantics.

---

## CSV Rules

Generic CSV output MUST:

- use one primary record per row;
- quote multiline content correctly;
- preserve unique IDs and canonical field order;
- encode multiline steps as embedded line breaks;
- remain importable by common spreadsheet tools.

UTF-8 with BOM is recommended for Windows/Excel interoperability.

---

## Coverage Semantics

Coverage exports MUST preserve the canonical sufficiency statuses exactly:

```text
Covered
Weakly Covered
Gap
Blocked
```

Legacy or vendor-specific labels MUST NOT replace canonical semantics inside the normalized model.

---

## Regression Semantics

Regression exports MUST preserve both the impact inventory and the three canonical execution-scope tiers:

```text
Minimum / Release-Gate Regression
Recommended Regression
Full Changed-Feature Verification
```

Tier membership and reported counts MUST reconcile with the unique selected test case IDs.

---

## Profiles

An export profile maps normalized QA-AI fields to a target file/import representation.

`generic` is the Phase 17 baseline profile.

A vendor profile MUST NOT be marked supported until its required columns, value constraints, and import behavior are verified from an authoritative specification or validated sample.

Profiles define mapping only. They do not authorize REST/API synchronization or bidirectional updates.

---

## Round-Trip Validation

Phase 17 round-trip validation means:

```text
Markdown
→ Normalized Model A
→ XLSX/CSV
→ Normalized Model B
→ semantic comparison
```

It does not mean writing exported data back into the canonical Markdown source.

---

## Workspace Location

Operational exports belong under:

```text
workspace/projects/<project>/features/<feature>/exports/
```

`exports/` is derived content and is not part of the canonical artifact baseline.

---

## Out of Scope

This standard does not define:

- test execution results;
- bug/defect synchronization;
- Jira/AIO/TestRail/Xray API writes;
- bidirectional synchronization;
- requirement/change interpretation;
- regression-scope generation;
- Excel/CSV overwrite of canonical Markdown.

---

## Validation Requirements

Before an export is accepted, verify that:

- canonical source parsing succeeds;
- unique IDs reconcile;
- record counts reconcile;
- mandatory semantic fields survive export/import normalization;
- multiline steps/outcomes are preserved;
- source checksum/provenance is recorded;
- stale exports are detectable;
- unsupported vendor mappings are not invented.

A semantic-loss, duplicate-ID, missing-ID, or source-count mismatch is a validation failure.
