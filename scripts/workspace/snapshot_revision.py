"""Snapshot the current canonical feature baseline before a new source revision."""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def git_revision() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True, stderr=subprocess.DEVNULL
        ).strip()
    except Exception:
        return "unknown"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("feature_path")
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
    if not isinstance(revision, str) or not revision.startswith("REV-"):
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

    revision_metadata = {
        "schema_version": "1.0",
        "project_id": data.get("project_id"),
        "feature_id": data.get("feature_id"),
        "revision_id": revision,
        "snapshot_at": now_iso(),
        "framework_revision": git_revision(),
        "sources": data.get("sources", []),
        "artifacts": data.get("artifacts", {}),
    }
    (target / "metadata.json").write_text(
        json.dumps(revision_metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"Snapshot created: {target.relative_to(ROOT)}")
    print("No current artifact/source state was modified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
