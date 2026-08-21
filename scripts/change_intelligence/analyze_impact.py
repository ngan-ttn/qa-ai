"""Propagate revision changes transitively through registered workspace dependencies."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RANK = {"Unknown": 0, "Potential": 1, "Dependency": 2, "Direct": 3}


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def stronger(existing: str | None, candidate: str) -> bool:
    return existing is None or RANK[candidate] > RANK[existing]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("feature_path")
    parser.add_argument("--change-set")
    parser.add_argument("--output")
    args = parser.parse_args()

    feature = Path(args.feature_path)
    feature = feature if feature.is_absolute() else ROOT / feature
    metadata = load(feature / "metadata.json")
    revision = metadata["current_revision"]
    change_path = (
        Path(args.change_set)
        if args.change_set
        else feature / "revisions" / revision / "change-intelligence" / "change-set.json"
    )
    change_set = load(change_path)
    changed = {
        row["item_key"]: row
        for row in change_set["changes"]
        if row["classification"] != "Unchanged"
    }

    # affected maps item keys (source/artifact) to propagated impact state and evidence origin.
    affected: dict[str, dict] = {}
    for item_key, change in changed.items():
        impact_type = "Unknown" if change["classification"] == "Unknown" else "Direct"
        affected[item_key] = {
            "impact_type": impact_type,
            "change": change,
            "relationship": "self",
            "upstream": item_key,
        }

    artifacts = metadata.get("artifacts", {})
    changed_any = True
    while changed_any:
        changed_any = False
        for artifact_key, artifact in artifacts.items():
            item_key = f"artifact:{artifact_key}"
            self_change = changed.get(item_key)
            if self_change:
                continue

            best = affected.get(item_key)
            for dep in artifact.get("dependencies", []):
                target = dep.get("target")
                upstream = affected.get(target)
                if not upstream:
                    continue
                relationship = dep.get("relationship", "registered")
                upstream_type = upstream["impact_type"]

                if upstream_type == "Unknown":
                    candidate = "Unknown"
                elif relationship == "required":
                    candidate = "Dependency" if upstream_type in {"Direct", "Dependency"} else "Potential"
                elif relationship in {"supporting", "conditional"}:
                    candidate = "Potential"
                else:
                    candidate = "Unknown"

                existing_type = best["impact_type"] if best else None
                if stronger(existing_type, candidate):
                    best = {
                        "impact_type": candidate,
                        "change": upstream["change"],
                        "relationship": relationship,
                        "upstream": target,
                    }

            if best and best != affected.get(item_key):
                affected[item_key] = best
                changed_any = True

    impacts = []
    index = 1
    for artifact_key in sorted(artifacts):
        item_key = f"artifact:{artifact_key}"
        state = affected.get(item_key)
        if not state:
            continue
        change = state["change"]
        impact_type = state["impact_type"]
        relationship = state["relationship"]
        upstream = state["upstream"]

        if impact_type == "Direct":
            reason = f"{change['classification']} change directly affects artifact {artifact_key}."
        elif impact_type == "Dependency":
            reason = (
                f"Supported change reaches artifact {artifact_key} transitively through required dependency {upstream}."
            )
        elif impact_type == "Potential":
            reason = (
                f"Change reaches artifact {artifact_key} through a supporting/conditional or potential dependency path via {upstream}; impact is possible but not proven as hard dependency."
            )
        else:
            reason = (
                f"Impact on artifact {artifact_key} cannot be resolved authoritatively from the registered dependency path via {upstream}."
            )

        impacts.append({
            "impact_id": f"IMP-{index:03d}",
            "change_id": change["change_id"],
            "artifact_key": artifact_key,
            "impact_type": impact_type,
            "relationship": relationship,
            "reason": reason,
            "evidence": [change["item_key"], upstream, *(change.get("evidence") or [])],
        })
        index += 1

    summary = {
        "total": len(impacts),
        "affected_artifacts": len({row["artifact_key"] for row in impacts}),
    }
    data = {
        "schema_version": "1.0",
        "base_revision": change_set["base_revision"],
        "target_revision": change_set["target_revision"],
        "impacts": impacts,
        "summary": summary,
    }
    output = Path(args.output) if args.output else change_path.parent / "impact-analysis.json"
    output.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Impact analysis created: {output}")
    print(f"Summary: {summary}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
