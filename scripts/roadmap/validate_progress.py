"""Validate roadmap-status.json lifecycle, aggregate counts, and closure consistency."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.utils.file_utils import read_json

ALLOWED = ["Planned", "In Progress", "Review", "Completed", "Frozen"]
DONE = {"Completed", "Frozen"}


def _aggregate_components(components: dict[str, object]) -> tuple[int, int] | None:
    """Return completed/total when component shape supports deterministic aggregation."""
    if not components:
        return None
    values = [value for value in components.values() if isinstance(value, dict)]
    if len(values) != len(components):
        return None
    if all(isinstance(value.get("expected"), int) and isinstance(value.get("completed"), int) for value in values):
        return (
            sum(int(value["completed"]) for value in values),
            sum(int(value["expected"]) for value in values),
        )
    return (sum(1 for value in values if value.get("status") in DONE), len(values))


def validate(registry: dict[str, object]) -> list[str]:
    errors: list[str] = []
    lifecycle = registry.get("status_lifecycle")
    if lifecycle is not None and lifecycle != ALLOWED:
        errors.append("status_lifecycle does not match canonical lifecycle")
    phases = registry.get("phases")
    if not isinstance(phases, dict):
        return errors + ["phases must be an object"]

    for phase_id, phase in phases.items():
        if not isinstance(phase, dict):
            errors.append(f"phase {phase_id} must be an object")
            continue
        if not isinstance(phase.get("name"), str) or not str(phase.get("name", "")).strip():
            errors.append(f"phase {phase_id} requires a non-empty name")
        status = phase.get("status")
        if status not in ALLOWED:
            errors.append(f"phase {phase_id} has invalid status: {status}")

        progress = phase.get("progress")
        completed = total = None
        if progress is not None and not isinstance(progress, dict):
            errors.append(f"phase {phase_id} progress must be an object")
        elif isinstance(progress, dict):
            completed = progress.get("completed")
            total = progress.get("total")
            if not isinstance(completed, int) or not isinstance(total, int) or completed < 0 or total < 0:
                errors.append(f"phase {phase_id} progress counts must be non-negative integers")
            elif completed > total:
                errors.append(f"phase {phase_id} completed count exceeds total")
            if not isinstance(progress.get("unit"), str) or not str(progress.get("unit", "")).strip():
                errors.append(f"phase {phase_id} progress requires a non-empty unit")

        components = phase.get("components", {})
        if components is not None and not isinstance(components, dict):
            errors.append(f"phase {phase_id} components must be an object")
            continue
        component_statuses: list[str] = []
        for name, component in (components or {}).items():
            if not isinstance(component, dict):
                errors.append(f"phase {phase_id} component {name} must be an object")
                continue
            component_status = component.get("status")
            if component_status not in ALLOWED:
                errors.append(f"phase {phase_id} component {name} has invalid status: {component_status}")
            else:
                component_statuses.append(component_status)
            if "expected" in component or "completed" in component:
                expected = component.get("expected")
                done = component.get("completed")
                if not isinstance(expected, int) or not isinstance(done, int) or expected < 0 or done < 0 or done > expected:
                    errors.append(f"phase {phase_id} component {name} has invalid expected/completed counts")

        if isinstance(progress, dict) and isinstance(components, dict) and components:
            aggregate = _aggregate_components(components)
            if aggregate is not None and isinstance(completed, int) and isinstance(total, int):
                aggregate_completed, aggregate_total = aggregate
                if (completed, total) != (aggregate_completed, aggregate_total):
                    errors.append(
                        f"phase {phase_id} progress {completed}/{total} does not match component aggregate "
                        f"{aggregate_completed}/{aggregate_total}"
                    )

        if status == "Frozen" and any(item != "Frozen" for item in component_statuses):
            errors.append(f"phase {phase_id} is Frozen but not all tracked components are Frozen")
        if status == "Completed" and any(item not in DONE for item in component_statuses):
            errors.append(f"phase {phase_id} is Completed but tracked components remain incomplete")
        if status in DONE and isinstance(completed, int) and isinstance(total, int) and completed != total:
            errors.append(f"phase {phase_id} is {status} but progress is not complete")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", default="roadmap-status.json")
    args = parser.parse_args()
    errors = validate(read_json(args.registry))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"FAIL: {len(errors)} roadmap progress issue(s)")
        return 1
    print("PASS: roadmap progress registry is internally consistent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
