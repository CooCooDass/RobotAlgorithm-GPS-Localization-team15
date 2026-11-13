"""Check the Python environment for the Week 1 project."""

import platform
import sys


def main() -> int:
    print(f"Python: {platform.python_version()}")
    print(f"OS: {platform.system()}")
    if sys.version_info < (3, 10):
        print("Python 3.10 or newer is required.", file=sys.stderr)
        return 1
    print("Python environment check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
