# Regression Analysis — Account Lock After Failed Login Attempts

## Regression Summary

This artifact analyzes the change impact of temporary account locking using `Sample-Requirement.md`, the upstream QA artifact chain, and existing coverage. Because no architecture, API contract, database design, integration map, or implementation detail is supplied, confirmed requirement-derived impact is separated from potential/unknown dependencies.

Canonical scope recommendation:

- **Minimum / Release-Gate Regression:** 10 existing test cases
- **Recommended Regression:** 18 existing test cases
- **Full Changed-Feature Verification:** 20 existing test cases

Counts are based on unique `TC-*` IDs listed in the tier sections below.

---

## Change Overview

The confirmed change adds account-specific consecutive-failure tracking, a five-failure lock threshold, successful-login reset, locked-state rejection/message, a 30-minute temporary lock, automatic unlock, restored authentication, and restarted failure tracking after unlock.

---

## Regression Impact / Coverage

| Impact ID | Area / Module | Change Relationship | Regression Scope / Behavior to Revalidate | Impact Type | Evidence / Traceability | Priority | Existing Coverage Reference | Decision |
|---|---|---|---|---|---|---|---|---|
| IMP-001 | Login Authentication | Direct | Valid login succeeds only when credentials are valid and account is not locked; existing normal login remains functional. | Confirmed | R1–R3; TS-001; TC-001 | High | TC-001 | Include |
| IMP-002 | Failed Login Handling | Direct | Incorrect-password rejection remains functional and participates in account-specific tracking. | Confirmed | R4–R5; BR-001; TS-002, TS-003 | High | TC-002, TC-003 | Include |
| IMP-003 | Lock Threshold | Direct | Failures 1–4 remain unlocked; fifth consecutive failure introduces locked state. | Confirmed | R6, R8; AC-01, AC-02; BR-002 | High | TC-004–TC-006 | Include |
| IMP-004 | Counter Reset | Direct | Successful login before threshold resets current failure sequence; later failures do not combine with prior sequence. | Confirmed | R7; AC-05; BR-003 | High | TC-007–TC-009 | Include |
| IMP-005 | Locked-State Authentication | Direct | Password authentication is rejected throughout active lock, including correct password. | Confirmed | R10; AC-03; BR-005 | High | TC-012, TC-013 | Include |
| IMP-006 | User Feedback | Direct | Locked-account login displays the defined temporary-lock message. | Confirmed | R11; AC-03; BR-006 | Medium | TC-014 | Include |
| IMP-007 | Time-Based State | Direct | Locked state remains active before the 30-minute period expires. | Confirmed | R9; BR-004 | High | TC-015 | Include |
| IMP-008 | Automatic Recovery | Direct | Account automatically transitions to unlocked when the lock period expires. | Confirmed | R12; AC-04; BR-007 | High | TC-016 | Include |
| IMP-009 | Post-Unlock Authentication | Direct | Normal valid authentication is available again after automatic unlock. | Confirmed | R13; AC-04; BR-008 | High | TC-017 | Include |
| IMP-010 | Post-Unlock Tracking | Direct | New failed-login tracking sequence begins after automatic unlock. | Confirmed | R14; BR-009 | High | TC-018, TC-019 | Include |
| IMP-011 | Account Isolation | Direct | Failure/lock state remains account-specific and does not affect unrelated registered accounts. | Confirmed | R5; BR-001 | High | TC-010, TC-011 | Include |
| IMP-012 | Confirmed Lifecycle | Direct | Core lock lifecycle remains coherent across threshold, active lock, expiration, and restored authentication. | Confirmed | R1–R14; TS-020 | High | TC-020 | Include |
| POT-001 | Lock Expiration Boundary | Potential | Exact request behavior precisely at 30-minute expiration requires clarification before deterministic regression expectation. | Potential | R9/R12 define duration but exact boundary semantics unresolved. | — | CTS-003 | Clarify |
| POT-002 | Locked-Attempt Counter/Timer | Potential | Determine whether attempts during active lock change counter or restart/extend duration. | Potential | Requirement defines rejection only. | — | CTS-001, CTS-002 | Clarify |
| POT-003 | Cross-Session / Device | Potential | Determine whether failed-login state aggregates across sessions/browsers/devices. | Potential | No aggregation contract supplied. | — | CTS-004, CTS-005 | Clarify |
| POT-004 | Concurrency | Potential | Determine simultaneous near-threshold update behavior before defining regression expectations. | Potential | No concurrency contract supplied. | — | CTS-006 | Clarify |
| POT-005 | Existing Sessions | Potential | Determine effect of new lock on sessions authenticated before lock. | Potential | Existing-session behavior not supplied. | — | CTS-007 | Clarify |
| POT-006 | Password Management | Potential | Determine password reset/change interaction with lock/failure state. | Potential | Password-management interaction not supplied. | — | CTS-008 | Clarify |
| POT-007 | Unknown Account | Potential | Determine failure handling for unregistered email. | Potential | Unknown-account behavior not supplied. | — | CTS-009 | Clarify |
| POT-008 | API / Database / Technical Mechanism | Unsupported by current evidence | Do not create mandatory regression against endpoints, status codes, schemas, SQL, persistence fields, or timer implementation without actual contracts. | Potential | No technical contracts in input. | — | N/A | Exclude / Clarify if later evidence appears |

---

## Regression Scope Tiers

### Minimum / Release-Gate Regression — 10 cases

`TC-001`, `TC-002`, `TC-005`, `TC-006`, `TC-008`, `TC-010`, `TC-012`, `TC-015`, `TC-016`, `TC-017`

Rationale: covers baseline valid/invalid authentication, both sides of the critical lock threshold, reset behavior, account isolation, locked-state bypass prevention, pre-expiry lock, automatic unlock, and restored authentication. These are the smallest directly changed/high-risk behaviors needed for release-gate confidence.

### Recommended Regression — 18 cases

Minimum set plus:

`TC-004`, `TC-007`, `TC-009`, `TC-011`, `TC-014`, `TC-018`, `TC-019`, `TC-020`

Unique total: **18**.

Rationale: adds lower-bound threshold behavior, additional reset partitions, unaffected-account authentication, required user feedback, post-unlock tracking/re-lock, and full lifecycle coherence.

### Full Changed-Feature Verification — 20 cases

Recommended set plus:

`TC-003`, `TC-013`

Unique total: **20** (`TC-001`–`TC-020`).

These two depth cases provide additional focused tracking and active-lock rejection verification but are not required in the default Recommended tier because equivalent release-critical behavior is already represented by stronger/focused coverage.

---

## Excluded Scope

No API/database/architecture-specific regression is confirmed by the supplied end-to-end input. Potential dependencies remain outside executable tiers until authoritative evidence establishes them.

---

## Entry Criteria

- Confirmed requirement/change and current artifact chain are available.
- Existing scenario/testcase coverage is available for reuse.
- Test environment can establish the required account/timing states.

---

## Exit Criteria

- All selected Minimum/Recommended cases for the chosen release scope pass.
- No unresolved blocker exists within the confirmed selected regression scope.
- Clarification-dependent potential impact remains excluded from executable expectations unless resolved authoritatively.

---

## Assumptions / Open Questions

Potential rows remain `Clarify` until supported by architecture, UI, API, database, session, password-management, or concurrency evidence. No implementation coupling is inferred from generic knowledge.

---

## Execution Notes

The three scope tiers are evidence-based decision levels, not percentage targets. Full Changed-Feature Verification is retained as a complete functional reference and is not automatically the default regression recommendation.
