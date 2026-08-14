"""Shared deterministic file helpers for QA-AI scripts."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable


def repo_root(start: str | Path | None = None) -> Path:
    """Return repository root by walking upward to manifest.json or .git."""
    current = Path(start or __file__).resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / "manifest.json").exists() or (candidate / ".git").exists():
            return candidate
    raise FileNotFoundError("Could not locate QA-AI repository root")


def resolve_repo_path(path: str | Path, root: Path | None = None) -> Path:
    p = Path(path)
    return p.resolve() if p.is_absolute() else (root or repo_root()) / p


def read_text(path: str | Path, *, encoding: str = "utf-8") -> str:
    p = resolve_repo_path(path)
    if not p.is_file():
        raise FileNotFoundError(p)
    return p.read_text(encoding=encoding)


def write_text(path: str | Path, content: str, *, encoding: str = "utf-8") -> Path:
    p = resolve_repo_path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding=encoding, newline="\n")
    return p


def read_json(path: str | Path) -> Any:
    try:
        return json.loads(read_text(path))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {path}: {exc}") from exc


def write_json(path: str | Path, data: Any, *, indent: int = 2) -> Path:
    return write_text(path, json.dumps(data, indent=indent, ensure_ascii=False) + "\n")


def iter_files(base: str | Path, patterns: Iterable[str] = ("*",)) -> list[Path]:
    root = resolve_repo_path(base)
    if not root.exists():
        return []
    files: set[Path] = set()
    for pattern in patterns:
        files.update(p for p in root.rglob(pattern) if p.is_file())
    return sorted(files)


def relative_to_repo(path: str | Path) -> str:
    p = resolve_repo_path(path)
    return p.relative_to(repo_root()).as_posix()
