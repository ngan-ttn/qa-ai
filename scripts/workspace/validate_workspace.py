"""Validate a canonical QA-AI feature workspace deterministically."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LIFECYCLE = {"Draft", "Review", "Approved", "Superseded", "Archived"}
FRESHNESS = {"Current", "Stale", "Unknown"}
DEPENDENCY_TYPES = {"required", "supporting", "conditional"}
FEATURE_STATUS = {"Active", "Inactive", "Archived"}
REVISION_RE = re.compile(r"^REV-[0-9]{3,}$")
SOURCE_RE = re.compile(r"^SRC-[0-9]{3,}$")
REQUIRED_DIRS = (
    "source/requirements", "source/supporting", "artifacts", "exports/generic",
    "executions", "revisions", "archive",
)
REQUIRED_METADATA_FIELDS = (
    "schema_version", "project_id", "feature_id", "feature_name", "status",
    "current_revision", "framework_revision", "created_at", "updated_at", "sources", "artifacts",
)

def rel(path: Path) -> str:
    try: return path.resolve().relative_to(ROOT.resolve()).as_posix()
    except ValueError: return str(path)
def load_json(path: Path) -> dict: return json.loads(path.read_text(encoding="utf-8"))

def validate(feature_dir: Path) -> list[str]:
    errors=[]
    if not feature_dir.is_dir(): return [f"feature workspace directory not found: {rel(feature_dir)}"]
    for required in REQUIRED_DIRS:
        if not (feature_dir/required).is_dir(): errors.append(f"missing required directory: {rel(feature_dir/required)}")
    metadata_path=feature_dir/"metadata.json"
    if not metadata_path.is_file(): return errors+[f"missing metadata.json: {rel(metadata_path)}"]
    try: data=load_json(metadata_path)
    except Exception as exc: return errors+[f"invalid metadata JSON: {exc}"]
    for field in REQUIRED_METADATA_FIELDS:
        if field not in data: errors.append(f"metadata missing required field: {field}")
    if data.get("schema_version")!="1.0": errors.append("metadata schema_version must be 1.0")
    if data.get("status") not in FEATURE_STATUS: errors.append(f"invalid feature status: {data.get('status')}")
    current_revision=data.get("current_revision")
    if not isinstance(current_revision,str) or not REVISION_RE.fullmatch(current_revision): errors.append(f"invalid current_revision: {current_revision}")
    sources=data.get("sources",[])
    if not isinstance(sources,list): errors.append("sources must be an array"); sources=[]
    source_ids=set()
    for idx,source in enumerate(sources,start=1):
        if not isinstance(source,dict): errors.append(f"source[{idx}] must be an object"); continue
        source_id=source.get("source_id")
        if not isinstance(source_id,str) or not SOURCE_RE.fullmatch(source_id): errors.append(f"invalid source_id at source[{idx}]: {source_id}")
        elif source_id in source_ids: errors.append(f"duplicate source_id: {source_id}")
        else: source_ids.add(source_id)
        for field in ("type","path","authoritative","registered_at"):
            if field not in source: errors.append(f"source {source_id or idx} missing field: {field}")
        source_path=source.get("path")
        if isinstance(source_path,str) and source_path and not (feature_dir/source_path).exists(): errors.append(f"registered source path does not exist: {source_path}")
    artifacts=data.get("artifacts",{})
    if not isinstance(artifacts,dict): errors.append("artifacts must be an object"); artifacts={}
    artifact_keys=set(artifacts); artifact_paths=set()
    for key,artifact in artifacts.items():
        if not isinstance(artifact,dict): errors.append(f"artifact {key} must be an object"); continue
        for field in ("artifact_type","path","status","freshness","revision","source_revision","dependencies"):
            if field not in artifact: errors.append(f"artifact {key} missing field: {field}")
        if artifact.get("status") not in LIFECYCLE: errors.append(f"artifact {key} has invalid lifecycle status: {artifact.get('status')}")
        if artifact.get("freshness") not in FRESHNESS: errors.append(f"artifact {key} has invalid freshness: {artifact.get('freshness')}")
        source_revision=artifact.get("source_revision")
        if not isinstance(source_revision,str) or not REVISION_RE.fullmatch(source_revision): errors.append(f"artifact {key} has invalid source_revision: {source_revision}")
        path_value=artifact.get("path")
        if isinstance(path_value,str) and path_value:
            if path_value in artifact_paths: errors.append(f"duplicate artifact path registration: {path_value}")
            artifact_paths.add(path_value); full=feature_dir/path_value
            if artifact.get("status") in {"Review","Approved","Superseded","Archived"} and not full.is_file(): errors.append(f"registered non-Draft artifact path does not exist: {path_value}")
        dependencies=artifact.get("dependencies",[])
        if not isinstance(dependencies,list): errors.append(f"artifact {key} dependencies must be an array"); continue
        for dep_idx,dep in enumerate(dependencies,start=1):
            if not isinstance(dep,dict): errors.append(f"artifact {key} dependency[{dep_idx}] must be an object"); continue
            target=dep.get("target"); relationship=dep.get("relationship")
            if relationship not in DEPENDENCY_TYPES: errors.append(f"artifact {key} dependency {target} has invalid relationship: {relationship}")
            if not isinstance(target,str) or not target: errors.append(f"artifact {key} dependency[{dep_idx}] missing target")
            elif target.startswith("artifact:"):
                target_key=target.split(":",1)[1]
                if target_key not in artifact_keys: errors.append(f"artifact {key} dependency references unknown artifact: {target_key}")
            elif target.startswith("source:"):
                target_id=target.split(":",1)[1]
                if target_id not in source_ids: errors.append(f"artifact {key} dependency references unknown source: {target_id}")
            else: errors.append(f"artifact {key} dependency target must use artifact:<key> or source:<id>: {target}")
            if relationship=="required" and isinstance(target,str) and target.startswith("artifact:"):
                target_key=target.split(":",1)[1]; upstream=artifacts.get(target_key); expected=dep.get("target_revision")
                if isinstance(upstream,dict) and expected and upstream.get("revision")!=expected and artifact.get("freshness")!="Stale": errors.append(f"artifact {key} required dependency revision mismatch with {target_key}; freshness must be Stale")
    return errors

def main()->int:
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument("feature_path"); args=parser.parse_args(); feature_dir=Path(args.feature_path)
    if not feature_dir.is_absolute(): feature_dir=ROOT/feature_dir
    errors=validate(feature_dir)
    if errors:
        for error in errors: print(f"ERROR {error}")
        print(f"Workspace validation failed; issues={len(errors)}"); return 1
    print(f"PASS workspace validation: {rel(feature_dir)}"); return 0
if __name__=="__main__": raise SystemExit(main())
