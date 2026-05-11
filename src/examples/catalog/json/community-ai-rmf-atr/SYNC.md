# Vendored catalog sync metadata

This file documents the provenance of the vendored AI RMF community catalog and the mechanism by which it is kept in sync with its upstream source.

## Upstream

- **Repository**: github.com/Agent-Threat-Rule/ai-rmf-oscal-catalog
- **License**: CC0 1.0 (public domain)
- **Catalog URL**: https://github.com/Agent-Threat-Rule/ai-rmf-oscal-catalog/blob/main/catalogs/ai-rmf-v0.4.json

## Current vendored snapshot

| Field | Value |
|---|---|
| Upstream version | v0.4.0 |
| Upstream commit | 03f059dee9f4f76e6e54de2c6f88c7e8a8e5e2a4 (head of main at sync time) |
| Vendored at | 2026-05-12T00:00:00Z |
| OSCAL version | 1.1.3 (downgraded from upstream's 1.2.2 to match oscal-content convention) |
| Catalog UUID | 99317ca7-4bca-52d2-95ee-ccbb761f223d |
| Control count | 72 (covering all four AI RMF functions: GOVERN, MAP, MEASURE, MANAGE) |

## Sync mechanism

The vendored catalog is kept in sync via the GitHub Action at `.github/workflows/community-ai-rmf-atr-sync.yml`. The workflow:

1. Runs weekly (Mondays 06:00 UTC) or on manual dispatch.
2. Fetches the latest catalog from the upstream repository.
3. Applies the OSCAL 1.2.2 → 1.1.3 downgrade transformation defined in the workflow.
4. Diffs the result against the currently-vendored copy.
5. If different, opens a DRAFT pull request against `pre-release` (or `main` per repo default) for human review.

The workflow does NOT auto-merge. Sage maintainers (or in this repo, NIST OSCAL Team maintainers) retain editorial control over what lands in this repository.

## Downgrade transformation

The upstream community catalog is authored at OSCAL 1.2.2. This vendored copy is at OSCAL 1.1.3 to match the predominant `oscal-version` used by NIST-authored content in this repository (SP800-53, SP800-171, etc.). The downgrade is mechanical and lossless: every OSCAL feature used by this catalog is available in 1.1.3 (verified via schema validation against the published OSCAL 1.1.3 catalog schema).

Specifically, the catalog uses only the following constructs, all of which are stable in OSCAL 1.0 and forward:

- `groups`, `controls`, `parts`, `props`, `links`
- `back-matter.resources`
- `metadata.parties`, `metadata.responsible-parties`
- Custom prop namespaces under `https://github.com/Agent-Threat-Rule`

No 1.2.2-only features are used. The downgrade reduces the `metadata.oscal-version` string and refreshes the `metadata.last-modified` timestamp; no structural changes are required.

## How to manually re-sync

If the workflow has not run since an upstream change, a maintainer can manually re-sync:

```sh
cd /tmp
git clone --depth 1 https://github.com/Agent-Threat-Rule/ai-rmf-oscal-catalog
cd ai-rmf-oscal-catalog
# Apply downgrade
python3 -c "
import json
d = json.load(open('catalogs/ai-rmf-v0.4.json'))
d['catalog']['metadata']['oscal-version'] = '1.1.3'
print(json.dumps(d, indent=2))
" > /path/to/oscal-content/src/examples/catalog/json/community-ai-rmf-atr/ai-rmf-atr-catalog.json
```

Then update the upstream-version / upstream-commit fields in this SYNC.md and open a PR.

## Verification

After sync, two validations must pass:

1. **Schema validation**: the JSON catalog validates against `oscal_catalog_schema.json` from the OSCAL 1.1.3 release.
2. **Profile resolution**: all four profiles in `../../profile/json/community-ai-rmf-atr/` successfully resolve against the new catalog.

These checks are part of the `make all` build target via `validate-json-content` and `resolve-xml-profiles`.

## NIST is not responsible

The ATR community is solely responsible for the sync workflow correctness, the downgrade transformation correctness, and the upstream catalog's authoritative content. NIST has not endorsed any of these artifacts and is not responsible for their maintenance.
