# Coverage Review — Account Lock After Failed Login Attempts

## 1. Review Summary

The current test scenario set provides coverage for the primary account-lock flow, including:

- Successful authentication.
- Incorrect-password handling.
- Lock-threshold behavior.
- Successful-login counter reset.
- Authentication restriction while locked.
- Lock-message display.
- Automatic unlock.
- Login after automatic unlock.
- Account-specific failed-login isolation.

However, the scenario set does not provide complete coverage of all requirement-defined behavior.

The main identified gaps are:

1. No direct coverage that the account remains locked during the 30-minute lock period.
2. No coverage that failed-login tracking starts again after automatic unlock.
3. Counter-reset coverage confirms the reset action but does not demonstrate that subsequent failed attempts belong to a new consecutive-failure sequence.

Overall coverage is therefore **Partial**.

---

## 2. Coverage Status

| Area | Coverage Status | Assessment |
|---|---|---|
| Authentication | Covered | Successful and incorrect-password login behavior is represented. |
| Failed-Login Tracking | Partial | Threshold behavior is covered, but post-unlock tracking is missing. |
| Lock Threshold | Covered | Behavior immediately below and at the five-attempt threshold is represented. |
| Counter Reset | Partial | Reset is covered, but the resulting new failure sequence is not verified. |
| Locked-State Authentication | Covered | Correct-password authentication while locked is rejected. |
| Lock Message | Covered | Required lock message is represented. |
| Lock Duration | Missing | No scenario verifies that the account remains locked before the 30-minute period expires. |
| Automatic Unlock | Covered | Automatic unlock after the lock period is represented. |
| Post-Unlock Login | Covered | Successful login after automatic unlock is represented. |
| Post-Unlock Tracking | Missing | No scenario verifies that failed-login tracking starts again after unlock. |
| Account Isolation | Covered | Failed-login activity between separate accounts is represented. |

---

## 3. Requirement Coverage Review

| Requirement | Requirement Summary | Current Coverage | Status | Review Finding |
|---|---|---|---|---|
| R1 | Registered user can attempt login using email and password. | TS-001 | Covered | Primary valid-login flow is represented. |
| R2 | System validates submitted credentials. | TS-001, TS-002 | Covered | Both successful and failed credential outcomes are represented. |
| R3 | Valid credentials authenticate an unlocked account. | TS-001 | Covered | Direct coverage exists. |
| R4 | Incorrect password causes login failure. | TS-002 | Covered | Direct negative coverage exists. |
| R5 | Failed attempts are tracked separately for each account. | TS-010 | Covered | Account-isolation behavior is represented. |
| R6 | Five consecutive incorrect-password attempts trigger account locking. | TS-003, TS-004 | Covered | Below-threshold and threshold boundaries are represented. |
| R7 | Successful login before the fifth failure resets the counter. | TS-005 | Partial | Reset is represented, but subsequent sequence behavior is not demonstrated. |
| R8 | Account becomes locked after the fifth consecutive failed attempt. | TS-004 | Covered | Direct threshold transition is represented. |
| R9 | Account remains locked for 30 minutes. | None | Missing | No scenario verifies locked state before expiration. |
| R10 | Authentication is prohibited while locked even with the correct password. | TS-006 | Covered | Direct locked-state coverage exists. |
| R11 | Defined temporary-lock message is displayed while locked. | TS-007 | Covered | Direct message coverage exists. |
| R12 | Account automatically unlocks after 30 minutes. | TS-008 | Covered | Automatic unlock is represented. |
| R13 | User can attempt login again after unlock. | TS-009 | Covered | Successful post-unlock authentication is represented. |
| R14 | Failed-login tracking starts again after unlock. | None | Missing | No post-unlock failed-login sequence is represented. |

---

## 4. Acceptance Criteria Coverage Review

| Acceptance Criteria | Current Coverage | Status | Review |
|---|---|---|---|
| AC-01 — Failed Login Below Threshold | TS-003 | Covered | Scenario verifies the account remains unlocked immediately below the threshold. |
| AC-02 — Lock Account at Threshold | TS-004 | Covered | Scenario verifies the fifth consecutive failure causes locking. |
| AC-03 — Login While Locked | TS-006, TS-007 | Covered | Authentication rejection and required message are both represented. |
| AC-04 — Automatic Unlock | TS-008, TS-009 | Covered | Unlock and subsequent login behavior are represented. |
| AC-05 — Successful Login Resets Counter | TS-005 | Partial | Counter reset is represented, but no scenario proves later failures start a new sequence. |

---

## 5. Missing Coverage

### GAP-001 — Account Remains Locked Before Expiration

**Related Requirement:** Requirement 9

The scenario set verifies automatic unlock after the 30-minute period but does not verify the complementary requirement that the account remains locked before that period expires.

Current coverage:

```text
Account Locked
      ↓
30-Minute Period Expires
      ↓
Automatic Unlock
```

Missing coverage:

```text
Account Locked
      ↓
Less Than 30 Minutes Elapsed
      ↓
Account Still Locked
```

**Severity:** High

**Reason:** An implementation that unlocks the account prematurely could still pass the existing automatic-unlock scenario.

**Recommended scenario:**

> Verify the account remains locked before the 30-minute lock period expires.

---

### GAP-002 — Failed-Login Tracking After Automatic Unlock

**Related Requirement:** Requirement 14

No current scenario verifies that failed-login tracking starts again after automatic unlock.

Missing coverage should demonstrate:

```text
Account Locked
      ↓
Automatic Unlock
      ↓
New Failed Login Attempts
      ↓
New Consecutive-Failure Sequence
```

**Severity:** High

**Reason:** Incorrect post-unlock counter state could cause premature re-locking or prevent the next lock threshold from being applied correctly.

**Recommended scenario:**

> Verify failed-login tracking starts again after the account has been automatically unlocked.

---

### GAP-003 — New Failure Sequence After Successful-Login Reset

**Related Requirement:** Requirement 7 / AC-05

TS-005 verifies that a successful login resets the failed-login counter.

However, it does not demonstrate the behavioral consequence of that reset.

Current coverage:

```text
Failed Attempts
      ↓
Successful Login
      ↓
Counter Reset
```

Additional coverage should demonstrate:

```text
Failed Attempts
      ↓
Successful Login
      ↓
Counter Reset
      ↓
New Failed Attempt
      ↓
New Failure Sequence
```

**Severity:** Medium

**Reason:** A system could report/reset the counter but still incorrectly retain previous failures when evaluating the next threshold.

**Recommended scenario:**

> Verify a new consecutive failed-login sequence starts after a successful login resets the failed-login counter.

---

## 6. Boundary Coverage Review

### Five-Attempt Threshold

Current scenarios provide appropriate boundary coverage:

```text
4 Failures → Unlocked
5 Failures → Locked
```

Covered by:

- TS-003.
- TS-004.

**Status: Covered**

---

### 30-Minute Lock Boundary

Current coverage verifies:

```text
After lock period expires
→ Automatically unlocked
```

But it does not verify:

```text
Before lock period expires
→ Remains locked
```

Therefore, lock-duration boundary coverage is incomplete.

The exact behavior at the precise expiration instant is not sufficiently defined by the requirement and should not be assigned an assumed expected result.

**Status: Partial**

---

## 7. State Transition Coverage Review

The primary account states are:

```text
UNLOCKED
LOCKED
```

### Unlocked → Locked

```text
UNLOCKED
    │
    │ Fifth consecutive failed login
    ▼
LOCKED
```

Covered by TS-003 and TS-004.

**Status: Covered**

### Locked → Unlocked

```text
LOCKED
    │
    │ 30-minute period expires
    ▼
UNLOCKED
```

Covered by TS-008.

**Status: Covered**

### Failed Counter Reset

```text
UNLOCKED
    │
1–4 Failed Attempts
    │
Successful Login
    ▼
UNLOCKED
Counter Reset
```

Covered by TS-005.

However, continuation into a new failure sequence is not covered.

**Status: Partial**

### Post-Unlock Tracking

```text
LOCKED
    ↓
Automatic Unlock
    ↓
Failed-Login Tracking Starts Again
```

No scenario covers the final tracking behavior.

**Status: Missing**

---

## 8. Duplicate Coverage Review

No material duplicate scenarios were identified.

Some scenarios operate within the same functional areas but verify distinct objectives.

For example:

```text
TS-003
→ Below-threshold account state

TS-004
→ At-threshold lock transition
```

These scenarios are complementary boundary coverage rather than duplicates.

Similarly:

```text
TS-008
→ Automatic unlock

TS-009
→ Authentication after unlock
```

These represent separate behaviors and should remain independent.

**Duplicate Coverage Status: PASS**

---

## 9. Clarification-Dependent Coverage

The following potential testing areas are relevant but are not sufficiently defined by the supplied requirement.

They should not be classified as missing required coverage until expected behavior is clarified.

| Area | Undefined Behavior | Review Classification |
|---|---|---|
| Exact timer boundary | Login exactly at the 30-minute expiration instant. | Clarification Required |
| Attempts while locked | Effect on failed-login counter. | Clarification Required |
| Lock extension | Whether attempts while locked restart or extend the timer. | Clarification Required |
| Cross-device/session tracking | Whether attempts across devices, browsers, or sessions contribute to the same account counter. | Clarification Required |
| Unknown email address | Failed-login behavior for an unregistered email. | Clarification Required |
| Concurrent login attempts | Counter behavior for simultaneous attempts near the threshold. | Clarification Required |
| Exact post-unlock counter value | Requirement says tracking starts again but does not explicitly state a numeric value. | Clarification Required |

These items must remain separate from confirmed coverage gaps.

---

## 10. Recommended Coverage Additions

The following scenarios should be added to close requirement-supported coverage gaps:

| Recommendation ID | Priority | Recommended Scenario | Related Requirement |
|---|---|---|---|
| REC-001 | High | Verify the account remains locked before the 30-minute lock period expires. | Requirement 9 |
| REC-002 | High | Verify failed-login tracking starts again after automatic unlock. | Requirement 14 |
| REC-003 | Medium | Verify a new consecutive failed-login sequence begins after a successful login resets the previous failed-login counter. | Requirement 7 / AC-05 |

Adding these scenarios would improve coverage without requiring assumptions about undefined behavior.

---

## 11. Coverage Summary

### Requirement Coverage

```text
Fully Covered Requirements:     11
Partially Covered Requirements:  1
Missing Requirements:            2
```

Classification:

- Fully covered: R1–R6, R8, R10–R13.
- Partial: R7.
- Missing: R9, R14.

### Acceptance Criteria Coverage

```text
Fully Covered ACs:      4
Partially Covered ACs:  1
Missing ACs:            0
```

Classification:

- Fully covered: AC-01, AC-02, AC-03, AC-04.
- Partial: AC-05.

---

## 12. Final Assessment

**Overall Coverage Status: PARTIAL**

The current scenario set covers the primary account-lock behavior and all major acceptance-criteria flows.

However, it does not yet provide complete requirement coverage.

Three meaningful improvements are required:

```text
1. Verify account remains locked before 30-minute expiration.
2. Verify failed-login tracking starts again after automatic unlock.
3. Verify successful-login reset creates a genuinely new failure sequence.
```

No significant duplicate coverage was identified.

Potential scenarios involving undefined timer semantics, attempts during lock, cross-device behavior, unknown accounts, concurrency, and exact post-unlock counter values should remain clarification-dependent rather than being treated as confirmed missing coverage.

After adding the three recommended scenarios, the scenario set would provide substantially stronger coverage of all currently defined feature behavior.