#!/usr/bin/env python3
"""Repair and merge Phase-C variable blocks into knowledge-schema.json.
This script reads the active knowledge-schema.json and all phase-C patch files,
deduplicates by id, and writes a single valid knowledge-schema.json with a
single top-level "variables" array containing all known variables.
"""
import json
import re
from pathlib import Path

BASE = Path('knowledge-schema.json')
PHASE_FILES = [
  Path('knowledge/variables/phase-c.json'),
  Path('knowledge/variables/phase-c-2.json'),
  Path('knowledge/variables/phase-c-3.json'),
]

def load_json(p: Path):
  with p.open('r', encoding='utf-8') as f:
    text = f.read()
    # naive cleanup: remove single-line comments starting with #
    text = re.sub(r'(?m)^\s*#.*\n?', '', text)
    return json.loads(text)

def save_json(obj, p: Path):
  with p.open('w', encoding='utf-8') as f:
    json.dump(obj, f, indent=2)

def main():
  if not BASE.exists():
    print('knowledge-schema.json not found')
    return
  data = load_json(BASE)
  if 'variables' not in data:
    data['variables'] = []
  existing_ids = {v['id'] for v in data['variables'] if isinstance(v, dict) and 'id' in v}

  for pf in PHASE_FILES:
    if not pf.exists():
      continue
    patch = load_json(pf)
    for v in patch.get('variables', []):
      if isinstance(v, dict) and v.get('id') not in existing_ids:
        data['variables'].append(v)
        existing_ids.add(v['id'])

  # Optional: sort by id to keep deterministic order
  data['variables'] = sorted(data['variables'], key=lambda x: int(x.get('id', '0').replace('v','')))
  save_json(data, BASE)
  print('Knowledge schema repaired and merged Phase-C blocks')

if __name__ == '__main__':
  main()
