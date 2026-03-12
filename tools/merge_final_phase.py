#!/usr/bin/env python3
import json
from pathlib import Path

def load_json(p: Path):
  with p.open('r', encoding='utf-8') as f:
    try:
      return json.load(f)
    except json.JSONDecodeError:
      text = f.read()
      try:
        return json.loads(text)
      except json.JSONDecodeError:
        return {}

def save_json(obj, p: Path):
  p.write_text(json.dumps(obj, indent=2), encoding='utf-8')

def main():
  base = Path('knowledge-schema.json')
  if not base.exists():
    print('knowledge-schema.json not found')
    return
  data = load_json(base)
  if 'variables' not in data or not isinstance(data['variables'], list):
    data['variables'] = []
  existing = {v.get('id') for v in data['variables'] if isinstance(v, dict) and 'id' in v}

  phase_files = [Path('knowledge/variables/phase-c.json'), Path('knowledge/variables/phase-c-2.json'), Path('knowledge/variables/phase-c-3.json')]
  for pf in phase_files:
    if pf.exists():
      patch = load_json(pf)
      for v in patch.get('variables', []) or []:
        if isinstance(v, dict) and v.get('id') not in existing:
          data['variables'].append(v)
          existing.add(v.get('id'))

  # try to order by numeric id suffix if possible
  def keyfn(x):
    lid = str(x.get('id','0'))
    if lid.startswith('v'):
      try:
        return int(lid[1:])
      except ValueError:
        return 9999
    return 9999
  data['variables'] = sorted(data['variables'], key=keyfn)
  save_json(data, base)
  print("Merged phase-c blocks into knowledge-schema.json (final)")

if __name__ == '__main__':
  main()
