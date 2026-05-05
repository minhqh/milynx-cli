from pathlib import Path

def generate_docker(project_type: str = None):
    files = {
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

    for filename, content in files.items():
        path = Path(filename)

        if path.exists():
            print(f"[SKIP] {filename} already exists")
            continue

        path.write_text(content)
        print(f"[CREATED] {filename}")