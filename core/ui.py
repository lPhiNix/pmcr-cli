# core/ui.py
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn

# Clase encargada de toda la interfaz de terminal
class UI:
    def __init__(self):
        self.console = Console()

    def header(self, title):
        self.console.rule(f"[bold blue]{title}")

    def info(self, msg):
        self.console.print(f"[cyan][INFO][/cyan] {msg}")

    def error(self, msg):
        self.console.print(f"[red][ERROR][/red] {msg}")

    def fatal(self, msg):
        self.console.print(f"[bold red][FATAL][/bold red] {msg}")

    def success(self, msg):
        self.console.print(f"[green][DONE][/green] {msg}")

    def progress(self, description):
        return Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("{task.percentage:>3.0f}%"),
            console=self.console,
        )