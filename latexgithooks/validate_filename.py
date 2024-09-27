import re
from pathlib import Path
from typing import List, Optional

import typer
from typing_extensions import Annotated

app = typer.Typer(help="__description__")


@app.command()
def validate(
    filenames: Annotated[
        List[str],
        typer.Option(prompt=False, help="Filenames to validate."),
    ] = [],
    min_len: Annotated[
        Optional[int],
        typer.Option(prompt=False, help="Minimum length for a filename."),
    ] = 3,
) -> None:
    """
    Tool for validating filenames meet certain requirements.
    """
    SNAKE_CASE_REGEX = re.compile(r"^[a-z_]+$")

    for filename in filenames:
        name = Path(filename).stem

        if len(name) < min_len:
            typer.echo(f"Name too short ({min_len=}): {filename}", err=True)

        if not SNAKE_CASE_REGEX.match(name):
            typer.echo(f"Filename is not in snake case: {filename}", err=True)


if __name__ == "__main__":
    app()
