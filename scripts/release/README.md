# Release Tooling

Phase 20 release tooling builds and validates a QA-AI release baseline without replacing subsystem validators.

## Commands

```text
python scripts/release/build_manifest.py --release-id QA-AI-1.0.0 --status Candidate
python scripts/release/validate_manifest.py
python scripts/release/validate_release.py --workspace <feature-path> --revision <REV-N> --execution <run-path>
python scripts/release/generate_release_report.py
```

`validate_release.py` is fail-closed: any mandatory gate failure makes overall release readiness FAIL. The generated evidence is revision-bound and must be rerun after repository changes.
