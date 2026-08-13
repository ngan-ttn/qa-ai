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


def package(paths: list[str], output: str) -> Path:
    files: list[tuple[str, bytes]] = []
    for raw in paths:
        path = resolve_repo_path(raw)
        if not path.is_file():
            raise FileNotFoundError(path)
        try:
            arcname = path.relative_to(ROOT).as_posix()
        except ValueError:
            arcname = path.name
        files.append((arcname, path.read_bytes()))
    files.sort(key=lambda item: item[0])
    manifest = {
        "files": [{"path": name, "sha256": sha256(data), "bytes": len(data)} for name, data in files]
    }
    target = resolve_repo_path(output)
    target.parent.mkdir(parents=True, exist_ok=True)
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
