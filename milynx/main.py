import typer
from milynx.core.engine import  add_component
from milynx.core.detector import detect_project_type

app = typer.Typer()

@app.command()
def add(component: str):
    add_component(component)

@app.command()
def init(project_type: str = typer.Argument(None)):
    if project_type is None:
        project_type = detect_project_type()
        print(f"[INFO] Detected project type: {project_type}")
    else:
        print(f"[INFO] Using manual project type: {project_type}")

    context = {"project_type": project_type}

    add_component("gitignore", context)
    add_component("makefile", context)
    add_component("docker", context)

def run():
    app()

if __name__ == "__main__":
    run()