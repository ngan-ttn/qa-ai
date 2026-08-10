# Prompt Standard

## Purpose

This document defines the standard for designing, organizing, and maintaining prompts used throughout the repository.

The objective is to create prompts that are clear, reusable, maintainable, and capable of producing consistent, high-quality outputs across different AI models.

---

## Scope

This standard applies to all prompts in the repository, including:

* System prompts
* Task prompts
* Prompt templates
* Prompt patterns
* AI workflows
* Multi-step prompt chains

---

## Prompt Principles

Every prompt SHOULD be:

* **Clear** — State the objective explicitly.
* **Specific** — Provide sufficient context and constraints.
* **Reusable** — Avoid unnecessary task-specific assumptions.
* **Maintainable** — Be easy to update as requirements evolve.
* **Consistent** — Follow a predictable structure.

---

## Prompt Structure

A prompt SHOULD be organized into logical sections.

Typical sections include:

1. Role
2. Context
3. Task
4. Constraints
5. Expected Output

Not every prompt requires every section, but the structure SHOULD remain intentional and easy to understand.

---

## Role

The role defines the perspective or expertise the AI should adopt.

Examples:

* QA Engineer
* Technical Writer
* Business Analyst
* Software Architect

The assigned role SHOULD align with the intended task.

---

## Context

Context provides the information necessary to perform the task.

Context MAY include:

* Background information
* Business rules
* Project constraints
* Existing documentation
* Input data

Provide only the context relevant to the requested task.

---

## Task

The task describes what the AI is expected to accomplish.

Tasks SHOULD:

* Use clear action verbs.
* Define a single primary objective.
* Avoid combining unrelated goals.

Examples:

* Analyze requirements.
* Generate test scenarios.
* Review documentation.
* Summarize technical content.

---

## Constraints

Constraints define the boundaries of the expected output.

Examples include:

* Output format
* Writing style
* Language
* Repository standards
* Excluded content

Constraints SHOULD be explicit and measurable whenever possible.

---

## Expected Output

The expected output SHOULD define:

* Output format
* Required sections
* Level of detail
* Organization

A clearly defined output format improves consistency and reduces ambiguity.

---

## Prompt Composition

Large tasks SHOULD be divided into smaller prompts whenever practical.

Each prompt SHOULD have a single primary responsibility.

Avoid creating prompts that attempt to perform unrelated tasks simultaneously.

---

## Reusability

Reusable prompts SHOULD:

* Minimize project-specific assumptions.
* Accept configurable inputs.
* Remain independent of implementation details.

Prefer parameterized prompts over duplicated prompts.

---

## Prompt Maintenance

Prompts SHOULD be reviewed whenever:

* Requirements change.
* Repository standards are updated.
* Output quality declines.
* Repeated prompt modifications become necessary.

Maintain prompts as living assets rather than one-time instructions.

---

## Anti-Patterns

Avoid prompts that:

* Mix multiple unrelated objectives.
* Contain conflicting instructions.
* Rely on undocumented assumptions.
* Specify unnecessary implementation details.
* Duplicate existing prompt logic.

---

## Quality Checklist

Before publishing a prompt, verify that it:

* Has a clearly defined objective.
* Provides sufficient context.
* Specifies meaningful constraints.
* Defines the expected output.
* Can be reused with minimal modification.
* Aligns with repository standards.

---

## Best Practices

* Design prompts around a single responsibility.
* Keep instructions explicit and unambiguous.
* Prefer reusable structures over one-off solutions.
* Maintain consistency across related prompts.
* Continuously refine prompts based on practical usage and feedback.
