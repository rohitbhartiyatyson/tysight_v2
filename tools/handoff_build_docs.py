#!/usr/bin/env python3
from pathlib import Path
import os

os.makedirs('handoff', exist_ok=True)
master = Path('handoff/master_spec.md')
if not master.exists():
    master.write_text("""# Master Spec (Seed)

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

""")
spec = Path('handoff/spec_extract.md')
spec.write_text(master.read_text() + "\n\n---\n\n(Summary extract)\n")
# assemble new_chat_bundle
caps = Path('handoff/capsule.md')
if caps.exists():
    (Path('handoff/new_chat_bundle.md')).write_text(caps.read_text() + "\n---\n" + spec.read_text())
print('wrote handoff docs')
