# Regression Analysis — Account Lock After Failed Login Attempts

## 1. Regression Summary

The Account Lock After Failed Login Attempts feature extends the existing authentication flow by introducing:

- Account-specific failed-login tracking.
- A five-consecutive-failure lock threshold.
- Temporary account lock state.
- Authentication rejection while an account is locked.
- A 30-minute lock period.
- Automatic account unlock.
- Failed-login counter reset after successful authentication.
- Restarted failed-login tracking after automatic unlock.

The primary regression impact is concentrated around the existing authentication flow.

Based on the available system context, the highest-confidence regression scope includes:

- Login Page.
- Authentication Service.
- User Account Store interaction.
- Session Management after successful authentication.

Existing behaviors such as logout and protected-route authorization have no confirmed functional change, but selected regression verification is appropriate because they participate in the broader authentication lifecycle.

Several possible dependencies cannot be confirmed from the supplied context and remain investigation items.

---

## 2. Change Analysis

### Current Behavior

The existing authentication flow is:

```text
Email + Password
      ↓
Authentication Service
      ↓
Validate Credentials
   ┌──┴──┐
 Valid Invalid
   │       │
   ▼       ▼
Session   Reject
Created   Login
```

An incorrect password currently causes authentication failure but does not create a temporary account lock.

### New Behavior

The change introduces additional authentication state and decision logic:

```text
Login Attempt
      ↓
Account Locked?
   ┌──┴──┐
  Yes     No
   │       │
   ▼       ▼
Reject   Validate Credentials
Login          │
             ┌─┴─┐
           Valid Invalid
             │      │
             ▼      ▼
          Success  Track Failure
             │          │
             ▼          ▼
           Reset     Threshold?
           Counter     │
                    ┌──┴──┐
                    No    Yes
                    │      │
                    ▼      ▼
                 Reject   Lock
                 Login   Account
```

The existing successful-login path remains valid when the submitted credentials are valid and the account is not locked.

---

## 3. Direct Impact Analysis

### 3.1 Login Page

**Impact: Direct**

The Login Page participates directly in the changed authentication flow.

Potentially affected behavior includes:

- Submission of login credentials.
- Handling failed authentication.
- Handling authentication rejection caused by account lock.
- Displaying the required temporary-lock message.
- Successful login after automatic unlock.

Regression should confirm that existing successful and invalid-password login behavior continues to function correctly alongside the new locked-account response.

---

### 3.2 Authentication Service

**Impact: Direct**

The Authentication Service is the primary affected component.

The service currently validates credentials and determines authentication success or failure.

The new feature requires authentication decisions to additionally consider:

```text
Failed-Login State
      +
Account Lock State
      +
Credentials
```

Relevant changed behavior includes:

- Recording consecutive incorrect-password attempts.
- Evaluating the five-attempt threshold.
- Applying temporary account lock.
- Rejecting authentication while locked.
- Resetting failed-login tracking after successful authentication.
- Allowing authentication after automatic unlock.

This component requires the highest regression attention.

---

### 3.3 User Account Store Interaction

**Impact: Direct / Implementation-Dependent**

The Authentication Service already interacts with the User Account Store during authentication.

The new feature introduces account-specific authentication state.

However, the supplied context does not define where:

- Failed-login count.
- Lock state.
- Lock start time.
- Lock expiration information.

are stored.

Therefore:

```text
Account-specific state requirement
→ Confirmed

Exact persistence implementation
→ Unknown
```

Regression must validate account-level behavior without assuming a specific persistence design.

---

### 3.4 Session Management

**Impact: Direct Integration**

Session creation occurs only after successful authentication.

The new locked state introduces another condition under which authentication must not result in session creation.

Required regression relationship:

```text
Unlocked + Valid Credentials
        ↓
Session Created

Locked + Valid Credentials
        ↓
Authentication Rejected
        ↓
No New Authenticated Session
```

Existing successful session creation should also be revalidated to ensure the new authentication logic does not block valid unlocked users.

---

## 4. Indirect Regression Impact

### 4.1 Protected Application Routes

**Impact: Indirect / Regression Verification**

Protected routes depend on a valid authenticated session.

No change to protected-route authorization rules is specified.

However, because session creation depends on successful authentication, selected regression should verify that:

```text
Successful Login
      ↓
Valid Session
      ↓
Protected Route Access
```

continues to work.

The feature does not provide evidence that protected-route authorization logic itself changes.

---

### 4.2 Logout

**Impact: Low / Regression Verification**

Logout terminates an authenticated session.

No change to logout behavior is specified.

Basic regression is appropriate to ensure the modified authentication flow does not unintentionally affect the existing authenticated lifecycle:

```text
Login
  ↓
Authenticated Session
  ↓
Logout
  ↓
Unauthenticated
```

No expanded logout-specific regression scope is justified by the supplied context.

---

## 5. Functional Regression Scope

### High Priority

Regression should prioritize behavior directly affected by the change.

| Area | Regression Focus | Priority |
|---|---|---|
| Authentication | Successful login for unlocked account | High |
| Authentication | Incorrect-password rejection | High |
| Failed Login Tracking | Account-specific consecutive failure tracking | High |
| Lock Threshold | Account remains unlocked below five failures | High |
| Lock Threshold | Account locks on fifth consecutive failure | High |
| Counter Reset | Successful login resets current failure sequence | High |
| Locked State | Correct password cannot bypass active lock | High |
| Locked State | Authentication rejection while locked | High |
| Lock Duration | Account remains locked during active lock period | High |
| Automatic Unlock | Account becomes available after lock expiration | High |
| Post-Unlock Tracking | Failed-login tracking starts again | High |
| Account Isolation | One account's failed attempts do not affect another account | High |
| Session Management | No authenticated session is created for locked account | High |
| Session Management | Successful unlocked login still creates a session | High |

### Medium Priority

| Area | Regression Focus | Priority |
|---|---|---|
| Login Page | Required lock message is displayed correctly | Medium |
| Protected Routes | Valid authenticated session still grants expected protected access | Medium |
| Repeated Lifecycle | Account can complete more than one lock/unlock cycle | Medium |

### Low Priority

| Area | Regression Focus | Priority |
|---|---|---|
| Logout | Existing logout flow remains functional after successful authentication | Low |

---

## 6. Regression by Authentication State

### Unlocked Account

Verify existing authentication remains functional when the account is not locked.

```text
Valid Credentials
→ Login Success

Incorrect Password
→ Login Failure
```

The new feature must not break the existing successful-login behavior.

---

### Unlocked Account with Previous Failures

Verify authentication correctly handles an account with an active consecutive-failure sequence.

Key regression paths:

```text
1–4 Failures
    +
Another Failure
    ↓
Threshold Evaluation
```

and:

```text
1–4 Failures
    +
Successful Login
    ↓
Counter Reset
```

---

### Locked Account

Verify the new lock state prevents authentication.

```text
Locked + Correct Password
→ Authentication Rejected

Locked + Login Attempt
→ Required Lock Message
```

No new authenticated session should be created from a rejected locked-account login.

---

### Automatically Unlocked Account

Verify the account correctly returns to an authentication-capable state.

```text
Locked
  ↓
30-Minute Expiration
  ↓
Unlocked
  ↓
Valid Login Allowed
```

Failed-login tracking must also start again according to the requirement.

---

## 7. Regression by Component

| Component | Impact Classification | Regression Level | Reason |
|---|---|---|---|
| Login Page | Direct | High | Handles changed authentication outcomes and lock message. |
| Authentication Service | Direct | High | Contains the primary changed authentication decision behavior. |
| User Account Store Interaction | Direct / Implementation-Dependent | High | Account-specific authentication state is required, although storage design is unknown. |
| Session Management | Direct Integration | High | Session must only be created after successful authentication. |
| Protected Application Routes | Indirect | Medium | Depends on successful session creation but has no confirmed rule change. |
| Logout | No Confirmed Change / Related | Low | Existing authenticated lifecycle should remain intact. |

---

## 8. No-Confirmed-Change Areas

The available requirement does not specify functional changes to:

- Logout behavior.
- Protected-route authorization rules.
- Existing authenticated-session lifetime.
- Password reset.
- Password change.
- User registration.
- Administrative account management.

These areas must not automatically be classified as directly impacted.

The appropriate classification is:

```text
No requirement change
        ≠
Guaranteed unaffected

No confirmed dependency
        ↓
Do not invent regression impact
```

Where a known integration exists, targeted regression may still be appropriate.

---

## 9. Unknown Dependencies and Investigation Items

The following dependencies cannot be determined from the supplied requirement and system context.

| Investigation ID | Area | Unknown Dependency / Behavior |
|---|---|---|
| INV-001 | Persistence | Where failed-login counters are stored. |
| INV-002 | Persistence | Where temporary lock state and expiration information are stored. |
| INV-003 | Timer | How automatic unlock is implemented. |
| INV-004 | Locked Attempts | Whether attempts during lock affect failed-login state. |
| INV-005 | Lock Duration | Whether attempts during lock restart or extend the timer. |
| INV-006 | Cross-Device | Whether failed attempts are shared across browsers, devices, and sessions. |
| INV-007 | Concurrency | How simultaneous login attempts update the account state. |
| INV-008 | Unknown Account | How unregistered email addresses participate in failed-login handling. |
| INV-009 | Existing Sessions | Whether account locking affects sessions authenticated before the lock. |
| INV-010 | Password Management | Whether password reset or password change modifies failed-login or lock state. |
| INV-011 | Administration | Whether administrative account-unlock capability exists. |
| INV-012 | Audit | Whether authentication failures or lock events are recorded in an audit log. |

These items require additional system information before they can be added as confirmed regression scope.

---

## 10. Regression Risk Prioritization

### Priority 1 — Authentication Protection

```text
5-Failure Threshold
      +
Locked-State Enforcement
      +
30-Minute Lock
      +
Automatic Unlock
```

Failures here directly compromise the intended account-protection behavior or legitimate user access.

**Regression Priority: High**

### Priority 2 — Authentication State Integrity

```text
Counter Reset
      +
Post-Unlock Tracking
      +
Account Isolation
      +
Session Creation
```

Incorrect state handling can cause premature lockouts, failure to lock, cross-account effects, or unauthorized session creation.

**Regression Priority: High**

### Priority 3 — Existing Authentication Integration

```text
Normal Login
      +
Protected Access
      +
Logout
```

These existing flows should remain functional after authentication changes.

**Regression Priority: Medium to Low depending on dependency strength**

---

## 11. Recommended Regression Coverage

### Smoke Regression

Minimum post-change verification should include:

- Successful login for an unlocked account.
- Incorrect-password login failure.
- Account lock on fifth consecutive failed attempt.
- Authentication rejection while locked.
- Automatic unlock after the defined lock period.
- Successful login after automatic unlock.

### Focused Regression

Focused authentication regression should additionally include:

- Account remains unlocked through the fourth consecutive failure.
- Successful-login counter reset.
- New failed-login sequence after reset.
- Account remains locked before expiration.
- Post-unlock failed-login tracking.
- Account isolation.
- No session creation for locked-account authentication.
- Successful session creation for valid unlocked authentication.
- Repeated lock/unlock lifecycle.

### Related Regression

Based on confirmed existing dependencies:

- Successful login → protected-route access.
- Successful login → logout → unauthenticated state.

Additional regression areas should only be introduced when investigation confirms further dependencies.

---

## 12. Regression Scope Matrix

| Scope Area | Include in Regression | Priority | Basis |
|---|---|---|---|
| Login success | Yes | High | Existing authentication path directly modified |
| Invalid-password login | Yes | High | Existing failure path extended |
| Failed-login tracking | Yes | High | New requirement |
| Five-attempt threshold | Yes | High | New requirement |
| Counter reset | Yes | High | New requirement |
| Temporary lock | Yes | High | New requirement |
| Lock message | Yes | Medium | New requirement |
| 30-minute lock duration | Yes | High | New requirement |
| Automatic unlock | Yes | High | New requirement |
| Post-unlock tracking | Yes | High | New requirement |
| Account isolation | Yes | High | New requirement |
| Session creation | Yes | High | Direct authentication integration |
| Protected-route access | Yes, targeted | Medium | Existing session dependency |
| Logout | Yes, basic | Low | Related authenticated lifecycle |
| Password reset | Investigation required | — | Dependency not defined |
| Password change | Investigation required | — | Dependency not defined |
| Existing session invalidation | Investigation required | — | Behavior not defined |
| User registration | No confirmed regression need | — | No change/dependency identified |
| Administrative account management | Investigation required | — | Capability/dependency unknown |
| Audit logging | Investigation required | — | Capability/dependency unknown |

---

## 13. Regression Analysis Summary

The regression scope is concentrated around authentication rather than the entire application.

The strongest confirmed impact chain is:

```text
Login Page
    ↓
Authentication Service
    ↓
Account Authentication State
    ↓
Authentication Decision
    ↓
Session Management
    ↓
Protected Access
```

The highest-priority regression areas are:

1. Existing successful and failed login behavior.
2. Five-attempt threshold enforcement.
3. Locked-state authentication rejection.
4. 30-minute lock lifecycle.
5. Successful-login counter reset.
6. Post-unlock failed-login tracking.
7. Account isolation.
8. Session creation behavior.

Protected-route access and logout require targeted regression because they participate in the known authentication lifecycle but have no confirmed functional rule changes.

Password management, existing-session invalidation, concurrency, cross-device behavior, administrative unlocking, audit logging, and persistence implementation remain investigation areas.

They must not be promoted to confirmed regression scope without additional system evidence.