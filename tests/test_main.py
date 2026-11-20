#!/usr/bin/env python3
"""Tests for main.py (standard library only).

Run from the repository root:
    python3 -m unittest discover -s tests -v
"""

import hashlib
import os
import struct
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIN = os.path.join(ROOT, "main.py")
ENTRY = os.path.join(ROOT, "entry.png")


def png_size(path):
    with open(path, "rb") as fh:
        head = fh.read(33)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG file")
    width, height = struct.unpack(">II", head[16:24])
    return width, height


class TestMain(unittest.TestCase):
    def run_main(self, out_dir):
        env = dict(os.environ)
        env["MAKEFUN_OUTPUT_DIR"] = out_dir
        proc = subprocess.run(
            [sys.executable, "-P", "-s", MAIN],
            env=env, capture_output=True, text=True, timeout=60,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        return os.path.join(out_dir, "entry.png")

    def test_copies_entry_byte_for_byte(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = self.run_main(tmp)
            self.assertTrue(os.path.exists(out))
            with open(ENTRY, "rb") as fh:
                want = fh.read()
            with open(out, "rb") as fh:
                got = fh.read()
            self.assertEqual(got, want)
            self.assertEqual(
                hashlib.sha256(got).hexdigest(),
                hashlib.sha256(want).hexdigest(),
            )

    def test_two_runs_are_byte_identical(self):
        with tempfile.TemporaryDirectory() as a, \
                tempfile.TemporaryDirectory() as b:
            out_a = self.run_main(a)
            out_b = self.run_main(b)
            with open(out_a, "rb") as fh:
                data_a = fh.read()
            with open(out_b, "rb") as fh:
                data_b = fh.read()
            self.assertEqual(data_a, data_b)

    def test_output_is_a_valid_1024x1024_png_under_1mib(self):
        self.assertLessEqual(os.path.getsize(ENTRY), 1024 * 1024)
        width, height = png_size(ENTRY)
        self.assertEqual((width, height), (1024, 1024))


if __name__ == "__main__":
    unittest.main()
