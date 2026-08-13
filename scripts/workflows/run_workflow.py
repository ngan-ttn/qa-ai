"""Create a deterministic execution plan for a QA-AI workflow.

This script does not execute AI skills. It validates workflow/skill availability and
produces an explicit plan for adapters or human-driven execution.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.workflows.load_workflow import load_workflow
from scripts.workflows.resolve_skills import resolve
from scripts.utils.file_utils import write_json


def build_plan(workflow: str, input_path: str | None = None) -> dict[str, object]:
    definition = load_workflow(workflow)
    resolved = resolve(workflow)
    if resolved["missing"]:
        raise RuntimeError("Cannot plan workflow with missing skills: " + ", ".join(resolved["missing"]))
    skill_order = definition.get("required_skills", [])
    stages = [
        {
            "order": index,
            "skill": skill,
            "skill_readme": f"skills/{skill}/README.md",
            "execution": "external-capability-invocation",
        }
        for index, skill in enumerate(skill_order, 1)
    ]
    return {
        "workflow": definition["name"],
        "workflow_source": definition["source"],
        "input": input_path,
        "stages": stages,
        "note": "Plan only; skill execution belongs to a platform adapter/runtime or human workflow.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workflow")
    parser.add_argument("--input")
    parser.add_argument("--output", default="output/workflow-plan.json")
    args = parser.parse_args()
    plan = build_plan(args.workflow, args.input)
    write_json(args.output, plan)
    print(f"Planned {len(plan['stages'])} stage(s) for {plan['workflow']} -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
