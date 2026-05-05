from milynx.core.registry import REGISTRY

def add_component(name: str, project_type: str = None):
    generator = REGISTRY.get(name)

    if not generator:
        print(f"[WARN] Unknown component: {name}")
        return

    generator(project_type)