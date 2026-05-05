from pathlib import Path
def test_docker_content(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    from milynx.generators.docker import generate

    generate({"base_image": "python:3.12-slim", "port": 5000})

    content = Path("Dockerfile").read_text()

    assert "python:3.12-slim" in content