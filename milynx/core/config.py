import json
from pathlib import Path

CONFIG_FILE = ".milynxrc"

def load_config():
    if not Path(CONFIG_FILE).exists():
        return None

    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)