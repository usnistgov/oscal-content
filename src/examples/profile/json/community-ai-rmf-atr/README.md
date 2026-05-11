# Community AI RMF profile examples

This directory contains four worked-example OSCAL profiles derived from a community-maintained OSCAL representation of the NIST AI Risk Management Framework (AI RMF 1.0).

## Status: community contribution, NOT a NIST product

These profiles are NOT authored by NIST, NOT endorsed by NIST, and NOT a NIST publication. They are community-authored worked examples submitted under the path described in [usnistgov/OSCAL#2234][issue] (Path 1, community example with no implicit endorsement). The NIST AI RMF Core (NIST AI 100-1) remains the authoritative source for the framework itself; the NIST OSCAL Team is the authoritative source for any official OSCAL representation of the AI RMF.

The OSCAL representation of the NIST AI Risk Management Framework is currently on hold at NIST due to resource constraints. This community contribution exists so that downstream OSCAL-based AI governance work can proceed against a machine-readable AI RMF representation without claiming to replace any future official NIST artifact.

[issue]: https://github.com/usnistgov/OSCAL/issues/2234

## Provenance

| Field | Value |
|---|---|
| Source repository | github.com/Agent-Threat-Rule/ai-rmf-oscal-catalog (CC0 1.0) |
| Source release | v0.4.0 |
| Profile authors | ATR community (not NIST) |
| Author contact | adam@agentthreatrule.org |
| License | CC0 1.0 (public domain) |
| OSCAL version | 1.1.3 |
| Vendored catalog | `../../../catalog/json/community-ai-rmf-atr/ai-rmf-atr-catalog.json` |
| Sync mechanism | `.github/workflows/community-ai-rmf-atr-sync.yml` (disabled by default; opt-in) |
| Last sync | See `../../../catalog/json/community-ai-rmf-atr/SYNC.md` |
| UUID derivation | Deterministic UUIDv5 over upstream catalog UUID (re-running the sync produces identical UUIDs) |
| Format | JSON canonical; XML and YAML can be generated via the existing `make all` Makefile targets if the NIST OSCAL Team prefers a different canonical format |

## Files

| File | Profile UUID | Selection | Use case |
|---|---|---|---|
| `ai-rmf-baseline-profile.json` | `6a56f56a-b1ca-539f-8b75-0915a64df13b` | `include-all` (72 controls) | Reference profile, no tier opinion |
| `ai-rmf-tier-1-foundational-profile.json` | `1a9d9829-4c56-5619-8a33-9d04dff5b683` | `with-ids` (18 controls) | Low-risk internal AI use |
| `ai-rmf-tier-2-customer-facing-profile.json` | `98740a87-821d-565e-8e44-b2452d68b005` | `with-ids` (55 controls) | AI deployed to external users |
| `ai-rmf-tier-3-high-risk-profile.json` | `85d809b3-8f48-5268-a085-95189052b156` | `include-all` (72 controls) | Regulated / safety-critical |

Tier rationale and selection criteria are documented at `TIER_RATIONALE.md` in this directory.

## Profile resolution edge-case audit

The OSCAL Profile Resolution Specification has the following open issues at the time of authoring this profile (verified against the live tracker on 2026-05-11). Each is checked against this profile and the imported catalog to confirm it does not affect resolved-catalog correctness:

- **[#2233][resolution-2233]** Profile resolution `as-is` import-type can yield invalid catalogs. Not applicable: these profiles use `include-controls`, not `as-is`.
- **[#2231][resolution-2231]** Profile syntax does not provide for group-ID collision. Not applicable: the imported catalog uses unique group IDs (`ai-rmf-gv`, `ai-rmf-mp`, `ai-rmf-ms`, `ai-rmf-mg` with numbered subgroups).
- **[#2166][resolution-2166]** Profile resolution test for `merge` functionality fails. Not applicable: these profiles use `merge.flat`, not `merge.combine`.
- **[#1314][resolution-1314]** Profile resolution clarification on pruning. Not applicable: every selected control is fully retained without pruning ambiguity.

The audit is reproduced in `metadata.remarks` of each profile so reviewers can verify without consulting external documentation.

If the NIST OSCAL Team maintains a broader list of known edge cases for Profile Resolution Specification compliance, the contributor commits to extending this audit to cover them before requesting non-draft status. Please reference any specific edge-case-tracking document in PR review comments.

[resolution-2233]: https://github.com/usnistgov/OSCAL/issues/2233
[resolution-2231]: https://github.com/usnistgov/OSCAL/issues/2231
[resolution-2166]: https://github.com/usnistgov/OSCAL/issues/2166
[resolution-1314]: https://github.com/usnistgov/OSCAL/issues/1314

## Disclaimers (this is the human-readable mirror of the per-profile remarks)

1. **Not NIST**. No NIST employee, contractor, or partner authored these profiles. No NIST endorsement is implied. NIST publications are NIST authoritative; community artifacts are not. The placement of these files inside the `usnistgov/oscal-content` repository does not constitute NIST endorsement; the NIST OSCAL Team decides what is endorsed by deciding what to merge, not by receiving a contribution.

2. **Not a baseline**. Tier 1 / Tier 2 / Tier 3 selections are illustrative worked examples derived from the community catalog. They are not normative AI RMF baselines. Organizations adopting these as starting points should evaluate their own context.

3. **CC0 public domain**. These files carry no copyright restriction. Users may copy, modify, and redistribute freely. The CC0 dedication appears in `LICENSE.md` in this directory and in `metadata.remarks` of each profile.

4. **Sync responsibility**. The vendored catalog is kept in sync via the workflow at `.github/workflows/community-ai-rmf-atr-sync.yml`. The workflow opens DRAFT pull requests for review; it does not auto-merge. NIST is not responsible for sync correctness.

5. **Subject to upstream**. The NIST OSCAL Team retains full authority over what merges to `main`. This contribution is offered without precondition.

## Imports

Each profile imports the vendored AI RMF community catalog at `../../../catalog/json/community-ai-rmf-atr/ai-rmf-atr-catalog.json`. The catalog reproduces the AI RMF Core statement text and the AI RMF Playbook guidance per control, with Core wording taking precedence where the two diverge (see upstream remediation proposals at the source repository).

## Profile resolution behavior

The four profiles use OSCAL Profile Resolution Specification semantics as follows:

- **Baseline**: `include-all`, `merge.flat`. Produces a resolved catalog containing all 72 AI RMF controls with the canonical Core statement text.
- **Tier 1**: `include-controls` with explicit 18 control IDs. Produces a subset catalog suitable for low-risk internal AI use cases.
- **Tier 2**: `include-controls` with explicit 55 control IDs. Produces a superset of Tier 1 covering customer-facing AI risk surface.
- **Tier 3**: `include-all`, `merge.flat`. Same control set as Baseline; the difference is contextual framing in the profile metadata for high-risk deployment.

A tier-subset invariant (Tier 1 ⊂ Tier 2 ⊂ Baseline) is enforced by the test at `tests/test_tier_subset_invariant.py`.

## Validation

Source files in this directory validate against the OSCAL 1.1.3 catalog and profile schemas published at:

- https://github.com/usnistgov/OSCAL/releases/tag/v1.1.3
- `oscal_catalog_schema.json` (for the imported catalog)
- `oscal_profile_schema.json` (for these profiles)

Local validation runs via the `oscal-cli` tool downloaded during `make dependencies`. The CI workflow `.github/workflows/content-artifacts.yml` validates this content as part of every PR.
