"""
Cross-format round-trip test.

Verifies that converting JSON to YAML and back produces semantically
identical content (modulo whitespace and key ordering). This is the
lightweight test; the full XML round-trip requires oscal-cli (Java + Saxon)
and is exercised by the oscal-content `make all` pipeline.

Why both:
- This test runs in <1 second with only Python + PyYAML. CI-friendly.
- The Saxon-based XML round-trip catches semantic loss the JSON-YAML pass
  cannot (XML namespaces, mixed content, ordered children).

If this test fails, the JSON profile uses a structure that does not survive
YAML representation (typically: very long strings with embedded special
characters that PyYAML truncates).
"""
from __future__ import annotations

import json
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


def install_yaml() -> None:
    try:
        import yaml  # noqa: F401
    except ImportError:
        import subprocess
        subprocess.run([sys.executable, "-m", "pip", "install", "--quiet", "PyYAML"], check=True)


def round_trip(path: Path) -> bool:
    import yaml
    with open(path) as f:
        original = json.load(f)
    serialized = yaml.safe_dump(original, sort_keys=False, allow_unicode=True, default_flow_style=False)
    deserialized = yaml.safe_load(serialized)
    if deserialized != original:
        print(f"  ✗ {path.name}: round-trip lost data")
        return False
    print(f"  ✓ {path.name}: round-trip clean")
    return True


def main() -> int:
    install_yaml()

    ok = True
    print("Catalog:")
    ok &= round_trip(CATALOG_PATH)

    print("Profiles:")
    for name in PROFILE_NAMES:
        ok &= round_trip(PROFILE_DIR / name)

    if not ok:
        return 1
    print("All catalog + profile artifacts JSON↔YAML round-trip cleanly.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
