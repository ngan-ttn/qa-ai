"""Create deterministic revision change-set evidence from snapshot or working revision state."""
from __future__ import annotations
import argparse, hashlib, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REV = re.compile(r"^REV-[0-9]{3,}$")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def inventory_from_metadata(feature: Path, metadata: dict, artifact_root: Path, rev: str) -> dict:
    out = {}
    for key, artifact in metadata.get("artifacts", {}).items():
        if not isinstance(artifact, dict):
            continue
        name = Path(artifact.get("path", "")).name
        path = artifact_root / name
        out[f"artifact:{key}"] = {
            "checksum": digest(path) if path.is_file() else None,
            "path": str(path.relative_to(feature)).replace("\\", "/"),
            "revision": artifact.get("revision"),
        }
    for source in metadata.get("sources", []):
        if isinstance(source, dict) and source.get("source_id"):
            out[f"source:{source['source_id']}"] = {
                "checksum": source.get("checksum"),
                "path": source.get("path"),
                "revision": source.get("revision") or rev,
            }
    return out


def inventory(feature: Path, rev: str) -> dict:
    snapshot = feature / "revisions" / rev
    snapshot_meta = snapshot / "metadata.json"
    if snapshot_meta.is_file():
        return inventory_from_metadata(feature, load(snapshot_meta), snapshot / "artifacts", rev)

    working_meta = feature / "metadata.json"
    if not working_meta.is_file():
        raise ValueError(f"feature metadata not found: {working_meta}")
    current = load(working_meta)
    if current.get("current_revision") != rev:
        raise ValueError(
            f"revision snapshot metadata not found and requested revision is not current working revision: {rev}"
        )
    return inventory_from_metadata(feature, current, feature / "artifacts", rev)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("feature_path")
    parser.add_argument("base_revision")
    parser.add_argument("target_revision")
    parser.add_argument("--output")
    args = parser.parse_args()

    feature = Path(args.feature_path)
    feature = feature if feature.is_absolute() else ROOT / feature
    if (
        not REV.fullmatch(args.base_revision)
        or not REV.fullmatch(args.target_revision)
        or args.base_revision == args.target_revision
    ):
        print("ERROR revisions must be distinct canonical REV-* IDs")
        return 1

    try:
        base = inventory(feature, args.base_revision)
        target = inventory(feature, args.target_revision)
    except Exception as exc:
        print(f"ERROR {exc}")
        return 1

    rows = []
    for index, key in enumerate(sorted(set(base) | set(target)), 1):
        if key not in base:
            classification = "Added"
        elif key not in target:
            classification = "Removed"
        elif base[key].get("checksum") and target[key].get("checksum"):
            classification = "Unchanged" if base[key]["checksum"] == target[key]["checksum"] else "Modified"
        else:
            classification = "Unknown" if base[key].get("checksum") != target[key].get("checksum") else "Unchanged"
        rows.append({
            "change_id": f"CHG-{index:03d}",
            "item_key": key,
            "classification": classification,
            "reason": f"Deterministic revision inventory comparison classified {key} as {classification}.",
            "evidence": [
                base.get(key, {}).get("path", "base:absent"),
                target.get(key, {}).get("path", "target:absent"),
            ],
        })

    counts = {
        label: sum(row["classification"] == label for row in rows)
        for label in ["Added", "Modified", "Removed", "Unchanged", "Unknown"]
    }
    data = {
        "schema_version": "1.0",
        "base_revision": args.base_revision,
        "target_revision": args.target_revision,
        "changes": rows,
        "summary": {"total": len(rows), **counts},
    }
    output = (
        Path(args.output)
        if args.output
        else feature / "revisions" / args.target_revision / "change-intelligence" / "change-set.json"
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Change set created: {output}")
    print(f"Summary: {data['summary']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
