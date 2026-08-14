# Claude Knowledge Mapping

Claude Code can read repository files directly, so the adapter does not copy the knowledge library.

## Resolution Order

Use only the relevant domain for the task:

- generic QA process and quality concepts → `shared/knowledge/qa/`
- test-design techniques → `shared/knowledge/testing-techniques/`
- API behavior/testing → `shared/knowledge/api/`
- database/SQL/persistence → `shared/knowledge/database/`
- reusable business/domain concepts → `shared/knowledge/domain/`

Catalogs are navigation/index sources; article content provides the detailed reusable knowledge.

Authoritative project context always overrides generic knowledge. Generic knowledge may suggest analysis dimensions but cannot establish project-specific facts.
