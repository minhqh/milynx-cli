from milynx.generators.gitignore import generate_gitignore
from milynx.utils.file_io import write_file
from milynx.generators.docker import generate_docker

def init_project(project_type: str):
    print(f"Init project: {project_type}")

    gitignore = generate_gitignore(project_type)
    write_file(".gitignore", gitignore)

def add_component(name: str):
    if name == "docker":
        generate_docker()

    elif name == "gitignore":
        generate_gitignore()

    else:
        print(f"[WARN] Unknown component: {name}")