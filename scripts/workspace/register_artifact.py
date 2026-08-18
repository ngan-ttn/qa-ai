"""Register/update artifact provenance, freshness, and dependency metadata for a feature workspace."""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALID_FRESHNESS = {"Current", "Stale", "Unknown"}
VALID_RELATIONSHIPS = {"required", "supporting", "conditional"}


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def parse_dependency(raw: str) -> dict:
    # Format: relationship,target,target_revision(optional)
    parts = [part.strip() for part in raw.split(",")]
    if len(parts) not in {2, 3}:
        raise argparse.ArgumentTypeError(
            "dependency must be relationship,target[,target_revision], e.g. required,artifact:test-scenarios,ART-001"
        )
    relationship, target = parts[0], parts[1]
    if relationship not in VALID_RELATIONSHIPS:
        raise argparse.ArgumentTypeError(f"invalid dependency relationship: {relationship}")
    if not (target.startswith("artifact:") or target.startswith("source:")):
        raise argparse.ArgumentTypeError("dependency target must use artifact:<key> or source:<id>")
    dep = {"relationship": relationship, "target": target}
    if len(parts) == 3 and parts[2]:
        dep["target_revision"] = parts[2]
    return dep


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("feature_path")
    parser.add_argument("artifact_key")
    parser.add_argument("--generated-by", required=True, help="platform/runtime provenance, e.g. cursor, chatgpt, claude")
    parser.add_argument("--freshness", choices=tuple(sorted(VALID_FRESHNESS)), default="Current")
    parser.add_argument("--dependency", action="append", type=parse_dependency, default=[])
    parser.add_argument("--replace-dependencies", action="store_true")
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
    artifact = artifacts.get(args.artifact_key) if isinstance(artifacts, dict) else None
    if not isinstance(artifact, dict):
        print(f"ERROR unknown artifact key: {args.artifact_key}")
        return 1

    artifact_path = feature_dir / artifact.get("path", "")
    if not artifact_path.is_file():
        print(f"ERROR artifact file does not exist: {artifact_path}")
        return 1

    sources = data.get("sources", [])
    source_ids = {s.get("source_id") for s in sources if isinstance(s, dict)}
    artifact_keys = set(artifacts)
    for dep in args.dependency:
        target = dep["target"]
        if target.startswith("source:") and target.split(":", 1)[1] not in source_ids:
            print(f"ERROR dependency references unknown source: {target}")
            return 1
        if target.startswith("artifact:") and target.split(":", 1)[1] not in artifact_keys:
            print(f"ERROR dependency references unknown artifact: {target}")
            return 1

    timestamp = now_iso()
    artifact["generated_by"] = args.generated_by
    artifact["freshness"] = args.freshness
    artifact["source_revision"] = data.get("current_revision")
    artifact["updated_at"] = timestamp
    if args.replace_dependencies:
        artifact["dependencies"] = args.dependency
    elif args.dependency:
        existing = artifact.setdefault("dependencies", [])
        for dep in args.dependency:
            if dep not in existing:
                existing.append(dep)
    data["updated_at"] = timestamp
    metadata_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Registered artifact metadata: {args.artifact_key}")
    print(f"Freshness: {artifact['freshness']}; generated_by: {artifact['generated_by']}")
    print(f"Dependencies: {len(artifact.get('dependencies', []))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
