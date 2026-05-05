from milynx.core.registry import REGISTRY

def add_component(name: str, context: dict):
    generator = REGISTRY.get(name)

    if not generator:
        print(f"[WARN] Unknown component: {name}")
        return

    generator(context)