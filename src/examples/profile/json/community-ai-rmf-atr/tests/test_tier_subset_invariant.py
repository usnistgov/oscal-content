"""
Tier subset invariant test.

Enforces:  Tier 1 ⊂ Tier 2 ⊂ Baseline = Tier 3

If this fails, the tier rationale documentation in TIER_RATIONALE.md is out of
sync with the actual `with-ids` selections in the profiles, or the upstream
catalog has dropped a control referenced by one of the tier profiles.

The "Baseline = Tier 3" relationship is intentional: Tier 3 differs from
Baseline only in profile metadata framing, not in control selection.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[6]
PROFILE_DIR = REPO_ROOT / "src/examples/profile/json/community-ai-rmf-atr"
CATALOG_PATH = REPO_ROOT / "src/examples/catalog/json/community-ai-rmf-atr/ai-rmf-atr-catalog.json"


def load_profile_controls(name: str) -> set[str]:
    """Extract the set of control IDs a profile selects.

    Returns the empty set if the profile selects every control (`include-all`).
    Returns the explicit set if the profile uses `include-controls` with
    `with-ids`. Raises if neither pattern matches.
    """
    with open(PROFILE_DIR / name) as f:
        d = json.load(f)
    imp = d["profile"]["imports"][0]
    if imp.get("include-all") is not None:
        return None  # sentinel for include-all
    inc = imp.get("include-controls", [])
    ids: set[str] = set()
    for entry in inc:
        ids.update(entry.get("with-ids", []))
    if not ids:
        raise RuntimeError(f"{name}: neither include-all nor include-controls.with-ids present")
    return ids


def catalog_control_ids() -> set[str]:
    """Return every control ID in the imported catalog."""
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


def main() -> int:
    catalog_ids = catalog_control_ids()
    print(f"Catalog has {len(catalog_ids)} controls")

    baseline_set = load_profile_controls("ai-rmf-baseline-profile.json")
    tier1_set = load_profile_controls("ai-rmf-tier-1-foundational-profile.json")
    tier2_set = load_profile_controls("ai-rmf-tier-2-customer-facing-profile.json")
    tier3_set = load_profile_controls("ai-rmf-tier-3-high-risk-profile.json")

    if baseline_set is None:
        baseline_set = catalog_ids
        print("Baseline: include-all (interpreted as full catalog)")
    if tier3_set is None:
        tier3_set = catalog_ids
        print("Tier 3: include-all (interpreted as full catalog)")

    print(f"Tier 1: {len(tier1_set)} explicit controls")
    print(f"Tier 2: {len(tier2_set)} explicit controls")
    print(f"Baseline: {len(baseline_set)} controls")
    print(f"Tier 3: {len(tier3_set)} controls")

    failures: list[str] = []

    # Invariant 1: Tier 1 ⊂ Tier 2
    leaked = tier1_set - tier2_set
    if leaked:
        failures.append(
            f"Tier 1 has {len(leaked)} controls not in Tier 2: "
            f"{sorted(leaked)[:5]}{'...' if len(leaked) > 5 else ''}"
        )

    # Invariant 2: Tier 2 ⊂ Baseline
    leaked = tier2_set - baseline_set
    if leaked:
        failures.append(
            f"Tier 2 has {len(leaked)} controls not in Baseline: "
            f"{sorted(leaked)[:5]}{'...' if len(leaked) > 5 else ''}"
        )

    # Invariant 3: Baseline = Tier 3
    only_baseline = baseline_set - tier3_set
    only_tier3 = tier3_set - baseline_set
    if only_baseline or only_tier3:
        failures.append(
            f"Baseline and Tier 3 differ: "
            f"baseline-only={sorted(only_baseline)[:3]}, "
            f"tier3-only={sorted(only_tier3)[:3]}"
        )

    # Invariant 4: every tier ID exists in the catalog
    for label, ids in [("Tier 1", tier1_set), ("Tier 2", tier2_set)]:
        unknown = ids - catalog_ids
        if unknown:
            failures.append(
                f"{label} references {len(unknown)} control IDs not in catalog: "
                f"{sorted(unknown)[:5]}"
            )

    if failures:
        print("\nFAIL:")
        for f in failures:
            print(f"  - {f}")
        return 1

    print("\nAll tier subset invariants hold.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
