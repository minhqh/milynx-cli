from jinja2 import Environment, FileSystemLoader
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = BASE_DIR / "templates"

env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))


def render(component: str, file_name: str, context: dict):
    template_path = f"{component}/{file_name}.j2"
    template = env.get_template(template_path)
    return template.render(**context)