import typer
from milynx.core.engine import  add_component
from milynx.core.engine import run_init

app = typer.Typer()

@app.command()
def add(component: str):
    add_component(component)

@app.command()
def init(
    project_type: str = typer.Argument(None),
    no: str = typer.Option(None, "--no"),
    only: str = typer.Option(None, "--only")
    ):
    run_init(project_type, no, only)

def run():
    app()

if __name__ == "__main__":
    run()