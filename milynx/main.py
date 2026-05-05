import typer

app = typer.Typer()

@app.command()
def init(name: str):
    print(f"Init project: {name}")

@app.command()
def add(component: str):
    print(f"Add: {component}")

@app.command()
def explain():
    print("Explain config")
    
def run():
    app()

if __name__ == "__main__":
    run()