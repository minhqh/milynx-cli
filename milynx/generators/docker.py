from pathlib import Path

def generate(context: dict):
    project_type = context.get("project_type", "python")

    content = {
        "Dockerfile": """FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
""",

        ".dockerignore": """__pycache__/
*.pyc
.venv/
""",

        "docker-compose.yml": """version: '3.8'
services:
  app:
    build: .
    ports:
      - "8000:8000"
"""
    }

    path = Path("Dockerfile")

    if path.exists():
        print("[SKIP] Dockerfile already exists")
        return

    path.write_text(content)
    print("[CREATED] Dockerfile")