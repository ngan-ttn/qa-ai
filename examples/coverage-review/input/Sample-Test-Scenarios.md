# Sample Test Scenarios — Account Lock After Failed Login Attempts

## Scenario Summary

This intentionally partial scenario set is used as input for the QA-AI coverage-review capability. It covers representative authentication, threshold, reset, locked-state, automatic-unlock, and account-isolation behavior while leaving known gaps for the reviewer to identify.

---

## Scope

Partial coverage only; the fixture is not intended to be exhaustive.

---

## Test Scenarios

| Scenario ID | Module / Feature | Scenario | Type | Preconditions / Conditions | Expected Behavior | Requirement / Rule Traceability | Risk Traceability | Priority |
|---|---|---|---|---|---|---|---|---|
| TS-001 | Authentication | Verify a registered user with valid credentials can log in when the account is not locked. | Positive | Registered account; unlocked; valid credentials. | Authentication succeeds. | Requirements 1–3 | N/A | Medium |
| TS-002 | Authentication | Verify login fails when a registered user enters an incorrect password. | Negative | Registered account; unlocked; incorrect password. | Authentication fails. | Requirement 4 | N/A | High |
| TS-003 | Failed Login Tracking | Verify the account remains unlocked after four consecutive incorrect-password attempts. | Boundary | New sequence; four consecutive failures. | Account remains unlocked after failure 4. | Requirement 6; AC-01 | N/A | High |
| TS-004 | Account Lock | Verify the account becomes temporarily locked on the fifth consecutive incorrect-password attempt. | Boundary / State | Account unlocked with four consecutive failures; fifth failure occurs. | Account becomes temporarily locked. | Requirements 6, 8; AC-02 | N/A | High |
| TS-005 | Counter Reset | Verify successful login before five consecutive failures resets the failed-login counter. | Positive / State | Account unlocked with 1–4 failures; valid credentials submitted. | Login succeeds and current failure sequence resets. | Requirement 7; AC-05 | N/A | High |
| TS-006 | Account Lock | Verify a locked account cannot authenticate when the correct password is entered. | Negative / State | Account locked; lock period active; correct password. | Authentication is rejected. | Requirement 10; AC-03 | N/A | High |
| TS-007 | Account Lock | Verify the defined temporary-lock message is displayed for a login attempt while locked. | Functional | Account locked; login attempted. | Defined temporary-lock message is displayed and authentication is rejected. | Requirement 11; AC-03 | N/A | Medium |
| TS-008 | Automatic Unlock | Verify the account automatically unlocks after the 30-minute lock period expires. | Time Boundary / State | Account locked; lock period expires. | Account automatically transitions to unlocked. | Requirement 12; AC-04 | N/A | High |
| TS-009 | Automatic Unlock | Verify valid credentials can authenticate after automatic unlock. | Positive / State | Automatic unlock completed; valid credentials. | Authentication succeeds. | Requirement 13; AC-04 | N/A | High |
| TS-010 | Account Isolation | Verify failed attempts for one account do not affect another registered account. | Isolation | Two registered accounts with independent state. | Failure state remains isolated per account. | Requirement 5 | N/A | High |

---

## Open Questions / Known Fixture Gaps

The fixture intentionally omits direct scenario coverage for Requirement 9 (before-expiry lock duration behavior), Requirement 14 (post-unlock tracking restart), repeated lifecycle, and additional boundary/state combinations so that coverage-review can detect meaningful gaps.

---

## Coverage Summary

| Requirement / Acceptance Criteria | Covered By |
|---|---|
| Requirement 1 | TS-001 |
| Requirement 2 | TS-001, TS-002 |
| Requirement 3 | TS-001 |
| Requirement 4 | TS-002 |
| Requirement 5 | TS-010 |
| Requirement 6 | TS-003, TS-004 |
| Requirement 7 | TS-005 |
| Requirement 8 | TS-004 |
| Requirement 9 | — |
| Requirement 10 | TS-006 |
| Requirement 11 | TS-007 |
| Requirement 12 | TS-008 |
| Requirement 13 | TS-009 |
| Requirement 14 | — |
| AC-01 | TS-003 |
| AC-02 | TS-004 |
| AC-03 | TS-006, TS-007 |
| AC-04 | TS-008, TS-009 |
| AC-05 | TS-005 |
