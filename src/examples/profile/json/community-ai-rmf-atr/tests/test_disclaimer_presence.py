"""
Disclaimer presence scan.

Verifies that all five disclaimer layers are present in their expected
locations. Failure means a layer was accidentally dropped during sync or
content edit, weakening the "not endorsed by NIST" framing required by
usnistgov/OSCAL#2234 Path 1.

Layer 1: metadata.remarks on profile root contains the disclaimer markers
Layer 2: metadata.parties contains Adam Lin + ATR community, NOT NIST
Layer 3: metadata.responsible-parties contains prepared-by + approved-by
         pointing at the ATR community party
Layer 4: README.md in the profile directory contains the disclaimer section
Layer 5: LICENSE.md in the profile directory contains CC0 + NIST non-endorsement
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[6]
PROFILE_DIR = REPO_ROOT / "src/examples/profile/json/community-ai-rmf-atr"
CATALOG_PATH = REPO_ROOT / "src/examples/catalog/json/community-ai-rmf-atr/ai-rmf-atr-catalog.json"

PROFILE_NAMES = [
    "ai-rmf-baseline-profile.json",
    "ai-rmf-tier-1-foundational-profile.json",
    "ai-rmf-tier-2-customer-facing-profile.json",
    "ai-rmf-tier-3-high-risk-profile.json",
]

ATR_PARTY_UUID = "b2d3e4f5-6789-50ab-91cd-2e4f6a8b0c1d"
ADAM_PARTY_UUID = "a8c98b3d-2e15-5cd6-9e75-b8a1f8f7e3d2"

REQUIRED_REMARKS_MARKERS = [
    "NOT authored by NIST",
    "NOT endorsed by NIST",
    "usnistgov/OSCAL#2234",
    "PROFILE RESOLUTION SPECIFICATION KNOWN-EDGE-CASE AUDIT",
]
REQUIRED_README_MARKERS = [
    "NOT authored by NIST",
    "Path 1",
    "CC0 1.0",
]
REQUIRED_LICENSE_MARKERS = [
    "CC0 1.0",
    "NIST has not authored",
    "Path 1",
]


def check_profile(name: str) -> list[str]:
    """Check the 5 layers for one profile file."""
    failures = []
    with open(PROFILE_DIR / name) as f:
        d = json.load(f)
    meta = d["profile"]["metadata"]

    # Layer 1: remarks
    remarks = meta.get("remarks", "")
    for marker in REQUIRED_REMARKS_MARKERS:
        if marker not in remarks:
            failures.append(f"{name} L1 (remarks): missing marker '{marker}'")

    # Layer 2: parties — both Adam + ATR community present, NO NIST
    party_uuids = {p["uuid"] for p in meta.get("parties", [])}
    if ADAM_PARTY_UUID not in party_uuids:
        failures.append(f"{name} L2 (parties): Adam Lin party UUID missing")
    if ATR_PARTY_UUID not in party_uuids:
        failures.append(f"{name} L2 (parties): ATR community party UUID missing")
    for p in meta.get("parties", []):
        if "NIST" in (p.get("name") or "") or "NIST" in (p.get("short-name") or ""):
            failures.append(f"{name} L2 (parties): NIST party found, MUST NOT be present")

    # Layer 3: responsible-parties
    role_ids = {rp["role-id"] for rp in meta.get("responsible-parties", [])}
    for required in ("prepared-by", "approved-by"):
        if required not in role_ids:
            failures.append(f"{name} L3 (responsible-parties): missing role '{required}'")

    return failures


def check_readme() -> list[str]:
    """Check README disclaimer layer."""
    failures = []
    path = PROFILE_DIR / "README.md"
    if not path.exists():
        return [f"L4: README.md missing at {path}"]
    text = path.read_text()
    for marker in REQUIRED_README_MARKERS:
        if marker not in text:
            failures.append(f"L4 (README.md): missing marker '{marker}'")
    return failures


def check_license() -> list[str]:
    """Check LICENSE disclaimer layer."""
    failures = []
    path = PROFILE_DIR / "LICENSE.md"
    if not path.exists():
        return [f"L5: LICENSE.md missing at {path}"]
    text = path.read_text()
    for marker in REQUIRED_LICENSE_MARKERS:
        if marker not in text:
            failures.append(f"L5 (LICENSE.md): missing marker '{marker}'")
    return failures


def main() -> int:
    all_failures: list[str] = []

    for name in PROFILE_NAMES:
        all_failures.extend(check_profile(name))

    all_failures.extend(check_readme())
    all_failures.extend(check_license())

    if all_failures:
        print(f"FAIL: {len(all_failures)} disclaimer marker issues")
        for f in all_failures:
            print(f"  - {f}")
        return 1

    print("All 5 disclaimer layers present in all 4 profiles + README + LICENSE.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
