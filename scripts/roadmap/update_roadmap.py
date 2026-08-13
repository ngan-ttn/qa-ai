"""Render registry-backed roadmap status into a generated roadmap status region."""
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
    current = read_text(roadmap_path)
    if START not in current or END not in current:
        if check:
            return True
        current = _bootstrap_region(current)
    desired = REGION_RE.sub(render(registry), current, count=1)
    changed = desired != read_text(roadmap_path)
    if changed and not check:
        write_text(roadmap_path, desired)
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", default="roadmap-status.json")
    parser.add_argument("--roadmap", default="docs/11-Roadmap.md")
    parser.add_argument("--check", action="store_true", help="Fail if roadmap generated region is missing or stale")
    args = parser.parse_args()
    changed = update(args.registry, args.roadmap, check=args.check)
    if args.check:
        print("FAIL: roadmap generated status is missing/stale" if changed else "PASS: roadmap generated status is synchronized")
        return 1 if changed else 0
    print("Updated roadmap generated status" if changed else "Roadmap generated status already synchronized")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
