import json
import os
from pathlib import Path

CONFIG_DIR = Path.home() / ".config" / "terminai"
CONFIG_FILE = CONFIG_DIR / "config.json"

def get_config():
    if not CONFIG_FILE.exists():
        return {}
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def save_config(config):
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)

def get_api_key():
    config = get_config()
    return config.get("api_key") or os.environ.get("GEMINI_API_KEY")

def set_api_key(api_key):
    config = get_config()
    if isinstance(config, dict):
        config["api_key"] = api_key
        save_config(config)

