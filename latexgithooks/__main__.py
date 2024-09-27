from typing import Optional

import typer
from rich.console import Console
from rich.table import Table
from typing_extensions import Annotated

from . import __description__
from .version import package_summary, package_version

app = typer.Typer(help=__description__)
console = Console()


@app.command()
def version(
    verbose: Annotated[
        Optional[bool],
        typer.Option(prompt=False, help="Verbose options for exceptions"),
    ] = False,
):
    """Shows package version"""

    if not verbose:
        console.print(f"Version: ", style="white", end=None)
        console.print(f"{package_version()}", style="yellow")
    else:
        table = Table()
        table.add_column("Field", justify="right", style="cyan", no_wrap=True)
        table.add_column("Value", justify="left", style="yellow", no_wrap=True)
        summary = package_summary()
        for item in summary:
            table.add_row(item["field"], item["value"])
        console.print(table)


if __name__ == "__main__":
    app()
