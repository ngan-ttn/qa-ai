# Regression Analysis — Account Lock After Failed Login Attempts

## 1. Overview

This artifact analyzes the regression impact of introducing temporary account locking after repeated failed login attempts.

The analysis is based on:

- `Sample-Requirement.md`
- `Requirement-Analysis.md`
- `Business-Rules.md`
- `Risk-Analysis.md`
- `Test-Scenarios.md`
- `Coverage-Review.md`
- `Test-Cases.md`

No existing-system architecture, API contract, database design, integration map, or implementation detail is provided in the end-to-end input.

Therefore, this analysis distinguishes between:

```text
Confirmed Requirement-Derived Impact
Potential Regression Area
Unknown Dependency
Investigation Required
```

Potential system dependencies are not promoted to confirmed impact without supporting evidence.

---

## 2. Change Summary

The feature introduces new authentication behavior around repeated incorrect-password attempts.

The confirmed change includes:

- Tracking consecutive incorrect-password attempts per registered account.
- Locking the account on the fifth consecutive failed attempt.
- Resetting failed-login tracking after successful authentication before the threshold.
- Rejecting authentication during an active temporary lock.
- Keeping the account locked for 30 minutes.
- Automatically unlocking the account after the lock period.
- Allowing authentication again after unlock.
- Starting failed-login tracking again after unlock.

Conceptually:

```text
Existing Login Behavior
        +
Failed-Login Tracking
        +
Temporary Lock State
        +
Automatic Recovery
        ↓
Updated Authentication Behavior
```

---

## 3. Confirmed Functional Impact

The following areas are directly supported by the requirement and therefore represent confirmed functional impact.

| Impact ID | Area | Confirmed Change | Priority |
|---|---|---|---|
| IMP-001 | Login Authentication | Login success now depends on both valid credentials and the account not being locked. | High |
| IMP-002 | Failed Login Handling | Incorrect-password attempts must participate in account-specific consecutive-failure tracking. | High |
| IMP-003 | Lock Threshold | Fifth consecutive failed attempt introduces a new locked state. | High |
| IMP-004 | Counter Reset | Successful login before threshold resets the current failed-login sequence. | High |
| IMP-005 | Locked-State Authentication | Authentication must be rejected while temporary lock is active. | High |
| IMP-006 | User Feedback | Locked-account login attempts must display the required message. | Medium |
| IMP-007 | Time-Based State | The locked state must remain active for 30 minutes. | High |
| IMP-008 | Automatic Recovery | The account must automatically return to an unlocked state after expiration. | High |
| IMP-009 | Post-Unlock Authentication | Login must become available again after unlock. | High |
| IMP-010 | Post-Unlock Tracking | Failed-login tracking must start again after unlock. | High |
| IMP-011 | Account Isolation | Failed-login state must remain account-specific. | High |

---

## 4. Confirmed Regression Scope

Regression should include existing behaviors that are explicitly part of the modified requirement flow.

### 4.1 Normal Login

Existing valid-login behavior must continue to work when:

```text
Account = Unlocked
Credentials = Valid
```

Regression focus:

- Valid authentication still succeeds.
- New account-lock logic does not incorrectly block eligible users.

**Priority: High**

---

### 4.2 Invalid Password Login

Existing incorrect-password rejection remains part of the flow but now has additional state consequences.

Regression focus:

```text
Incorrect Password
→ Authentication Fails
→ Failure Is Tracked
```

The original failure behavior must not be lost while adding tracking.

**Priority: High**

---

### 4.3 Repeated Failed Login

Repeated failed authentication now introduces threshold-dependent behavior.

Regression focus:

```text
Failures 1–4
→ Remain Unlocked

Failure 5
→ Locked
```

Potential regression includes:

- Early locking.
- Late locking.
- Missing lock.
- Incorrect sequence tracking.

**Priority: High**

---

### 4.4 Successful Login During Failure Sequence

Successful authentication must continue to work before the threshold while also resetting the failure sequence.

Regression focus:

```text
1–4 Failures
+
Valid Login
→ Authentication Success
→ Previous Failure Sequence Reset
```

**Priority: High**

---

### 4.5 Locked-State Login

The new locked state modifies login eligibility.

Regression focus:

```text
Locked + Correct Password
→ Rejected

Locked + Login Attempt
→ Required Message
```

**Priority: High**

---

### 4.6 Automatic Recovery

Login behavior must recover after expiration.

Regression focus:

```text
Locked
→ 30-Minute Expiration
→ Unlocked
→ Valid Authentication Available
```

**Priority: High**

---

### 4.7 Account-Specific Behavior

The feature introduces account-specific tracking.

Regression must confirm that state created for one account does not affect another.

**Priority: High**

---

## 5. Regression Coverage from Existing Test Cases

The current generated test suite already provides confirmed regression coverage for the requirement-defined areas.

| Regression Area | Existing Test Cases |
|---|---|
| Normal valid login | TC-001 |
| Invalid-password rejection | TC-002 |
| Failed-login tracking | TC-003 |
| Below-threshold behavior | TC-004, TC-005 |
| Lock threshold | TC-006 |
| Successful-login reset | TC-007, TC-008, TC-009 |
| Account isolation | TC-010, TC-011 |
| Locked-state authentication | TC-012, TC-013 |
| Locked-account message | TC-014 |
| Lock duration | TC-015 |
| Automatic unlock | TC-016 |
| Post-unlock authentication | TC-017 |
| Post-unlock tracking | TC-018 |
| Repeated lock lifecycle | TC-019 |
| Full lifecycle | TC-020 |

The existing test suite therefore provides a reusable regression baseline for the confirmed feature behavior.

---

## 6. High-Priority Regression Areas

### RG-001 — Authentication Eligibility

New lock state affects whether valid credentials are sufficient for authentication.

Regression must preserve:

```text
Unlocked + Valid Credentials
→ Allowed

Locked + Valid Credentials
→ Rejected
```

This is one of the highest-priority areas because incorrect behavior could either bypass account protection or block legitimate users.

---

### RG-002 — Failure Sequence Integrity

Regression should verify that:

```text
Failure Count
        +
Consecutive Sequence
        +
Successful Login Reset
```

remain consistent across repeated login actions.

Relevant cases:

- TC-003
- TC-005
- TC-006
- TC-007
- TC-008
- TC-009

---

### RG-003 — Lock-State Transition

Regression must preserve the correct state transition:

```text
UNLOCKED
    ↓
5th Consecutive Failure
    ↓
LOCKED
```

and prevent:

```text
Early lock
Late lock
Missing lock
```

Relevant cases:

- TC-005
- TC-006

---

### RG-004 — Recovery Transition

Regression must preserve:

```text
LOCKED
    ↓
30-Minute Expiration
    ↓
UNLOCKED
```

Relevant cases:

- TC-015
- TC-016
- TC-017

---

### RG-005 — Account Isolation

Tracking must remain isolated by account.

Relevant cases:

- TC-010
- TC-011

This is high priority because state leakage could cause incorrect lockouts or authentication behavior across users.

---

## 7. Regression by State

### Unlocked State

Regression should verify:

```text
Valid Credentials
→ Authentication succeeds

Incorrect Password
→ Authentication fails

Failures 1–4
→ Account remains unlocked
```

Relevant test cases:

```text
TC-001
TC-002
TC-004
TC-005
```

---

### Locked State

Regression should verify:

```text
Login Attempt
→ Rejected

Correct Password
→ Still rejected

Required Message
→ Displayed
```

Relevant test cases:

```text
TC-012
TC-013
TC-014
TC-015
```

---

### Automatically Unlocked State

Regression should verify:

```text
Automatic Unlock
→ Login available

New failed attempts
→ New tracking sequence
```

Relevant test cases:

```text
TC-016
TC-017
TC-018
TC-019
```

---

## 8. Regression by Business Rule

| Business Rule | Regression Focus | Test Coverage |
|---|---|---|
| BR-001 | Preserve account-specific tracking | TC-003, TC-010, TC-011 |
| BR-002 | Preserve exact five-attempt threshold | TC-004, TC-005, TC-006 |
| BR-003 | Preserve reset semantics | TC-007, TC-008, TC-009 |
| BR-004 | Preserve 30-minute locked state | TC-015, TC-016 |
| BR-005 | Preserve authentication rejection while locked | TC-012, TC-013 |
| BR-006 | Preserve lock message | TC-014 |
| BR-007 | Preserve automatic unlock | TC-016 |
| BR-008 | Preserve login availability after unlock | TC-017 |
| BR-009 | Preserve restarted tracking after unlock | TC-018, TC-019 |

All confirmed business rules have corresponding regression coverage in the generated test baseline.

---

## 9. Potential Regression Areas Requiring System Context

The following areas may be related to authentication changes, but the end-to-end input does not provide enough evidence to classify them as confirmed impact.

### POT-001 — Existing Authenticated Sessions

Potential question:

```text
If Account Becomes Locked
        ↓
What Happens to Existing Session?
```

The requirement does not define this behavior.

**Classification:** Investigation Required

---

### POT-002 — Password Reset

Potential relationship:

```text
Password Reset
↔
Failed Login State / Lock State
```

No dependency is supplied.

**Classification:** Clarification / Investigation Required

---

### POT-003 — Password Change

No information defines whether password change interacts with:

- Failed-login tracking.
- Active lock state.

**Classification:** Clarification / Investigation Required

---

### POT-004 — Multiple Browsers or Devices

The requirement says tracking is account-specific but does not define how that behavior is implemented across access channels.

**Classification:** Clarification / Investigation Required

---

### POT-005 — Concurrent Login Requests

No concurrency model is provided.

Potential issues may include:

- Lost counter updates.
- Incorrect threshold evaluation.
- Inconsistent state transition.

**Classification:** Clarification / Investigation Required

---

### POT-006 — Authentication API

The requirement does not provide:

- API endpoints.
- Request schema.
- Response schema.
- Status codes.

Therefore API regression scope cannot be confirmed.

**Classification:** Investigation Required

---

### POT-007 — Database Persistence

The requirement does not provide:

- Database tables.
- Counter fields.
- Lock-state fields.
- Transaction behavior.

Database regression checks cannot be specified from the available input.

**Classification:** Investigation Required

---

### POT-008 — Audit Logging

No audit or security-event requirement is supplied.

It is unknown whether:

```text
Failed Login
Account Lock
Automatic Unlock
```

must be recorded.

**Classification:** Investigation Required

---

### POT-009 — Notification Behavior

No email, SMS, push, or other notification behavior is defined.

**Classification:** No Confirmed Impact

---

## 10. Clarification-Dependent Regression Areas

The clarification-dependent scenario candidates remain relevant to regression assessment:

```text
CTS-001 → CTS-009
```

Mapping:

| Candidate | Regression Concern |
|---|---|
| CTS-001 | Counter behavior during active lock |
| CTS-002 | Timer behavior during active lock |
| CTS-003 | Exact expiration instant |
| CTS-004 | Cross-browser behavior |
| CTS-005 | Cross-device behavior |
| CTS-006 | Concurrent requests |
| CTS-007 | Existing authenticated sessions |
| CTS-008 | Password-management interaction |
| CTS-009 | Unknown-account behavior |

These areas should not enter the confirmed regression suite until their expected behavior is defined.

---

## 11. Regression Priority Matrix

| Regression Area | Impact | Priority |
|---|---|---|
| Valid authentication | High | High |
| Incorrect-password rejection | High | High |
| Failed-login tracking | High | High |
| Five-attempt threshold | High | High |
| Successful-login reset | High | High |
| Account isolation | High | High |
| Locked-state enforcement | High | High |
| 30-minute lock period | High | High |
| Automatic unlock | High | High |
| Post-unlock tracking | High | High |
| Lock message | Medium | Medium |
| Existing sessions | Unknown | Investigation |
| Password management | Unknown | Investigation |
| Cross-device/session behavior | Unknown | Investigation |
| Concurrent authentication | Unknown | Investigation |
| API behavior | Unknown | Investigation |
| Database behavior | Unknown | Investigation |
| Audit behavior | Unknown | Investigation |

---

## 12. Recommended Smoke Regression

A minimum smoke regression set should verify the most critical authentication lifecycle.

Recommended baseline:

```text
TC-001
Normal successful login

TC-002
Incorrect-password rejection

TC-005
Account remains unlocked below threshold

TC-006
Account locks at threshold

TC-012
Correct password cannot bypass lock

TC-016
Automatic unlock

TC-017
Successful authentication after unlock
```

This provides fast confirmation of:

```text
Normal Login
        +
Failure Handling
        +
Threshold
        +
Lock Enforcement
        +
Recovery
```

---

## 13. Recommended Focused Regression

Focused regression should include:

```text
TC-001 → TC-019
```

with particular attention to:

- Counter sequences.
- Threshold boundaries.
- Successful-login reset.
- Isolation.
- Lock duration.
- Post-unlock behavior.

`TC-020` should additionally be executed as lifecycle integration coverage.

---

## 14. Full Confirmed Regression Baseline

The current feature-level confirmed regression baseline is:

```text
TC-001 → TC-020
```

These tests represent behavior supported directly by the current requirement and upstream QA artifacts.

This baseline may be expanded when additional system dependencies become known.

---

## 15. Regression Scope Exclusions

The following areas are not included as confirmed regression scope from the current input alone:

```text
API contract validation
Database validation
Existing-session invalidation
Password reset integration
Password change integration
Audit-event verification
Notification verification
Cross-device synchronization
Concurrency synchronization
```

Exclusion does not mean these areas are proven unaffected.

It means:

```text
Current Input
      ↓
Insufficient Evidence
      ↓
No Confirmed Regression Claim
```

---

## 16. Investigation Questions

Before extending regression beyond the confirmed requirement scope, the following information should be collected:

1. What existing authentication components are modified by the feature?
2. Where is failed-login state stored?
3. Where is temporary lock state stored?
4. How is the 30-minute expiration implemented?
5. Is authentication exposed through an API requiring contract regression?
6. Do web/mobile/other clients share the same account lock state?
7. What happens to existing sessions when the account becomes locked?
8. Does password reset or password change alter lock state?
9. Is there an administrative unlock flow?
10. Are lock/unlock events recorded in logs or audit records?
11. Are users notified when an account becomes locked?
12. How are simultaneous login attempts synchronized?

Answers to these questions may expand the regression scope.

---

## 17. Regression Traceability

The confirmed chain is:

```text
Requirement
    ↓
Business Rules
    ↓
Risks
    ↓
Test Scenarios
    ↓
Test Cases
    ↓
Regression Baseline
```

For this example:

```text
R1–R14
   ↓
BR-001–BR-009
   ↓
RISK-001–RISK-009
   ↓
TS-001–TS-020
   ↓
TC-001–TC-020
   ↓
Confirmed Regression Baseline
```

Clarification-dependent items remain outside that confirmed chain.

---

## 18. Regression Analysis Summary

The confirmed regression impact is concentrated on requirement-defined authentication behavior:

```text
Normal Login
      +
Incorrect Password Handling
      +
Failed-Login Tracking
      +
Five-Attempt Threshold
      +
Counter Reset
      +
Account Isolation
      +
Temporary Lock
      +
Lock Enforcement
      +
30-Minute Recovery
      +
Post-Unlock Tracking
```

The generated `TC-001 → TC-020` suite provides a reusable feature-level regression baseline for these confirmed behaviors.

A broader regression impact assessment cannot be completed from the requirement alone.

Areas such as APIs, databases, existing sessions, password management, concurrency, multiple clients, audit logging, and notifications require additional existing-system context.

Therefore:

```text
Confirmed Requirement Impact
→ Regression baseline available

Unknown System Dependency
→ Investigation required

Undefined Business Behavior
→ Clarification required
```

No unsupported system dependency is treated as a confirmed regression fact.