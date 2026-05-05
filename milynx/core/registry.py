from milynx.generators.gitignore import generate_gitignore
from milynx.generators.docker import generate_docker
from milynx.generators.makefile import generate_makefile

REGISTRY = {
    "gitignore": generate_gitignore,
    "docker": generate_docker,
    "makefile": generate_makefile,
}