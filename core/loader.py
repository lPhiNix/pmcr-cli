# core/loader.py
import importlib.util
from pathlib import Path

# Carga dinámicamente un módulo y devuelve la función solicitada
def load_callable(path, func_name):
    file_path = Path(path).resolve()

    if not file_path.exists():
        raise RuntimeError(f"Command file not found: {file_path}")

    spec = importlib.util.spec_from_file_location(file_path.stem, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if not hasattr(module, func_name):
        raise RuntimeError(f"Function '{func_name}' not found in {file_path}")

    return getattr(module, func_name)