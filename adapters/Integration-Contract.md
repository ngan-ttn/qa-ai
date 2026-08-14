# Adapter Integration Contract

## Purpose

Define how platform adapters consume the frozen QA-AI core without creating a second copy of QA semantics.

## Canonical Core

The authoritative QA-AI core remains:

```text
README.md / FRAMEWORK.md
skills/
workflows/
shared/
datasets/
scripts/
```

Adapter files translate this core into platform-native loading and invocation mechanisms. They do not become an independent source of QA behavior.

## Baseline Runtime Topology

Phase 13 validates three platform integrations against the QA-AI repository itself.

```text
Authoritative project input
        ↓
QA-AI repository core
        ↓
adapters/<platform>/
        ↓
Platform runtime
```

Project requirements may be pasted into the runtime, attached/uploaded where the platform supports it, or placed in files accessible to the runtime. They remain higher-authority input than reusable QA-AI knowledge.

## Repository-Root Assumption

Claude and Cursor package files contain repository-relative references such as `skills/`, `workflows/`, `shared/`, and `scripts/`.

Therefore the Phase 13 baseline assumes those platform packages are installed into the **QA-AI repository root**.

Copying only the adapter files into an unrelated repository would leave canonical references unresolved and is not a valid installation.

A future consumer-repository packaging mode may vendor, mount, submodule, or otherwise expose the QA-AI core under a stable path, but that mode must define and validate its own path contract before it is treated as supported.

## Platform Loading Models

### ChatGPT

ChatGPT does not read the repository directly in the Custom GPT baseline. Canonical sources are transformed into a bounded set of text-forward Knowledge bundles, while runtime behavior is configured in Custom GPT Instructions.

### Claude Code

The adapter instruction file is installed as repository-root `CLAUDE.md`. Repository-relative imports/references then resolve against the QA-AI repository. Claude should load only the specific owning skill/workflow and relevant supporting sources for the current task.

### Cursor

The `.cursor/` package is copied into the QA-AI repository root. Project Rules and Commands then reference canonical repository paths directly.

## Source Priority

All adapters preserve this priority:

1. authoritative project requirement and project context;
2. applicable canonical workflow;
3. owning canonical skill;
4. applicable shared standards/templates/checklists/knowledge;
5. platform adapter guidance;
6. generic model knowledge when it does not invent project behavior.

## Installation Quality Gate

An adapter is eligible for `Completed` only when:

- its native package files are present;
- all canonical path references resolve under the supported topology;
- all 11 canonical skills remain routable;
- all 3 canonical workflows remain routable;
- project input remains authoritative over reusable knowledge;
- missing project information remains explicit;
- adapter instructions do not redefine core QA semantics;
- platform-specific limitations are documented;
- a platform-appropriate smoke validation has passed.

`Frozen` additionally requires cross-platform review and roadmap synchronization.
