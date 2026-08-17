"""Validate the canonical Phase 13 platform-adapter baseline deterministically."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
ADAPTERS = ROOT / "adapters"

PLATFORMS = ("chatgpt", "claude", "cursor")
SKILLS = (
    "requirement-analyzer",
    "business-rule-extractor",
    "risk-analyzer",
    "scenario-generator",
    "testcase-generator",
    "test-data-generator",
    "coverage-reviewer",
    "regression-impact",
    "bug-report-reviewer",
    "api-test-generator",
    "sql-validation",
)
WORKFLOWS = ("testcase-generation", "testcase-quality-review", "regression-analysis")
EXPECTED_CHATGPT_BUNDLE_COUNT = 14

REQUIRED_FILES: dict[str, tuple[str, ...]] = {
    "chatgpt": (
        "README.md",
        "Instructions.md",
        "Knowledge-Manifest.md",
        "Skill-Mapping.md",
        "Workflow-Mapping.md",
        "Usage.md",
        "build_knowledge_bundles.py",
    ),
    "claude": (
        "README.md",
        "CLAUDE.md",
        "Skill-Mapping.md",
        "Workflow-Mapping.md",
        "Knowledge-Mapping.md",
        "Usage.md",
        "install.py",
    ),
    "cursor": (
        "README.md",
        "Skill-Mapping.md",
        "Workflow-Mapping.md",
        "Knowledge-Mapping.md",
        "Usage.md",
        "package/.cursor/rules/qa-ai-core.mdc",
        "package/.cursor/rules/qa-ai-testing.mdc",
        "package/.cursor/commands/analyze-requirement.md",
        "package/.cursor/commands/generate-testcases.md",
        "package/.cursor/commands/review-testcases.md",
        "package/.cursor/commands/analyze-regression.md",
    ),
}


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def validate() -> list[str]:
    errors: list[str] = []

    for common in ("README.md", "Integration-Contract.md"):
        path = ADAPTERS / common
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"missing/non-content adapter file: adapters/{common}")

    for platform in PLATFORMS:
        base = ADAPTERS / platform
        for rel in REQUIRED_FILES[platform]:
            path = base / rel
            if not path.is_file() or path.stat().st_size == 0:
                errors.append(f"missing/non-content {platform} file: adapters/{platform}/{rel}")

        skill_mapping = base / "Skill-Mapping.md"
        if skill_mapping.is_file():
            text = _read(skill_mapping)
            for skill in SKILLS:
                if f"`{skill}`" not in text:
                    errors.append(f"{platform} skill mapping missing canonical skill: {skill}")

        workflow_mapping = base / "Workflow-Mapping.md"
        if workflow_mapping.is_file():
            text = _read(workflow_mapping)
            for workflow in WORKFLOWS:
                if workflow not in text:
                    errors.append(f"{platform} workflow mapping missing canonical workflow: {workflow}")

    # Claude Code loads project instructions from repo-root CLAUDE.md. The adapter
    # copy is the source; the root file is the installed runtime representation.
    claude_source = ADAPTERS / "claude" / "CLAUDE.md"
    claude_root = ROOT / "CLAUDE.md"
    if not claude_root.is_file() or claude_root.stat().st_size == 0:
        errors.append("Claude Code project instruction missing/non-content: CLAUDE.md")
    elif claude_source.is_file() and _read(claude_root) != _read(claude_source):
        errors.append(
            "Claude Code project instruction is stale: CLAUDE.md differs from "
            "adapters/claude/CLAUDE.md; run python adapters/claude/install.py"
        )

    for skill in SKILLS:
        path = ROOT / "skills" / skill / "README.md"
        if not path.is_file():
            errors.append(f"canonical mapped skill missing: skills/{skill}/README.md")

    for workflow in WORKFLOWS:
        path = ROOT / "workflows" / workflow / "README.md"
        if not path.is_file():
            errors.append(f"canonical mapped workflow missing: workflows/{workflow}/README.md")

    manifest_path = ROOT / "manifest.json"
    if not manifest_path.is_file():
        errors.append("manifest.json missing")
    else:
        manifest = json.loads(_read(manifest_path))
        if manifest.get("components", {}).get("adapters") != "adapters/":
            errors.append("manifest.json does not register adapters/")

    registry_path = ROOT / "roadmap-status.json"
    if not registry_path.is_file():
        errors.append("roadmap-status.json missing")
    else:
        registry = json.loads(_read(registry_path))
        phase = registry.get("phases", {}).get("13", {})
        components = phase.get("components", {}) if isinstance(phase, dict) else {}
        if set(components) != set(PLATFORMS):
            errors.append("Phase 13 registry components must be exactly: chatgpt, claude, cursor")
        progress = phase.get("progress", {}) if isinstance(phase, dict) else {}
        if progress.get("total") != 3 or progress.get("unit") != "platform_adapters":
            errors.append("Phase 13 registry progress contract must be total=3 unit=platform_adapters")

    try:
        from adapters.chatgpt.build_knowledge_bundles import BUNDLES
    except Exception as exc:  # pragma: no cover - diagnostic path
        errors.append(f"cannot import ChatGPT bundle builder: {exc}")
    else:
        if len(BUNDLES) != EXPECTED_CHATGPT_BUNDLE_COUNT:
            errors.append(
                "ChatGPT canonical upload bundle count must be "
                f"{EXPECTED_CHATGPT_BUNDLE_COUNT}, got {len(BUNDLES)}"
            )
        if len(BUNDLES) > 20:
            errors.append("ChatGPT Knowledge package exceeds platform 20-file limit")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR {error}")
        print(f"Phase 13 adapter validation failed; issues={len(errors)}")
        return 1
    print(
        "PASS Phase 13 adapters: "
        f"platforms=3 skills=11 workflows=3 chatgpt_bundles={EXPECTED_CHATGPT_BUNDLE_COUNT}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
