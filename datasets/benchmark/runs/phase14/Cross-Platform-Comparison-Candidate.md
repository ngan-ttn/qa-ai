# Phase 14 Cross-Platform Comparison — Candidate

## Comparison Metadata

- Comparison ID: `P14-XPLAT-001`
- Run Set: `P14-RUNSET-001`
- Dataset: `REQ-AUTH-001`
- Artifact: `Structured Test Case Model`
- Evaluation Configuration: `EVAL-CRITERIA-001` + `EVAL-RUBRIC-001` + `EVAL-SCORING-001`
- Status: `Complete Candidate — final approval pending`

This record compares the accepted controlled runtime candidate from each supported platform. It is not yet an Approved/Frozen benchmark; promotion depends on the Phase 14 benchmark-record, reproducibility/traceability, and final quality gates.

## Platform Results

| Platform | Run ID | Final Score | Result | Critical Failures | Baseline Eligible | Evidence Status |
|---|---|---:|---|---:|---|---|
| ChatGPT | `P14-RUN-CHATGPT-003` | 100 | PASS | 0 | Yes — Candidate | Complete |
| Claude | `P14-RUN-CLAUDE-001` | 99 | PASS | 0 | Yes — Candidate | Complete |
| Cursor | `P14-RUN-CURSOR-001` | 99 | PASS | 0 | Yes — Candidate | Complete |

## Criterion-Level Comparison

| Criterion | ChatGPT | Claude | Cursor | Observation |
|---|---|---|---|---|
| C01 Requirement Fidelity | L4 | L4 | L4 | No material difference |
| C02 Correctness | L4 | L4 | L4 | No material difference |
| C03 Completeness | L4 | L4 | L4 | No material difference |
| C04 Scope Control | L4 | L4 | L4 | No material difference |
| C05 Assumption Control | L4 | L4 | L4 | No material difference |
| C06 Traceability | L4 | L4 | L4 | No material difference |
| C07 Clarity | L4 | L3 | L3 | Claude and Cursor retain more supporting analysis/verbosity than ChatGPT; non-critical quality difference |
| C08 Testability | L4 | L4 | L4 | No material difference |
| C09 Coverage Efficiency | L4 | L4 | L4 | No material difference |
| C10 Boundary and State Coverage | L4 | L4 | L4 | No material difference |
| C11 Risk Awareness | N/A | N/A | N/A | Supporting-only for this artifact evaluation |
| C12 Internal Consistency | L4 | L4 | L4 | No material difference |

## Controlled-Contract Review

### ChatGPT

The accepted post-fix run retrieves and preserves the authoritative five-attempt threshold, 15-minute duration, reset behavior, locked-state rejection, automatic unlock, and per-account isolation. Earlier ChatGPT FAIL/BLOCKED runs remain historical regression evidence and are not substituted for the accepted run.

### Claude

The accepted run preserves the same authoritative behaviors and executes the canonical requirement-analysis → business-rule → scenario → testcase chain. It explicitly surfaces undefined counter behavior during an active lock and the undefined elapsed-time verification mechanism rather than inventing implementation details. Its C07 deduction reflects verbosity only.

### Cursor

The accepted run preserves the same authoritative behaviors and canonical workflow traceability. Its only scored difference versus ChatGPT is additional verbosity under C07.

## Cross-Platform Equivalence Assessment

The three accepted runs use the same:

- authoritative dataset: `REQ-AUTH-001`;
- target artifact: Structured Test Case Model;
- canonical workflow: `testcase-generation`;
- evaluation criteria: `EVAL-CRITERIA-001`;
- rubric: `EVAL-RUBRIC-001`;
- scoring semantics: `EVAL-SCORING-001`;
- evaluation profile: `canonical-default`.

All three preserve the material product contract and pass without critical failures. Score spread is one point (`100` to `99`) and is attributable to C07 clarity/verbosity, not requirement fidelity, correctness, scope, assumptions, traceability, testability, boundary coverage, or internal consistency.

## Candidate Conclusion

**PASS — three-platform comparison candidate complete.**

Measured results:

- ChatGPT: `100 / Excellent / PASS`;
- Claude: `99 / Excellent / PASS`;
- Cursor: `99 / Excellent / PASS`.

No material cross-platform QA behavior divergence is identified in the accepted run set. The comparison is eligible to proceed to benchmark-record review and reproducibility/traceability validation.

It must remain `Candidate` until the Phase 14 final quality gate approves the regression-ready baseline.
