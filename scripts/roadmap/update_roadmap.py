"""Render registry-backed roadmap status and summary into the human-readable roadmap."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.roadmap.validate_progress import validate
from scripts.utils.file_utils import read_json, read_text, write_text

START = "<!-- ROADMAP_STATUS:START -->"
END = "<!-- ROADMAP_STATUS:END -->"
REGION_RE = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
OVERVIEW_TABLE_RE = re.compile(
    r"\| Phase \| Name \| Status \|\n"
    r"\|---\|---\|---\|\n"
    r"(?:\|[^\n]+\|\n?)+",
    re.M,
)
SUMMARY_RE = re.compile(
    r"Current baseline and active phase:\n\n```text\n.*?\n```",
    re.S,
)


def render(registry: dict[str, object]) -> str:
    phases = registry.get("phases", {})
    lines = [START, "", "| Phase | Name | Status | Progress |", "|---|---|---|---|"]
    for phase_id in sorted(phases, key=lambda value: int(value)):
        phase = phases[phase_id]
        progress = phase.get("progress") if isinstance(phase, dict) else None
        progress_text = "—"
        if isinstance(progress, dict) and isinstance(progress.get("completed"), int) and isinstance(progress.get("total"), int):
            progress_text = f"{progress['completed']}/{progress['total']} {progress.get('unit', '')}".strip()
        lines.append(f"| Phase {phase_id} | {phase.get('name', '')} | {phase.get('status', '')} | {progress_text} |")
    lines.extend(["", END])
    return "\n".join(lines)


def _latest_frozen(phases: dict[str, object]) -> tuple[str, dict[str, object]] | None:
    frozen: list[tuple[int, str, dict[str, object]]] = []
    for phase_id, phase in phases.items():
        if isinstance(phase, dict) and phase.get("status") == "Frozen":
            frozen.append((int(phase_id), phase_id, phase))
    if not frozen:
        return None
    _, phase_id, phase = max(frozen)
    return phase_id, phase


def _active_phases(phases: dict[str, object]) -> list[tuple[str, dict[str, object]]]:
    active_statuses = {"Planned", "In Progress", "Review"}
    result: list[tuple[str, dict[str, object]]] = []
    for phase_id in sorted(phases, key=lambda value: int(value)):
        phase = phases[phase_id]
        if isinstance(phase, dict) and phase.get("status") in active_statuses:
            result.append((phase_id, phase))
    return result


def render_summary(registry: dict[str, object]) -> str:
    phases = registry.get("phases", {})
    if not isinstance(phases, dict):
        phases = {}

    latest = _latest_frozen(phases)
    latest_text = "None"
    if latest:
        phase_id, phase = latest
        latest_text = f"Phase {phase_id} — {phase.get('name', '')}"

    phase_4 = phases.get("4", {}) if isinstance(phases.get("4", {}), dict) else {}
    phase_10 = phases.get("10", {}) if isinstance(phases.get("10", {}), dict) else {}
    phase_12 = phases.get("12", {}) if isinstance(phases.get("12", {}), dict) else {}
    phase_13 = phases.get("13", {}) if isinstance(phases.get("13", {}), dict) else {}

    foundation = phase_4.get("progress", {}) if isinstance(phase_4.get("progress", {}), dict) else {}
    expansion = phases.get("11", {}) if isinstance(phases.get("11", {}), dict) else {}
    library = expansion.get("library_baseline", {}) if isinstance(expansion.get("library_baseline", {}), dict) else {}
    knowledge = phase_10.get("progress", {}) if isinstance(phase_10.get("progress", {}), dict) else {}
    scripts = phase_12.get("script_baseline", {}) if isinstance(phase_12.get("script_baseline", {}), dict) else {}
    adapters = phase_13.get("progress", {}) if isinstance(phase_13.get("progress", {}), dict) else {}

    skill_total = library.get("total") or foundation.get("total") or "—"
    knowledge_completed = knowledge.get("completed", "—")
    knowledge_total = knowledge.get("total", "—")
    script_count = scripts.get("scripts", "—")
    script_groups = scripts.get("groups", "—")
    adapter_completed = adapters.get("completed", "—")
    adapter_total = adapters.get("total", "—")

    active = _active_phases(phases)
    if not active:
        active_text = "None — next phase not yet opened"
    else:
        active_text = "; ".join(
            f"Phase {phase_id} — {phase.get('name', '')} ({phase.get('status', '')})"
            for phase_id, phase in active
        )

    lines = [
        "Current baseline and active phase:",
        "",
        "```text",
        f"Latest Frozen Phase: {latest_text}",
        f"Canonical Skill Library: {skill_total}/{skill_total}" if skill_total != "—" else "Canonical Skill Library: —",
        f"Knowledge Baseline: {knowledge_completed}/{knowledge_total}",
        f"Canonical Scripts: {script_count} / {script_groups} groups",
        f"Platform Adapters: ChatGPT + Claude + Cursor ({adapter_completed}/{adapter_total} Frozen)",
        f"Active Phase: {active_text}",
        "```",
    ]
    return "\n".join(lines)


def _bootstrap_region(current: str) -> str:
    match = OVERVIEW_TABLE_RE.search(current)
    if not match:
        raise ValueError("Cannot bootstrap roadmap status region: implementation overview table not found")
    wrapped = f"{START}\n\n{match.group(0).rstrip()}\n\n{END}"
    return current[:match.start()] + wrapped + current[match.end():]


def update(registry_path: str, roadmap_path: str, *, check: bool = False) -> bool:
    registry = read_json(registry_path)
    errors = validate(registry)
    if errors:
        raise ValueError("Invalid roadmap registry: " + "; ".join(errors))

    original = read_text(roadmap_path)
    current = original
    if START not in current or END not in current:
        if check:
            return True
        current = _bootstrap_region(current)

    desired = REGION_RE.sub(render(registry), current, count=1)
    summary = render_summary(registry)
    if SUMMARY_RE.search(desired):
        desired = SUMMARY_RE.sub(summary, desired, count=1)
    else:
        raise ValueError("Cannot synchronize roadmap summary: summary block not found")

    changed = desired != original
    if changed and not check:
        write_text(roadmap_path, desired)
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", default="roadmap-status.json")
    parser.add_argument("--roadmap", default="docs/11-Roadmap.md")
    parser.add_argument("--check", action="store_true", help="Fail if roadmap generated status or summary is missing/stale")
    args = parser.parse_args()
    changed = update(args.registry, args.roadmap, check=args.check)
    if args.check:
        print("FAIL: roadmap generated status/summary is missing/stale" if changed else "PASS: roadmap generated status and summary are synchronized")
        return 1 if changed else 0
    print("Updated roadmap generated status/summary" if changed else "Roadmap generated status/summary already synchronized")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
