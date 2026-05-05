from pathlib import Path

def generate(context: dict):
    project_type = context.get("project_type", "python")

    templates = {
        "python": "__pycache__/\n.venv/\n*.pyc\n",
        "java": "target/\n*.class\n",
        "node": "node_modules/\n"
    }

    content = templates.get(project_type, templates["python"])

    path = Path(".gitignore")

    if path.exists():
        print("[SKIP] .gitignore already exists")
        return

    path.write_text(content)
    print("[CREATED] .gitignore")