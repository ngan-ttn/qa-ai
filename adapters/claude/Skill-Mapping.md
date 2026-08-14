# Claude Skill Mapping

Claude Code resolves QA-AI capabilities directly from `skills/<skill>/README.md`.

| Objective | Canonical Skill |
|---|---|
| Requirement analysis | `requirement-analyzer` |
| Business-rule extraction | `business-rule-extractor` |
| QA risk analysis | `risk-analyzer` |
| Test scenarios | `scenario-generator` |
| Executable test cases | `testcase-generator` |
| Test data | `test-data-generator` |
| Coverage review | `coverage-reviewer` |
| Regression impact | `regression-impact` |
| Bug-report review | `bug-report-reviewer` |
| API test design | `api-test-generator` |
| SQL/database validation | `sql-validation` |

The adapter provides routing only; the skill README owns the contract.
