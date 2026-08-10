# Naming Standard

## Purpose

This document defines the naming conventions used throughout the repository.

Consistent naming improves readability, discoverability, maintainability, and collaboration. Every repository asset SHOULD follow these conventions unless a documented exception applies.

---

## Scope

This standard applies to all repository assets, including but not limited to:

* Directories
* Files
* Markdown documents
* Templates
* Checklists
* Prompt patterns
* Knowledge documents
* Workflows

---

## Naming Principles

All names SHOULD follow these principles:

* **Clear** — Clearly describe the purpose of the asset.
* **Consistent** — Use the same naming style across similar assets.
* **Concise** — Avoid unnecessary words or abbreviations.
* **Predictable** — Make names easy to locate and understand.
* **Scalable** — Support future growth without requiring renaming.

---

## General Rules

Names MUST:

* Use English.
* Be descriptive and meaningful.
* Avoid special characters unless required.
* Avoid version numbers in filenames.
* Avoid dates in filenames.
* Avoid temporary suffixes such as `new`, `latest`, or `final`.

Names SHOULD NOT:

* Use unclear abbreviations.
* Include implementation details.
* Repeat parent directory names unnecessarily.

---

## Directory Naming

Directory names SHOULD:

* Use lowercase.
* Use hyphens (`-`) to separate multiple words.
* Represent a single logical category.

### Examples

| Good              | Avoid            |
| ----------------- | ---------------- |
| `standards`       | `Standards`      |
| `prompt-patterns` | `PromptPatterns` |
| `test-data`       | `test_data`      |

---

## File Naming

Documentation files SHOULD:

* Use PascalCase.
* Represent a single topic.
* Match the document title whenever practical.

### Examples

| Good          | Avoid               |
| ------------- | ------------------- |
| `Metadata.md` | `metadata.md`       |
| `Naming.md`   | `NamingStandard.md` |
| `Prompt.md`   | `Prompt_Final.md`   |

---

## Template Naming

Template files SHOULD end with `Template`.

Examples:

```text
RequirementTemplate.md
TestCaseTemplate.md
BugReportTemplate.md
WorkflowTemplate.md
```

---

## Checklist Naming

Checklist files SHOULD end with `Checklist`.

Examples:

```text
CodeReviewChecklist.md
ReleaseChecklist.md
RegressionChecklist.md
```

---

## Prompt Naming

Prompt documents SHOULD describe the intended purpose rather than the AI model.

### Good

```text
RequirementAnalyzerPrompt.md
ScenarioGeneratorPrompt.md
TestCaseReviewerPrompt.md
```

### Avoid

```text
GPTPrompt.md
ClaudePrompt.md
AIPrompt.md
```

---

## Knowledge Document Naming

Knowledge documents SHOULD represent a single concept or topic.

Examples:

```text
APIAuthentication.md
RegressionTesting.md
RESTPrinciples.md
```

Avoid combining unrelated concepts into a single document.

---

## Workflow Naming

Workflow names SHOULD describe the business or operational process.

Examples:

```text
RequirementReview.md
TestCaseGeneration.md
BugVerification.md
ReleaseValidation.md
```

---

## Acronyms

Well-known acronyms MAY be used when they are widely understood.

Examples:

* API
* UI
* UX
* QA
* CI
* CD
* SQL

Avoid introducing project-specific abbreviations without documentation.

---

## Words to Avoid

Avoid vague or temporary names such as:

```text
New
Latest
Final
Copy
Backup
Temp
Test
Misc
```

These names become misleading over time.

---

## Examples

| Asset     | Recommended Name             |
| --------- | ---------------------------- |
| Standard  | `Documentation.md`           |
| Template  | `BugReportTemplate.md`       |
| Checklist | `SmokeTestChecklist.md`      |
| Prompt    | `ScenarioGeneratorPrompt.md` |
| Workflow  | `RequirementReview.md`       |
| Knowledge | `RESTAPI.md`                 |

---

## Best Practices

* Prefer descriptive names over shortened names.
* Use consistent terminology throughout the repository.
* Keep names stable after publication.
* Rename assets only when the current name no longer reflects their purpose.
* Apply the same naming style to similar asset types.
