"""Install or verify the QA-AI Claude Code project instruction file."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "adapters" / "claude" / "CLAUDE.md"
TARGET = ROOT / "CLAUDE.md"


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check() -> list[str]:
    errors: list[str] = []
    if not SOURCE.is_file() or SOURCE.stat().st_size == 0:
        errors.append("missing/non-content Claude adapter source: adapters/claude/CLAUDE.md")
        return errors
    if not TARGET.is_file():
        errors.append("Claude Code project instruction is not installed: CLAUDE.md")
        return errors
    if _read(TARGET) != _read(SOURCE):
        errors.append("CLAUDE.md is stale; run: python adapters/claude/install.py")
    return errors


def install() -> None:
    if not SOURCE.is_file() or SOURCE.stat().st_size == 0:
        raise FileNotFoundError("adapters/claude/CLAUDE.md is missing or empty")
    TARGET.write_text(_read(SOURCE), encoding="utf-8")
    print("Installed Claude Code project instructions: adapters/claude/CLAUDE.md -> CLAUDE.md")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify repo-root CLAUDE.md exists and is synchronized with the adapter source",
    )
    args = parser.parse_args()

    if args.check:
        errors = check()
        if errors:
            for error in errors:
                print(f"ERROR {error}")
            print(f"Claude adapter installation check failed; issues={len(errors)}")
            return 1
        print("PASS Claude adapter installation: CLAUDE.md synchronized")
        return 0

    install()
    errors = check()
    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1
    print("PASS Claude adapter installation: CLAUDE.md synchronized")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
