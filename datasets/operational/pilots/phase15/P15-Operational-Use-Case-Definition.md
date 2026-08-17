# Phase 15 Operational Use-Case Definition

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-14

---

## 1. Purpose

Define the controlled operational pilot contract for Phase 15 using a real project requirement as authoritative input.

This definition establishes what QA-AI must process, which artifacts are expected, where human QC review is required, what evidence must be preserved, and what constitutes successful operational adoption.

It does not pre-approve generated QA artifacts or fill gaps in the authoritative requirement.

---

## 2. Pilot Identity

| Field | Value |
|---|---|
| Pilot ID | `P15-PILOT-001` |
| Phase | Phase 15 — Operational Usage & Project Adoption |
| Authoritative Input | `FRS - Webview - My rewards 3.0` |
| Requirement Version | `v1.0` |
| Requirement Date | `2026-06-15` |
| Product Scope | Webview — My Rewards 3.0 |
| Target User | Manual QC Engineer |
| Pilot Type | Real-requirement operational QA pilot |

---

## 3. Pilot Objective

Validate whether the frozen QA-AI framework can support a Manual QC Engineer in transforming a real-world functional requirement into a usable, traceable QA artifact chain without inventing unresolved product behavior.

The pilot evaluates operational usefulness rather than textual similarity to a reference answer.

The pilot must demonstrate that QA-AI can:

1. understand and structure the supplied requirement;
2. extract explicit business rules without promoting generic knowledge into project policy;
3. identify QA risks and unresolved requirement gaps;
4. derive test scenarios from confirmed requirement information;
5. review scenario coverage against authoritative source material;
6. generate executable test cases only where expected behavior is sufficiently confirmed;
7. define required test data without inventing unavailable project values;
8. preserve traceability across the artifact chain;
9. support later requirement-change and regression-impact analysis;
10. produce artifacts that a Manual QC Engineer can practically review and continue using.

---

## 4. Authoritative Input Contract

The authoritative source for this pilot is the supplied `FRS - Webview - My rewards 3.0` document.

Confirmed source scope includes:

- My Rewards voucher list;
- country display and country filtering;
- voucher Available and Past Rewards states;
- voucher sorting;
- voucher empty state;
- voucher detail screen enhancements;
- fulfillment-provider pending behavior;
- provider logo behavior;
- voucher name, brand, country, and applicable-at display;
- Wogi HTTPS CTA behavior;
- Flight Available and Past Rewards states;
- new-redemption indicator;
- flight sorting;
- flight detail information;
- reservation-code copy behavior;
- flight expiration behavior;
- flight dates, fare class/deal, route information, connecting-flight display, and passenger quantities;
- flight empty state;
- Coupon Available and Past Rewards states;
- coupon indicator;
- coupon detail/conditions navigation;
- coupon sorting;
- coupon empty state.

The document also contains source areas represented as restricted exported synced blocks. Their hidden contents are not available to this pilot and must not be reconstructed from inference.

---

## 5. Source-Grounding Rules

The following rules are mandatory throughout the pilot:

1. The supplied FRS is the highest-priority source for product behavior in pilot scope.
2. QA-AI shared knowledge may support QA reasoning but must not override or extend project behavior.
3. Missing synced-block content remains unresolved.
4. Jira/Figma references named by the FRS are references only unless their content is separately retrieved and explicitly admitted into the pilot evidence set.
5. Ambiguous or contradictory requirement statements must be surfaced as clarification items.
6. Missing API contracts, database schemas, integration mechanisms, backend status mappings, configured time values, and implementation details must not be invented.
7. An expected result may be executable only when the underlying expected behavior is sufficiently supported by authoritative input.
8. Derived QA coverage must remain distinguishable from confirmed product behavior.

---

## 6. Operational QA Task

The Manual QC operational task is:

> Review the My Rewards 3.0 FRS and produce a complete QA design baseline that can be used to understand scope, clarify gaps, plan coverage, prepare execution-ready test cases where possible, identify required test data, and later assess regression impact when the requirement changes.

The pilot intentionally uses a requirement with multiple related functional areas and state-dependent behavior so that cross-artifact consistency can be evaluated.

---

## 7. Functional Pilot Scope

### 7.1 Voucher

Evaluate coverage for:

- default and applied country filtering;
- country-filter persistence within the app/session behaviors explicitly described by the FRS;
- Reset and Apply actions;
- country display per voucher;
- Available voucher listing and sorting;
- Past Rewards listing;
- voucher selection and detail navigation;
- empty state and redemption CTA;
- pending fulfillment-provider state;
- provider logo configuration behavior;
- voucher name placement;
- Wogi HTTPS CTA and in-app browser behavior;
- brand/country/applicable-at information.

### 7.2 Flight

Evaluate coverage for:

- Available flight redemption list;
- Past Rewards flight list;
- new-redemption indicator lifecycle explicitly stated by the FRS;
- sorting options and defaults;
- read-only ticket details;
- reservation-code copy action;
- expiration behavior and QR blur;
- departure/return date formatting;
- fare class and deal display;
- departure/destination information;
- estimated flight time and flight/plane number;
- connecting-flight text/color behavior;
- passenger quantities;
- empty state.

### 7.3 Coupon

Evaluate coverage for:

- Available coupon list;
- Past Rewards coupon list;
- Promotion × Voucherify display rule as stated by the FRS;
- new-promotion indicator lifecycle;
- View details and Conditions actions;
- sorting options and defaults;
- empty state;
- coupon-detail loading behavior.

---

## 8. Expected Artifact Chain

The pilot uses the canonical QA-AI capability chain:

```text
Authoritative Requirement
        ↓
Structured Requirement Analysis
        ↓
Structured Business Rule Model
        ↓
Structured Risk Analysis
        ↓
Structured Test Scenario Model
        ↓
Coverage Review
        ↓
Structured Test Case Model
        ↓
Test Data Model
```

A later controlled requirement change will additionally invoke:

```text
Requirement Change
        ↓
Regression Impact Analysis
```

Each downstream artifact must consume validated upstream information rather than independently reinterpret the FRS from scratch where the canonical workflow defines an upstream dependency.

---

## 9. Canonical Capabilities Involved

| Capability | Pilot Responsibility |
|---|---|
| `requirement-analyzer` | Structure requirement scope, flows, rules, edge conditions, assumptions, and clarification needs. |
| `business-rule-extractor` | Extract explicit product/business rules without inventing policy. |
| `risk-analyzer` | Identify and prioritize QA-relevant risk. |
| `scenario-generator` | Produce traceable test scenarios from validated upstream artifacts. |
| `coverage-reviewer` | Evaluate coverage against authoritative source and structured upstream artifacts. |
| `testcase-generator` | Produce executable cases only where expected behavior is sufficiently grounded. |
| `test-data-generator` | Define test-data requirements and partitions without fabricating project values. |
| `regression-impact` | Evaluate impact after a controlled requirement change is introduced. |

Specialized API or SQL/database skills are not automatically invoked. They may only be used if authoritative technical contracts are admitted into pilot scope.

---

## 10. Human-QC Checkpoints

Human QC review is mandatory at operational decision points.

| Checkpoint | Human Review Objective |
|---|---|
| HC-01 Requirement Understanding | Confirm feature scope is represented accurately and unresolved source gaps are visible. |
| HC-02 Business Rules | Confirm rules reflect the FRS and no product policy has been invented. |
| HC-03 Scenario Coverage | Confirm scenarios represent practical functional/risk coverage and avoid material duplication. |
| HC-04 Test Case Usability | Confirm executable cases can be run without hidden interpretation; unresolved behavior is not disguised as expected results. |
| HC-05 Test Data Usability | Confirm required data states are actionable and fabricated project values are absent. |
| HC-06 Regression Usefulness | Confirm change-impact output helps select meaningful regression scope. |
| HC-07 Adoption Review | Assess whether the artifact chain reduces manual analysis effort while preserving QC judgment. |

Human review is evidence, not a replacement for source grounding.

---

## 11. Evidence Requirements

Phase 15 pilot evidence must preserve at least:

- pilot ID;
- authoritative input identity/version;
- repository/framework revision used for generation;
- generated artifact identities;
- artifact generation order;
- source-to-artifact traceability;
- assumptions and clarification items;
- human-QC review findings;
- revisions made because of review;
- requirement-change input used for regression pilot;
- regression-impact output;
- adoption-readiness decision.

A generated file alone is not proof that a pilot stage passed.

---

## 12. Success Criteria

The operational pilot succeeds only if all of the following are demonstrated with evidence:

1. **Requirement fidelity** — material functional behavior in pilot scope is represented without silent contradiction or invention.
2. **Source discipline** — unavailable synced-block content and other missing contracts remain explicit unresolved inputs.
3. **Traceability** — downstream scenarios/cases can be traced to requirement/rule/risk sources as applicable.
4. **Coverage usability** — a Manual QC Engineer can understand what is covered, missing, duplicated, or clarification-dependent.
5. **Executable-case safety** — confirmed expected results are separated from unresolved behavior.
6. **Test-data practicality** — data requirements describe actionable states/partitions without invented environment-specific values.
7. **Cross-artifact consistency** — later artifacts do not materially contradict validated earlier artifacts.
8. **Change support** — a controlled requirement change can be translated into a useful regression-impact scope.
9. **Human usability** — Manual QC review confirms the artifacts are practically usable rather than merely structurally valid.
10. **Adoption readiness** — no unresolved blocking issue remains that would make the framework unsafe or impractical for the defined Manual QC use case.

---

## 13. Failure / Blocking Conditions

The pilot must not be marked successful if any of the following occurs:

- QA-AI invents project-specific behavior to close an FRS gap;
- unavailable synced-block content is treated as known;
- test cases contain authoritative-looking expected results unsupported by the FRS;
- critical functional scope disappears between artifacts without explicit rationale;
- downstream artifacts materially contradict upstream validated artifacts;
- traceability is insufficient to identify the basis of critical cases;
- human QC determines that significant reinterpretation is still required before execution;
- regression output cannot explain why affected coverage was selected;
- pilot evidence is incomplete or cannot be reconstructed.

---

## 14. Out of Scope

This pilot does not:

- redefine canonical skills, workflows, standards, or knowledge;
- add project-specific rules to shared QA-AI knowledge;
- assume access to Jira, Figma, CMS, Voucherify, fulfillment-provider, API, database, or partner-system contracts not included in the admitted evidence set;
- validate implementation code;
- perform production testing;
- invent backend/API/DB assertions;
- use textual similarity as the primary adoption criterion;
- treat AI output as accepted without Human QC review.

Framework gaps discovered during the pilot must be recorded as findings and reviewed separately before any canonical framework change.

---

## 15. Stage Mapping

```text
15.1 Operational Use-Case Definition   ← this document
15.2 Real-Requirement Pilot
15.3 Artifact Chain Validation
15.4 Change & Regression Pilot
15.5 Usability / Manual-QC Review
15.6 Adoption Readiness Gate
```

Completion of this definition authorizes execution of 15.2. It does not imply that later Phase 15 stages have passed.

---

## 16. 15.1 Quality Gate

### Review Result

**PASS**

The operational use-case definition:

- identifies a real authoritative requirement;
- defines Manual QC operational intent;
- establishes Voucher, Flight, and Coupon scope;
- defines the canonical artifact chain;
- preserves QA-AI source-authority rules;
- explicitly handles unavailable synced-block content;
- defines Human-QC checkpoints;
- defines evidence, success, failure, and out-of-scope boundaries;
- avoids pre-judging pilot outputs.

### Stage Status

`Completed — P15-PILOT-001 operational use-case contract approved`
