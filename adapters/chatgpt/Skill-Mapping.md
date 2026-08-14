# ChatGPT Skill Mapping

| QA-AI Skill | ChatGPT Runtime Use |
|---|---|
| `requirement-analyzer` | Analyze raw requirements into structured requirement understanding |
| `business-rule-extractor` | Extract explicit/supported business rules |
| `risk-analyzer` | Produce structured QA risk analysis |
| `scenario-generator` | Generate structured test scenarios |
| `testcase-generator` | Generate executable test cases |
| `test-data-generator` | Define logical test-data requirements and datasets |
| `coverage-reviewer` | Review completeness, consistency, duplication, and traceability |
| `regression-impact` | Analyze authoritative change delta and regression scope |
| `bug-report-reviewer` | Review bug-report quality and actionability |
| `api-test-generator` | Produce API-specific test design and assertions |
| `sql-validation` | Produce QA-oriented SQL/database validation design |

## Mapping Rule

The Custom GPT routes to these capabilities through `Instructions.md`; it does not reimplement them. The corresponding `skills/<name>/README.md` remains the capability authority.
