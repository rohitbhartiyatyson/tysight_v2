# Insight Agent – Starter Capsule (2025-09-18T02:01:47.657184+00:00)

Objective

This repository provides a minimal bootstrap for the Insight Agent: packaging, Rails placeholder, handoff documentation tooling, and CI scaffolding for smoke and e2e checks.

Core constraints

- NL prompt: selected Kind only, present columns only, ≤2 micro-examples.
- No joins (v1); must LIMIT; no SELECT *; mapped/present columns only.
- Market & Time filters default to "All".
- Auto-fill at Kind creation: format_hint + unit only (hints).
- No instance-level overrides of Nice fields.
- Allowed values for dropdowns come from the actual Instance (observed distincts; cap ~200).
- Additivity rule: if is_additive = no, forbid SUM(col).

What's implemented

- Rails + Handoff only (bootstrap)

Pending next

- Streamlit skeleton; Kinds Manager v1; Instance onboarding v1; Ask (NL→SQL) v1

Current status

- Branch: feat/ci-and-bundle
- HEAD: a28dd1a19d444ab5b3fc0630adf0467efeb3c502
- CI: smoke: unknown, e2e: unknown
- UI: n/a
- Last run: n/a

Pointers

- handoff/capsule.md
- handoff/status.json
- handoff/spec_extract.md
- handoff/new_chat_bundle.md

How to reproduce quickly

1. python -m pip install --upgrade pip
2. pip install -r requirements.txt && pip install -e .
3. TEST_MODE=1 timeout 180 make smoke
4. TEST_MODE=1 timeout 300 make e2e

---
# Master Spec (Seed)

This is a seed outline of the product plan and architecture.

1. Architecture
- Rails backend (placeholder)
- Handoff documentation tools (Python)

2. Flows
- Kinds creation and validation
- Instance onboarding
- NL -> SQL translation rules

3. NL->SQL rules
- Only selected Kind, present columns
- No joins (v1), LIMIT required, no SELECT *
- Default filters: Market = All, Time = All

4. Validator rules and telemetry
- Column mapping validation
- Distincts cap for dropdowns



---

(Summary extract)
