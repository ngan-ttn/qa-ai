"""Update a registered workspace artifact lifecycle state with transition validation."""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALID_TRANSITIONS = {
    "Draft": {"Review"},
    "Review": {"Draft", "Approved"},
    "Approved": {"Superseded"},
    "Superseded": {"Archived"},
    "Archived": set(),
}


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("feature_path")
    parser.add_argument("artifact_key")
    parser.add_argument("new_status", choices=tuple(VALID_TRANSITIONS))
    parser.add_argument(
        "--approved-by",
        help="required when promoting Review -> Approved; records explicit human/operator approval evidence",
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
    artifacts = data.get("artifacts", {})
    artifact = artifacts.get(args.artifact_key)
    if not isinstance(artifact, dict):
        print(f"ERROR unknown artifact key: {args.artifact_key}")
        return 1

    current = artifact.get("status")
    allowed = VALID_TRANSITIONS.get(current)
    if allowed is None:
        print(f"ERROR invalid current artifact status: {current}")
        return 1
    if args.new_status not in allowed:
        print(f"ERROR invalid lifecycle transition: {current} -> {args.new_status}")
        return 1
    if args.new_status == "Approved" and not args.approved_by:
        print("ERROR Review -> Approved requires --approved-by <human/operator evidence>")
        return 1

    artifact_path = feature_dir / artifact.get("path", "")
    if args.new_status in {"Review", "Approved", "Superseded", "Archived"} and not artifact_path.is_file():
        print(f"ERROR artifact file must exist before transition to {args.new_status}: {artifact_path}")
        return 1

    timestamp = now_iso()
    artifact["status"] = args.new_status
    artifact["updated_at"] = timestamp
    if args.new_status == "Approved":
        artifact["approval"] = {
            "approved_by": args.approved_by,
            "approved_at": timestamp,
        }
    data["updated_at"] = timestamp
    metadata_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Updated artifact state: {args.artifact_key}: {current} -> {args.new_status}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
