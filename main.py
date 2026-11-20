#!/usr/bin/env python3
"""Entry point for the make.fun news-image-20261120-v2 submission.

Copies the pre-rendered entry.png (drawn at authoring time by render.py)
byte-for-byte to the harness output directory. Pure standard library:
no network, no third-party packages, deterministic output.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SRC, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
