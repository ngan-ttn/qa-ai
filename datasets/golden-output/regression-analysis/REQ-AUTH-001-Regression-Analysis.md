# Regression Analysis — Account Lockout After Failed Login Attempts

## Golden Output Metadata

- Dataset ID: `REQ-AUTH-001`
- Source Requirement: `datasets/requirements/simple/REQ-AUTH-001.md`
- Artifact Type: `Regression Analysis`
- Review Status: `Approved`
- Evaluation Purpose: Reference output for evaluating direct-versus-potential impact separation, prioritization, dependency reasoning, canonical regression-scope tiering, traceability, count integrity, and assumption management

---

## Regression Summary

The requirement changes username-and-password authentication by adding per-account failed-attempt tracking, a five-attempt threshold, a 15-minute temporary lock, active-lock rejection, automatic unlock/reset, and successful-login reset/new-sequence behavior.

The source does not define UI, API, database, session-management, password-reset, alternative-authentication, or concurrency contracts; these remain potential/clarification areas rather than confirmed impact.

Scope reference based on the existing confirmed `TS-AUTH-*` coverage:

- **Minimum / Release-Gate Regression:** 10 scenarios
- **Recommended Regression:** 15 scenarios
- **Full Changed-Feature Verification:** 17 scenarios

These counts are based on unique scenario IDs listed in the tier sections below, not target percentages.

---

## Change Overview

Confirmed change relationship: existing password authentication now depends on account-specific failure/lock state and time/reset transitions in addition to credential validity.

---

## Regression Impact / Coverage

| Impact ID | Area / Module | Change Relationship | Regression Scope / Behavior to Revalidate | Impact Type | Evidence / Traceability | Priority | Existing Coverage Reference | Decision |
|---|---|---|---|---|---|---|---|---|
| REG-AUTH-001 | Successful Password Authentication | Direct | Correct password succeeds for an unlocked account; successful login resets any below-threshold failed sequence. | Confirmed | AC-08; BR-AUTH-011 | High | TS-AUTH-001, TS-AUTH-012, TS-AUTH-013 | Include |
| REG-AUTH-002 | Incorrect Password Handling | Direct | Incorrect password remains rejected, increments only the corresponding account counter, and remains unlocked below threshold. | Confirmed | AC-01, AC-02; BR-AUTH-001, BR-AUTH-002, BR-AUTH-003 | High | TS-AUTH-002, TS-AUTH-003, TS-AUTH-004 | Include |
| REG-AUTH-003 | Failed-Attempt Threshold | Direct | Attempts 1–4 remain below lock; fifth consecutive failure locks; reset separates sequences. | Confirmed | AC-02, AC-03, AC-09; BR-AUTH-003, BR-AUTH-004, BR-AUTH-012 | High | TS-AUTH-004, TS-AUTH-005, TS-AUTH-014 | Include |
| REG-AUTH-004 | Locked-State Authentication | Direct | Correct and incorrect password-based login attempts are rejected throughout active lock. | Confirmed | AC-05; BR-AUTH-007, BR-AUTH-008 | High | TS-AUTH-007, TS-AUTH-008, TS-AUTH-009 | Include |
| REG-AUTH-005 | Lock Duration / Automatic Unlock | Direct | Lock starts at fifth recorded failure, remains active before expiry, and automatically unlocks after 15 minutes. | Confirmed | AC-04, AC-05, AC-06; BR-AUTH-005, BR-AUTH-006, BR-AUTH-009 | High | TS-AUTH-006, TS-AUTH-009, TS-AUTH-010 | Include |
| REG-AUTH-006 | Counter Reset After Unlock | Direct | Automatic unlock resets counter to zero; first subsequent failure becomes failure one and remains unlocked. | Confirmed | AC-07, AC-09; BR-AUTH-010, BR-AUTH-012 | High | TS-AUTH-011, TS-AUTH-016 | Include |
| REG-AUTH-007 | Counter Reset After Successful Login | Direct | Successful login after early/four failures resets counter and later failures start a new sequence. | Confirmed | AC-08, AC-09; BR-AUTH-011, BR-AUTH-012 | High | TS-AUTH-012, TS-AUTH-013, TS-AUTH-014 | Include |
| REG-AUTH-008 | Per-Account State Isolation | Direct | Interleaved authentication activity maintains independent failure/lock state per account. | Confirmed | AC-01; account-specific tracking constraint; BR-AUTH-001 | High | TS-AUTH-015 | Include |
| REG-AUTH-009 | Repeated Lock Lifecycle | Direct | After automatic unlock/reset, new failures 1–4 remain below threshold and fifth new failure locks again. | Confirmed | AC-02, AC-03, AC-06, AC-07, AC-09; BR-AUTH-003, BR-AUTH-004, BR-AUTH-009, BR-AUTH-010, BR-AUTH-012 | High | TS-AUTH-017 | Include |
| POT-AUTH-001 | Login UI / Error Presentation | Adjacent | Determine whether UI presentation requires dedicated regression after implementation/UI evidence is available. | Potential | No UI behavior/message/countdown specification in source. | — | N/A | Clarify |
| POT-AUTH-002 | Authentication API Contract | Adjacent | Determine API response regression only from actual endpoint/contract evidence. | Potential | No endpoint/status/schema in source. | — | N/A | Clarify |
| POT-AUTH-003 | Authentication State Persistence | Adjacent | Determine persistence regression only after storage/dependency design is known. | Potential | Technical mechanism explicitly not defined. | — | N/A | Clarify |
| POT-AUTH-004 | Existing Sessions | Adjacent | Determine whether existing authenticated sessions interact with new account lock state. | Potential | Source defines password-based login attempts only. | — | N/A | Clarify |
| POT-AUTH-005 | Password Reset / Credential Change | Adjacent | Determine interaction with failed-attempt/lock state only if additional requirements establish it. | Potential | No password-management behavior defined. | — | N/A | Clarify |
| POT-AUTH-006 | Alternative Authentication | Outside current source scope | No mandatory regression for non-password authentication from this dataset. | Potential | Dataset explicitly limits scope to username/password. | — | N/A | Exclude |
| POT-AUTH-007 | Concurrent Authentication | Adjacent technical risk | Determine concurrency regression only after architecture/implementation semantics are known. | Potential | Concurrency semantics undefined. | — | N/A | Clarify |

---

## Regression Scope Tiers

### Minimum / Release-Gate Regression — 10 scenarios

`TS-AUTH-001`, `TS-AUTH-002`, `TS-AUTH-004`, `TS-AUTH-005`, `TS-AUTH-007`, `TS-AUTH-009`, `TS-AUTH-010`, `TS-AUTH-011`, `TS-AUTH-012`, `TS-AUTH-015`

Rationale: covers normal/failed authentication, threshold below/at lock, correct-password rejection while locked, active-lock duration, automatic unlock, post-unlock reset, successful-login reset, and per-account isolation.

### Recommended Regression — 15 scenarios

Minimum set plus:

`TS-AUTH-003`, `TS-AUTH-006`, `TS-AUTH-013`, `TS-AUTH-014`, `TS-AUTH-016`

Unique total: **15**.

Rationale: adds tracking detail, lock-start timing, additional successful-login reset partition, sequence separation, and first post-unlock failure behavior.

### Full Changed-Feature Verification — 17 scenarios

Recommended set plus:

`TS-AUTH-008`, `TS-AUTH-017`

Unique total: **17** (`TS-AUTH-001`–`TS-AUTH-017`).

These add depth for incorrect-password attempts during active lock and repeated full lifecycle verification. They remain valid confirmed feature coverage but are not required by default in the smaller regression tiers.

---

## Excluded Scope

Alternative authentication is explicitly outside current dataset scope. UI/API/storage/session/password-management/concurrency areas are not confirmed direct impacts and must not be treated as executable regression without additional evidence.

---

## Entry Criteria

- `REQ-AUTH-001` and the current password-authentication baseline are available.
- Existing scenario/testcase coverage can be mapped to the confirmed changed behaviors.

---

## Exit Criteria

- The selected release tier passes for all confirmed included behavior.
- No critical regression remains in the five-attempt threshold, active lock, 15-minute lifecycle, reset paths, or account isolation represented by that tier.
- Potential rows are either supported by new evidence and promoted through review or remain explicitly non-confirmed.

---

## Assumptions / Open Questions

No implementation architecture is assumed. Potential adjacent rows require additional UI/API/database/session/password-management/concurrency evidence before becoming confirmed regression scope.

---

## Count Integrity Self-Check

- Minimum unique scenario IDs: **10**.
- Recommended unique scenario IDs: **15** = 10 Minimum + 5 additional.
- Full Changed-Feature unique scenario IDs: **17** = 15 Recommended + 2 additional.
- Confirmed direct impact rows: **9**.
- Potential/excluded adjacent rows: **7**.

All reported tier counts and additions reconcile with the listed unique IDs.
