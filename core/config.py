import configparser
from pathlib import Path

# Carga y valida el archivo settings.cfg
def load_config(path):
    cfg_path = Path(path)

    if not cfg_path.exists():
        raise RuntimeError("Configuration file not found. Add settings.cfg to your folder.")

    parser = configparser.ConfigParser()
    parser.read(cfg_path)

    if "app" not in parser:
        raise RuntimeError("Missing [app] section")

    if "modules" not in parser:
        raise RuntimeError("Missing [modules] section")

    if not parser["modules"]:
        raise RuntimeError("No modules defined")

    return parser
