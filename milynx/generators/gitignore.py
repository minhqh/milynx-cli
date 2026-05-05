from pathlib import Path

def generate_gitignore(project_type: str = None):
    content_map = {
        "python": "__pycache__/\n.venv/\n*.pyc\n.env\n",
        "java": "target/\n*.class\n.idea/\n",
        "node": "node_modules/\n.env\n"
    }

    content = content_map.get(project_type, content_map["python"])

    path = Path(".gitignore")

    if path.exists():
        print("[SKIP] .gitignore already exists")
        return

    path.write_text(content)
    print("[CREATED] .gitignore")