# core/config.py
import configparser
from pathlib import Path

def _load_cfg(path: str) -> configparser.ConfigParser:
    cfg_path = Path(path)

    if not cfg_path.exists():
        raise RuntimeError(f"Configuration file not found: {path}")

    parser = configparser.ConfigParser()
    parser.read(cfg_path)

    return parser


def load_app_config(path: str) -> dict:
    """
    Load and validate cli.cfg
    """
    cfg = _load_cfg(path)

    if "app" not in cfg:
        raise RuntimeError("Missing [app] section in cli.cfg")

    app = cfg["app"]

    required_keys = ("name", "version", "description")
    for key in required_keys:
        if key not in app or not app[key].strip():
            raise RuntimeError(f"Missing or empty '{key}' in [app] section")

    return {
        "name": app["name"],
        "version": app["version"],
        "description": app["description"],
    }


def load_modules_config(path: str) -> dict:
    """
    Load and validate modules_config.cfg
    """
    cfg = _load_cfg(path)

    if "modules" not in cfg:
        raise RuntimeError("Missing [modules] section in modules_config.cfg")

    modules = cfg["modules"]

    if not modules:
        raise RuntimeError("No modules defined in modules_config.cfg")

    parsed_modules = {}

    for name, target in modules.items():
        if ":" not in target:
            raise RuntimeError(
                f"Invalid module definition for '{name}'. "
                "Expected format: path/to/file.py:function"
            )

        path_part, func_part = target.split(":", 1)

        if not path_part or not func_part:
            raise RuntimeError(
                f"Invalid module definition for '{name}'. "
                "Path and function must be non-empty"
            )

        parsed_modules[name] = {
            "path": path_part,
            "function": func_part,
        }

    return parsed_modules


def load_config(app_cfg_path: str, modules_cfg_path: str) -> dict:
    """
    Load full application configuration
    """
    app_config = load_app_config(app_cfg_path)
    modules_config = load_modules_config(modules_cfg_path)

    return {
        "app": app_config,
        "modules": modules_config,
    }