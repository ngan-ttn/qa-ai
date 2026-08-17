# Regression Analysis — Account Lock After Failed Login Attempts

## Regression Summary

The change extends the existing authentication flow with per-account failed-login tracking, a five-consecutive-failure lock threshold, temporary account lock, locked-state authentication rejection, a 30-minute lock period, automatic unlock, successful-login reset, and restarted tracking after unlock.

Confirmed regression impact is concentrated around the login/authentication lifecycle. Unknown implementation dependencies remain investigation items rather than confirmed impact.

---

## Change Overview

Existing successful and invalid-password login behavior remains part of the baseline. The change adds failure-state tracking and lock-state decisions before authentication/session creation can complete.

---

## Regression Impact / Coverage

| Impact ID | Area / Module | Change Relationship | Regression Scope / Behavior to Revalidate | Impact Type | Evidence / Traceability | Priority | Existing Coverage Reference | Decision |
|---|---|---|---|---|---|---|---|---|
| RI-001 | Login Page | Direct | Successful login for an unlocked account remains functional. | Confirmed | Existing authentication path + Requirements 1–3 | High | Login scenarios/test cases | Include |
| RI-002 | Login Page | Direct | Incorrect-password rejection remains functional alongside new tracking. | Confirmed | Requirement 4 | High | Invalid-password coverage | Include |
| RI-003 | Failed Login Tracking | Direct | Consecutive failed attempts are tracked per account. | Confirmed | Requirements 5–6 | High | Threshold/isolation coverage | Include |
| RI-004 | Lock Threshold | Direct | Account remains unlocked through four consecutive failures. | Confirmed | Requirement 6; AC-01 | High | Boundary coverage | Include |
| RI-005 | Lock Threshold | Direct | Account locks on the fifth consecutive failure. | Confirmed | Requirements 6, 8; AC-02 | High | Boundary/state coverage | Include |
| RI-006 | Counter Reset | Direct | Successful login before threshold resets the current failure sequence. | Confirmed | Requirement 7; AC-05 | High | Counter-reset coverage | Include |
| RI-007 | Locked State | Direct | Correct password cannot bypass an active lock. | Confirmed | Requirement 10; AC-03 | High | Locked-state coverage | Include |
| RI-008 | Locked State | Direct | Authentication attempts during active lock are rejected and required lock feedback is shown. | Confirmed | Requirements 10–11; AC-03 | High | Locked-state/message coverage | Include |
| RI-009 | Lock Duration | Direct | Account remains locked before the 30-minute duration expires. | Confirmed | Requirements 9–10 | High | Time-boundary coverage | Include |
| RI-010 | Automatic Unlock | Direct | Account automatically unlocks after the defined lock duration and permits valid login. | Confirmed | Requirements 12–13; AC-04 | High | Unlock coverage | Include |
| RI-011 | Post-Unlock Tracking | Direct | Failed-login tracking starts again after automatic unlock. | Confirmed | Requirement 14 | High | Post-unlock coverage | Include |
| RI-012 | Account Isolation | Direct | One account's failures/lock state do not affect another account. | Confirmed | Requirement 5; Notes | High | Isolation coverage | Include |
| RI-013 | Authentication Service | Direct | Authentication decision correctly incorporates credentials plus account lock/failure state. | Confirmed | Requirements 5–14 | High | Authentication lifecycle coverage | Include |
| RI-014 | User Account Store Interaction | Dependency | Account-specific authentication state behaves consistently, without assuming where/how it is persisted. | Potential | Account-specific state is required; persistence design not defined | High | Behavioral state coverage | Include |
| RI-015 | Session Management | Direct Dependency | Locked-account authentication creates no new authenticated session; valid unlocked authentication still creates a session. | Confirmed | Existing auth→session relationship in supplied context | High | Session integration coverage | Include |
| RI-016 | Protected Application Routes | Indirect | Existing protected access continues after a valid authenticated session is created. | Potential | Known dependency on successful session creation; no rule change specified | Medium | Existing protected-route coverage | Include |
| RI-017 | Logout | Indirect / Related | Existing logout flow remains functional after successful authentication. | Potential | Related authenticated lifecycle; no functional change specified | Low | Existing logout coverage | Include |
| RI-018 | Password Reset | Unknown Dependency | Determine whether password reset affects failed-login or lock state before adding regression scope. | Potential | Dependency not defined | — | N/A | Clarify |
| RI-019 | Password Change | Unknown Dependency | Determine whether password change affects failed-login or lock state before adding regression scope. | Potential | Dependency not defined | — | N/A | Clarify |
| RI-020 | Existing Sessions | Unknown Dependency | Determine whether account locking affects sessions authenticated before the lock. | Potential | Behavior not defined | — | N/A | Clarify |
| RI-021 | User Registration | No confirmed relationship | No change or dependency is identified from supplied context. | Potential | No supporting change/dependency evidence | — | N/A | Exclude |
| RI-022 | Administration | Unknown Dependency | Determine whether administrative unlock/account management exists and is affected. | Potential | Capability/dependency unknown | — | N/A | Clarify |
| RI-023 | Audit Logging | Unknown Dependency | Determine whether lock/failure events are audited before adding regression scope. | Potential | Capability/dependency unknown | — | N/A | Clarify |
| RI-024 | Concurrency / Cross-Device | Unknown Dependency | Determine shared counter/update semantics before defining regression expectations. | Potential | Concurrent and cross-device behavior undefined | — | N/A | Clarify |

---

## Excluded Scope

User registration has no confirmed change/dependency and is excluded from the confirmed regression scope. Password management, existing-session invalidation, administrative behavior, audit logging, concurrency, cross-device aggregation, and exact persistence/timer mechanisms remain clarification/investigation items rather than silently included impact.

---

## Entry Criteria

- Authoritative account-lock requirement/change is available.
- Baseline login/session behavior is available for comparison.
- Required test accounts and controllable account states are available.

---

## Exit Criteria

- High-priority confirmed regression rows have been revalidated.
- Existing successful and invalid-password authentication remain functional.
- New lock/reset/unlock/isolation behavior passes expected results.
- No unresolved blocker remains in the agreed regression scope.

---

## Assumptions / Open Questions

| Investigation ID | Area | Unknown Dependency / Behavior |
|---|---|---|
| INV-001 | Persistence | Where failed-login counters are stored. |
| INV-002 | Persistence | Where lock state/expiration information is stored. |
| INV-003 | Timer | How automatic unlock is implemented. |
| INV-004 | Locked Attempts | Whether attempts during lock affect failed-login state. |
| INV-005 | Lock Duration | Whether attempts during lock restart/extend timer. |
| INV-006 | Cross-Device | Whether failed attempts aggregate across browsers/devices/sessions. |
| INV-007 | Concurrency | How simultaneous attempts update account state. |
| INV-008 | Unknown Account | How unregistered email addresses participate in failure handling. |
| INV-009 | Existing Sessions | Whether locking affects sessions created before lock. |
| INV-010 | Password Management | Whether password reset/change modifies failure or lock state. |
| INV-011 | Administration | Whether administrative unlock exists. |
| INV-012 | Audit | Whether authentication failures/lock events are audited. |

---

## Execution Notes

Smoke regression should cover valid unlocked login, invalid-password rejection, lock on fifth failure, rejection while locked, automatic unlock, and valid login after unlock. Focused regression should additionally cover below-threshold behavior, reset/new sequence, account isolation, session creation/rejection, and repeated lifecycle.

---

## Regression Summary

The confirmed regression scope is intentionally concentrated around authentication rather than the whole application. Direct impact covers login, failure tracking, lock state, timer lifecycle, reset, isolation, and session creation. Protected access/logout receive targeted related regression, while unsupported implementation dependencies remain `Clarify` rather than being promoted to confirmed scope.
