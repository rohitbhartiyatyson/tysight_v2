from pathlib import Path
if __name__==__main__:
    out=Path('handoff/new_chat_bundle.md'); cap=Path('handoff/capsule.md'); spec=Path('handoff/spec_extract.md'); out.parent.mkdir(parents=True, exist_ok=True); cap_t=cap.read_text() if cap.exists() else ; spec_t=spec.read_text() if spec.exists() else ; out.write_text(cap_t+
---
+spec_t)