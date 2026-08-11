# Risk Analysis — Account Lock After Failed Login Attempts

## 1. Overview

This artifact identifies and prioritizes risks associated with the Account Lock After Failed Login Attempts feature.

The analysis is based on:

- `Sample-Requirement.md`
- `Requirement-Analysis.md`
- `Business-Rules.md`

The purpose is to determine where failures would have the greatest impact and which areas require stronger testing attention.

This artifact does not generate test scenarios or test cases.

---

## 2. Risk Assessment Model

Each identified risk is evaluated using:

### Likelihood

| Level | Meaning |
|---|---|
| High | Failure is reasonably likely because of boundary, state, timing, or interaction complexity. |
| Medium | Failure is possible but depends on specific conditions or implementation behavior. |
| Low | Failure is less likely based on the available requirement information. |

### Impact

| Level | Meaning |
|---|---|
| High | Failure may compromise account protection or prevent legitimate authentication. |
| Medium | Failure causes incorrect functional behavior but does not completely defeat the primary protection mechanism. |
| Low | Failure has limited functional or user impact. |

### Risk Priority

Risk priority is determined qualitatively from likelihood and impact.

```text
High Impact + High/Medium Likelihood
→ High Priority

Medium Impact + Medium/High Likelihood
→ Medium Priority

Limited Impact + Low Likelihood
→ Low Priority
```

This example does not assign unsupported numeric probability or financial-impact values.

---

## 3. Risk Summary

| Risk ID | Risk | Related Rules | Likelihood | Impact | Priority |
|---|---|---|---|---|---|
| RISK-001 | Account is not locked at the fifth consecutive failed attempt. | BR-002 | High | High | High |
| RISK-002 | Account is locked before the fifth consecutive failed attempt. | BR-002 | Medium | High | High |
| RISK-003 | Successful login does not reset the failed-login sequence. | BR-003 | Medium | High | High |
| RISK-004 | Failed attempts from one account affect another account. | BR-001 | Medium | High | High |
| RISK-005 | Locked account can authenticate with valid credentials. | BR-005 | Medium | High | High |
| RISK-006 | Account unlocks before the required 30-minute period. | BR-004, BR-007 | Medium | High | High |
| RISK-007 | Account remains locked after the lock period expires. | BR-004, BR-007, BR-008 | Medium | High | High |
| RISK-008 | Incorrect or missing locked-account message is displayed. | BR-006 | Medium | Medium | Medium |
| RISK-009 | Failed-login tracking does not restart correctly after automatic unlock. | BR-009 | Medium | High | High |
| RISK-010 | Undefined lock-period behavior causes inconsistent authentication results. | BR-004, BR-005 | Medium | High | High |
| RISK-011 | Undefined cross-session behavior causes inconsistent account-level tracking. | BR-001 | Medium | High | High |
| RISK-012 | Concurrent attempts near the threshold produce incorrect lock behavior. | BR-002 | Medium | High | High |

---

## 4. Detailed Risk Analysis

### RISK-001 — Account Not Locked at Threshold

**Related Rule:** BR-002  
**Likelihood:** High  
**Impact:** High  
**Priority:** High

#### Risk Description

The account may remain unlocked after the fifth consecutive incorrect-password attempt.

#### Trigger Area

```text
4 Consecutive Failures
        ↓
5th Incorrect Password
        ↓
Expected: LOCKED
```

#### Potential Impact

Failure would directly violate the primary protection behavior defined by the feature.

Additional authentication attempts could remain available when the account should already be locked.

#### Testing Focus

Testing should strongly cover:

- Attempts immediately below the threshold.
- The exact threshold.
- Account state immediately after the fifth failure.

---

### RISK-002 — Premature Account Lock

**Related Rule:** BR-002  
**Likelihood:** Medium  
**Impact:** High  
**Priority:** High

#### Risk Description

The account may become locked before five consecutive failures occur.

#### Potential Impact

A legitimate user could lose authentication access earlier than required.

#### Testing Focus

The boundary immediately below the lock threshold requires explicit verification.

```text
1–4 failures
→ Must remain unlocked
```

---

### RISK-003 — Failed-Login Sequence Not Reset

**Related Rule:** BR-003  
**Likelihood:** Medium  
**Impact:** High  
**Priority:** High

#### Risk Description

A successful login before the threshold may fail to reset previous failed-login tracking.

Example failure pattern:

```text
3 Failures
    ↓
Successful Login
    ↓
2 Later Failures
    ↓
Incorrectly Treated as 5 Consecutive Failures
```

#### Potential Impact

The user could be locked even though the failures were not consecutive.

#### Testing Focus

Testing should verify interruption of the failed-login sequence by successful authentication.

---

### RISK-004 — Failed-Login State Leaks Between Accounts

**Related Rule:** BR-001  
**Likelihood:** Medium  
**Impact:** High  
**Priority:** High

#### Risk Description

Failed attempts belonging to one registered account may incorrectly influence another account's failed-login state.

#### Potential Impact

This could cause:

- Incorrect account locking.
- Incorrect failed-login counts.
- Loss of account isolation.

#### Testing Focus

Use at least two registered accounts with independent failure sequences.

---

### RISK-005 — Authentication Allowed During Active Lock

**Related Rule:** BR-005  
**Likelihood:** Medium  
**Impact:** High  
**Priority:** High

#### Risk Description

The system may validate correct credentials and allow authentication even though the account is temporarily locked.

#### Potential Impact

This would bypass the account-lock protection.

#### Testing Focus

A correct password must be tested explicitly while the account is in the locked state.

---

### RISK-006 — Account Unlocks Too Early

**Related Rules:** BR-004, BR-007  
**Likelihood:** Medium  
**Impact:** High  
**Priority:** High

#### Risk Description

The account may become available for authentication before the required 30-minute lock duration has expired.

#### Potential Impact

The protection period would be shorter than required.

#### Testing Focus

Verify authentication behavior shortly before expiration and after expiration.

The exact expiration instant remains clarification-dependent.

---

### RISK-007 — Account Remains Locked Too Long

**Related Rules:** BR-004, BR-007, BR-008  
**Likelihood:** Medium  
**Impact:** High  
**Priority:** High

#### Risk Description

The account may fail to unlock automatically after the required lock period.

#### Potential Impact

A legitimate user may remain unable to access the account beyond the required restriction period.

#### Testing Focus

Verify:

```text
Locked
   ↓
30-Minute Period Expires
   ↓
Unlocked
   ↓
Authentication Available Again
```

---

### RISK-008 — Incorrect Locked-Account Message

**Related Rule:** BR-006  
**Likelihood:** Medium  
**Impact:** Medium  
**Priority:** Medium

#### Risk Description

The required message may:

- Not appear.
- Contain incorrect wording.
- Appear under the wrong state.

#### Expected Message

```text
Your account has been temporarily locked. Please try again later.
```

#### Potential Impact

The user may not understand why authentication is being rejected.

#### Testing Focus

Verify the exact requirement-defined message while the account is locked.

---

### RISK-009 — Incorrect Tracking After Automatic Unlock

**Related Rule:** BR-009  
**Likelihood:** Medium  
**Impact:** High  
**Priority:** High

#### Risk Description

The previous failed-login sequence may incorrectly continue after automatic unlock.

#### Potential Impact

The account could be locked again earlier than expected during a new failed-login sequence.

#### Testing Focus

Verify that failed-login tracking starts again after automatic unlock.

The internal counter representation should not be assumed.

---

## 5. Boundary Risks

Two requirement boundaries carry particularly high risk.

### Failure Threshold

```text
4 failures
    │
    ├── Expected: UNLOCKED
    │
5 failures
    │
    └── Expected: LOCKED
```

Potential defects include:

- Lock at attempt 4.
- No lock at attempt 5.
- Lock only after attempt 6.
- Incorrect state transition after attempt 5.

This boundary should receive high testing priority.

---

### Lock Duration

```text
Before expiration
→ LOCKED

After expiration
→ UNLOCKED
```

Potential defects include:

- Early unlock.
- Late unlock.
- No automatic unlock.
- Inconsistent behavior near expiration.

The exact behavior at the precise 30-minute instant remains undefined.

---

## 6. State-Transition Risks

The feature contains critical state transitions:

```text
UNLOCKED
    │
    │ 5 consecutive failures
    ▼
LOCKED
    │
    │ 30-minute expiration
    ▼
UNLOCKED
```

Incorrect transitions could produce:

```text
Failure threshold reached
→ Still UNLOCKED

Lock not expired
→ Already UNLOCKED

Lock expired
→ Still LOCKED
```

Because authentication behavior changes based on state, transition defects may affect several business rules simultaneously.

---

## 7. Sequence Risks

The term **consecutive** creates sequence-sensitive behavior.

Valid rule:

```text
Failure
Failure
Success
Failure
Failure
```

must not be treated as:

```text
4 Consecutive Failures
```

Therefore, testing must distinguish:

- Total failures.
- Consecutive failures.
- Interrupted failure sequences.

This risk primarily affects BR-002 and BR-003.

---

## 8. Isolation Risks

BR-001 requires account-specific tracking.

Example:

```text
Account A
4 failures

Account B
1 failure
```

must not produce:

```text
5 shared failures
→ Account B locked
```

Testing should therefore validate independent account state.

The requirement does not define the implementation mechanism used to achieve this isolation.

---

## 9. Clarification-Dependent Risks

Some risks cannot be converted into confirmed expected behavior because the requirement is incomplete.

### RISK-010 — Login Attempts During Active Lock

The requirement does not define whether attempts during lock:

- Affect failed-login tracking.
- Restart the lock timer.
- Extend the lock timer.

#### Risk

Different implementations may produce inconsistent lock behavior.

#### Status

```text
Clarification Required
```

Testing may observe current behavior, but it cannot determine correctness without an approved expected rule.

---

### RISK-011 — Cross-Session Tracking

The requirement defines account-specific tracking but does not explicitly define behavior across:

- Browsers.
- Devices.
- Sessions.

#### Risk

The same account may have inconsistent failure state depending on where authentication is attempted.

#### Status

```text
Clarification Required
```

---

### RISK-012 — Concurrent Threshold Attempts

The requirement does not define simultaneous authentication behavior near the threshold.

Example:

```text
Current Failed Attempts = 4

Request A ─┐
           ├── submitted concurrently
Request B ─┘
```

#### Risk

Concurrent processing could produce:

- Incorrect failed-login count.
- Delayed lock.
- Duplicate transition.
- Inconsistent authentication result.

#### Status

```text
Clarification Required
+
Investigation Required
```

Functional expectations require clarification, while implementation risk requires system-level investigation.

---

## 10. Additional Undefined Risk Areas

The requirement analysis identified other undefined interactions:

- Existing authenticated sessions after account lock.
- Password reset during active lock.
- Password change during active lock.
- Unknown/unregistered email behavior.

These areas are valid investigation or clarification candidates, but they are not promoted to confirmed feature risks without additional business context.

Downstream test design should not invent expected behavior for them.

---

## 11. Risk-to-Rule Traceability

| Risk | Business Rule(s) | Requirement Basis |
|---|---|---|
| RISK-001 | BR-002 | R6, R8, AC-02 |
| RISK-002 | BR-002 | R6, AC-01, AC-02 |
| RISK-003 | BR-003 | R7, AC-05 |
| RISK-004 | BR-001 | R5 |
| RISK-005 | BR-005 | R10, AC-03 |
| RISK-006 | BR-004, BR-007 | R9, R12, AC-04 |
| RISK-007 | BR-004, BR-007, BR-008 | R9, R12, R13, AC-04 |
| RISK-008 | BR-006 | R11, AC-03 |
| RISK-009 | BR-009 | R14 |
| RISK-010 | BR-004, BR-005 | Q-001, Q-002 |
| RISK-011 | BR-001 | Q-004, Q-005 |
| RISK-012 | BR-002 | Q-006 |

---

## 12. Testing Priority

Based on the available requirement information, testing attention should be prioritized as follows.

### Priority 1 — Critical Functional Protection

```text
RISK-001
RISK-002
RISK-003
RISK-004
RISK-005
```

Focus:

- Lock threshold.
- Consecutive-failure semantics.
- Reset behavior.
- Account isolation.
- Locked-state authentication.

### Priority 2 — Time and Recovery

```text
RISK-006
RISK-007
RISK-009
```

Focus:

- Lock duration.
- Automatic unlock.
- Post-unlock behavior.

### Priority 3 — User Feedback

```text
RISK-008
```

Focus:

- Required locked-account message.

### Clarification / Investigation

```text
RISK-010
RISK-011
RISK-012
```

These risks should influence test planning, but undefined behavior must not be converted into assumed expected results.

---

## 13. Risk Coverage Guidance

The downstream scenario set should provide sufficient coverage for:

```text
Threshold
Boundary
Sequence
Reset
Isolation
Locked State
Time Boundary
Automatic Recovery
Post-Unlock Tracking
User Feedback
```

High-priority risks should receive stronger scenario coverage than lower-impact behavior.

However, this artifact intentionally does not define individual scenarios.

Scenario generation remains the responsibility of the downstream `scenario-generator` capability.

---

## 14. Risk Analysis Summary

The feature has a concentrated risk profile around four areas:

```text
1. Threshold Correctness
        ↓
4 failures vs. 5 failures

2. Sequence Correctness
        ↓
Consecutive failures + reset

3. State Enforcement
        ↓
Unlocked ↔ Locked

4. Time-Based Recovery
        ↓
30-minute automatic unlock
```

The highest-impact failure would be an account remaining accessible when it should be locked.

A second major failure class is legitimate-user lockout caused by premature locking, incorrect reset behavior, or failure to unlock automatically.

The requirement provides sufficient information to prioritize confirmed functional risks.

Behavior involving concurrency, cross-session tracking, and login attempts during an active lock remains clarification- or investigation-dependent and must not be silently converted into business expectations.