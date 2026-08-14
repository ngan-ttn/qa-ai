# Phase 14 Cross-Platform Comparison — Candidate

## Comparison Metadata

- Comparison ID: `P14-XPLAT-001`
- Run Set: `P14-RUNSET-001`
- Dataset: `REQ-AUTH-001`
- Artifact: `Structured Test Case Model`
- Evaluation Configuration: `EVAL-CRITERIA-001` + `EVAL-RUBRIC-001` + `EVAL-SCORING-001`
- Status: `Partial — Claude pending`

This record is intentionally not an approved cross-platform benchmark. It captures only the measured results currently available and preserves the unresolved Claude runtime dependency.

## Platform Results

| Platform | Run ID | Final Score | Result | Critical Failures | Baseline Eligible | Evidence Status |
|---|---|---:|---|---:|---|---|
| ChatGPT | `P14-RUN-CHATGPT-003` | 100 | PASS | 0 | Yes — Candidate | Complete |
| Claude | `P14-RUN-CLAUDE-001` | Pending | Pending | Pending | No decision | Runtime unavailable |
| Cursor | `P14-RUN-CURSOR-001` | 99 | PASS | 0 | Yes — Candidate | Complete |

## Criterion-Level Comparison

| Criterion | ChatGPT | Claude | Cursor | Current Observation |
|---|---|---|---|---|
| C01 Requirement Fidelity | L4 | Pending | L4 | No material difference between available runs |
| C02 Correctness | L4 | Pending | L4 | No material difference between available runs |
| C03 Completeness | L4 | Pending | L4 | No material difference between available runs |
| C04 Scope Control | L4 | Pending | L4 | No material difference between available runs |
| C05 Assumption Control | L4 | Pending | L4 | No material difference between available runs |
| C06 Traceability | L4 | Pending | L4 | No material difference between available runs |
| C07 Clarity | L4 | Pending | L3 | Cursor is more verbose than required; non-critical quality difference |
| C08 Testability | L4 | Pending | L4 | No material difference between available runs |
| C09 Coverage Efficiency | L4 | Pending | L4 | No material difference between available runs |
| C10 Boundary and State Coverage | L4 | Pending | L4 | No material difference between available runs |
| C11 Risk Awareness | N/A | Pending | N/A | Supporting-only for this artifact evaluation |
| C12 Internal Consistency | L4 | Pending | L4 | No material difference between available runs |

## Available-Run Contract Review

### ChatGPT

The accepted post-fix run retrieves and preserves the authoritative 5-attempt threshold, 15-minute duration, reset behavior, locked-state behavior, automatic unlock, and per-account isolation. The prior ChatGPT FAIL/BLOCKED runs remain regression evidence and are not substituted for the accepted run.

### Cursor

The accepted run preserves the same authoritative behaviors and canonical workflow traceability. Its only scored difference versus ChatGPT is additional verbosity under C07.

### Claude

No measured result exists yet. Claude must remain `Pending` rather than being assigned a synthetic score, PASS, FAIL, or baseline eligibility state.

## Interim Conclusion

The two available measured runs are comparable at the product-behavior and evaluation-contract level and both satisfy the quality threshold without critical failures. However, Phase 14 cross-platform comparison remains incomplete because the defined run set requires ChatGPT, Claude, and Cursor.

This candidate comparison must be updated after `P14-RUN-CLAUDE-001` is executed and evaluated. It must not be promoted to Approved while Claude is pending.
