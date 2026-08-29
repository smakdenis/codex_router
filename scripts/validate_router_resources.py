#!/usr/bin/env python3
"""Validate the router's declarative configuration and manual evaluation corpus."""
from __future__ import annotations
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "skills" / "recommend-ai-mode" / "references" / "routing-config.json"
CASES_PATH = ROOT / "tests" / "evaluation-cases.json"

def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)

def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"{path}: {exc}")

config = load_json(CONFIG_PATH)
cases = load_json(CASES_PATH)
if config.get("schemaVersion") != 1 or cases.get("schemaVersion") != 1:
    fail("unsupported schema version")
models = config.get("models", {})
if set(models) != {"luna", "terra", "sol"}:
    fail("config must declare luna, terra, and sol")
valid_models = {model["displayName"]: set(model["efforts"]) for model in models.values()}
valid_speeds = {config["speed"]["default"], config["speed"]["urgent"]}
seen_ids: set[str] = set()
for case in cases.get("cases", []):
    case_id = case.get("id")
    expected = case.get("expected", {})
    if not case_id or case_id in seen_ids:
        fail(f"case id must be present and unique: {case_id!r}")
    seen_ids.add(case_id)
    if not case.get("prompt") or not case.get("acceptance"):
        fail(f"{case_id}: prompt and acceptance criteria are required")
    model = expected.get("model")
    if model not in valid_models:
        fail(f"{case_id}: unknown expected model {model!r}")
    if expected.get("effort") not in valid_models[model]:
        fail(f"{case_id}: effort is not supported by {model}")
    if expected.get("speed") not in valid_speeds:
        fail(f"{case_id}: unknown speed")
if len(seen_ids) < 6:
    fail("at least six evaluation cases are required")
print(f"OK: validated {len(seen_ids)} routing evaluation cases")
