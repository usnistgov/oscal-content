"""
Validate the community AI RMF catalog and four profiles against the published
OSCAL 1.1.3 JSON schemas via ajv (the validator used by oscal-content).

Requires the OSCAL submodule + node_modules (run `make dependencies` from the
build directory first).

Run from the repository root:
    python3 src/examples/profile/json/community-ai-rmf-atr/tests/test_schema_validation.py

The schemas are downloaded on first run (cached at /tmp/oscal-schemas/).

Why ajv instead of Python jsonschema: the OSCAL schemas use Unicode property
escapes (\p{L}) that Python's `re` module does not support. ajv supports
these via the `unicode` regex engine. This test mirrors how `make all`
invokes ajv for content validation.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[6]
CATALOG_PATH = REPO_ROOT / "src/examples/catalog/json/community-ai-rmf-atr/ai-rmf-atr-catalog.json"
PROFILE_DIR = REPO_ROOT / "src/examples/profile/json/community-ai-rmf-atr"
PROFILE_NAMES = [
    "ai-rmf-baseline-profile.json",
    "ai-rmf-tier-1-foundational-profile.json",
    "ai-rmf-tier-2-customer-facing-profile.json",
    "ai-rmf-tier-3-high-risk-profile.json",
]

OSCAL_VERSION = "1.1.3"
SCHEMA_BASE = f"https://github.com/usnistgov/OSCAL/releases/download/v{OSCAL_VERSION}"
SCHEMA_CACHE = Path("/tmp/oscal-schemas")
AJV_CANDIDATES = [
    REPO_ROOT / "build/oscal/build/node_modules/.bin/ajv",  # OSCAL submodule, primary
    Path("/usr/local/bin/ajv"),
    Path("/opt/homebrew/bin/ajv"),
]


def fetch_schema(name: str) -> Path:
    SCHEMA_CACHE.mkdir(exist_ok=True)
    local = SCHEMA_CACHE / name
    if not local.exists():
        url = f"{SCHEMA_BASE}/{name}"
        print(f"fetching {url}")
        urllib.request.urlretrieve(url, local)
    return local


def find_ajv() -> Path:
    for cand in AJV_CANDIDATES:
        if cand.is_file() and os.access(cand, os.X_OK):
            return cand
    # Try PATH
    from shutil import which
    p = which("ajv")
    if p:
        return Path(p)
    raise RuntimeError(
        "ajv not found. Run `make dependencies` from build/ first to install "
        "via the OSCAL submodule's node_modules, or `npm install -g ajv-cli`."
    )


def validate_ajv(ajv: Path, schema: Path, data: Path) -> tuple[bool, str]:
    """Run ajv validate and return (success, output)."""
    cmd = [
        str(ajv),
        "-s", str(schema),
        "-d", str(data),
        "--spec=draft7",
        "--strict=false",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    out = (result.stdout + result.stderr).strip()
    success = result.returncode == 0 and "valid" in out and "invalid" not in out.lower()
    return success, out


def main() -> int:
    print(f"Validating community AI RMF artifacts against OSCAL {OSCAL_VERSION}")
    ajv = find_ajv()
    print(f"using ajv at {ajv}")

    cat_schema = fetch_schema("oscal_catalog_schema.json")
    prof_schema = fetch_schema("oscal_profile_schema.json")

    ok = True

    print("\n[catalog]")
    success, out = validate_ajv(ajv, cat_schema, CATALOG_PATH)
    marker = "✓" if success else "✗"
    summary = out.splitlines()[-1] if out else "(no output)"
    print(f"  {marker} {CATALOG_PATH.name}: {summary}")
    if not success:
        print(out)
        ok = False

    print("\n[profiles]")
    for name in PROFILE_NAMES:
        success, out = validate_ajv(ajv, prof_schema, PROFILE_DIR / name)
        marker = "✓" if success else "✗"
        summary = out.splitlines()[-1] if out else "(no output)"
        print(f"  {marker} {name}: {summary}")
        if not success:
            print(out)
            ok = False

    if ok:
        print("\nAll artifacts validate against OSCAL 1.1.3.")
        return 0
    print("\nValidation failures. See output above.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
