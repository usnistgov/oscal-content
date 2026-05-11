"""
Profile resolution test.

For each of the four profiles, manually walk the include-controls selection
against the imported catalog and confirm:

1. Every control referenced in `with-ids` exists in the catalog.
2. The resolved catalog (the set of controls retained after profile
   resolution) is non-empty and matches the expected count from the tier
   rationale.

This is a deterministic, dependency-free check of the OSCAL profile
resolution semantics for the subset of features these profiles use
(`include-controls.with-ids` and `include-all`). It does NOT exercise the
full Profile Resolution Specification (no `match`, no `as-is`, no `modify`,
no `back-matter`-derived imports) because these profiles intentionally use
only the documented stable subset.

The full Profile Resolution Specification is exercised by `oscal-cli profile
resolve` in the CI pipeline. This test is the lightweight first-line check.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[6]
PROFILE_DIR = REPO_ROOT / "src/examples/profile/json/community-ai-rmf-atr"
CATALOG_PATH = REPO_ROOT / "src/examples/catalog/json/community-ai-rmf-atr/ai-rmf-atr-catalog.json"

EXPECTED = {
    "ai-rmf-baseline-profile.json": 72,
    "ai-rmf-tier-1-foundational-profile.json": 18,
    "ai-rmf-tier-2-customer-facing-profile.json": 55,
    "ai-rmf-tier-3-high-risk-profile.json": 72,
}


def catalog_control_ids() -> set[str]:
    with open(CATALOG_PATH) as f:
        d = json.load(f)
    ids: set[str] = set()
    for group in d["catalog"].get("groups", []):
        for sub in group.get("groups", []):
            for ctrl in sub.get("controls", []):
                ids.add(ctrl["id"])
        for ctrl in group.get("controls", []):
            ids.add(ctrl["id"])
    return ids


def resolve_profile(name: str, catalog_ids: set[str]) -> tuple[int, list[str]]:
    """Return (resolved control count, list of errors)."""
    errors: list[str] = []
    with open(PROFILE_DIR / name) as f:
        d = json.load(f)
    imports = d["profile"].get("imports", [])
    if not imports:
        return 0, [f"{name}: no imports"]
    imp = imports[0]
    if imp.get("include-all") is not None:
        return len(catalog_ids), []
    inc = imp.get("include-controls", [])
    selected: set[str] = set()
    for entry in inc:
        for cid in entry.get("with-ids", []):
            if cid not in catalog_ids:
                errors.append(f"{name}: with-ids references unknown control {cid}")
            selected.add(cid)
    return len(selected), errors


def main() -> int:
    catalog_ids = catalog_control_ids()
    print(f"Catalog: {len(catalog_ids)} controls")

    failures: list[str] = []
    for name, expected in EXPECTED.items():
        count, errors = resolve_profile(name, catalog_ids)
        failures.extend(errors)
        if count != expected:
            failures.append(
                f"{name}: resolved {count} controls, expected {expected}"
            )
        marker = "✓" if (count == expected and not errors) else "✗"
        print(f"  {marker} {name}: resolved {count} controls (expected {expected})")

    if failures:
        print(f"\nFAIL: {len(failures)} issues")
        for f in failures:
            print(f"  - {f}")
        return 1
    print("\nAll 4 profiles resolve to expected control counts.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
