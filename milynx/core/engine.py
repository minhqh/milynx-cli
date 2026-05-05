from milynx.core.registry import REGISTRY
from milynx.config.presets import PRESETS
from milynx.core.detector import detect_project_type

def ask_yes_no(question: str) -> bool:
    answer = input(f"{question} (y/n): ").strip().lower()
    return answer in ["y", "yes"]    

def run_init(
    project_type: str | None,
    wizard: bool,
    no: str | None,
    only: str | None
    ):
    
    if project_type is None:
        project_type = detect_project_type()
        print(f"[INFO] Detected: {project_type}")

    components = PRESETS.get(project_type, PRESETS["base"])

    components = set(components)

    # 1. ONLY mode (override everything)
    if only:
        allowed = set(only.split(","))
        components = components.intersection(allowed)

    # 2. NO mode (remove components)
    if no:
        removed = set(no.split(","))
        components = components - removed

    # execute
    if wizard:
        final = []
        for c in components:
            if ask_yes_no(f"Include {c}?"):
                final.append(c)
        components = final
    
    for c in components:
        add_component(c, {"project_type": project_type})

def add_component(name: str, context: dict):
    generator = REGISTRY.get(name)

    if not generator:
        print(f"[WARN] Unknown component: {name}")
        return

    generator(context)