# pmcr.py
import sys
from core.config import load_config
from core.runner import run_command
from core.ui import UI

def main():
    ui = UI()

    try:
        config = load_config("cli.cfg", "modules_config.cfg")
    except Exception as e:
        ui.fatal(str(e))
        sys.exit(1)

    app = config["app"]
    app_name = app["name"]

    if len(sys.argv) < 2:
        ui.error("No command specified")
        ui.info(f"Usage: {app_name} <command> [args]")
        sys.exit(1)

    command_name = sys.argv[1]
    command_args = sys.argv[2:]

    try:
        run_command(config, command_name, command_args, ui)
    except Exception as e:
        ui.fatal(str(e))
        input("Press ENTER to exit...")
        sys.exit(1)


if __name__ == "__main__":
    main()