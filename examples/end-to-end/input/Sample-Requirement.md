# Sample Requirement — Account Lock After Failed Login Attempts

## Feature

Account Lock After Failed Login Attempts

---

## User Story

As a registered user,

I want my account to be temporarily locked after multiple consecutive failed login attempts,

So that my account is protected from unauthorized access.

---

## Background

The application allows registered users to sign in using their email address and password.

To improve account security, the system must temporarily lock a user account when multiple consecutive login attempts fail because an incorrect password is entered.

---

## Requirements

### Login

1. A registered user can attempt to log in using an email address and password.

2. The system validates the submitted credentials when the user attempts to log in.

3. If the credentials are valid and the account is not locked, the user is successfully authenticated.

4. If the password is incorrect, the login attempt fails.

### Failed Login Tracking

5. Failed login attempts caused by an incorrect password must be tracked separately for each user account.

6. If a user enters an incorrect password five consecutive times, the account must be temporarily locked.

7. A successful login before the fifth consecutive failed attempt resets the failed-login counter.

### Account Lock

8. The account becomes locked after the fifth consecutive failed login attempt.

9. The account remains locked for 30 minutes.

10. While the account is locked, the user cannot log in even when the correct password is entered.

11. When a user attempts to log in while the account is locked, the system displays the following message:

`Your account has been temporarily locked. Please try again later.`

### Account Unlock

12. After the 30-minute lock period expires, the account is automatically unlocked.

13. After the account is unlocked, the user can attempt to log in again.

14. Failed login tracking starts again after the account has been unlocked.

---

## Acceptance Criteria

### AC-01 — Failed Login Below Threshold

**Given** a registered user's account is not locked  
**And** the user has fewer than four consecutive failed login attempts  
**When** the user enters an incorrect password  
**Then** the login attempt fails  
**And** the failed-login counter is increased by one  
**And** the account remains unlocked.

### AC-02 — Lock Account at Threshold

**Given** a registered user's account is not locked  
**And** the user has four consecutive failed login attempts  
**When** the user enters an incorrect password again  
**Then** the login attempt fails  
**And** the account is temporarily locked.

### AC-03 — Login While Locked

**Given** the user's account is temporarily locked  
**When** the user attempts to log in  
**Then** authentication is not allowed  
**And** the system displays:

`Your account has been temporarily locked. Please try again later.`

### AC-04 — Automatic Unlock

**Given** the user's account is temporarily locked  
**When** the 30-minute lock period expires  
**Then** the account is automatically unlocked  
**And** the user can attempt to log in again.

### AC-05 — Successful Login Resets Counter

**Given** the user's account is not locked  
**And** the user has at least one but fewer than five consecutive failed login attempts  
**When** the user logs in successfully  
**Then** the failed-login counter is reset.

---

## Notes

- Failed-login tracking is account-specific.
- Account locking is temporary.
- No manual action is required to unlock the account after the lock period expires.