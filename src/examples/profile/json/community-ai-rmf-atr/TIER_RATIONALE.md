# Tier selection rationale

This document explains the control selection criteria for each of the three tier profiles. It is informational, not normative. The selections are the work of the ATR community and have not been reviewed or endorsed by NIST.

## Overview

| Profile | Controls | Selection mechanism | Use case |
|---|---|---|---|
| Baseline | 72 | `include-all` | Reference, neutral framing |
| Tier 1 (foundational) | 18 | `include-controls` with explicit IDs | Low-risk internal AI use |
| Tier 2 (customer-facing) | 55 | `include-controls` with explicit IDs | AI deployed to external users |
| Tier 3 (high-risk) | 72 | `include-all` | Regulated, safety-critical deployment |

Subset relationship enforced by `tests/test_tier_subset_invariant.py`:

```
Tier 1 ⊂ Tier 2 ⊂ Baseline = Tier 3
```

Tier 1 controls are a strict subset of Tier 2. Tier 2 controls are a strict subset of Baseline. Tier 3 and Baseline have identical control sets; the difference is contextual framing in profile metadata for organizations interpreting "high-risk" under regulatory regimes (EU AI Act, Colorado AI Act).

## Tier 1 (foundational) — 18 controls

**Target audience**: Organizations using AI for internal-only purposes with limited customer exposure (analytics, internal knowledge bases, productivity tools). Risk surface is bounded; AI failure does not impact external users or regulated decisions.

**Inclusion criteria**: Controls that are minimum hygiene for ANY production AI system. Controls about governance basics, model evaluation, and incident response.

**Control selection** (with AI RMF function):
- GV-1.1 Legal compliance posture
- GV-1.2 AI risk management goals
- GV-2.1 Roles and responsibilities
- GV-3.1 Workforce diversity (governance prerequisite)
- GV-4.1 Risk culture
- MP-1.1 Define context and scope
- MP-1.2 Map system stakeholders
- MP-2.1 Identify AI system tasks
- MP-3.1 Map data and inputs
- MS-1.1 Identify model evaluation approach
- MS-2.1 Test approach selected
- MS-2.5 Model accuracy
- MG-1.1 Risk treatment plan
- MG-1.2 Risk prioritization
- MG-1.3 Risk response
- MG-2.1 Risk allocation
- MG-2.2 Risk awareness
- MG-4.1 Continuous monitoring approach

**Rationale for exclusions** at Tier 1:
- Most fairness/bias controls deferred to Tier 2 (only matter when external users see decisions)
- Most explainability controls deferred to Tier 2 (only matter when external users can ask why)
- Most privacy controls deferred to Tier 2 (Tier 1 assumes internal data)
- Most third-party / value-chain controls deferred to Tier 2
- Most post-deployment monitoring controls deferred to Tier 2 / Tier 3

## Tier 2 (customer-facing) — 55 controls

**Target audience**: Organizations deploying AI to external users (web/mobile apps, chatbots, AI-powered features in consumer products). AI failure becomes visible to non-technical end users; regulatory scrutiny increases.

**Inclusion criteria**: Tier 1 (18) plus 37 additional controls covering:
- Fairness, bias, and explainability (10 controls)
- Privacy and data subject rights (6 controls)
- Post-deployment monitoring and feedback loops (8 controls)
- Third-party and value-chain risk (6 controls)
- Documentation and human oversight (7 controls)

Tier 2 covers the typical surface for AI-enabled SaaS, consumer AI, and customer-service AI.

**Rationale for exclusions** at Tier 2:
- High-risk-specific controls (life-safety, regulated-decision authorization) deferred to Tier 3
- Detailed third-party audit obligations deferred to Tier 3 where regulated context applies

## Tier 3 (high-risk) — 72 controls

**Target audience**: Organizations deploying AI in regulated, safety-critical, or rights-affecting decisions (healthcare AI, financial-decisioning AI, public-sector AI, AI used in employment/credit/housing per US discrimination law and EU AI Act high-risk categorization).

**Selection mechanism**: `include-all`. Every AI RMF control applies.

The difference between Tier 3 and Baseline is framing, not control set. Tier 3 profile metadata documents the high-risk deployment context for compliance teams that need a context-specific OSCAL profile for use in System Security Plans (SSPs) or Assessment Plans (APs).

## Methodology notes

These tier selections were made by the ATR community against ATR's own internal benchmark of AI detection rules and compliance mapping data. The methodology is documented at the upstream catalog repository: https://github.com/Agent-Threat-Rule/ai-rmf-oscal-catalog

The tier selections are NOT a NIST recommendation. Organizations should evaluate their own risk surface and consult appropriate compliance counsel before adopting any tier as a basis for their AI risk management program.

## Profile resolution semantics

When you run a profile resolution tool (e.g. `oscal-cli profile resolve`) against any of these four profiles, the output is a resolved catalog containing the selected subset of AI RMF controls with full statement text, props, parts, and links from the upstream catalog. The resolved catalog is suitable as input to OSCAL System Security Plans or Component Definitions.

The resolved catalogs are NOT committed to this repository; they are generated on demand by the OSCAL build pipeline (`make resolve-xml-profiles`).
