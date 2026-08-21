"""Register or revise an authoritative/supporting source in a QA-AI feature workspace."""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def next_source_id(sources: list[dict]) -> str:
    numbers: list[int] = []
    for source in sources:
        value = source.get("source_id") if isinstance(source, dict) else None
        if isinstance(value, str) and value.startswith("SRC-"):
            try:
                numbers.append(int(value.split("-", 1)[1]))
            except ValueError:
                pass
    return f"SRC-{max(numbers, default=0) + 1:03d}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("feature_path")
    parser.add_argument("source_file")
    parser.add_argument("--type", default="requirement", choices=("requirement", "supporting"))
    parser.add_argument("--revision")
    parser.add_argument("--authoritative", action="store_true")
    parser.add_argument("--copy", action="store_true", dest="copy_file", help="copy the source into the canonical workspace source folder")
    args = parser.parse_args()

    feature_dir = Path(args.feature_path)
    if not feature_dir.is_absolute():
        feature_dir = ROOT / feature_dir
    metadata_path = feature_dir / "metadata.json"
    if not metadata_path.is_file():
        print(f"ERROR metadata not found: {metadata_path}")
        return 1

    source_file = Path(args.source_file)
    if not source_file.is_absolute():
        source_file = ROOT / source_file
    if not source_file.is_file():
        print(f"ERROR source file not found: {source_file}")
        return 1

    data = json.loads(metadata_path.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", [])
    if not isinstance(sources, list):
        print("ERROR metadata sources must be an array")
        return 1

    destination_dir = feature_dir / "source" / ("requirements" if args.type == "requirement" else "supporting")
    destination_dir.mkdir(parents=True, exist_ok=True)
    destination = destination_dir / source_file.name
    if args.copy_file:
        if source_file.resolve() != destination.resolve():
            shutil.copy2(source_file, destination)
    elif source_file.resolve() != destination.resolve():
        print("ERROR source must already be inside the canonical workspace source folder unless --copy is supplied")
        return 1

    checksum = sha256(destination)
    relative_path = destination.relative_to(feature_dir).as_posix()
    timestamp = now_iso()

    # A canonical source keeps stable identity across revisions when its type/path stay the same.
    matching = [
        source for source in sources
        if isinstance(source, dict)
        and source.get("type") == args.type
        and source.get("path") == relative_path
    ]

    if matching:
        stable = sorted(matching, key=lambda item: str(item.get("source_id", "")))[0]
        source_id = stable.get("source_id")
        if stable.get("checksum") == checksum and stable.get("revision") == args.revision:
            print(f"ERROR identical source revision already registered: {source_id} {relative_path}")
            return 1

        stable.update({
            "type": args.type,
            "path": relative_path,
            "authoritative": bool(args.authoritative),
            "revision": args.revision,
            "checksum": checksum,
            "registered_at": timestamp,
        })

        # Repair pre-stabilization duplicate registrations for the same canonical path.
        sources[:] = [
            source for source in sources
            if source is stable
            or not (
                isinstance(source, dict)
                and source.get("type") == args.type
                and source.get("path") == relative_path
            )
        ]
        action = "Updated"
    else:
        source_id = next_source_id(sources)
        sources.append({
            "source_id": source_id,
            "type": args.type,
            "path": relative_path,
            "authoritative": bool(args.authoritative),
            "revision": args.revision,
            "checksum": checksum,
            "registered_at": timestamp,
        })
        action = "Registered"

    data["updated_at"] = timestamp
    metadata_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"{action} source: {source_id} -> {relative_path}")
    print(f"Revision: {args.revision}; SHA-256: {checksum}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
