"""Snapshot the current canonical feature baseline before a new source revision."""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REVISION_RE = re.compile(r"^REV-([0-9]{3,})$")


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def git_revision() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True, stderr=subprocess.DEVNULL
        ).strip()
    except Exception:
        return "unknown"


def next_revision(revision: str) -> str:
    match = REVISION_RE.fullmatch(revision)
    if not match:
        raise ValueError(f"invalid revision: {revision}")
    digits = match.group(1)
    return f"REV-{int(digits) + 1:0{len(digits)}d}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("feature_path")
    parser.add_argument(
        "--advance",
        action="store_true",
        help="after snapshot, advance current revision and mark prior-baseline artifacts stale",
    )
    args = parser.parse_args()

    feature_dir = Path(args.feature_path)
    if not feature_dir.is_absolute():
        feature_dir = ROOT / feature_dir
    metadata_path = feature_dir / "metadata.json"
    if not metadata_path.is_file():
        print(f"ERROR metadata not found: {metadata_path}")
        return 1

    data = json.loads(metadata_path.read_text(encoding="utf-8"))
    revision = data.get("current_revision")
    if not isinstance(revision, str) or not REVISION_RE.fullmatch(revision):
        print(f"ERROR invalid current_revision: {revision}")
        return 1

    target = feature_dir / "revisions" / revision
    if target.exists():
        print(f"ERROR revision snapshot already exists: {target}")
        return 1
    target.mkdir(parents=True, exist_ok=False)

    artifacts_dir = feature_dir / "artifacts"
    snapshot_artifacts = target / "artifacts"
    snapshot_artifacts.mkdir()
    if artifacts_dir.is_dir():
        for item in artifacts_dir.iterdir():
            if item.is_file():
                shutil.copy2(item, snapshot_artifacts / item.name)

    timestamp = now_iso()
    revision_metadata = {
        "schema_version": "1.0",
        "project_id": data.get("project_id"),
        "feature_id": data.get("feature_id"),
        "revision_id": revision,
        "snapshot_at": timestamp,
        "framework_revision": git_revision(),
        "sources": data.get("sources", []),
        "artifacts": data.get("artifacts", {}),
    }
    (target / "metadata.json").write_text(
        json.dumps(revision_metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"Snapshot created: {target.relative_to(ROOT)}")

    if args.advance:
        new_revision = next_revision(revision)
        data["current_revision"] = new_revision
        data["updated_at"] = timestamp
        data["framework_revision"] = git_revision()
        for artifact in data.get("artifacts", {}).values():
            if not isinstance(artifact, dict):
                continue
            if artifact.get("source_revision") == revision:
                artifact["freshness"] = "Stale"
                artifact["updated_at"] = timestamp
        metadata_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Advanced feature revision: {revision} -> {new_revision}")
        print("Artifacts registered against the prior source revision were marked Stale.")
    else:
        print("No current artifact/source state was modified. Use --advance to open the next revision.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
