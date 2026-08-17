# P15 Change & Regression Pilot

> Version: 1.0.0  
> Status: Completed  
> Last Updated: 2026-08-14

## 1. Purpose

Validate whether the canonical `regression-impact` capability can translate an explicit requirement delta into a practical regression scope without inventing implementation dependencies.

This document uses a **controlled pilot change fixture**. It is not asserted to be a real production change.

## 2. Controlled Change Fixture

### Baseline

Coupon Available list default sort is nearest expiration date; alternate sort is Newest campaign/coupon timeframe.

### Pilot Change Delta

For regression-evaluation purposes only:

> Change Coupon Available default sorting from `Expiry date` to `Newest`. Keep `Expiry date` available as the alternate sort option. No other Coupon, Voucher, or Flight requirement is changed by this fixture.

This fixture exists solely to test change-impact reasoning.

## 3. Delta Analysis

### Changed

- Coupon default sort selection.
- Default ordering of Coupon Available list on initial load/reset to default sort state.

### Explicitly Unchanged

- Coupon availability eligibility.
- Coupon detail navigation.
- Conditions navigation.
- Coupon indicator behavior.
- Coupon Past Rewards behavior.
- Coupon empty state.
- Voucher behavior.
- Flight behavior.

## 4. Direct Impact

| Impact ID | Artifact/Behavior | Impact | Rationale |
|---|---|---|---|
| RI-D-001 | `BR-C-005` | Update required | Default/alternate sort semantics changed. |
| RI-D-002 | `SC-C-006` | Update required | Scenario must expect Newest as default. |
| RI-D-003 | `TC-C-004` | Update required | Existing expected result asserts nearest expiry as default. |
| RI-D-004 | `TD-C-001` | Retain but verify adequacy | Existing data needs distinct expiry and campaign times and remains suitable. |

## 5. Indirect Impact Through Known Relationships

| Impact ID | Area | Classification | Rationale |
|---|---|---|---|
| RI-I-001 | Coupon sort bottomsheet/options | Required | Default marker/selection must align with new default; this is directly tied to sort behavior defined in FRS. |
| RI-I-002 | Coupon list ordering after selecting Expiry date | Required | Expiry date becomes alternate and still needs explicit coverage. |
| RI-I-003 | Coupon detail navigation | Retained-unaffected | No stated dependency on list default sort. |
| RI-I-004 | Coupon indicator | Retained-unaffected | No known requirement dependency on sort. |
| RI-I-005 | Coupon Past Rewards | Uncertain/limited | FRS sort wording appears under Coupon screen generally; pilot fixture explicitly scopes change to Available, so no Past behavior is added. |
| RI-I-006 | Voucher and Flight | Retained-unaffected | Fixture explicitly states no change and no known dependency is documented. |

No database index, API ordering parameter, cache, CMS field, Voucherify request, or backend implementation dependency is inferred.

## 6. Existing Coverage Mapping

### Needs Update

- `SC-C-006`
- `TC-C-004`
- `BR-C-005`

### Still Valid

- `SC-C-001..005`, `SC-C-007..009` subject to their existing blocked/clarification states;
- `TC-C-001..003`;
- all Voucher cases;
- all Flight cases;
- `TD-C-001` as a data requirement, because distinct expiry and campaign times remain necessary.

## 7. Regression Scope

### Required

1. Coupon Available initial sort defaults to Newest.
2. Newest ordering uses the defined campaign/coupon timeframe ordering from the change fixture/baseline terminology.
3. User can switch to Expiry date sorting.
4. Expiry-date sorting still orders by nearest expiration date.
5. Sort UI/default selection reflects Newest.

### Recommended

- re-check Coupon Available list eligibility while sorted to ensure ordering change did not alter which coupons are shown;
- re-check View details/Conditions from differently sorted rows to catch list-render/navigation regression.

### Retained-Unaffected

- Voucher country/list/detail flows;
- Flight list/detail flows;
- Coupon indicator;
- Coupon empty state;
- Coupon detail content beyond navigation.

### Uncertain

- whether backend/API request parameters change;
- whether sort state is persisted across sessions;
- whether Past Rewards shares the same sort control.

These are not inferred because no authoritative technical or behavioral dependency was supplied.

## 8. Priority

| Priority | Regression Focus |
|---|---|
| High | Coupon Available default ordering and alternate Expiry sorting. |
| Medium | Sort UI state and Coupon navigation from reordered list. |
| Low / Retained | Unchanged Voucher/Flight sanity only if broader release policy requires it; not required by this delta itself. |

## 9. Regression Pilot Result

**PASS**

The regression analysis:

- establishes a precise delta;
- distinguishes changed vs explicitly unchanged behavior;
- maps existing rules/scenarios/cases affected by the change;
- keeps unaffected coverage out of required scope;
- does not invent implementation coupling;
- produces a prioritized regression scope with rationale.

15.4 is therefore completed for the controlled change fixture.
