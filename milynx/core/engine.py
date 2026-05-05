from milynx.generators.gitignore import generate_gitignore
from milynx.utils.file_io import write_file

def init_project(project_type: str):
    print(f"Init project: {project_type}")

    gitignore = generate_gitignore(project_type)
    write_file(".gitignore", gitignore)