from pathlib import Path

def detect_project_type():
    if Path("package.json").exists():
        return "node"

    if Path("pom.xml").exists():
        return "java"

    if Path("requirements.txt").exists():
        return "python"

    if Path("go.mod").exists():
        return "go"

    return "unknown"