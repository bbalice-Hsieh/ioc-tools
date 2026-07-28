#!/usr/bin/env python3

import hashlib
import sys

def sha256sum(filename):
    h = hashlib.sha256()

    with open(filename, "rb") as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            h.update(chunk)

    return h.hexdigest()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python hash-checker.py <file>")
        sys.exit(1)

    print("SHA256:", sha256sum(sys.argv[1]))
