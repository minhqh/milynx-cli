import typer
from milynx.core.engine import  add_component

app = typer.Typer()

@app.command()
def add(component: str):
    add_component(component)

@app.command()
def init(project_type: str):
    add_component("gitignore", project_type)
    add_component("makefile", project_type)
    add_component("docker", project_type)

def run():
    app()

if __name__ == "__main__":
    run()