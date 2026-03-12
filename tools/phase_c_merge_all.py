#!/usr/bin/env python3
import json
from pathlib import Path

def load_json(p: Path):
    with p.open('r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            # Try a lenient load by stripping comments
            text = f.read()
            import re
            text = re.sub(r'(?m)^\s*#.*\n?', '', text)
            return json.loads(text)

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

    patches = [
        Path('knowledge/variables/phase-c.json'),
        Path('knowledge/variables/phase-c-2.json'),
        Path('knowledge/variables/phase-c-3.json')
    ]
    for p in patches:
        if not p.exists():
            print(f'Skipping missing patch: {p}')
            continue
        patch = load_json(p)
        for v in patch.get('variables', []) or []:
            if isinstance(v, dict) and v.get('id') not in existing:
                data['variables'].append(v)
                existing.add(v['id'])

    # Sort by numeric id suffix if possible
    def keyfn(x):
        lid = x.get('id','0')
        try:
            return int(lid.strip('v'))
        except Exception:
            return 9999
    data['variables'] = sorted(data['variables'], key=keyfn)
    save_json(data, base)
    print('Phase-C blocks merged into knowledge-schema.json')

if __name__ == '__main__':
    main()
