# Coverage Review — Account Lock After Failed Login Attempts

## 1. Review Summary

The current test scenario set provides coverage for the primary account-lock flow, including successful authentication, incorrect-password handling, lock-threshold behavior, successful-login counter reset, authentication restriction while locked, lock-message display, automatic unlock, login after automatic unlock, and account-specific failed-login isolation.

However, the scenario set does not provide complete coverage of all requirement-defined behavior.

The main identified gaps are:

1. No direct coverage that the account remains locked during the 30-minute lock period.
2. No coverage that failed-login tracking starts again after automatic unlock.
3. Counter-reset coverage confirms the reset action but does not demonstrate that subsequent failed attempts belong to a new consecutive-failure sequence.

Overall coverage is therefore **NOT FULLY COVERED**.

---

## 2. Canonical Coverage Status Model

| Status | Meaning |
|---|---|
| Covered | Confirmed obligation is represented with enough explicitness that downstream work does not need to reconstruct the intended oracle. |
| Weakly Covered | Confirmed obligation is represented, but coverage is broad, implicit, aggregated, or insufficiently precise for reliable downstream expansion. |
| Gap | Confirmed obligation has no adequate coverage in the reviewed artifact set. |
| Blocked | Coverage cannot be authoritatively completed because the source, oracle, dependency, or required context is unresolved. |

Clarification-dependent behavior is classified as **Blocked**, not as a confirmed Gap, unless authoritative behavior exists and only the test-design coverage is missing.

---

## 3. Coverage Status

| Area | Coverage Status | Assessment |
|---|---|---|
| Authentication | Covered | Successful and incorrect-password login behavior is represented. |
| Failed-Login Tracking | Weakly Covered | Threshold behavior is covered, but post-unlock tracking is missing. |
| Lock Threshold | Covered | Behavior immediately below and at the five-attempt threshold is represented. |
| Counter Reset | Weakly Covered | Reset is covered, but the resulting new failure sequence is not verified. |
| Locked-State Authentication | Covered | Correct-password authentication while locked is rejected. |
| Lock Message | Covered | Required lock message is represented. |
| Lock Duration | Gap | No scenario verifies that the account remains locked before the 30-minute period expires. |
| Automatic Unlock | Covered | Automatic unlock after the lock period is represented. |
| Post-Unlock Login | Covered | Successful login after automatic unlock is represented. |
| Post-Unlock Tracking | Gap | No scenario verifies that failed-login tracking starts again after unlock. |
| Account Isolation | Covered | Failed-login activity between separate accounts is represented. |

---

## 4. Requirement Coverage Review

| Requirement | Requirement Summary | Current Coverage | Status | Review Finding |
|---|---|---|---|---|
| R1 | Registered user can attempt login using email and password. | TS-001 | Covered | Primary valid-login flow is represented. |
| R2 | System validates submitted credentials. | TS-001, TS-002 | Covered | Both successful and failed credential outcomes are represented. |
| R3 | Valid credentials authenticate an unlocked account. | TS-001 | Covered | Direct coverage exists. |
| R4 | Incorrect password causes login failure. | TS-002 | Covered | Direct negative coverage exists. |
| R5 | Failed attempts are tracked separately for each account. | TS-010 | Covered | Account-isolation behavior is represented. |
| R6 | Five consecutive incorrect-password attempts trigger account locking. | TS-003, TS-004 | Covered | Below-threshold and threshold boundaries are represented. |
| R7 | Successful login before the fifth failure resets the counter. | TS-005 | Weakly Covered | Reset is represented, but subsequent sequence behavior is not demonstrated. |
| R8 | Account becomes locked after the fifth consecutive failed attempt. | TS-004 | Covered | Direct threshold transition is represented. |
| R9 | Account remains locked for 30 minutes. | None | Gap | No scenario verifies locked state before expiration. |
| R10 | Authentication is prohibited while locked even with the correct password. | TS-006 | Covered | Direct locked-state coverage exists. |
| R11 | Defined temporary-lock message is displayed while locked. | TS-007 | Covered | Direct message coverage exists. |
| R12 | Account automatically unlocks after 30 minutes. | TS-008 | Covered | Automatic unlock is represented. |
| R13 | User can attempt login again after unlock. | TS-009 | Covered | Successful post-unlock authentication is represented. |
| R14 | Failed-login tracking starts again after unlock. | None | Gap | No post-unlock failed-login sequence is represented. |

---

## 5. Acceptance Criteria Coverage Review

| Acceptance Criteria | Current Coverage | Status | Review |
|---|---|---|---|
| AC-01 — Failed Login Below Threshold | TS-003 | Covered | Scenario verifies the account remains unlocked immediately below the threshold. |
| AC-02 — Lock Account at Threshold | TS-004 | Covered | Scenario verifies the fifth consecutive failure causes locking. |
| AC-03 — Login While Locked | TS-006, TS-007 | Covered | Authentication rejection and required message are both represented. |
| AC-04 — Automatic Unlock | TS-008, TS-009 | Covered | Unlock and subsequent login behavior are represented. |
| AC-05 — Successful Login Resets Counter | TS-005 | Weakly Covered | Counter reset is represented, but no scenario proves later failures start a new sequence. |

---

## 6. Confirmed Coverage Findings

| Finding ID | Classification | Related Source | Current Evidence | Finding | Priority | Recommended Owning Action |
|---|---|---|---|---|---|---|
| COV-001 | Gap | R9 | None | No scenario verifies that the account remains locked before the 30-minute lock period expires. | High | Scenario Generator should add focused confirmed coverage. |
| COV-002 | Gap | R14 | None | No scenario verifies that failed-login tracking starts again after automatic unlock. | High | Scenario Generator should add focused confirmed coverage. |
| COV-003 | Weakly Covered | R7 / AC-05 | TS-005 | Reset is represented, but the downstream consequence—starting a genuinely new failure sequence—is implicit rather than directly demonstrated. | Medium | Scenario Generator should strengthen or add focused sequence coverage. |

---

## 7. Boundary Coverage Review

### Five-Attempt Threshold

Current scenarios provide appropriate boundary coverage:

```text
4 Failures → Unlocked
5 Failures → Locked
```

Covered by TS-003 and TS-004.

**Status: Covered**

### 30-Minute Lock Boundary

Current coverage verifies automatic unlock after the lock period expires, but does not verify the complementary pre-expiry state.

The exact behavior at the precise expiration instant is not sufficiently defined by the requirement and should not be assigned an assumed expected result.

**Status: Weakly Covered**

The pre-expiry confirmed obligation is a Gap; the exact expiration-instant behavior is Blocked pending clarification.

---

## 8. State Transition Coverage Review

| Transition / State Behavior | Evidence | Status | Assessment |
|---|---|---|---|
| Unlocked → Locked on fifth consecutive failure | TS-003, TS-004 | Covered | Threshold transition is explicit. |
| Locked → Unlocked after 30-minute period | TS-008 | Covered | Automatic unlock is explicit. |
| Successful login resets current failed sequence | TS-005 | Weakly Covered | Reset is represented, but the new post-reset sequence is not demonstrated. |
| Post-unlock failed-login tracking starts again | None | Gap | Confirmed post-unlock tracking behavior lacks scenario coverage. |

---

## 9. Duplicate Coverage Review

No material duplicate scenarios were identified. Scenarios that share a functional area still verify distinct objectives, such as below-threshold versus at-threshold behavior and automatic unlock versus post-unlock authentication.

**Duplicate Coverage Status: PASS**

---

## 10. Blocked / Clarification-Dependent Coverage

The following testing areas are relevant but are not sufficiently defined by the supplied requirement. They are **Blocked**, not confirmed coverage Gaps.

| Area | Undefined Behavior | Coverage Status |
|---|---|---|
| Exact timer boundary | Login exactly at the 30-minute expiration instant. | Blocked |
| Attempts while locked | Effect on failed-login counter. | Blocked |
| Lock extension | Whether attempts while locked restart or extend the timer. | Blocked |
| Cross-device/session tracking | Whether attempts across devices, browsers, or sessions contribute to the same account counter. | Blocked |
| Unknown email address | Failed-login behavior for an unregistered email. | Blocked |
| Concurrent login attempts | Counter behavior for simultaneous attempts near the threshold. | Blocked |
| Exact post-unlock counter value | Requirement says tracking starts again but does not explicitly state a numeric value. | Blocked |

These items must remain separate from confirmed coverage gaps until an authoritative oracle or dependency is available.

---

## 11. Recommended Coverage Additions

| Recommendation ID | Priority | Recommended Scenario | Related Requirement | Finding |
|---|---|---|---|---|
| REC-001 | High | Verify the account remains locked before the 30-minute lock period expires. | R9 | COV-001 |
| REC-002 | High | Verify failed-login tracking starts again after automatic unlock. | R14 | COV-002 |
| REC-003 | Medium | Verify a new consecutive failed-login sequence begins after a successful login resets the previous failed-login counter. | R7 / AC-05 | COV-003 |

Adding these scenarios would improve confirmed coverage without inventing behavior for Blocked items.

---

## 12. Coverage Summary

### Requirement Coverage

```text
Covered:         11
Weakly Covered:   1
Gap:              2
Blocked:          0 confirmed requirements in the reviewed requirement set
Total:           14
```

### Acceptance Criteria Coverage

```text
Covered:          4
Weakly Covered:   1
Gap:              0
Blocked:          0
Total:             5
```

All counts reconcile to the unique requirement/acceptance-criteria rows above.

---

## 13. Final Assessment

**Overall Coverage Status: GAPS REMAIN**

The scenario set covers the primary account-lock behavior and all major acceptance-criteria flows, but confirmed coverage is not yet complete.

Two confirmed Gaps and one Weakly Covered item require remediation:

1. Verify account remains locked before 30-minute expiration.
2. Verify failed-login tracking starts again after automatic unlock.
3. Strengthen successful-login reset coverage so the new failure sequence is explicit.

No significant duplicate coverage was identified. Clarification-dependent timer, locked-attempt, cross-device, unknown-account, concurrency, and exact counter semantics remain Blocked rather than being misclassified as confirmed coverage Gaps.