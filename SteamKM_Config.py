# SteamKM_Config.py
from pathlib import Path
import json

CONFIG_FILE_PATH = Path("manager_settings.json").resolve()

def load_config():
    if CONFIG_FILE_PATH.exists():
        try:
            return json.loads(CONFIG_FILE_PATH.read_text())
        except json.JSONDecodeError:
            return {}
    return {}

def save_config(config):
    CONFIG_FILE_PATH.write_text(json.dumps(config, indent=4))