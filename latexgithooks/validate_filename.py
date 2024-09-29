__description__ = "Tool for validating TeX filenames meet certain requirements"

import re
import sys
import traceback
from pathlib import Path
from typing import List, Optional

import typer
from typing_extensions import Annotated


def preprocess_args():
    """
    Based on https://github.com/fastapi/typer/issues/554#issuecomment-2323176039
    Typer doesn't support whitespace-separated multi-value options.

    We preprocess the sysargv so that:
    - python3 app.py some_command --filters filter1 filter2 filter3 --environments env1 env2 env3

    becomes:
    - python3 app.py some_command --filters filter1 --filters filter2 --filters filter3 --environments env1 --environments env2 --environments env3

    //!\\ DOWNSIDE: options should always be after arguments in the CLI command //!\\
    """
    print("-" * 30, "\n")
    # get main cmd
    final_cmd = []
    for idx, arg in enumerate(sys.argv):
        if any(arg.startswith(_) for _ in ["-", "--"]):
            break
        else:
            final_cmd.append(arg)
    print(f"Main command is: {final_cmd}")

    # get options and their values
    for idx, arg in enumerate(sys.argv):
        if any(arg.startswith(_) for _ in ["-", "--"]):
            opt_values = []
            for value in sys.argv[idx + 1 :]:
                if any(value.startswith(_) for _ in ["-", "--"]):
                    break
                else:
                    opt_values.append(value)

            if len(opt_values) >= 1:
                [final_cmd.extend([arg, opt_value]) for opt_value in opt_values]
            else:
                final_cmd.append(arg)

    # replace by reformatted
    print(f"Final command is: {final_cmd}")
    sys.argv = final_cmd


preprocess_args()
app = typer.Typer(help=__description__)


def has_mixed_case(input_string: str) -> bool:
    """ "Checks if an input string contains both uppercase and lowercase letters.

    Args:
        input_string (str): The input string to check.

    Returns:
        bool:  True if the input string contains both uppercase and lowercase letters, False otherwise.
    """

    has_uppercase = any(char.isupper() for char in input_string)
    has_lowercase = any(char.islower() for char in input_string)

    return has_uppercase and has_lowercase


@app.command()
def validate(
    min_len: Annotated[
        Optional[int],
        typer.Option(prompt=False, help="Minimum length for a filename."),
    ] = 4,
    verbose: Annotated[
        Optional[bool],
        typer.Option(prompt=False, help="Prints additional information"),
    ] = True,
    filenames: List[str] = typer.Option([], help="List of filenames to validate"),
) -> None:
    """
    Method for validating TeX filenames meet certain requirements.
    """

    # SNAKE_CASE_REGEX = re.compile(r"^[a-z_]+$")
    TEX_FILENAME_REGEX = re.compile("^[a-zA-Z0-9_.-]+$")

    for filename in filenames:
        try:
            name = Path(filename).stem
            if verbose:
                typer.echo(f"Processing filename: {filename}", err=False)

            if len(name) < min_len:
                typer.echo(f"Name too short ({min_len=}): {filename}", err=True)

            if not TEX_FILENAME_REGEX.match(name):
                typer.echo(f"TeX filename is not valid: {filename}", err=True)

            if has_mixed_case(filename[1:]):
                typer.echo(f"TeX filename should not contain mixed cases: {filename}", err=True)

        except Exception:
            # if verbose:
            typer.echo(f"Filename: {filenames}; exception: {traceback.format_exc()}", err=True)


if __name__ == "__main__":
    preprocess_args()
    app()
