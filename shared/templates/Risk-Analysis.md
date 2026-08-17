# Risk Analysis

## Purpose

This template provides a structured approach for identifying, assessing, prioritizing, and documenting risks that may affect software quality, testing activities, or successful project delivery.

Its purpose is to enable proactive, evidence-based risk management without converting uncertainty into confirmed product behavior.

---

## Canonical Output Format

Risk-analysis documents use a **hybrid format**. Risk context and analysis notes remain section-based, while the canonical risk inventory is maintained as a table for prioritization, review, and traceability.

---

## Template Structure

```text
# Risk Analysis

## Risk Summary

## Risk Register
    → canonical risk table

## Assumptions / Dependencies

## Monitoring Notes

## Open Questions

## Analysis Summary
```

---

## Canonical Risk Table

| Risk ID | Area / Feature | Risk Description | Trigger / Cause | Impact | Likelihood | Severity / Exposure | Mitigation / QA Focus | Traceability | Status |
|---|---|---|---|---|---|---|---|---|---|
| R-001 | <area> | <potential quality/business risk> | <supported cause or condition> | <business/quality impact> | High / Medium / Low / Not Rated | High / Medium / Low / Not Rated | <test/clarification/monitoring focus> | <REQ/AC/BR IDs> | Open / Monitored / Mitigated / Clarification-Dependent |

### Column Rules

| Column | Requirement |
|---|---|
| Risk ID | Stable unique identifier, e.g. `R-001`. |
| Area / Feature | Functional or quality area affected. |
| Risk Description | A potential failure or exposure, not a confirmed defect. |
| Trigger / Cause | Requirement condition, ambiguity, dependency, change, or plausible supported cause. |
| Impact | Consequence if the risk materializes. |
| Likelihood | Use the project/canonical rating only when evidence supports it; otherwise `Not Rated`. |
| Severity / Exposure | Relative priority or exposure; do not invent numeric formulas unless a defined model exists. |
| Mitigation / QA Focus | Practical test, review, clarification, or monitoring action. |
| Traceability | Requirement/rule/change references supporting the risk. |
| Status | Operational state of the risk item. |

---

## Writing Guidelines

- Focus on risks rather than confirmed issues.
- Distinguish facts, assumptions, and uncertainty.
- Prioritize according to available evidence; do not fabricate likelihood or severity.
- Keep one primary risk per row.
- Trace each material risk to the requirement, rule, change, or dependency that supports it.
- Use mitigation as QA focus, not as invented implementation guidance.
- Keep clarification-dependent risks visible until authoritative behavior is available.

---

## Expected Output

A completed risk analysis should:

- provide one scanable risk register;
- make prioritization and mitigation focus easy to compare;
- expose uncertainty and dependencies explicitly;
- support scenario/testcase prioritization and regression planning;
- remain traceable to authoritative project inputs.

---

## Related Templates

- `Requirement-Analysis.md`
- `Business-Rule.md`
- `Scenario.md`
- `TestCase.md`
- `Regression.md`
