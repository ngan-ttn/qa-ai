"""Collect repository evidence for tracked roadmap components without inferring completion."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.utils.file_utils import read_json, write_json


def evidence_for_component(name: str) -> dict[str, object]:
    candidates = [
        ROOT / "skills" / name / "README.md",
        ROOT / "shared" / "knowledge" / name,
        ROOT / "scripts" / name,
        ROOT / name,
    ]
    for path in candidates:
        if path.exists():
            if path.is_dir():
                files = [p for p in path.rglob("*") if p.is_file()]
                return {
                    "path": path.relative_to(ROOT).as_posix(),
                    "exists": True,
                    "file_count": len(files),
                    "nonempty_file_count": sum(p.stat().st_size > 0 for p in files),
                }
            return {
                "path": path.relative_to(ROOT).as_posix(),
                "exists": True,
                "bytes": path.stat().st_size,
            }
    return {"path": None, "exists": False}


def collect(registry_path: str = "roadmap-status.json") -> dict[str, object]:
    registry = read_json(registry_path)
    phases_out: dict[str, object] = {}
    for phase_id, phase in registry.get("phases", {}).items():
        components = phase.get("components", {}) if isinstance(phase, dict) else {}
        phases_out[str(phase_id)] = {
            "declared_status": phase.get("status") if isinstance(phase, dict) else None,
            "components": {
                name: {
                    "declared_status": value.get("status") if isinstance(value, dict) else None,
                    "evidence": evidence_for_component(name),
                }
                for name, value in components.items()
            },
        }
    return {"registry": registry_path, "phases": phases_out}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", default="roadmap-status.json")
    parser.add_argument("--output", default="output/roadmap-evidence.json")
    args = parser.parse_args()
    data = collect(args.registry)
    write_json(args.output, data)
    count = sum(len(p["components"]) for p in data["phases"].values())
    print(f"Collected evidence for {count} tracked component(s) -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
