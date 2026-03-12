#!/usr/bin/env python3
import json
from pathlib import Path
import re

def load_clean_json(path: Path) -> dict:
    raw = path.read_text(encoding='utf-8')
    # Remove single-line comments starting with '#'
    cleaned = re.sub(r'(?m)^\s*#.*\n?', '', raw)
    return json.loads(cleaned)

def save_json(obj: dict, path: Path):
    path.write_text(json.dumps(obj, indent=2), encoding='utf-8')

def main():
    path = Path('knowledge-schema.json')
    if not path.exists():
        print('knowledge-schema.json not found')
        return
    data = load_clean_json(path)
    save_json(data, path)
    print('Cleaned knowledge-schema.json (comments removed)')

if __name__ == '__main__':
    main()
