# Risk Analysis — Account Lock After Failed Login Attempts

## Risk Summary

This artifact identifies QA risks derived from `Sample-Requirement.md`, `Requirement-Analysis.md`, and `Business-Rules.md`. The highest-risk areas are threshold enforcement, reset behavior, account isolation, active-lock authentication, lock timing/recovery, post-unlock tracking, and state consistency.

Qualitative likelihood/impact values are QA prioritization for this example and do not create product rules.

---

## Risk Register

| Risk ID | Area / Feature | Risk Description | Trigger / Cause | Impact | Likelihood | Severity / Exposure | Mitigation / QA Focus | Traceability | Status |
|---|---|---|---|---|---|---|---|---|---|
| RISK-001 | Lock Threshold | Account is not locked at the fifth consecutive failed attempt. | Fifth-failure transition not enforced. | Primary protection behavior fails. | High | High | Verify exact fifth-failure transition and resulting state. | BR-002; R6, R8, AC-02 | Open |
| RISK-002 | Lock Threshold | Account is locked before the fifth consecutive failed attempt. | Off-by-one threshold/counter logic. | Legitimate user loses access earlier than required. | Medium | High | Verify failures 1–4 remain unlocked. | BR-002; R6, AC-01 | Open |
| RISK-003 | Counter Reset | Successful login does not reset the failed-login sequence. | Reset transition omitted/inconsistent. | Separate sequences may combine and cause premature lock. | Medium | High | Verify reset after representative counts and fresh sequence afterward. | BR-003; R7, AC-05 | Open |
| RISK-004 | Account Isolation | Failed attempts from one account affect another account. | Account-specific state isolation fails. | Unrelated user may be locked or have corrupted security state. | Medium | High | Interleave two-account failures/authentication and compare states. | BR-001; R5 | Open |
| RISK-005 | Locked State | Locked account can authenticate with valid credentials. | Lock state does not override credential validity. | Account-lock control can be bypassed. | Medium | High | Verify correct password is rejected throughout active lock. | BR-005; R10, AC-03 | Open |
| RISK-006 | Lock Duration | Account unlocks before the required 30-minute period. | Timer/expiry is evaluated too early. | Protection ends sooner than required. | Medium | High | Verify account remains locked before expiry. | BR-004, BR-007; R9, R12 | Open |
| RISK-007 | Automatic Unlock | Account remains locked after the 30-minute period expires. | Automatic unlock transition fails/is delayed. | Legitimate users remain unavailable. | Medium | High | Verify automatic unlock and valid login after expiry. | BR-004, BR-007, BR-008; R12–R13, AC-04 | Open |
| RISK-008 | User Feedback | Locked-account message is incorrect or missing. | Locked-state feedback handling incomplete. | User receives incorrect/insufficient feedback. | Medium | Medium | Verify exact required message during active lock. | BR-006; R11, AC-03 | Open |
| RISK-009 | Post-Unlock Tracking | Failed-login tracking does not restart correctly after automatic unlock. | Residual pre-lock state remains. | Account may relock too early or sequence becomes inconsistent. | Medium | High | Verify new post-unlock failures form a new sequence. | BR-009; R14 | Open |
| RISK-010 | Lock Boundary Semantics | Undefined exact lock-period boundary causes inconsistent authentication results. | Precise request-at-expiry semantics are not defined. | Timing behavior may vary and tests may be nondeterministic. | Medium | High | Clarify exact boundary; assert supported before/after behavior only. | BR-004, BR-005 | Clarification-Dependent |
| RISK-011 | Cross-Session / Device | Undefined cross-session behavior causes inconsistent account-level tracking. | Requirement does not explicitly define browser/device/session aggregation. | Account-level failed state may differ by access channel. | Medium | High | Clarify/validate implementation before assigning expected result. | BR-001 | Clarification-Dependent |
| RISK-012 | Concurrency | Concurrent attempts near threshold produce incorrect lock behavior. | Simultaneous state updates are not defined. | Lost/extra increments or inconsistent lock state/timing. | Medium | High | Treat as technical risk pending concurrency semantics. | BR-002 | Clarification-Dependent |

---

## Assumptions / Dependencies

- No unsupported numeric probability or financial impact is assigned.
- Implementation storage/timer/concurrency mechanisms are not treated as source behavior.

---

## Monitoring Notes

Highest-priority downstream coverage should emphasize the 4→5 boundary, successful-login reset, account isolation, correct-password rejection during lock, before/after 30-minute expiry, automatic recovery, and post-unlock sequence behavior.

---

## Open Questions

| Area | Missing Definition | QA Handling |
|---|---|---|
| Exact expiry instant | Request behavior precisely at 30-minute boundary | Clarify; do not assume |
| Attempts during lock | Counter/timer side effects | Clarify; assert rejection only |
| Cross-session/device | Aggregation semantics | Clarify/validate implementation |
| Concurrency | Simultaneous near-threshold updates | Technical validation after semantics are known |

---

## Analysis Summary

The register separates confirmed requirement-derived risks from clarification-dependent implementation/specification risks and supplies traceable QA focus without generating downstream scenarios or test cases.
