"""Package QA-AI output files into a deterministic ZIP archive with checksums."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.utils.file_utils import resolve_repo_path

FIXED_TIME = (1980, 1, 1, 0, 0, 0)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _repo_file(raw: str) -> Path:
    path = resolve_repo_path(raw).resolve()
    try:
        path.relative_to(ROOT.resolve())
    except ValueError as exc:
        raise ValueError(f"Package inputs must be inside the QA-AI repository: {raw}") from exc
    if not path.is_file():
        raise FileNotFoundError(path)
    return path


def package(paths: list[str], output: str) -> Path:
    target = resolve_repo_path(output).resolve()
    target.parent.mkdir(parents=True, exist_ok=True)
    files_by_name: dict[str, bytes] = {}
    for raw in paths:
        path = _repo_file(raw)
        if path == target:
            raise ValueError("Output archive cannot also be an input file")
        arcname = path.relative_to(ROOT.resolve()).as_posix()
        if arcname in files_by_name:
            raise ValueError(f"Duplicate package input: {arcname}")
        files_by_name[arcname] = path.read_bytes()

    files = sorted(files_by_name.items())
    manifest = {
        "files": [{"path": name, "sha256": sha256(data), "bytes": len(data)} for name, data in files]
    }
    with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, data in files:
            info = zipfile.ZipInfo(name, FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, data)
        info = zipfile.ZipInfo("package-manifest.json", FIXED_TIME)
        info.compress_type = zipfile.ZIP_DEFLATED
        archive.writestr(info, (json.dumps(manifest, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))
    return target


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+")
    parser.add_argument("--output", default="output/qa-ai-output.zip")
    args = parser.parse_args()
    target = package(args.paths, args.output)
    print(f"Packaged {len(args.paths)} file(s) -> {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
