from pathlib import Path

def write_file(path: str, content: str):
    file_path = Path(path)

    # tránh overwrite nguy hiểm
    if file_path.exists():
        print(f"[SKIP] {path} already exists")
        return

    file_path.write_text(content)
    print(f"[CREATED] {path}")