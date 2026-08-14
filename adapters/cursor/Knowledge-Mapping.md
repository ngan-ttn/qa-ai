# Cursor Knowledge Mapping

Cursor can read repository content directly, so the adapter references canonical sources instead of duplicating knowledge.

## Domain Routing

- QA lifecycle/process/quality → `shared/knowledge/qa/`
- test-design techniques → `shared/knowledge/testing-techniques/`
- API-specific knowledge → `shared/knowledge/api/`
- database/SQL/persistence → `shared/knowledge/database/`
- reusable business/domain concepts → `shared/knowledge/domain/`

## Context Rule

Load only the knowledge relevant to the current task. Prefer catalogs for navigation and the matching article for detailed reasoning. Authoritative project sources override generic QA-AI knowledge whenever they differ.
