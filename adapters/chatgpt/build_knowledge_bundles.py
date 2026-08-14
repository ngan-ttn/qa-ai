"""Build deterministic text-forward Knowledge bundles for the QA-AI Custom GPT adapter."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

BUNDLES: dict[str, tuple[str, ...]] = {
    "01-framework.md": ("README.md", "FRAMEWORK.md", "docs"),
    "02-standards.md": ("shared/standards", "shared/templates", "shared/checklists"),
    "03-prompt-patterns.md": ("shared/prompt-patterns",),
    "04-skills.md": ("skills",),
    "05-workflows.md": ("workflows",),
    "06-qa-knowledge.md": ("shared/knowledge/qa",),
    "07-testing-techniques.md": ("shared/knowledge/testing-techniques",),
    "08-api-knowledge.md": ("shared/knowledge/api",),
    "09-database-knowledge.md": ("shared/knowledge/database",),
    "10-domain-knowledge.md": ("shared/knowledge/domain",),
    "11-glossary.md": ("shared/glossary",),
    "12-evaluation.md": ("datasets/evaluation", "datasets/benchmark"),
    "13-controlled-requirements.md": ("datasets/requirements",),
    "14-phase14-pilot-requirement.md": ("datasets/requirements/simple/REQ-AUTH-001.md",),
}


def _resolve_source(raw: str) -> list[Path]:
    source = (ROOT / raw).resolve()
    try:
        source.relative_to(ROOT)
    except ValueError as exc:
        raise ValueError(f"Source escapes repository root: {raw}") from exc
    if not source.exists():
        raise FileNotFoundError(source)
    if source.is_file():
        return [source]
    return sorted(
        (path for path in source.rglob("*.md") if path.is_file()),
        key=lambda path: path.relative_to(ROOT).as_posix(),
    )


def _render_bundle(name: str, sources: tuple[str, ...]) -> str:
    files: list[Path] = []
    for source in sources:
        files.extend(_resolve_source(source))
    seen: set[str] = set()
    ordered: list[Path] = []
    for path in files:
        rel = path.relative_to(ROOT).as_posix()
        if rel not in seen:
            seen.add(rel)
            ordered.append(path)

    lines = [
        f"# QA-AI Knowledge Bundle — {name}",
        "",
        "> Generated deterministically from canonical repository sources. Do not edit this bundle manually.",
        "",
    ]
    for path in ordered:
        rel = path.relative_to(ROOT).as_posix()
        content = path.read_text(encoding="utf-8").strip()
        lines.extend([
            "---",
            "",
            f"<!-- SOURCE: {rel} -->",
            f"## Source: `{rel}`",
            "",
            content,
            "",
        ])
    return "\n".join(lines).rstrip() + "\n"


def build(output_dir: Path, *, check: bool = False) -> tuple[int, list[str]]:
    output_dir = output_dir.resolve()
    if not check:
        output_dir.mkdir(parents=True, exist_ok=True)
    changed: list[str] = []
    manifest: dict[str, object] = {"bundle_count": len(BUNDLES), "bundles": []}

    for name, sources in BUNDLES.items():
        content = _render_bundle(name, sources)
        target = output_dir / name
        digest = hashlib.sha256(content.encode("utf-8")).hexdigest()
        current = target.read_text(encoding="utf-8") if target.is_file() else None
        if current != content:
            changed.append(name)
            if not check:
                target.write_text(content, encoding="utf-8", newline="\n")
        manifest["bundles"].append({
            "file": name,
            "sources": list(sources),
            "sha256": digest,
            "bytes": len(content.encode("utf-8")),
        })

    manifest_text = json.dumps(manifest, indent=2, ensure_ascii=False) + "\n"
    manifest_path = output_dir / "bundle-manifest.json"
    current_manifest = manifest_path.read_text(encoding="utf-8") if manifest_path.is_file() else None
    if current_manifest != manifest_text:
        changed.append("bundle-manifest.json")
        if not check:
            manifest_path.write_text(manifest_text, encoding="utf-8", newline="\n")

    return len(BUNDLES), changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT / "output" / "chatgpt-knowledge",
        help="Generated package directory",
    )
    parser.add_argument("--check", action="store_true", help="Fail when generated bundles are missing or stale")
    args = parser.parse_args()

    if len(BUNDLES) > 20:
        raise SystemExit("ERROR: Custom GPT package exceeds the 20-file Knowledge limit")

    count, changed = build(args.output_dir, check=args.check)
    if args.check:
        if changed:
            print("FAIL: ChatGPT Knowledge package missing/stale: " + ", ".join(changed))
            return 1
        print(f"PASS: {count} ChatGPT Knowledge bundle(s) synchronized")
        return 0

    print(f"Built {count} ChatGPT Knowledge bundle(s) -> {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
