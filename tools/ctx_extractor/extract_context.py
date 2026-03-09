#!/usr/bin/env python3
"""
A tiny extractor to parse THE CONTEXT.txt and emit a skeleton variables.json
Usage: python tools/ctx_extractor/extract_context.py
Output: prints JSON to stdout (structure compatible with knowledge-schema.json 'variables' array)
"""
import json
from pathlib import Path

CONTEXT_PATH = Path(r"C:\Users\Puvu_Admin\OneDrive\Desktop\THE CONTEXT.txt")

SAMPLE_VARS = [
    {
        "id": "v001",
        "name": "product_type",
        "category": "Product",
        "description": "Type of product to build",
        "type": "enum",
        "options": ["marketplace", "saas", "social", "ecommerce", "internal", "content"],
        "dependencies": []
    },
    {
        "id": "v002",
        "name": "client_architecture",
        "category": "Client",
        "description": "Primary client architecture (web/ios/android/desktop/public_api)",
        "type": "enum",
        "options": ["web", "ios", "android", "desktop", "public_api"],
        "dependencies": ["v001"]
    },
    {
        "id": "v003",
        "name": "data_types",
        "category": "Data",
        "description": "Data types involved (images, video, audio, documents, realtime)",
        "type": "enum",
        "options": ["images", "video", "audio", "documents", "realtime"],
        "dependencies": ["v001"]
    }
]

def main():
    # Build a minimal output; in the future we will parse THE CONTEXT.txt fully
    out = {"variables": SAMPLE_VARS}
    print(json.dumps(out, indent=2))

if __name__ == "__main__":
    main()
