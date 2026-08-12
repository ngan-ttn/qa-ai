# Regression Analysis — Account Lockout After Failed Login Attempts

## Golden Output Metadata

- Dataset ID: `REQ-AUTH-001`
- Source Requirement: `datasets/requirements/simple/REQ-AUTH-001.md`
- Artifact Type: `Regression Analysis`
- Review Status: `Approved`
- Evaluation Purpose: Reference output for evaluating regression-impact identification, direct-versus-potential impact separation, regression prioritization, dependency reasoning, scope control, traceability, and assumption management

---

## Regression Analysis Summary

The account-lockout requirement changes password-based authentication behavior by introducing account-specific failed-attempt tracking, a five-attempt lock threshold, a 15-minute temporary lock, automatic unlock, and failed-attempt counter reset behavior.

The highest-confidence regression impact is therefore concentrated around:

- Username-and-password authentication
- Successful login behavior
- Failed login behavior
- Authentication state maintained per account
- Lock-state enforcement
- Time-based transition from locked to unlocked
- Counter reset and subsequent authentication sequences

The source requirement does not provide implementation architecture, API contracts, database schema, UI specifications, session-management behavior, password-reset behavior, or alternative authentication behavior.

Those areas must not be represented as confirmed regression impacts.

---

## Regression Classification

Regression impact is classified into three levels.

### Confirmed Direct Impact

Behavior explicitly changed or governed by the source requirement.

These areas require regression coverage.

### Potential Adjacent Impact

Behavior that may interact with the feature in a real implementation but is not sufficiently defined by the source requirement.

These areas should be validated against system architecture or implementation changes before being added to the regression suite.

### Unsupported / Out of Scope

Behavior outside the defined source scope or behavior for which no dependency can be established from the supplied requirement.

These areas must not be presented as required regression coverage.

---

## Confirmed Direct Regression Impact

### REG-AUTH-001 — Successful Password Authentication

**Impact**

Existing successful username-and-password login behavior may be affected by the introduction of failed-attempt tracking and account lock state.

**Regression Risk**

A valid user who is not locked may be incorrectly prevented from authenticating.

A successful login may also fail to reset an existing below-threshold failed-attempt sequence.

**Regression Coverage**

Verify:

- Correct password succeeds when the account is unlocked.
- Successful login resets a below-threshold failed-attempt counter.
- Authentication remains available after the reset.

**Priority**

High

**Traceability**

- AC-08
- BR-AUTH-011
- TS-AUTH-001
- TS-AUTH-012
- TS-AUTH-013

---

### REG-AUTH-002 — Incorrect Password Handling

**Impact**

Incorrect-password behavior now affects persistent or logical account security state through the failed-attempt counter.

**Regression Risk**

An incorrect password may:

- Fail to increment the counter.
- Increment the wrong account's counter.
- Increment by an incorrect amount.
- Trigger lock behavior too early.

**Regression Coverage**

Verify:

- Incorrect password remains rejected.
- Corresponding account counter increases by one.
- Account remains unlocked below the threshold.

**Priority**

High

**Traceability**

- AC-01
- AC-02
- BR-AUTH-001
- BR-AUTH-002
- BR-AUTH-003
- TS-AUTH-002
- TS-AUTH-003
- TS-AUTH-004

---

### REG-AUTH-003 — Failed-Attempt Threshold

**Impact**

Password authentication now includes a state transition when the consecutive failed-attempt counter reaches five.

**Regression Risk**

The threshold may be enforced incorrectly, causing:

- Premature lock before five failures.
- Missing lock after five failures.
- Incorrect treatment of non-consecutive failures.

**Regression Coverage**

Verify:

- Attempts 1–4 do not lock the account.
- Attempt 5 locks the account.
- Reset separates failure sequences.

**Priority**

High

**Traceability**

- AC-02
- AC-03
- AC-09
- BR-AUTH-003
- BR-AUTH-004
- BR-AUTH-012
- TS-AUTH-004
- TS-AUTH-005
- TS-AUTH-014

---

### REG-AUTH-004 — Authentication While Account Is Locked

**Impact**

Password authentication must now evaluate account lock state before allowing authentication.

**Regression Risk**

Existing credential validation behavior may incorrectly bypass the lock when valid credentials are submitted.

**Regression Coverage**

Verify:

- Correct password is rejected while locked.
- Incorrect password is rejected while locked.
- Password-based authentication remains unavailable throughout the active lock period.

**Priority**

High

**Traceability**

- AC-05
- BR-AUTH-007
- BR-AUTH-008
- TS-AUTH-007
- TS-AUTH-008
- TS-AUTH-009

---

### REG-AUTH-005 — Lock Duration and Automatic Unlock

**Impact**

Authentication availability now depends on a 15-minute time-based account state.

**Regression Risk**

The account may:

- Unlock too early.
- Remain locked too long.
- Calculate the lock duration from the wrong event.
- Fail to become available after lock expiry.

**Regression Coverage**

Verify:

- Lock duration begins from the fifth recorded failed attempt.
- Account remains locked before expiry.
- Account automatically unlocks after 15 minutes.
- Correct-password authentication succeeds after unlock.

**Priority**

High

**Traceability**

- AC-04
- AC-05
- AC-06
- BR-AUTH-005
- BR-AUTH-006
- BR-AUTH-009
- TS-AUTH-006
- TS-AUTH-009
- TS-AUTH-010

---

### REG-AUTH-006 — Counter Reset After Automatic Unlock

**Impact**

Automatic unlock must restore the account's failed-attempt sequence to its reset state.

**Regression Risk**

Previous failures may remain associated with the account after unlock and cause premature re-locking.

**Regression Coverage**

Verify:

- Automatic unlock resets the failed-attempt counter to zero.
- First subsequent failed login becomes failure one.
- Account remains unlocked after that first new failure.

**Priority**

High

**Traceability**

- AC-07
- AC-09
- BR-AUTH-010
- BR-AUTH-012
- TS-AUTH-011
- TS-AUTH-016

---

### REG-AUTH-007 — Counter Reset After Successful Login

**Impact**

Successful authentication now explicitly terminates the current consecutive failed-login sequence.

**Regression Risk**

Failures occurring before and after a successful login may be incorrectly accumulated.

**Regression Coverage**

Verify:

- Successful login after an early failure resets the counter.
- Successful login after four failures resets the counter.
- New failures start from one.
- Historical failures do not contribute to a later threshold.

**Priority**

High

**Traceability**

- AC-08
- AC-09
- BR-AUTH-011
- BR-AUTH-012
- TS-AUTH-012
- TS-AUTH-013
- TS-AUTH-014

---

### REG-AUTH-008 — Per-Account Authentication State Isolation

**Impact**

Failed-attempt and lock state must be maintained independently for each account.

**Regression Risk**

Authentication activity for one account may affect another account.

Possible symptoms include:

- Incorrect counter increments.
- Premature lock of another account.
- Incorrect authentication rejection for an unrelated user.

**Regression Coverage**

Verify interleaved authentication activity across at least two independent accounts.

**Priority**

High

**Traceability**

- AC-01
- Constraint: failed-attempt tracking is maintained separately for each account.
- BR-AUTH-001
- TS-AUTH-015

---

### REG-AUTH-009 — Repeated Lock Lifecycle

**Impact**

The account-lock mechanism must continue to behave correctly after a complete lock and automatic-unlock lifecycle.

**Regression Risk**

Residual state from a previous lock may affect later authentication attempts.

**Regression Coverage**

Verify:

- Previous lock expires.
- Counter resets.
- New failures 1–4 remain below threshold.
- Fifth new consecutive failure locks the account again.

**Priority**

High

**Traceability**

- AC-02
- AC-03
- AC-06
- AC-07
- AC-09
- BR-AUTH-003
- BR-AUTH-004
- BR-AUTH-009
- BR-AUTH-010
- BR-AUTH-012
- TS-AUTH-017

---

## Direct Regression Matrix

| Regression ID | Impact Area | Regression Level | Priority |
|---|---|---|---|
| REG-AUTH-001 | Successful password authentication | Direct | High |
| REG-AUTH-002 | Incorrect-password handling | Direct | High |
| REG-AUTH-003 | Five-attempt threshold | Direct | High |
| REG-AUTH-004 | Locked-state authentication | Direct | High |
| REG-AUTH-005 | Lock duration and automatic unlock | Direct | High |
| REG-AUTH-006 | Counter reset after automatic unlock | Direct | High |
| REG-AUTH-007 | Counter reset after successful login | Direct | High |
| REG-AUTH-008 | Per-account state isolation | Direct | High |
| REG-AUTH-009 | Repeated lock lifecycle | Direct | High |

All confirmed direct regression areas are security- or authentication-state-sensitive and therefore receive High regression priority.

---

## Potential Adjacent Regression Impact

The following areas may be affected depending on the implementation architecture.

The source requirement does not provide enough evidence to classify them as confirmed regression impacts.

### POT-AUTH-001 — Login UI State and Error Presentation

**Potential Dependency**

The login interface may need to represent authentication rejection caused by account lock.

**Why Not Confirmed**

The source does not define:

- UI behavior
- Error-message content
- Disabled controls
- Countdown display
- Lock notification

**QA Handling**

Review implementation or UI specification before adding dedicated regression coverage.

---

### POT-AUTH-002 — Authentication API Contract

**Potential Dependency**

If password authentication is exposed through an API, lock-state rejection may affect its responses.

**Why Not Confirmed**

No API contract, endpoint, status code, or response schema is provided.

**QA Handling**

Inspect the actual authentication interface before defining API regression cases.

Do not invent response codes or payloads.

---

### POT-AUTH-003 — Authentication State Persistence

**Potential Dependency**

Failed-attempt counter, lock state, and lock timing require some form of system state.

**Why Not Confirmed**

The requirement explicitly does not define the technical mechanism used to track lock expiration or automatic unlock.

No database or storage model is provided.

**QA Handling**

Validate persistence-related regression only after implementation dependencies are known.

---

### POT-AUTH-004 — Session Behavior

**Potential Dependency**

An implementation may have interactions between account lock state and existing authenticated sessions.

**Why Not Confirmed**

The source only defines password-based login attempts.

It does not define behavior for already-authenticated sessions.

**QA Handling**

Do not assume that account lock terminates or preserves existing sessions.

Clarify or inspect implementation scope first.

---

### POT-AUTH-005 — Password Reset or Credential Change

**Potential Dependency**

Password reset or password change may interact with failed-attempt or lock state in some systems.

**Why Not Confirmed**

No password-reset or credential-change behavior is defined.

**QA Handling**

Treat as an adjacent dependency candidate only.

Do not include it in mandatory regression coverage without additional requirements.

---

### POT-AUTH-006 — Alternative Authentication Methods

**Potential Dependency**

The account may support authentication methods other than username and password in the wider system.

**Why Not Confirmed**

The dataset explicitly limits scope to username-and-password authentication.

**QA Handling**

Alternative authentication regression is outside the confirmed scope.

Validate only if implementation or product requirements establish a dependency.

---

### POT-AUTH-007 — Concurrent Authentication Requests

**Potential Dependency**

Concurrent requests against the same account may interact with failed-attempt counting and threshold enforcement.

**Why Not Confirmed**

Concurrency semantics are not defined by the source.

**QA Handling**

Treat as a technical regression candidate pending architecture or implementation information.

Do not prescribe a specific serialization strategy.

---

## Potential Impact Matrix

| Potential ID | Adjacent Area | Evidence Level | Mandatory Regression? |
|---|---|---|---|
| POT-AUTH-001 | Login UI / error presentation | Insufficient | No |
| POT-AUTH-002 | Authentication API contract | Insufficient | No |
| POT-AUTH-003 | State persistence | Insufficient | No |
| POT-AUTH-004 | Existing sessions | Insufficient | No |
| POT-AUTH-005 | Password reset / credential change | Insufficient | No |
| POT-AUTH-006 | Alternative authentication | Explicitly outside current scope | No |
| POT-AUTH-007 | Concurrent authentication | Insufficient | No |

These candidates must not be counted as confirmed regression gaps.

---

## Regression Boundaries

### Failed-Attempt Boundary

The highest-priority counter boundary is:

- `4` consecutive failures → Account remains unlocked.
- `5` consecutive failures → Account becomes locked.

Regression must preserve both sides of this boundary.

### Time Boundary

The highest-priority timing boundary is:

- Before 15 minutes have expired → Account remains locked.
- After the defined 15-minute lock duration expires → Account is automatically unlocked.

The lock duration starts from the fifth recorded failed attempt.

### Reset Boundary

Regression must preserve both reset paths:

- Successful login before lock → Counter resets to `0`.
- Automatic unlock → Counter resets to `0`.

The next failed attempt after either reset starts a new sequence at `1`.

---

## State-Transition Regression

The following confirmed transitions require regression coverage:

| Current State | Event | Expected State |
|---|---|---|
| Unlocked | Incorrect password, counter remains below 5 | Unlocked |
| Unlocked | Successful login before threshold | Unlocked with counter reset |
| Unlocked | Fifth consecutive failed login | Locked |
| Locked | Password-based login before expiry | Locked |
| Locked | 15-minute duration expires | Unlocked with counter reset |
| Unlocked after reset | New failed attempts | New consecutive sequence |

Regression coverage should verify the complete lifecycle rather than only isolated authentication requests.

---

## Recommended Regression Suite

### P0 — Critical Authentication Protection

Execute for every change directly affecting the account-lockout implementation or password-authentication decision flow:

- TC-AUTH-004 — Account remains unlocked after four failures
- TC-AUTH-005 — Fifth failure locks the account
- TC-AUTH-007 — Correct password rejected during active lock
- TC-AUTH-009 — Account remains locked before expiry
- TC-AUTH-010 — Automatic unlock after 15 minutes
- TC-AUTH-013 — Successful login resets counter after four failures
- TC-AUTH-015 — Per-account isolation
- TC-AUTH-016 — First failed attempt after automatic unlock starts at one

### P1 — Core Regression

Execute alongside P0 for complete confirmed feature regression:

- TC-AUTH-001 — Successful authentication while unlocked
- TC-AUTH-002 — Incorrect password increments counter
- TC-AUTH-003 — First failure remains below threshold
- TC-AUTH-006 — Lock starts at fifth recorded failure
- TC-AUTH-008 — Incorrect password rejected during active lock
- TC-AUTH-011 — Automatic unlock resets counter
- TC-AUTH-012 — Successful login resets counter after one failure
- TC-AUTH-014 — Failures across successful login are not consecutive
- TC-AUTH-017 — Repeated lock lifecycle

Together, P0 and P1 provide complete regression coverage for the confirmed behavior represented by the golden test suite.

---

## Regression Selection Guidance

### Run the Full Confirmed Regression Suite When

- Failed-attempt tracking changes.
- Lock-threshold logic changes.
- Lock-state validation changes.
- Lock-duration logic changes.
- Automatic-unlock behavior changes.
- Counter-reset behavior changes.
- Password-authentication decision logic changes.
- Account-specific authentication state handling changes.

### Consider Targeted Regression When

A change is isolated to one confirmed behavior and system dependencies are understood.

Examples:

- Counter-reset-only change → prioritize REG-AUTH-006 and REG-AUTH-007.
- Timer-only change → prioritize REG-AUTH-005.
- Account-state isolation change → prioritize REG-AUTH-008.

Targeted execution must not be interpreted as proof that unrelated areas cannot be affected when architecture information is unavailable.

---

## Regression Exclusions

The following are not part of the confirmed regression suite based on the supplied source:

- Administrative account unlock
- Password-reset behavior
- Password-change behavior
- Multi-factor authentication
- Social login
- Single sign-on
- Biometric authentication
- Existing authenticated-session behavior
- User notification behavior
- Email or SMS notification
- Specific lockout error messages
- Specific API status codes
- Database schema validation
- Cache implementation
- Distributed locking implementation
- Timer persistence implementation

These exclusions do not mean the areas are irrelevant to a real production system.

They mean the current dataset does not provide sufficient evidence to define their expected regression behavior.

---

## Traceability Summary

| Acceptance Criterion | Regression Coverage |
|---|---|
| AC-01 | REG-AUTH-002, REG-AUTH-008 |
| AC-02 | REG-AUTH-002, REG-AUTH-003, REG-AUTH-009 |
| AC-03 | REG-AUTH-003, REG-AUTH-009 |
| AC-04 | REG-AUTH-005 |
| AC-05 | REG-AUTH-004, REG-AUTH-005 |
| AC-06 | REG-AUTH-005, REG-AUTH-009 |
| AC-07 | REG-AUTH-006, REG-AUTH-009 |
| AC-08 | REG-AUTH-001, REG-AUTH-007 |
| AC-09 | REG-AUTH-003, REG-AUTH-006, REG-AUTH-007, REG-AUTH-009 |

All nine source acceptance criteria have confirmed regression-impact coverage.

---

## Regression Risk Summary

The most important regression failures would be:

1. Valid unlocked users can no longer authenticate.
2. Accounts lock before the fifth consecutive failure.
3. Accounts remain unlocked after the fifth consecutive failure.
4. Correct credentials bypass an active lock.
5. Accounts unlock before the 15-minute duration expires.
6. Accounts remain locked after the duration expires.
7. Counter state is not reset correctly.
8. Historical failures are incorrectly combined across reset boundaries.
9. Authentication state leaks between accounts.

These risks directly affect authentication availability, account isolation, or the intended password-guessing protection.

---

## Final Regression Assessment

### Confirmed Direct Impact Areas

`9`

### Potential Adjacent Impact Areas

`7`

### Confirmed Acceptance Criteria Covered

`9 / 9`

### Confirmed Regression Gaps

`0`

### Unsupported Dependencies Converted Into Confirmed Impact

`0`

## Final Verdict

**PASS — The regression scope covers all confirmed behavior introduced by `REQ-AUTH-001`.**

The regression suite should prioritize authentication-state transitions, the exact failed-attempt threshold, the 15-minute lock boundary, counter resets, and account isolation.

Potential UI, API, persistence, session, credential-management, alternative-authentication, and concurrency impacts remain conditional until supported by architecture, implementation, or additional requirements.
