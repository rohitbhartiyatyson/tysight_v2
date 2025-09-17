# Insight Agent — Starter Repo

This repository is a starter bootstrap for the Insight Agent project. It contains packaging, a Rails placeholder, handoff documentation tools, and CI configuration for smoke and e2e jobs. No Streamlit or application logic is included yet.

Quick start (local)

1. Install Python dependencies and package:

   python -m pip install --upgrade pip
   pip install -r requirements.txt
   pip install -e .

2. Run the Rails app (placeholder):

   # If you have Ruby on Rails installed
   cd rails_app || true
   rails server -b 0.0.0.0 -p 3000

   The Rails app is not provided in this bootstrap. The README documents how CI works and how to run smoke/e2e.

Testing (local)

- Smoke test:

  make install
  TEST_MODE=1 timeout 180 make smoke

- E2E test:

  TEST_MODE=1 timeout 300 make e2e

- Update handoff docs:

  make handoff-update

CI

The GitHub Actions workflow runs two jobs: `smoke` and `e2e`. The `e2e` job depends on `smoke`. Both jobs set TEST_MODE=1 and always upload artifacts from handoff/**, runs/**, logs/**.
