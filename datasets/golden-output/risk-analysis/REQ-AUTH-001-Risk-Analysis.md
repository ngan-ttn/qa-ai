# Risk Analysis — Account Lockout After Failed Login Attempts

## Golden Output Metadata

- Dataset ID: `REQ-AUTH-001`
- Source Requirement: `datasets/requirements/simple/REQ-AUTH-001.md`
- Artifact Type: `Risk Analysis`
- Review Status: `Approved`
- Evaluation Purpose: Reference output for evaluating risk identification, risk prioritization, business-impact reasoning, boundary-risk analysis, state-transition risk analysis, assumption control, and traceability

---

## Risk Summary

The account-lockout feature is small in functional scope but security-sensitive.

The highest-risk areas are:

- Incorrect enforcement of the five-attempt threshold
- Incorrect handling of the 15-minute lock duration
- Authentication bypass while the account is locked
- Incorrect reset of the failed-attempt counter
- Cross-account contamination of failed-attempt tracking
- Incorrect behavior around threshold and time boundaries

The feature therefore requires stronger attention to state transitions and boundary behavior than its functional size alone would suggest.

---

## Risk Rating Model

Each identified risk is evaluated using:

- **Likelihood** — probability that the defect could occur.
- **Impact** — severity of the business or user consequence if the defect occurs.
- **Priority** — overall testing priority derived from likelihood and impact.

Allowed values:

- Likelihood: `Low`, `Medium`, `High`
- Impact: `Low`, `Medium`, `High`
- Priority: `Low`, `Medium`, `High`

The ratings represent QA prioritization for this dataset and are not source-defined business rules.

---

## Identified Risks

### RISK-AUTH-001 — Account Locks Before the Fifth Consecutive Failure

**Risk**

The account may become locked after fewer than five consecutive failed login attempts.

**Potential Impact**

- Legitimate users may be locked prematurely.
- Authentication availability may be reduced.
- The implemented behavior would violate the defined threshold.

**Likelihood**

Medium

**Impact**

High

**Priority**

High

**Related Rules**

- BR-AUTH-002
- BR-AUTH-003
- BR-AUTH-004

**Source Traceability**

- AC-01
- AC-02
- AC-03

**Recommended Test Focus**

Verify account state after failed attempts 1, 2, 3, and 4, with special focus on the transition from attempt 4 to attempt 5.

---

### RISK-AUTH-002 — Account Does Not Lock on the Fifth Consecutive Failure

**Risk**

The account may remain unlocked after the fifth consecutive failed login attempt.

**Potential Impact**

- Repeated password guessing may continue beyond the intended threshold.
- The security control may fail to provide the required protection.

**Likelihood**

Medium

**Impact**

High

**Priority**

High

**Related Rules**

- BR-AUTH-004
- BR-AUTH-006

**Source Traceability**

- AC-03
- AC-04

**Recommended Test Focus**

Verify that the fifth consecutive incorrect-password attempt causes the account to enter the locked state immediately when that failure is recorded.

---

### RISK-AUTH-003 — Correct Password Bypasses an Active Lock

**Risk**

A user may be able to authenticate with the correct password while the account is still within the active lock period.

**Potential Impact**

- The account-lock security control may be bypassed.
- Locked-state behavior would be inconsistent with the requirement.
- Protection against repeated password guessing may be weakened.

**Likelihood**

Medium

**Impact**

High

**Priority**

High

**Related Rules**

- BR-AUTH-007
- BR-AUTH-008

**Source Traceability**

- AC-05

**Recommended Test Focus**

Attempt authentication with both correct and incorrect passwords while the account is actively locked.

---

### RISK-AUTH-004 — Failed Attempts Are Shared Across Accounts

**Risk**

Failed login attempts from one account may incorrectly contribute to the failed-attempt counter of another account.

**Potential Impact**

- Unrelated users may be locked incorrectly.
- Account-specific security state may become corrupted.
- The feature may behave unpredictably under multi-user activity.

**Likelihood**

Low

**Impact**

High

**Priority**

High

**Related Rules**

- BR-AUTH-001
- BR-AUTH-002

**Source Traceability**

- AC-01
- Constraint: failed-attempt tracking is maintained separately for each account.

**Recommended Test Focus**

Interleave failed login attempts across multiple accounts and verify that each account maintains an independent failed-attempt sequence.

---

### RISK-AUTH-005 — Successful Login Does Not Reset the Counter

**Risk**

A successful login before the lock threshold may fail to reset the consecutive failed-attempt counter.

**Potential Impact**

- Failures from separate sequences may be incorrectly combined.
- A legitimate user may later be locked before accumulating five new consecutive failures.

**Likelihood**

Medium

**Impact**

Medium

**Priority**

High

**Related Rules**

- BR-AUTH-011
- BR-AUTH-012

**Source Traceability**

- AC-08
- AC-09

**Recommended Test Focus**

Perform several failed attempts, log in successfully before reaching five, then begin another failed sequence and verify that counting restarts at one.

---

### RISK-AUTH-006 — Previous Failures Carry Over After Automatic Unlock

**Risk**

The failed-attempt counter may not reset to zero after the 15-minute lock expires.

**Potential Impact**

- The next failed login may incorrectly continue the previous sequence.
- The account may become locked again earlier than required.
- Automatic unlock may restore access without correctly restoring counter state.

**Likelihood**

Medium

**Impact**

Medium

**Priority**

High

**Related Rules**

- BR-AUTH-009
- BR-AUTH-010
- BR-AUTH-012

**Source Traceability**

- AC-06
- AC-07
- AC-09

**Recommended Test Focus**

Allow the lock to expire, perform a new incorrect-password attempt, and verify that it is treated as the first failure of a new sequence.

---

### RISK-AUTH-007 — Account Unlocks Before Fifteen Minutes

**Risk**

The account may become available for password authentication before the full 15-minute lock duration has expired.

**Potential Impact**

- The security control may provide less protection than required.
- Attackers may resume password guessing earlier than intended.

**Likelihood**

Medium

**Impact**

High

**Priority**

High

**Related Rules**

- BR-AUTH-005
- BR-AUTH-006
- BR-AUTH-007
- BR-AUTH-009

**Source Traceability**

- AC-04
- AC-05
- AC-06

**Recommended Test Focus**

Verify that login remains blocked throughout the active lock period, particularly immediately before the 15-minute expiry boundary.

---

### RISK-AUTH-008 — Account Remains Locked After Fifteen Minutes

**Risk**

The account may fail to unlock when the defined 15-minute lock duration expires.

**Potential Impact**

- Legitimate users may remain unable to authenticate.
- Manual intervention may be required even though the requirement specifies automatic unlock.
- User access may be disrupted.

**Likelihood**

Medium

**Impact**

High

**Priority**

High

**Related Rules**

- BR-AUTH-005
- BR-AUTH-009
- BR-AUTH-010

**Source Traceability**

- AC-06
- AC-07

**Recommended Test Focus**

Verify account behavior at the expiry boundary and confirm that password authentication becomes available when the 15-minute duration has expired.

---

### RISK-AUTH-009 — Lock Start Time Is Calculated From the Wrong Event

**Risk**

The 15-minute lock duration may be calculated from an event other than the recorded fifth consecutive failed login attempt.

Examples include starting the timer from:

- The first failed attempt
- The fourth failed attempt
- A later login attempt made while locked

**Potential Impact**

- Actual lock duration may be shorter or longer than required.
- Boundary behavior may become inconsistent.
- Users may unlock too early or remain locked too long.

**Likelihood**

Medium

**Impact**

Medium

**Priority**

High

**Related Rules**

- BR-AUTH-004
- BR-AUTH-005
- BR-AUTH-006

**Source Traceability**

- AC-03
- AC-04
- AC-06

**Recommended Test Focus**

Capture the time at which the fifth failed attempt is recorded and verify the lock-expiration boundary relative to that event.

---

### RISK-AUTH-010 — Consecutive Failure Sequence Is Calculated Incorrectly

**Risk**

The system may count total historical failures instead of consecutive failures.

**Potential Impact**

- Failures separated by successful logins may be combined incorrectly.
- Accounts may lock even though five consecutive failures have not occurred.
- Counter-reset behavior may become ineffective.

**Likelihood**

Medium

**Impact**

High

**Priority**

High

**Related Rules**

- BR-AUTH-003
- BR-AUTH-004
- BR-AUTH-011
- BR-AUTH-012

**Source Traceability**

- AC-02
- AC-03
- AC-08
- AC-09

**Recommended Test Focus**

Use multiple failure sequences separated by successful logins and verify that only failures since the latest reset contribute to the lock threshold.

---

### RISK-AUTH-011 — Locked-State Attempts Affect Undefined Counter or Timer Behavior

**Risk**

The requirement defines that password-based login attempts must be rejected while the account is locked, but it does not define whether those attempts:

- Increase the failed-attempt counter
- Restart the lock duration
- Extend the lock duration

Different implementations may therefore produce inconsistent behavior.

**Potential Impact**

- Lock duration may become unpredictable.
- Counter state after unlock may differ between implementations.
- Test expectations may be inconsistent without clarification.

**Likelihood**

Medium

**Impact**

Medium

**Priority**

Medium

**Related Rules**

- BR-AUTH-007
- BR-AUTH-008
- BR-AUTH-009
- BR-AUTH-010

**Source Traceability**

- AC-05
- AC-06
- AC-07

**Recommended Test Focus**

Treat this as a clarification-dependent area.

Do not assert counter or timer behavior for attempts made while locked until expected behavior is defined.

---

### RISK-AUTH-012 — Concurrent Attempts Cross the Lock Threshold Incorrectly

**Risk**

Multiple login attempts against the same account may be processed concurrently when the failed-attempt counter is near the threshold.

The source does not define concurrency behavior.

**Potential Impact**

Possible implementation outcomes include:

- Lost counter increments
- Counter values exceeding the threshold unexpectedly
- More than one request being accepted before lock enforcement
- Inconsistent lock-start timestamps

**Likelihood**

Low

**Impact**

High

**Priority**

Medium

**Related Rules**

- BR-AUTH-002
- BR-AUTH-004
- BR-AUTH-006

**Source Traceability**

- AC-01
- AC-03
- AC-04

**Recommended Test Focus**

Identify concurrency as a technical risk requiring clarification or implementation-specific validation rather than treating a particular concurrency strategy as a confirmed business rule.

---

## Risk Prioritization

| Risk ID | Risk Area | Likelihood | Impact | Priority |
|---|---|---|---|---|
| RISK-AUTH-001 | Premature lock | Medium | High | High |
| RISK-AUTH-002 | Missing lock at threshold | Medium | High | High |
| RISK-AUTH-003 | Lock bypass with correct password | Medium | High | High |
| RISK-AUTH-004 | Cross-account counter contamination | Low | High | High |
| RISK-AUTH-005 | Successful-login reset failure | Medium | Medium | High |
| RISK-AUTH-006 | Counter not reset after unlock | Medium | Medium | High |
| RISK-AUTH-007 | Early automatic unlock | Medium | High | High |
| RISK-AUTH-008 | Late or missing automatic unlock | Medium | High | High |
| RISK-AUTH-009 | Incorrect lock start time | Medium | Medium | High |
| RISK-AUTH-010 | Incorrect consecutive-sequence calculation | Medium | High | High |
| RISK-AUTH-011 | Undefined locked-attempt side effects | Medium | Medium | Medium |
| RISK-AUTH-012 | Concurrent threshold processing | Low | High | Medium |

---

## Risk Areas by Category

### Security Risks

- Failure to lock at the required threshold
- Correct-password bypass during active lock
- Early unlock
- Incorrect lock duration

### State-Management Risks

- Incorrect failed-attempt counter
- Incorrect counter reset
- Incorrect consecutive-sequence calculation
- Incorrect locked/unlocked transition

### Boundary Risks

- Transition from failed attempt 4 to 5
- Start of the 15-minute lock period
- Time immediately before lock expiry
- Exact lock-expiry boundary
- First failed attempt after counter reset

### Data-Isolation Risks

- Failed-attempt state leaking between accounts

### Specification Risks

- Counter behavior during active lock is unspecified
- Timer behavior during active lock attempts is unspecified
- Concurrent threshold behavior is unspecified

---

## Highest-Priority Test Focus

Testing should prioritize the following areas:

1. Exact transition from four to five consecutive failed attempts.
2. Rejection of both correct and incorrect passwords during active lock.
3. Exact start point and expiry of the 15-minute lock.
4. Successful-login counter reset before lock.
5. Automatic-unlock counter reset.
6. Independence of failed-attempt tracking across accounts.
7. Separation of multiple failed sequences by a successful login.
8. Timing behavior immediately before and at lock expiry.

These areas provide the highest value for validating the core security and state-transition behavior defined by the requirement.

---

## Clarification-Dependent Risks

The following risks arise from behavior not defined by the source and must not be converted into assumed expected results:

| Area | Missing Definition | QA Handling |
|---|---|---|
| Locked-attempt counter | Whether attempts while locked increment the counter | Raise clarification; do not assume |
| Locked-attempt timer | Whether attempts while locked restart or extend the lock | Raise clarification; do not assume |
| Concurrent attempts | How simultaneous attempts near threshold are serialized | Treat as technical risk pending system behavior |
| Manual unlock | Whether administrative unlock exists and how it affects counter state | Outside current scope |
| Alternative authentication | Whether the lock affects non-password authentication | Outside current scope |

---

## Traceability Summary

| Source Acceptance Criterion | Covered Risks |
|---|---|
| AC-01 — Incorrect password increments the corresponding account counter | RISK-AUTH-001, RISK-AUTH-004, RISK-AUTH-012 |
| AC-02 — Account remains unlocked after attempts 1–4 | RISK-AUTH-001, RISK-AUTH-010 |
| AC-03 — Fifth consecutive failure locks account | RISK-AUTH-001, RISK-AUTH-002, RISK-AUTH-010, RISK-AUTH-012 |
| AC-04 — Lock duration starts at fifth recorded failure | RISK-AUTH-002, RISK-AUTH-007, RISK-AUTH-009, RISK-AUTH-012 |
| AC-05 — Password-based login rejected while locked | RISK-AUTH-003, RISK-AUTH-007, RISK-AUTH-011 |
| AC-06 — Automatic unlock after 15 minutes | RISK-AUTH-007, RISK-AUTH-008, RISK-AUTH-009, RISK-AUTH-011 |
| AC-07 — Automatic unlock resets counter | RISK-AUTH-006, RISK-AUTH-011 |
| AC-08 — Successful login before lock resets counter | RISK-AUTH-005, RISK-AUTH-010 |
| AC-09 — Next failed attempt after reset starts at one | RISK-AUTH-005, RISK-AUTH-006, RISK-AUTH-010 |

All source acceptance criteria have associated risk coverage.

---

## Coverage Summary

The risk analysis covers:

- Lock-threshold correctness
- Failed-attempt counting
- Consecutive-sequence integrity
- Account-level data isolation
- Locked-state enforcement
- Lock-duration calculation
- Automatic unlock
- Counter reset
- Threshold boundaries
- Time boundaries
- Specification gaps
- Concurrency exposure

The analysis distinguishes confirmed requirement risks from clarification-dependent or implementation-sensitive risks.

No unspecified behavior is presented as a confirmed business rule or expected system result.
