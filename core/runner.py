# core/runner.py
import time
import traceback
from core.loader import load_callable


def run_command(config, name, args, ui):
    modules = config["modules"]
    app = config["app"]

    if name not in modules:
        raise RuntimeError(f"Command '{name}' not defined")

    module = modules[name]
    path = module["path"]
    func = module["function"]


    ui.header(f"{app['name']} · {name}")
    ui.info(f"Loading {path}:{func}")

    callable_fn = load_callable(path, func)

    start = time.time()

    try:
        with ui.progress("Executing command") as progress:
            task = progress.add_task("Working...", total=100)

            ctx = {
                "progress": lambda p: progress.update(task, completed=p),
                "log": ui.info,
            }

            callable_fn(args, ctx)

    except Exception:
        ui.error("Command failed")
        ui.console.print(traceback.format_exc())
        raise

    elapsed = time.time() - start
    ui.success(f"Completed in {elapsed:.2f}s")