# Workflows

## Overview

The `workflows` directory contains reusable QA task execution flows that guide the AI assistant in performing specific testing activities.

In this context, the AI assistant refers to any AI system using this skill repository to perform QA-related tasks.

Workflows define how QA knowledge and shared resources are applied together to complete a specific task and produce consistent QA outputs.

Examples of workflows:

* Requirement-based testcase generation
* Testcase quality review
* Regression impact analysis

---

## Purpose

The purpose of workflows is to provide a structured process for completing QA tasks.

Skills provide QA knowledge, and shared resources provide standards and reusable assets. However, a complete QA task requires a defined process to apply those resources effectively.

Workflows bridge this gap by defining:

* Task execution steps
* Required inputs
* Required QA knowledge
* Required resources
* Expected outputs
* Validation points

---

## Role in AI Skill Learning System

Within the AI Skill Learning System, each component has a specific responsibility:

```text
skills/

Provide QA knowledge

        |

        v

shared/

Provide standards and reusable resources

        |

        v

workflows/

Define QA task execution flows

        |

        v

QA Output
```

The workflow layer does not replace knowledge or standards.

It defines how existing knowledge and resources are combined and applied during a QA activity.

---

## Relationship With Other Components

Workflows work together with other components in the system.

| Component                 | Responsibility                                |
| ------------------------- | --------------------------------------------- |
| `skills/`                 | Provide QA knowledge and testing capabilities |
| `shared/standards/`       | Define QA principles and common rules         |
| `shared/templates/`       | Define output structures and formats          |
| `shared/checklists/`      | Define validation criteria                    |
| `shared/prompt-patterns/` | Provide reusable instruction patterns         |
| `workflows/`              | Define execution flows for specific QA tasks  |

Example:

```text
Requirement

    |

    v

Testcase Generation Workflow

    |

    +----------------+
    |                |
    v                v

Test Design Skill   Testcase Template

    |

    v

Generated Test Cases

    |

    v

Testcase Checklist Validation
```

---

## Workflow Concept

A workflow is a repeatable process for completing a specific QA task by applying relevant skills and shared resources.

A workflow defines:

### Input

Information required to start the workflow.

Examples:

* Requirement document
* User story
* Existing test cases
* Change request
* Test result information

---

### Process

The execution steps required to complete the task.

A workflow typically includes:

* Analyze input
* Identify required skills
* Apply relevant shared resources
* Perform QA activities
* Generate or update QA artifacts
* Validate results

---

### Output

The expected result produced by the workflow.

Examples:

* Test scenarios
* Test cases
* Review findings
* Regression analysis result

---

## Workflow Structure

Each workflow should be organized as:

```text
workflow-name/

└── README.md
```

Each workflow README should describe:

```md
## Purpose

## When To Use

## Input

## Workflow Steps

## Required Skills

## Required Resources

## Output

## Validation
```

The workflow documentation should explain how the workflow operates without duplicating detailed knowledge, templates, or checklist definitions.

---

## Available Workflows

Current workflows:

| Workflow                  | Purpose                                                  |
| ------------------------- | -------------------------------------------------------- |
| `testcase-generation`     | Generate test scenarios and test cases from requirements |
| `testcase-quality-review` | Review and improve existing test cases                   |
| `regression-analysis`     | Analyze change impact and define regression scope        |

Additional workflows can be added when new QA task capabilities are required.

---

## Adding New Workflow

New workflows should be added when a QA activity requires a defined and reusable execution flow.

A new workflow should:

* Have a clear purpose
* Define required inputs
* Define execution steps
* Identify required skills
* Identify required shared resources
* Define expected outputs
* Include validation criteria

A workflow should not:

* Store QA knowledge that belongs to `skills/`
* Define output formats that belong to `shared/templates/`
* Replace validation rules from `shared/checklists/`

New workflows should extend system capability while maintaining clear separation between knowledge, standards, and execution flow.
