# Risk Analysis — Account Lockout After Failed Login Attempts

## Golden Output Metadata

- Dataset ID: `REQ-AUTH-001`
- Source Requirement: `datasets/requirements/simple/REQ-AUTH-001.md`
- Artifact Type: `Risk Analysis`
- Review Status: `Approved`
- Evaluation Purpose: Reference output for evaluating risk identification, prioritization, boundary/state risk analysis, assumption control, and traceability

---

## Risk Summary

The feature is small in functional scope but security-sensitive. Highest-risk areas are the five-attempt threshold, 15-minute lock timing, active-lock authentication rejection, reset behavior, consecutive-sequence integrity, and per-account isolation.

The qualitative ratings below are QA prioritization for this dataset, not source-defined business rules.

---

## Risk Register

| Risk ID | Area / Feature | Risk Description | Trigger / Cause | Impact | Likelihood | Severity / Exposure | Mitigation / QA Focus | Traceability | Status |
|---|---|---|---|---|---|---|---|---|---|
| RISK-AUTH-001 | Threshold | Account may lock before the fifth consecutive failure. | Counter/threshold boundary implemented incorrectly. | Legitimate users locked prematurely; requirement violated. | Medium | High | Verify states after failures 1–4 and the 4→5 transition. | AC-01, AC-02, AC-03; BR-AUTH-002, BR-AUTH-003, BR-AUTH-004 | Open |
| RISK-AUTH-002 | Threshold | Account may remain unlocked after the fifth consecutive failure. | Fifth-failure state transition not enforced. | Password guessing can continue beyond intended threshold. | Medium | High | Verify fifth recorded failure immediately locks the account. | AC-03, AC-04; BR-AUTH-004, BR-AUTH-006 | Open |
| RISK-AUTH-003 | Locked State | Correct password may bypass an active lock. | Lock state not given precedence over valid credentials. | Primary security control can be bypassed. | Medium | High | Attempt both correct and incorrect passwords while lock is active. | AC-05; BR-AUTH-007, BR-AUTH-008 | Open |
| RISK-AUTH-004 | Account Isolation | Failed attempts may be shared across accounts. | Account-specific state isolation is incorrect. | Unrelated users may be locked; security state corrupted. | Low | High | Interleave failures across multiple accounts and verify independent sequences. | AC-01; BR-AUTH-001, BR-AUTH-002 | Open |
| RISK-AUTH-005 | Counter Reset | Successful login may not reset the counter. | Reset transition before lock is missing/incorrect. | Separate sequences may combine and lock account too early. | Medium | High | Fail below threshold → successful login → start new failure sequence at 1. | AC-08, AC-09; BR-AUTH-011, BR-AUTH-012 | Open |
| RISK-AUTH-006 | Automatic Unlock Reset | Previous failures may carry over after automatic unlock. | Unlock fails to reset counter to zero. | Account may relock earlier than five new failures. | Medium | High | After expiry, verify first new failure becomes 1 and account remains unlocked. | AC-06, AC-07, AC-09; BR-AUTH-009, BR-AUTH-010, BR-AUTH-012 | Open |
| RISK-AUTH-007 | Lock Duration | Account may unlock before fifteen minutes. | Expiry calculated too early. | Security protection shorter than required. | Medium | High | Verify password login remains blocked immediately before expiry. | AC-04, AC-05, AC-06; BR-AUTH-005, BR-AUTH-006, BR-AUTH-007, BR-AUTH-009 | Open |
| RISK-AUTH-008 | Automatic Unlock | Account may remain locked after fifteen minutes. | Automatic unlock transition fails/occurs late. | Legitimate users remain unavailable. | Medium | High | Verify account becomes password-authentication eligible when duration expires. | AC-06, AC-07; BR-AUTH-005, BR-AUTH-009, BR-AUTH-010 | Open |
| RISK-AUTH-009 | Lock Start Time | Lock duration may be calculated from the wrong event. | Timer starts from first/fourth failure or later locked attempt instead of fifth recorded failure. | Effective lock duration becomes shorter/longer than required. | Medium | High | Capture fifth-failure time and validate expiry relative to that event. | AC-03, AC-04, AC-06; BR-AUTH-004, BR-AUTH-005, BR-AUTH-006 | Open |
| RISK-AUTH-010 | Consecutive Sequence | System may count historical total failures instead of consecutive failures. | Reset/new-sequence handling incorrect. | Account may lock without five consecutive failures. | Medium | High | Use failure sequences separated by successful login and verify only latest sequence counts. | AC-02, AC-03, AC-08, AC-09; BR-AUTH-003, BR-AUTH-004, BR-AUTH-011, BR-AUTH-012 | Open |
| RISK-AUTH-011 | Locked Attempts | Attempts during lock may affect counter/timer in an undefined way. | Source defines rejection but not side effects of locked attempts. | Lock duration/counter state may vary by implementation; tests may become inconsistent. | Medium | Medium | Clarify side effects; assert only rejection until behavior is defined. | AC-05, AC-06, AC-07; BR-AUTH-007, BR-AUTH-008, BR-AUTH-009, BR-AUTH-010 | Clarification-Dependent |
| RISK-AUTH-012 | Concurrency | Simultaneous attempts near threshold may cross the lock boundary inconsistently. | Concurrent request serialization/state update behavior is undefined. | Lost increments, threshold overshoot, inconsistent lock timestamp, or extra accepted attempts. | Low | Medium | Treat as technical risk pending implementation-specific validation/clarification. | AC-01, AC-03, AC-04; BR-AUTH-002, BR-AUTH-004, BR-AUTH-006 | Clarification-Dependent |

---

## Assumptions / Dependencies

- Likelihood/impact/exposure are qualitative QA prioritization for the golden evaluation artifact.
- No probability, financial loss, persistence mechanism, or concurrency strategy is asserted as source-defined behavior.

---

## Monitoring Notes

Highest-priority testing should focus on the 4→5 threshold, active-lock password rejection, the fifth-failure timer start, immediately-before/at expiry behavior, successful-login reset, automatic-unlock reset, account isolation, and sequence separation.

---

## Open Questions

| Area | Missing Definition | QA Handling |
|---|---|---|
| Locked-attempt counter | Whether attempts during active lock increment the counter | Clarify; do not assume |
| Locked-attempt timer | Whether attempts during active lock restart/extend the lock | Clarify; do not assume |
| Concurrent attempts | How simultaneous attempts near threshold are serialized | Technical risk pending system behavior |
| Manual unlock | Whether administrative unlock exists and affects counter state | Outside current dataset scope |
| Alternative authentication | Whether lock affects non-password authentication | Outside current dataset scope |

---

## Analysis Summary

All nine source acceptance criteria have associated risk coverage. The register distinguishes confirmed requirement risks from clarification-dependent/implementation-sensitive risks and does not present unspecified behavior as an expected system result.
