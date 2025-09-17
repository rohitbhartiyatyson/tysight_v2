#!/usr/bin/env python3
import os
import json
import subprocess
from datetime import datetime, timezone

os.makedirs('handoff', exist_ok=True)

def git_head():
    try:
        head = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode().strip()
        branch = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).decode().strip()
        return head, branch
    except Exception:
        return None, None

head, branch = git_head()
status = {
    'repo_head': head or 'HEAD',
    'branch': branch or 'HEAD',
    'ci': {'smoke': 'unknown', 'e2e': 'unknown'},
    'ui': {'running': False, 'last_port': None, 'log': None},
    'updated_at': datetime.now(timezone.utc).isoformat(),
}
with open('handoff/status.json', 'w') as f:
    json.dump(status, f, indent=2)
print('wrote handoff/status.json')
