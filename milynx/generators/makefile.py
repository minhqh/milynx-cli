from pathlib import Path

def generate_makefile(project_type: str = None):
    content = """build:
\tpython main.py

test:
\tpytest

run:
\tpython main.py
"""

    path = Path("Makefile")

    if path.exists():
        print("[SKIP] Makefile already exists")
        return

    path.write_text(content)
    print("[CREATED] Makefile")