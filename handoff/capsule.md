# Insight Agent – Starter Capsule (2025-09-18T01:35:18.327536+00:00)

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

- Branch: feat/bootstrap-rails
- HEAD: 80ab17910494d1e678d4f25e610056ab572085c1
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
