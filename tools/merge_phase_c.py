#!/usr/bin/env python3
import json
from pathlib import Path

def main():
    knowledge_path = Path('knowledge-schema.json')
    phase_c_path = Path('knowledge/variables/phase-c.json')
    if not knowledge_path.exists():
        print('knowledge-schema.json not found')
        return
    if not phase_c_path.exists():
        print('phase-c.json not found')
        return
    with knowledge_path.open('r', encoding='utf-8') as f:
        data = json.load(f)
    with phase_c_path.open('r', encoding='utf-8') as f:
        patch = json.load(f)
    phase_vars = patch.get('variables', [])
    if 'variables' not in data:
        data['variables'] = []
    existing_ids = {v.get('id') for v in data['variables']}
    for v in phase_vars:
        if v.get('id') and v['id'] not in existing_ids:
            data['variables'].append(v)
            existing_ids.add(v['id'])
    with knowledge_path.open('w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print('Merged Phase C variables into knowledge-schema.json')

if __name__ == '__main__':
    main()
