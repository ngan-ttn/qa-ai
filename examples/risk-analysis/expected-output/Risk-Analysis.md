# Risk Analysis — Account Lock After Failed Login Attempts

## Risk Summary

The account-lock feature affects authentication state, failed-login tracking, time-based unlocking, and account isolation. The highest-risk failures are failure to lock at the defined threshold, premature lock, lock bypass, incorrect unlock timing, failed counter reset, and cross-account state leakage.

---

## Risk Register

| Risk ID | Area / Feature | Risk Description | Trigger / Cause | Impact | Likelihood | Severity / Exposure | Mitigation / QA Focus | Traceability | Status |
|---|---|---|---|---|---|---|---|---|---|
| RISK-001 | Lock Threshold | Account may not lock exactly on the fifth consecutive failed login. | Threshold/state transition implemented incorrectly. | Security protection may fail. | Medium | High | Verify 4→5 boundary and resulting account state. | Requirements 6, 8; AC-02 | Open |
| RISK-002 | Lock Threshold | Account may lock before five consecutive failed attempts. | Counter/threshold logic off by one. | Legitimate users may be locked prematurely. | Medium | High | Verify attempts 1–4 remain unlocked and successful-login reset behavior. | Requirements 6, 8; AC-01 | Open |
| RISK-003 | Authentication | Locked account may authenticate with valid credentials. | Lock state not enforced in authentication decision. | Primary account-protection control can be bypassed. | Medium | High | Verify correct password is rejected throughout active lock. | Requirement 10; AC-03 | Open |
| RISK-004 | Lock Duration | Account may unlock before the required 30-minute period. | Timer/expiry handling incorrect. | Security protection ends too early. | Medium | High | Verify locked state before expiration. | Requirements 9, 12; AC-04 | Open |
| RISK-005 | Automatic Unlock | Account may remain locked after 30 minutes. | Automatic unlock/state transition fails. | Legitimate user availability is impacted. | Medium | High | Verify automatic unlock and valid login after expiry. | Requirements 9, 12–13; AC-04 | Open |
| RISK-006 | Counter Reset | Successful login before threshold may fail to reset the current failed-login sequence. | Reset transition omitted/inconsistent. | Later failures may cause premature lock. | Medium | High | Verify successful-login reset after representative counts 1–4. | Requirement 7; AC-05 | Open |
| RISK-007 | Counter Reset | Failures before a successful login may incorrectly contribute to later sequences. | Counter history not separated into consecutive sequences. | Account may lock earlier than defined. | Medium | High | Verify reset followed by a fresh failure sequence. | Requirement 7; AC-05 | Open |
| RISK-008 | Account Isolation | Failed attempts for one account may affect another account. | Account-level state isolation incorrect. | Unauthorized/incorrect lockouts across users. | Low | High | Use two-account isolation scenarios and compare states. | Requirement 5; Notes | Open |
| RISK-009 | Unlock State | Pre-lock failures may incorrectly contribute to the next threshold after automatic unlock. | Post-unlock tracking state not restarted correctly. | New lifecycle may lock too early. | Medium | High | Verify four post-unlock failures remain below threshold and fifth new failure relocks. | Requirement 14 | Open |
| RISK-010 | Lock Message | Required temporary-lock message may not be displayed. | Locked-state feedback handling incomplete. | User receives incorrect/insufficient feedback. | Medium | Medium | Verify exact required message during active lock. | Requirement 11; AC-03 | Open |
| RISK-011 | State Consistency | Account lock state and failed-login counter may become inconsistent across consecutive actions. | Non-atomic/incomplete state transitions. | Security and availability behavior become unpredictable. | Medium | High | Exercise complete sequences and repeated lifecycle. | Requirements 5–14 | Open |
| RISK-012 | Time Boundary | Authentication may behave inconsistently around the 30-minute unlock boundary. | Precise boundary semantics/implementation timing. | Early/late unlock or nondeterministic user access. | Medium | High | Verify supported before/after boundary behavior; clarify exact-instant semantics. | Requirements 9, 12 | Clarification-Dependent |

---

## Assumptions / Dependencies

- Likelihood and exposure values are qualitative for this example; no unsupported numeric probability is asserted.
- Risk analysis does not define implementation storage, timer mechanism, or concurrency policy.

---

## Monitoring Notes / QA Focus

Priority QA focus should cover the `4 → 5` threshold, locked-state authentication rejection, 30-minute lifecycle, successful-login reset, post-unlock sequence, account isolation, and repeated state transitions.

---

## Open Questions

| Item ID | Area | Undefined Behavior | Risk if Implementations Differ |
|---|---|---|---|
| RG-001 | Lock Start Time | Exact event starting the 30-minute period. | Unlock timing may differ. |
| RG-002 | Locked Attempts | Effect of attempts during lock on failed-login counter. | Post-unlock counter state may be inconsistent. |
| RG-003 | Lock Extension | Whether attempts during lock restart/extend timer. | Users may remain locked for unintended duration. |
| RG-004 | Cross-Device Tracking | Whether attempts aggregate across browsers/devices/sessions. | Account-level state may differ by access channel. |
| RG-005 | Unknown Email | Behavior for unregistered email. | Authentication/failure handling may differ from intended policy. |
| RG-006 | Concurrency | Simultaneous attempts near threshold. | Counter/lock state may become inconsistent. |
| RG-007 | Unlock Counter | Exact numeric counter after automatic unlock. | Next failure sequence may start from wrong state. |

---

## Analysis Summary

The primary confirmed risk concentration is the interaction of failed-login counter, threshold, account lock state, timer, reset, and account isolation. Clarification-dependent areas remain visible and must not receive invented expected behavior during downstream test design.
