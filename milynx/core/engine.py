from milynx.core.registry import REGISTRY
from milynx.config.presets import PRESETS
from milynx.core.detector import detect_project_type
from milynx.core.config import load_config

def ask_yes_no(question: str) -> bool:
    answer = input(f"{question} (y/n): ").strip().lower()
    return answer in ["y", "yes"]    

def run_init(
    project_type: str | None,
    wizard: bool,
    no: str | None,
    only: str | None
    ):
    
    config = load_config()

    # 1. detect / default
    if project_type is None:
        project_type = detect_project_type()
        print(f"[INFO] Detected: {project_type}")

    components = PRESETS.get(project_type, PRESETS["base"])
    components = set(components)

    # =========================
    #  2. CONFIG LAYER (soft apply)
    # =========================
    if config:
        config_components = config.get("components", {})
        enabled = {k for k, v in config_components.items() if v}

        if enabled:
            components = components.intersection(enabled)

    # =========================
    # 3. CLI FLAGS (HIGHEST PRIORITY)
    # =========================
    if only:
        allowed = set(only.split(","))
        components = components.intersection(allowed)

    if no:
        removed = set(no.split(","))
        components = components - removed

    # =========================
    # WIZARD (optional)
    # =========================
    if wizard:
        final = []
        for c in components:
            ans = input(f"Include {c}? (y/n): ")
            if ans.lower() in ["y", "yes"]:
                final.append(c)
        components = final
    
    # =========================
    # EXECUTE
    # =========================
    for c in components:
        add_component(c, {"project_type": project_type})

def add_component(name: str, context: dict):
    generator = REGISTRY.get(name)

    if not generator:
        print(f"[WARN] Unknown component: {name}")
        return

    generator(context)