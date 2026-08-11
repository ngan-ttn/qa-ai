# Post-Allocation UPN Coverage Extension for Family-Mode Import Permit

## Dataset Metadata

- Dataset ID: `REQ-PERMIT-001`
- Complexity: `Complex`
- Domain: `Regulatory / Inventory Management`
- Primary Evaluation Focus: Requirement analysis, business-rule extraction, multi-role behavior, state-transition analysis, cross-module dependency analysis, data-integrity validation, concurrency risk identification, regression-impact analysis, ambiguity detection, and end-to-end test coverage

---

## Context

The application manages Import Permits used to authorize the import of regulated products.

Regulatory Affairs (RA) users maintain Import Permit records.

Product Requests may require quantities of regulated products and may be allocated against an approved Import Permit.

Import Permits can operate in either:

- `UPN` mode, where the permit covers explicitly defined product UPNs.
- `Family` mode, where the permit covers a Device Family and maintains a list of eligible UPNs belonging to that family.

This dataset focuses only on approved Family-mode Import Permits.

A Family-mode permit may already have quantity allocated to one or more Product Requests while still remaining valid for future allocations.

RA users must be able to extend the UPN coverage of such a permit without modifying the permit information or existing allocations.

---

## Requirement

As an authorized Regulatory Affairs user,

I want to add new UPNs to an approved Family-mode Import Permit after the permit has already been allocated,

So that additional eligible products can use the existing permit without changing previously approved permit information or existing Product Request allocations.

### Permit Quantity Model

A Family-mode Import Permit contains:

- Device Family
- Family Name
- Device Owner
- Approval Quantity
- Remaining Quantity
- Approval Status
- Approval Number
- Approved Period
- Approved Premise
- Covered UPNs

`Approval Quantity` represents the total quantity approved by the permit.

`Remaining Quantity` represents the portion of `Approval Quantity` that has not yet been allocated to Product Requests.

For a valid permit record:

`0 <= Remaining Quantity <= Approval Quantity`

The permit is considered:

- `Unallocated` when `Remaining Quantity = Approval Quantity`.
- `Partially Allocated` when `0 < Remaining Quantity < Approval Quantity`.
- `Fully Allocated` when `Remaining Quantity = 0`.

A record where `Remaining Quantity > Approval Quantity` or `Remaining Quantity < 0` is considered an invalid quantity state and is outside the normal business flow defined by this dataset.

Adding UPN coverage does not consume, restore, or otherwise change permit quantity.

### Allocation Dependency

The allocation process itself is outside the primary feature scope, but the following allocation rules are authoritative dependencies for this dataset:

1. Only an approved permit may be used for allocation.
2. The requested product UPN must exist in the permit's covered UPN list.
3. The permit must be within its approved period when allocation is performed.
4. The requested allocation quantity must not exceed the permit's current `Remaining Quantity`.
5. A successful allocation decreases `Remaining Quantity` by the allocated quantity.
6. An allocation retains the reference to the Import Permit and quantity used for that allocation.
7. `Remaining Quantity` must never become negative.

These rules are included because extending UPN coverage can affect eligibility for future Product Request allocations.

### Edit Availability

For an approved Family-mode permit:

- The normal edit behavior applies while the permit is `Unallocated`.
- Once the permit becomes `Partially Allocated` or `Fully Allocated`, the Edit action must remain available to an authorized RA user.
- Opening Edit for an allocated permit must display a restricted edit state.

The restricted edit state exists to allow UPN coverage extension without allowing previously approved or allocation-sensitive permit data to be changed.

### Restricted Edit State

When the permit is `Partially Allocated` or `Fully Allocated`, the following fields must display their current values and must not be editable:

- Device Family
- Family Name
- Device Owner
- Approval Quantity
- Approval Status
- Approval Number
- Approved Period
- Approved Premise

Existing covered UPN rows must also be read-only.

An existing covered UPN cannot be edited or removed.

The Remove action must not be available for an existing covered UPN row.

The restricted edit state must allow only the addition of new UPN coverage.

### Add UPN

An authorized RA user may add one or more UPNs while the permit is in the restricted edit state.

A UPN is eligible to be added only when:

1. The UPN exists in Product Master.
2. Product Master associates the UPN with the same Device Family as the permit.
3. The UPN does not already exist in the permit's saved covered UPN list.
4. The UPN has not already been added during the current edit session.

Product Master is the authoritative source for UPN existence and Device Family association.

A newly selected UPN remains pending until the update is submitted successfully.

A pending UPN may be removed during the current edit session before submission.

Removing a pending UPN does not affect any saved UPN coverage.

### Update Behavior

When the restricted edit update succeeds:

- Every successfully submitted new UPN becomes part of the permit's saved covered UPN list.
- Each newly saved UPN becomes read-only in subsequent restricted edit sessions.
- Existing covered UPNs remain unchanged.
- Device Family remains unchanged.
- Family Name remains unchanged.
- Device Owner remains unchanged.
- Approval Quantity remains unchanged.
- Remaining Quantity remains unchanged.
- Approval Status remains unchanged.
- Approval Number remains unchanged.
- Approved Period remains unchanged.
- Approved Premise remains unchanged.
- Existing Product Request allocations remain unchanged.

The operation extends UPN coverage only.

Submitting the restricted edit without any pending UPN must not change the permit.

### Duplicate Prevention

The same UPN must not appear more than once in the permit's covered UPN list.

A UPN must therefore be rejected as a duplicate when it:

- Already exists in the saved covered UPN list, or
- Already exists in the pending UPN list for the current edit session.

A rejected duplicate must not create another pending row.

### Future Allocation

After a new UPN is successfully saved, it becomes part of the permit's coverage and may be considered for future Product Request allocation.

The newly added UPN does not receive a separate quantity allowance.

`Remaining Quantity` is maintained at permit level and is shared across all covered UPNs.

For example, if:

- Approval Quantity = `100`
- Remaining Quantity = `30`

adding one or more new UPNs must leave:

- Approval Quantity = `100`
- Remaining Quantity = `30`

Future allocations for any covered UPN collectively consume the same permit-level `Remaining Quantity`.

### Fully Allocated Permit

UPN coverage may still be extended when:

`Remaining Quantity = 0`

Adding a UPN to a fully allocated permit:

- Does not restore permit quantity.
- Does not change existing allocations.
- Does not immediately allow additional quantity to be allocated.

A newly added UPN can be considered for allocation only when the permit has sufficient `Remaining Quantity` under the existing allocation rules.

Any business process that may later restore or adjust permit quantity is outside the scope of this dataset.

### Authorization

Only an RA user who already has permission to maintain Import Permits may use the restricted edit capability.

A user who has view-only access to the permit must not gain edit access because the permit becomes allocated.

This requirement does not introduce or modify the application's existing role and permission model.

### Existing Allocation Integrity

Extending UPN coverage must not:

- Change an existing Product Request allocation quantity.
- Reassign an existing Product Request to another permit.
- Change the Import Permit reference retained by an existing allocation.
- Recalculate historical allocation quantities.
- Consume additional permit quantity.
- Restore previously allocated permit quantity.
- Modify or remove existing covered UPNs.

Existing allocations must remain valid and unchanged solely because additional UPN coverage is added.

---

## Acceptance Criteria

1. An authorized RA user can access the Edit action for an approved Family-mode permit in `Partially Allocated` state.

2. An authorized RA user can access the Edit action for an approved Family-mode permit in `Fully Allocated` state.

3. Opening Edit for a partially or fully allocated Family-mode permit displays the restricted edit state.

4. Device Family, Family Name, Device Owner, Approval Quantity, Approval Status, Approval Number, Approved Period, and Approved Premise display their current values and cannot be modified in the restricted edit state.

5. Existing covered UPN rows cannot be modified.

6. Existing covered UPN rows cannot be removed.

7. The Remove action is not available for existing covered UPN rows.

8. An authorized RA user can select a new UPN that exists in Product Master and is associated with the same Device Family as the permit.

9. A UPN associated with a different Device Family is not eligible to be added.

10. A UPN that does not exist in Product Master is not eligible to be added.

11. A UPN already present in the saved covered UPN list cannot be added again.

12. The same UPN cannot be added more than once during the same edit session.

13. A newly selected pending UPN can be removed before the update is submitted.

14. Removing a pending UPN does not modify existing saved UPN coverage.

15. After a successful update, each submitted new UPN becomes part of the saved covered UPN list.

16. A newly saved UPN becomes read-only in subsequent restricted edit sessions.

17. A successful coverage update does not change Device Family, Family Name, Device Owner, Approval Status, Approval Number, Approved Period, or Approved Premise.

18. A successful coverage update does not change `Approval Quantity`.

19. A successful coverage update does not change `Remaining Quantity`.

20. A successful coverage update does not modify existing Product Request allocations.

21. Submitting the restricted edit without a pending UPN does not change the permit.

22. A newly saved UPN becomes eligible to be evaluated for future allocation under the existing permit allocation rules.

23. Adding a UPN does not reserve or consume permit quantity.

24. All covered UPNs share the same permit-level `Remaining Quantity`.

25. Adding one or more UPNs to a partially allocated permit leaves both `Approval Quantity` and `Remaining Quantity` unchanged.

26. Adding one or more UPNs to a fully allocated permit leaves `Remaining Quantity = 0`.

27. A newly added UPN cannot receive a positive allocation while `Remaining Quantity = 0`.

28. A future Product Request allocation for a newly covered UPN cannot exceed the permit's current `Remaining Quantity`.

29. A successful future allocation decreases `Remaining Quantity` by exactly the allocated quantity.

30. `Remaining Quantity` cannot become negative through allocation.

31. Adding UPN coverage does not change the Import Permit reference or allocated quantity retained by an existing Product Request allocation.

32. A user without Import Permit maintenance permission does not gain restricted edit access when the permit becomes allocated.

---

## Constraints / Notes

- This dataset covers approved Family-mode Import Permits only.
- Post-allocation editing begins only when the permit is `Partially Allocated` or `Fully Allocated`.
- Product Master is the authoritative source for UPN existence and Device Family association.
- `Remaining Quantity` is maintained at permit level, not per UPN.
- Allocation quantity is represented as a positive whole number.
- The restricted edit capability extends UPN coverage only.
- Creation and initial approval of an Import Permit are outside the scope of this dataset.
- Normal editing of an unallocated permit is outside the scope of this dataset.
- Changing approval information after allocation is outside the scope of this dataset.
- Changing Approval Quantity through the restricted edit flow is outside the scope of this dataset.
- Removing existing UPN coverage after allocation is outside the scope of this dataset.
- Processes that restore or adjust allocated permit quantity are outside the scope of this dataset.
- Technical persistence, transaction, and locking mechanisms are not prescribed by this dataset.

---

## Known Ambiguities

The following information is intentionally not specified:

1. When UPN eligibility must be revalidated against Product Master after initial selection, including whether validation must occur again when the update is submitted.

2. The expected result when two RA users edit the same allocated permit concurrently and submit different new UPNs.

3. The expected result when two RA users concurrently attempt to add the same UPN to the same permit.

4. The expected behavior when Product Master changes a selected UPN's Device Family association after selection but before the permit update is completed.

5. Whether an allocated permit whose Approved Period has expired may still receive new UPN coverage through the restricted edit flow.

6. Whether an update containing multiple new UPNs must be atomic when one or more UPNs fail validation or persistence.

7. The expected recovery behavior if persistence of multiple newly added UPNs partially succeeds.

8. Whether extending UPN coverage requires an audit-log entry and, if so, which changes and actor information must be recorded.

9. Whether users or downstream systems must receive a notification after UPN coverage is extended.

10. Whether an existing Product Request that could not previously be allocated because its UPN was not covered should automatically be re-evaluated after that UPN is added, or whether allocation must be retried explicitly.

These gaps are intentionally retained as evaluation targets. Downstream QA analysis is expected to identify the relevant clarification questions, risks, integration impacts, and regression areas without inventing unspecified business behavior.
