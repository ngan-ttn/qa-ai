# Regression Analysis — Account Lock After Failed Login Attempts

## Regression Summary

This artifact analyzes the change impact of temporary account locking using `Sample-Requirement.md`, the upstream QA artifact chain, and existing coverage. Because no architecture, API contract, database design, integration map, or implementation detail is supplied, confirmed requirement-derived impact is separated from potential/unknown dependencies.

---

## Change Overview

The confirmed change adds account-specific consecutive-failure tracking, a five-failure lock threshold, successful-login reset, locked-state rejection/message, a 30-minute temporary lock, automatic unlock, restored authentication, and restarted failure tracking after unlock.

---

## Regression Impact / Coverage

| Impact ID | Area / Module | Change Relationship | Regression Scope / Behavior to Revalidate | Impact Type | Evidence / Traceability | Priority | Existing Coverage Reference | Decision |
|---|---|---|---|---|---|---|---|---|
| IMP-001 | Login Authentication | Direct | Valid login succeeds only when credentials are valid and account is not locked; existing normal login remains functional. | Confirmed | R1–R3; TS-001; TC-001 | High | TS-001 / TC-001 | Include |
| IMP-002 | Failed Login Handling | Direct | Incorrect-password rejection remains functional and now participates in account-specific tracking. | Confirmed | R4–R5; BR-001; TS-002, TS-003 | High | TS-002, TS-003 / TC-002, TC-003 | Include |
| IMP-003 | Lock Threshold | Direct | Failures 1–4 remain unlocked; fifth consecutive failure introduces locked state. | Confirmed | R6, R8; AC-01, AC-02; BR-002 | High | TS-004–TS-006 / TC-004–TC-006 | Include |
| IMP-004 | Counter Reset | Direct | Successful login before threshold resets current failure sequence; later failures do not combine with prior sequence. | Confirmed | R7; AC-05; BR-003 | High | TS-007–TS-009 / TC-007–TC-009 | Include |
| IMP-005 | Locked-State Authentication | Direct | Password authentication is rejected throughout active lock, including correct password. | Confirmed | R10; AC-03; BR-005 | High | TS-012, TS-013 / TC-012, TC-013 | Include |
| IMP-006 | User Feedback | Direct | Locked-account login displays the defined temporary-lock message. | Confirmed | R11; AC-03; BR-006 | Medium | TS-014 / TC-014 | Include |
| IMP-007 | Time-Based State | Direct | Locked state remains active for 30 minutes. | Confirmed | R9; BR-004 | High | TS-015 / TC-015 | Include |
| IMP-008 | Automatic Recovery | Direct | Account automatically transitions to unlocked when lock period expires. | Confirmed | R12; AC-04; BR-007 | High | TS-016 / TC-016 | Include |
| IMP-009 | Post-Unlock Authentication | Direct | Normal valid authentication is available again after automatic unlock. | Confirmed | R13; AC-04; BR-008 | High | TS-017 / TC-017 | Include |
| IMP-010 | Post-Unlock Tracking | Direct | New failed-login tracking sequence begins after automatic unlock. | Confirmed | R14; BR-009 | High | TS-018, TS-019 / TC-018, TC-019 | Include |
| IMP-011 | Account Isolation | Direct | Failure/lock state remains account-specific and does not affect unrelated registered accounts. | Confirmed | R5; BR-001 | High | TS-010, TS-011 / TC-010, TC-011 | Include |
| POT-001 | Lock Expiration Boundary | Potential | Exact request behavior precisely at 30-minute expiration requires clarification before deterministic regression expectation. | Potential | R9/R12 define duration but exact boundary semantics unresolved. | — | CTS-003 | Clarify |
| POT-002 | Locked-Attempt Counter/Timer | Potential | Determine whether attempts during active lock change counter or restart/extend duration. | Potential | Requirement defines rejection only. | — | CTS-001, CTS-002 | Clarify |
| POT-003 | Cross-Session / Device | Potential | Determine whether failed-login state aggregates across sessions/browsers/devices. | Potential | No aggregation contract supplied. | — | CTS-004, CTS-005 | Clarify |
| POT-004 | Concurrency | Potential | Determine simultaneous near-threshold update behavior before defining regression expectations. | Potential | No concurrency contract supplied. | — | CTS-006 | Clarify |
| POT-005 | Existing Sessions | Potential | Determine effect of new lock on sessions authenticated before lock. | Potential | Existing-session behavior not supplied. | — | CTS-007 | Clarify |
| POT-006 | Password Management | Potential | Determine password reset/change interaction with lock/failure state. | Potential | Password-management interaction not supplied. | — | CTS-008 | Clarify |
| POT-007 | Unknown Account | Potential | Determine failure handling for unregistered email. | Potential | Unknown-account behavior not supplied. | — | CTS-009 | Clarify |
| POT-008 | API / Database / Technical Mechanism | Unsupported by current evidence | Do not create mandatory regression against endpoints, status codes, schemas, SQL, persistence fields, or timer implementation without actual contracts. | Potential | No technical contracts in input. | — | N/A | Exclude / Clarify if later evidence appears |

---

## Excluded Scope

No API/database/architecture-specific regression is confirmed by the supplied end-to-end input. Potential dependencies remain outside mandatory scope until authoritative evidence establishes them.

---

## Entry Criteria

- Confirmed requirement/change and current artifact chain are available.
- Existing scenario/testcase coverage is available for reuse.
- Test environment can establish the required account/timing states.

---

## Exit Criteria

- All high-priority confirmed impact rows are revalidated.
- Existing valid/invalid login behavior remains functional.
- Threshold, reset, lock, unlock, post-unlock, and isolation behavior passes.
- No unresolved blocker remains within confirmed regression scope.

---

## Assumptions / Open Questions

Potential rows remain `Clarify` until supported by architecture, UI, API, database, session, password-management, or concurrency evidence. No implementation coupling is inferred from generic knowledge.

---

## Execution Notes

A smoke subset should cover valid unlocked login, invalid-password rejection, lock on fifth failure, rejection during lock, automatic unlock, and valid login after unlock. Focused regression should add below-threshold behavior, reset/new sequence, account isolation, message, post-unlock tracking, and repeated lifecycle.

---

## Regression Summary

Confirmed regression is intentionally scoped to requirement-supported authentication behavior and reusable existing coverage. Potential system dependencies remain explicitly separate so the regression artifact does not overstate impact.
