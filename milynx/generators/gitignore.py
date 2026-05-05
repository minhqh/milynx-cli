from pathlib import Path

TEMPLATE_MAP = {
    "python": "python.txt",
    "node": "node.txt",
    "java": "java.txt",
    "go": "go.txt",
    "default": "general.txt"
}

def generate_gitignore(project_type: str):
    template_file = TEMPLATE_MAP.get(project_type, TEMPLATE_MAP["default"])

    template_path = Path(__file__).parent.parent / "templates/gitignore" / template_file

    with open(template_path, "r") as f:
        content = f.read()

    return content