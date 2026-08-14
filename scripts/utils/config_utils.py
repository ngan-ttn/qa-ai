"""Configuration loading and merge helpers used by QA-AI scripts."""
from __future__ import annotations

import os
from copy import deepcopy
from pathlib import Path
from typing import Any, Mapping

try:
    from scripts.utils.file_utils import read_json, resolve_repo_path
except ModuleNotFoundError:  # direct script execution
    from file_utils import read_json, resolve_repo_path


def deep_merge(base: Mapping[str, Any], override: Mapping[str, Any]) -> dict[str, Any]:
    result = deepcopy(dict(base))
    for key, value in override.items():
        if isinstance(value, Mapping) and isinstance(result.get(key), Mapping):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = deepcopy(value)
    return result


def load_config(path: str | Path | None = None, *, defaults: Mapping[str, Any] | None = None) -> dict[str, Any]:
    config = dict(defaults or {})
    if path is None:
        return config
    loaded = read_json(resolve_repo_path(path))
    if not isinstance(loaded, dict):
        raise ValueError(f"Configuration must be a JSON object: {path}")
    return deep_merge(config, loaded)


def env_bool(name: str, default: bool = False) -> bool:
    raw = os.getenv(name)
    if raw is None:
        return default
    value = raw.strip().lower()
    if value in {"1", "true", "yes", "on"}:
        return True
    if value in {"0", "false", "no", "off"}:
        return False
    raise ValueError(f"Environment variable {name} must be boolean-like, got {raw!r}")


def env_int(name: str, default: int | None = None) -> int | None:
    raw = os.getenv(name)
    if raw is None:
        return default
    try:
        return int(raw)
    except ValueError as exc:
        raise ValueError(f"Environment variable {name} must be an integer") from exc


def require_keys(config: Mapping[str, Any], keys: list[str]) -> None:
    missing = [key for key in keys if key not in config or config[key] in (None, "")]
    if missing:
        raise KeyError(f"Missing required configuration keys: {', '.join(missing)}")
