from pathlib import Path
from milynx.generators.docker import generate

def test_generate_docker(tmp_path, monkeypatch):
    # change working dir to temp
    monkeypatch.chdir(tmp_path)

    context = {
        "base_image": "python:3.11-slim",
        "port": 8000
    }

    generate(context)

    assert Path("Dockerfile").exists()
    assert Path("docker-compose.yml").exists()
    assert Path(".dockerignore").exists()