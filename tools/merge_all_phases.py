#!/usr/bin/env python3
import json
from pathlib import Path

def load_json(p: Path):
    with p.open('r', encoding='utf-8') as f:
        return json.load(f)

def save_json(obj, p: Path):
    with p.open('w', encoding='utf-8') as f:
        json.dump(obj, f, indent=2)

def merge(knowledge: dict, patch: dict):
    if 'variables' not in knowledge:
        knowledge['variables'] = []
    existing_ids = {v['id'] for v in knowledge['variables'] if isinstance(v, dict) and 'id' in v}
    for v in patch.get('variables', []):
        if isinstance(v, dict) and v.get('id') not in existing_ids:
            knowledge['variables'].append(v)
            existing_ids.add(v['id'])
    return knowledge

def main():
    knowledge_path = Path('knowledge-schema.json')
    if not knowledge_path.exists():
        print('knowledge-schema.json not found')
        return
    knowledge = load_json(knowledge_path)

    phase_files = [
        Path('knowledge/variables/phase-c.json'),
        Path('knowledge/variables/phase-c-2.json'),
        Path('knowledge/variables/phase-c-3.json'),
    ]
    for p in phase_files:
        if p.exists():
            patch = load_json(p)
            knowledge = merge(knowledge, patch)

    save_json(knowledge, knowledge_path)
    print("Merged Phase C patches into knowledge-schema.json")

if __name__ == '__main__':
    main()
