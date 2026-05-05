from pathlib import Path
from milynx.core.template_engine import render


def generate(context: dict):
    files = {
        "Dockerfile": render(
            "docker",
            "Dockerfile",
            {
                "base_image": context.get("base_image", "python:3.11-slim")
            }
        ),

        "docker-compose.yml": render(
            "docker",
            "docker-compose.yml",
            {
                "port": context.get("port", 8000)
            }
        ),

        ".dockerignore": render(
            "docker",
            "dockerignore",
            {}
        )
    }

    for filename, content in files.items():
        path = Path(filename)

        if path.exists():
            print(f"[SKIP] {filename}")
            continue

        path.write_text(content, encoding="utf-8")
        print(f"[CREATED] {filename}")