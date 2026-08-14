"""Load a QA-AI workflow README into a deterministic structured definition."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.utils.file_utils import read_text, resolve_repo_path, write_json

SKILL_RE = re.compile(r"`skills/([a-z0-9-]+)`")
STEP_RE = re.compile(r"^###\s+Step\s+(\d+)\s*:\s*(.+)$", re.M)
TITLE_RE = re.compile(r"^#\s+(.+)$", re.M)
SECTION_RE = re.compile(r"^##\s+(.+?)\s*$", re.M)


def _section(text: str, title: str) -> str | None:
    matches = list(SECTION_RE.finditer(text))
    for index, match in enumerate(matches):
        if match.group(1).strip().casefold() != title.casefold():
            continue
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        return text[start:end]
    return None


def load_workflow(name_or_path: str) -> dict[str, object]:
    candidate = resolve_repo_path(name_or_path)
    if candidate.is_dir():
        candidate = candidate / "README.md"
    elif not candidate.exists():
        candidate = ROOT / "workflows" / name_or_path / "README.md"
    if not candidate.is_file():
        raise FileNotFoundError(f"Workflow README not found: {name_or_path}")
    try:
        source = candidate.resolve().relative_to(ROOT.resolve()).as_posix()
    except ValueError as exc:
        raise ValueError("Workflow definition must be inside the QA-AI repository") from exc

    text = read_text(candidate)
    title = TITLE_RE.search(text)
    required_section = _section(text, "Required Skills")
    if required_section is None:
        raise ValueError(f"Workflow is missing canonical 'Required Skills' section: {source}")
    skills = list(dict.fromkeys(SKILL_RE.findall(required_section)))
    if not skills:
        raise ValueError(f"Workflow declares no skills in 'Required Skills': {source}")

    steps = [{"number": int(n), "name": label.strip()} for n, label in STEP_RE.findall(text)]
    numbers = [item["number"] for item in steps]
    if numbers and numbers != list(range(1, len(numbers) + 1)):
        raise ValueError(f"Workflow steps must be contiguous from 1: {source}")

    return {
        "name": candidate.parent.name,
        "title": title.group(1).strip() if title else candidate.parent.name,
        "source": source,
        "required_skills": skills,
        "steps": steps,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workflow")
    parser.add_argument("--output")
    args = parser.parse_args()
    data = load_workflow(args.workflow)
    if args.output:
        write_json(args.output, data)
        print(f"Loaded {data['name']} -> {args.output}")
    else:
        import json
        print(json.dumps(data, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
