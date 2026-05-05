from milynx.core.registry import REGISTRY
from milynx.config.presets import PRESETS
from milynx.core.detector import detect_project_type

def run_init(project_type: str | None):
    if project_type is None:
        project_type = detect_project_type()
        print(f"[INFO] Detected: {project_type}")

    components = PRESETS.get(project_type, PRESETS["base"])

    for c in components:
        add_component(c, {"project_type": project_type})
        
def add_component(name: str, context: dict):
    generator = REGISTRY.get(name)

    if not generator:
        print(f"[WARN] Unknown component: {name}")
        return

    generator(context)