# src/utils/config.py

import yaml
import os

CONFIG_PATH = os.path.join("config", "config.yaml")

def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)

# Carrega uma vez e deixa disponível
CONFIG = load_config()
