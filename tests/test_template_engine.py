from milynx.core.template_engine import render

def test_render_dockerfile():
    result = render(
        "docker",
        "Dockerfile",
        {"base_image": "python:3.11-slim"}
    )

    assert "FROM python:3.11-slim" in result