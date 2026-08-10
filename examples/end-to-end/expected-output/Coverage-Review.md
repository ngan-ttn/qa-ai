# Coverage Review — Account Lock After Failed Login Attempts

## 1. Review Overview

This artifact reviews the coverage quality of the generated test scenarios for the Account Lock After Failed Login Attempts feature.

The review is based on:

- `Sample-Requirement.md`
- `Requirement-Analysis.md`
- `Business-Rules.md`
- `Risk-Analysis.md`
- `Test-Scenarios.md`

The purpose of this review is to determine whether the current scenario set sufficiently covers the confirmed requirement behavior and identified risks before detailed test cases are generated.

This artifact reviews coverage.

It does not silently add new confirmed requirements, business rules, or expected behavior.

---

## 2. Review Scope

The review evaluates:

```text
Requirement Coverage
        +
Acceptance Criteria Coverage
        +
Business Rule Coverage
        +
Risk Coverage
        +
Boundary Coverage
        +
State Transition Coverage
        +
Sequence Coverage
        +
Isolation Coverage
        +
Scenario Duplication
        +
Clarification-Dependent Coverage
```

The review also checks whether high-priority risks receive appropriate testing attention.

---

## 3. Coverage Status Model

The following statuses are used.

| Status | Meaning |
|---|---|
| Covered | Confirmed behavior has sufficient scenario coverage. |
| Partial | Some aspects are covered, but additional confirmed coverage is required. |
| Missing | Confirmed behavior has no adequate scenario coverage. |
| Clarification-Dependent | Testing is relevant, but expected behavior is not sufficiently defined. |
| Duplicate | Scenario coverage repeats an existing objective without meaningful additional value. |
| Not Applicable | The item does not require independent scenario coverage. |

---

## 4. Overall Coverage Result

**Overall Status: PASS**

The current confirmed scenario set provides coverage for:

- All 14 functional requirements.
- All 5 acceptance criteria.
- All 9 confirmed business rules.
- All 9 confirmed functional risks.
- The primary failed-login boundary.
- The temporary-lock state transition.
- Counter-reset behavior.
- Account isolation.
- Automatic recovery.
- Post-unlock tracking.
- The complete confirmed lifecycle.

No confirmed requirement is currently missing scenario coverage.

However, several relevant behaviors remain clarification-dependent and therefore cannot yet be treated as executable confirmed coverage.

---

## 5. Requirement Coverage Review

| Requirement | Covered By | Status | Review |
|---|---|---|---|
| R1 | TS-001, TS-020 | Covered | Registered-user login entry is represented. |
| R2 | TS-001, TS-002, TS-020 | Covered | Credential validation is exercised through successful and failed authentication. |
| R3 | TS-001, TS-017, TS-020 | Covered | Successful authentication for an unlocked account is covered. |
| R4 | TS-002, TS-003, TS-020 | Covered | Incorrect-password authentication failure is covered. |
| R5 | TS-003, TS-010, TS-011 | Covered | Per-account tracking and isolation are covered. |
| R6 | TS-004, TS-005, TS-006, TS-019, TS-020 | Covered | Below-threshold and at-threshold behavior are explicitly covered. |
| R7 | TS-007, TS-008, TS-009 | Covered | Successful-login reset is covered at representative sequence points. |
| R8 | TS-006, TS-019, TS-020 | Covered | Transition into locked state is covered. |
| R9 | TS-015, TS-016, TS-020 | Covered | Active lock and expiration are covered within the defined time boundary. |
| R10 | TS-012, TS-013, TS-020 | Covered | Authentication prohibition during lock is covered. |
| R11 | TS-014 | Covered | Exact lock-message verification has dedicated coverage. |
| R12 | TS-016, TS-019, TS-020 | Covered | Automatic unlock is covered. |
| R13 | TS-017, TS-020 | Covered | Authentication availability after unlock is covered. |
| R14 | TS-018, TS-019 | Covered | Restarted failed-login tracking is covered. |

### Requirement Coverage Result

```text
14 / 14 requirements covered
```

**Status: PASS**

---

## 6. Acceptance Criteria Coverage Review

| Acceptance Criterion | Covered By | Status | Review |
|---|---|---|---|
| AC-01 | TS-004, TS-005 | Covered | Below-threshold failed-login behavior is covered. |
| AC-02 | TS-006 | Covered | Fifth-failure lock transition is directly covered. |
| AC-03 | TS-012, TS-013, TS-014 | Covered | Authentication rejection and required message are covered. |
| AC-04 | TS-016, TS-017 | Covered | Automatic unlock and restored login availability are covered. |
| AC-05 | TS-007, TS-008, TS-009 | Covered | Counter-reset behavior receives multiple sequence-focused scenarios. |

### Acceptance Criteria Coverage Result

```text
5 / 5 acceptance criteria covered
```

**Status: PASS**

---

## 7. Business Rule Coverage Review

| Business Rule | Covered By | Status | Review |
|---|---|---|---|
| BR-001 | TS-003, TS-010, TS-011 | Covered | Tracking and account isolation are represented. |
| BR-002 | TS-004, TS-005, TS-006, TS-019 | Covered | Threshold behavior receives boundary and lifecycle coverage. |
| BR-003 | TS-007, TS-008, TS-009 | Covered | Reset and consecutive-sequence semantics are covered. |
| BR-004 | TS-015, TS-016 | Covered | Active and expired lock-period conditions are covered. |
| BR-005 | TS-012, TS-013 | Covered | Locked-state authentication rejection is covered. |
| BR-006 | TS-014 | Covered | Required user feedback has dedicated verification. |
| BR-007 | TS-016, TS-019 | Covered | Automatic state transition is covered. |
| BR-008 | TS-017 | Covered | Authentication availability after unlock is covered. |
| BR-009 | TS-018, TS-019 | Covered | Restarted tracking receives focused and lifecycle coverage. |

### Business Rule Coverage Result

```text
9 / 9 confirmed business rules covered
```

**Status: PASS**

---

## 8. Risk Coverage Review

### Confirmed Functional Risks

| Risk | Priority | Covered By | Status | Review |
|---|---|---|---|---|
| RISK-001 | High | TS-006 | Covered | Exact lock threshold is directly tested. |
| RISK-002 | High | TS-005, TS-006 | Covered | Both sides of the `4 → 5` boundary are covered. |
| RISK-003 | High | TS-007, TS-008, TS-009 | Covered | Reset behavior receives strong sequence coverage. |
| RISK-004 | High | TS-010, TS-011 | Covered | Independent-account behavior is explicitly tested. |
| RISK-005 | High | TS-012 | Covered | Correct credentials during lock are explicitly tested. |
| RISK-006 | High | TS-015, TS-016 | Covered | Early-unlock risk is covered within the defined boundary. |
| RISK-007 | High | TS-016, TS-017 | Covered | Failure-to-unlock and post-unlock availability are covered. |
| RISK-008 | Medium | TS-014 | Covered | Required message has focused coverage. |
| RISK-009 | High | TS-018, TS-019 | Covered | Post-unlock tracking is covered. |

### Confirmed Risk Coverage Result

```text
9 / 9 confirmed risks covered
```

**Status: PASS**

---

## 9. Clarification-Dependent Risk Review

| Risk | Candidate Coverage | Status | Reason |
|---|---|---|---|
| RISK-010 | CTS-001, CTS-002 | Clarification-Dependent | Counter and timer behavior during active lock are undefined. |
| RISK-011 | CTS-004, CTS-005 | Clarification-Dependent | Cross-browser/device tracking behavior is undefined. |
| RISK-012 | CTS-006 | Clarification-Dependent | Concurrent threshold semantics are undefined. |

These risks are not considered coverage failures.

They are correctly preserved as unresolved testing areas until the associated expected behavior is defined.

---

## 10. Boundary Coverage Review

### Failed-Login Threshold

Confirmed boundary:

```text
4 Consecutive Failures
→ UNLOCKED

5 Consecutive Failures
→ LOCKED
```

Coverage:

```text
TS-005
→ 4 failures

TS-006
→ 5th failure
```

**Status: Covered**

The critical threshold has explicit two-sided coverage.

---

### Lock Duration Boundary

Confirmed behavior:

```text
Before expiration
→ LOCKED

After 30-minute period expires
→ UNLOCKED
```

Coverage:

```text
TS-015
→ Before expiration

TS-016
→ After expiration
```

**Status: Covered within requirement definition**

The precise instant at exactly 30 minutes remains clarification-dependent.

Candidate:

```text
CTS-003
```

This is not classified as a confirmed coverage gap because the expected boundary semantics are not explicitly defined.

---

## 11. State Transition Coverage Review

The confirmed state model is:

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

Coverage:

| Transition | Scenario | Status |
|---|---|---|
| Unlocked → Unlocked after failures 1–4 | TS-004, TS-005 | Covered |
| Unlocked → Locked | TS-006 | Covered |
| Locked → Locked before expiration | TS-015 | Covered |
| Locked → Unlocked | TS-016 | Covered |
| Unlocked → successful authentication after unlock | TS-017 | Covered |
| New post-unlock failure sequence | TS-018, TS-019 | Covered |

**State Transition Coverage: PASS**

---

## 12. Sequence Coverage Review

The feature depends on **consecutive** failed attempts.

Three important sequence types require coverage.

### Continuous Failure Sequence

```text
Failure
Failure
Failure
Failure
Failure
→ Locked
```

Covered by:

```text
TS-006
```

### Interrupted Failure Sequence

```text
Failure(s)
   ↓
Successful Login
   ↓
New Failure Sequence
```

Covered by:

```text
TS-007
TS-008
TS-009
```

### New Sequence After Unlock

```text
Locked
   ↓
Automatic Unlock
   ↓
New Failed-Login Sequence
```

Covered by:

```text
TS-018
TS-019
```

**Sequence Coverage: PASS**

---

## 13. Account Isolation Coverage Review

Confirmed rule:

```text
Failed-login tracking
→ Per account
```

Coverage:

```text
TS-010
→ Independent failed-login state

TS-011
→ Independent authentication availability
```

The scenario set verifies both:

- State isolation.
- Functional effect of that isolation.

**Status: Covered**

Cross-browser/device behavior for the **same account** remains separate and clarification-dependent.

---

## 14. Locked-State Coverage Review

The current scenario set verifies:

```text
Locked + Correct Password
→ Rejected
```

through `TS-012`.

It also verifies generic authentication rejection during lock through `TS-013` and the required message through `TS-014`.

This provides coverage for:

- Access restriction.
- Correct-password bypass risk.
- User feedback.

**Status: Covered**

Behavior of the counter and timer during those attempts remains undefined and is correctly excluded from confirmed expected results.

---

## 15. Recovery Coverage Review

Recovery consists of:

```text
30-Minute Expiration
        ↓
Automatic Unlock
        ↓
Authentication Available
        ↓
Failed-Login Tracking Restarts
```

Coverage:

```text
TS-016 → Automatic unlock
TS-017 → Authentication available
TS-018 → Tracking restarts
TS-019 → New complete failure lifecycle
```

**Status: Covered**

The recovery path receives sufficient focused coverage before detailed test-case generation.

---

## 16. End-to-End Coverage Review

`TS-020` covers the complete confirmed lifecycle:

```text
Normal Authentication
        ↓
Failed Login Sequence
        ↓
Threshold
        ↓
Temporary Lock
        ↓
Locked Authentication
        ↓
Expiration
        ↓
Automatic Unlock
        ↓
Authentication Restored
```

**Status: Covered**

However, `TS-020` is considered integration/lifecycle coverage.

It does not replace focused coverage such as:

- TS-005 for boundary behavior.
- TS-008 for reset behavior.
- TS-010 for isolation.
- TS-012 for locked-state bypass.
- TS-016 for automatic unlock.

---

## 17. Duplicate Coverage Review

Some scenarios touch the same business rule, but their primary objectives differ.

Examples:

```text
TS-005
→ Immediately below threshold

TS-006
→ At threshold
```

These are complementary boundary scenarios, not duplicates.

Similarly:

```text
TS-007
→ Reset after one failure

TS-008
→ Reset immediately below threshold

TS-009
→ Verify sequence separation
```

These scenarios share BR-003 but validate different risk conditions.

And:

```text
TS-016
→ Automatic state transition

TS-017
→ Authentication after transition

TS-018
→ Tracking after transition
```

These verify different recovery responsibilities.

### Duplicate Result

**No confirmed duplicate scenarios requiring removal.**

---

## 18. Coverage Gaps

### Confirmed Requirement Gaps

```text
None identified
```

All currently confirmed requirements, acceptance criteria, and business rules have scenario coverage.

### Clarification-Dependent Gaps

The following areas remain unresolved:

| Gap ID | Area | Current Candidate |
|---|---|---|
| GAP-001 | Counter behavior during active lock | CTS-001 |
| GAP-002 | Lock timer behavior during active lock | CTS-002 |
| GAP-003 | Exact expiration instant | CTS-003 |
| GAP-004 | Same-account cross-browser tracking | CTS-004 |
| GAP-005 | Same-account cross-device tracking | CTS-005 |
| GAP-006 | Concurrent threshold attempts | CTS-006 |
| GAP-007 | Existing authenticated session after lock | CTS-007 |
| GAP-008 | Password-management interaction | CTS-008 |
| GAP-009 | Unknown/unregistered email behavior | CTS-009 |

These are not counted as missing confirmed coverage.

They require requirement clarification before executable expected results can be finalized.

---

## 19. Coverage Strength Assessment

| Coverage Dimension | Result |
|---|---|
| Functional Requirement Coverage | Strong |
| Acceptance Criteria Coverage | Strong |
| Business Rule Coverage | Strong |
| High-Risk Coverage | Strong |
| Threshold Boundary Coverage | Strong |
| State Transition Coverage | Strong |
| Sequence Coverage | Strong |
| Account Isolation Coverage | Strong |
| Recovery Coverage | Strong |
| Clarification Handling | Strong |
| Duplicate Control | Pass |

No confirmed high-priority risk is left without scenario coverage.

---

## 20. Recommendation Before Test Case Generation

**Recommendation: PROCEED**

The current confirmed scenario set is sufficiently complete to proceed to detailed test-case generation.

Test-case generation should preserve:

```text
TS-001 → TS-020
```

as the approved confirmed scenario baseline.

The clarification-dependent candidates:

```text
CTS-001 → CTS-009
```

should not be converted into executable test cases with assumed expected results.

They should remain pending until the corresponding requirement questions are resolved.

---

## 21. Coverage Review Summary

The review confirms the following traceability chain:

```text
14 Requirements
        ↓
5 Acceptance Criteria
        ↓
9 Business Rules
        ↓
9 Confirmed Functional Risks
        ↓
20 Confirmed Test Scenarios
```

Coverage result:

```text
Requirements       14 / 14 Covered
Acceptance Criteria 5 / 5 Covered
Business Rules       9 / 9 Covered
Confirmed Risks      9 / 9 Covered
```

In addition:

```text
9 Clarification-Dependent Candidates
```

remain visible without being treated as confirmed behavior.

### Final Decision

**PASS — Proceed to Test Case Generation**

The scenario baseline provides sufficient confirmed functional, boundary, state, sequence, isolation, recovery, and risk-based coverage for detailed test-case generation.