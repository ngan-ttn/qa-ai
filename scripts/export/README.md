# Export Scripts

The export group contains both the existing generic structured-data exporters and the Phase 17 canonical-artifact export layer.

## Canonical Artifact Export

```text
Canonical Markdown
→ strict parser
→ normalized export model
→ generic XLSX/CSV
→ export metadata
→ integrity validation
```

| Script | Responsibility |
|---|---|
| `parse_testcases.py` | Parse the single canonical Test Case table into normalized records. |
| `parse_coverage.py` | Parse the canonical Coverage Review finding inventory and preserve canonical statuses. |
| `parse_regression.py` | Parse regression impact records and the three canonical scope tiers. |
| `export_artifact.py` | Render supported canonical artifacts to generic XLSX/CSV and write provenance sidecars. |
| `validate_export.py` | Compare canonical source semantics with XLSX/CSV round-trip data and sidecar metadata. |

## Existing Generic Exporters

`export_excel.py`, `export_markdown.py`, and `package_output.py` remain backward-compatible generic utilities. They are not the canonical Markdown artifact parser layer.

## Supported Baseline

Phase 17 supports the `generic` profile only unless a vendor import contract is independently verified.

```bash
python scripts/export/export_artifact.py artifacts/Test-Cases.md --type test-cases --format xlsx --output exports/generic/Test-Cases.xlsx
python scripts/export/validate_export.py artifacts/Test-Cases.md exports/generic/Test-Cases.xlsx --type test-cases
```

Canonical rules are defined in `shared/standards/Export.md`.
