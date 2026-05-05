from milynx.generators.gitignore import generate as gitignore
from milynx.generators.makefile import generate as makefile
from milynx.generators.docker import generate as docker

REGISTRY = {
    "gitignore": gitignore,
    "makefile": makefile,
    "docker": docker,
}