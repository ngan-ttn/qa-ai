# Change Intelligence Scripts

Deterministic Phase 19 tooling.

## Flow

```text
analyze_change.py
→ analyze_impact.py
→ plan_incremental_qa.py
→ render_change_report.py
→ validate_change_intelligence.py
```

The tools create revision evidence only. They do not regenerate/approve artifacts, alter freshness, select regression tiers, or execute tests.

`analyze_change.py` compares two existing revision snapshots. Therefore the target revision must be snapshotted before analysis; comparison never mutates either snapshot.
