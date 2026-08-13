"""Validate roadmap-status.json lifecycle, counts, and freeze consistency."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.utils.file_utils import read_json

ALLOWED = ["Planned", "In Progress", "Review", "Completed", "Frozen"]


def validate(registry: dict[str, object]) -> list[str]:
    errors: list[str] = []
    phases = registry.get("phases")
    if not isinstance(phases, dict):
        return ["phases must be an object"]
    for phase_id, phase in phases.items():
        if not isinstance(phase, dict):
            errors.append(f"phase {phase_id} must be an object")
            continue
        status = phase.get("status")
        if status not in ALLOWED:
            errors.append(f"phase {phase_id} has invalid status: {status}")
        progress = phase.get("progress")
        if isinstance(progress, dict):
            completed = progress.get("completed")
            total = progress.get("total")
            if not isinstance(completed, int) or not isinstance(total, int) or completed < 0 or total < 0:
                errors.append(f"phase {phase_id} progress counts must be non-negative integers")
            elif completed > total:
                errors.append(f"phase {phase_id} completed count exceeds total")
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
        if status == "Frozen" and any(item != "Frozen" for item in component_statuses):
            errors.append(f"phase {phase_id} is Frozen but not all tracked components are Frozen")
        if status == "Completed" and any(item not in {"Completed", "Frozen"} for item in component_statuses):
            errors.append(f"phase {phase_id} is Completed but tracked components remain incomplete")
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
