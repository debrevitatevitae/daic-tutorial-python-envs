import platform  # noqa: D100
import sys
from pathlib import Path


def show_project_info():  # noqa: D103
    print("Python version:", sys.version.split()[0])
    print("Platform:", platform.system(), platform.release())
    print("Current directory:", Path.cwd())

    print("\nProject files:")
    for p in Path(".").iterdir():
        print("-", p.name)
