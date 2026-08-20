"""Run fail-closed QA-AI release readiness validation and write revision-bound evidence."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def run(name: str, args: list[str]) -> dict:
    process = subprocess.run([sys.executable, *args], cwd=ROOT, text=True, capture_output=True)
    output = (process.stdout + process.stderr).strip()
    print(output)
    print(f"{name}: {'PASS' if process.returncode == 0 else 'FAIL'}")
    return {
        "name": name,
        "status": "PASS" if process.returncode == 0 else "FAIL",
        "command": "python " + " ".join(args),
        "exit_code": process.returncode,
        "output": output[-4000:],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", required=True)
    parser.add_argument("--revision", required=True)
    parser.add_argument("--execution", required=True)
    parser.add_argument("--output", type=Path, default=ROOT / "release/validation-report.json")
    args = parser.parse_args()

    manifest = json.loads((ROOT / "release/manifest.json").read_text(encoding="utf-8"))
    revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    manifest_revision = manifest.get("repository_revision")
    if manifest_revision != revision:
        print(
            "ERROR: release manifest is stale for the revision being validated: "
            f"manifest={manifest_revision} head={revision}"
        )
        print("Release Readiness: FAIL")
        return 1

    gates = [
        ("manifest", ["scripts/release/validate_manifest.py"]),
        ("structure", ["scripts/validation/validate_structure.py"]),
        ("links", ["scripts/validation/validate_links.py"]),
        ("metadata", ["scripts/validation/validate_metadata.py"]),
        ("outputs", ["scripts/validation/validate_outputs.py"]),
        ("adapters", ["adapters/validate_adapters.py"]),
        ("roadmap", ["scripts/roadmap/validate_progress.py"]),
        ("workspace", ["scripts/workspace/validate_workspace.py", args.workspace]),
        (
            "change-intelligence",
            ["scripts/change_intelligence/validate_change_intelligence.py", args.workspace, "--revision", args.revision],
        ),
        ("execution", ["scripts/execution/validate_execution.py", args.execution]),
    ]
    results = [run(name, command) for name, command in gates]
    overall = "PASS" if all(item["status"] == "PASS" for item in results) else "FAIL"
    report = {
        "schema_version": "1.0",
        "release_id": manifest["release_id"],
        "repository_revision": revision,
        "validated_at": datetime.now(timezone.utc).isoformat(),
        "validators": results,
        "overall": overall,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"Release Readiness: {overall}")
    return 0 if overall == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
