"""Validate knowledge Catalog.md file mappings against physical Markdown articles."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.utils.file_utils import relative_to_repo

FILE_CELL_RE = re.compile(r"`([^`]+\.md)`")


def catalog_files(catalog: Path) -> set[str]:
    result: set[str] = set()
    for line in catalog.read_text(encoding="utf-8").splitlines():
        if not line.lstrip().startswith("|"):
            continue
        for match in FILE_CELL_RE.findall(line):
            if match not in {"README.md", "Catalog.md"}:
                result.add(match.replace("\\", "/"))
    return result


def physical_files(domain: Path) -> set[str]:
    return {
        p.relative_to(domain).as_posix()
        for p in domain.rglob("*.md")
        if p.name not in {"README.md", "Catalog.md"}
    }


def validate_domain(domain: Path) -> list[str]:
    catalog = domain / "Catalog.md"
    if not catalog.is_file():
        return ["missing Catalog.md"]
    listed = catalog_files(catalog)
    physical = physical_files(domain)
    if not listed:
        return ["Catalog.md contains no backtick-wrapped .md file mappings"]
    errors = [f"catalog entry missing physical file: {p}" for p in sorted(listed - physical)]
    errors += [f"physical article missing catalog entry: {p}" for p in sorted(physical - listed)]
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", type=Path, default=ROOT / "shared" / "knowledge")
    args = parser.parse_args()
    issues = 0
    domains = [p for p in args.base.resolve().iterdir() if p.is_dir()]
    for domain in sorted(domains):
        errors = validate_domain(domain)
        for error in errors:
            issues += 1
            print(f"ERROR {relative_to_repo(domain)}: {error}")
        if not errors:
            print(f"PASS {relative_to_repo(domain)}")
    print(f"Validated {len(domains)} knowledge domain(s); issues={issues}")
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
