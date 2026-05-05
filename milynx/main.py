import typer
from milynx.core.engine import init_project, add_component

app = typer.Typer()

@app.command()
def init(project_type: str):
    init_project(project_type)

@app.command()
def add(component: str):
    add_component(component)

def run():
    app()

if __name__ == "__main__":
    run()