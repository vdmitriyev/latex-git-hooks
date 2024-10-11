__description__ = "Runs linter 'paperlinter'"

import argparse
import sys
import traceback
from typing import Sequence

from paperlinter import run_linter_once


def run_linter(filename: str, min_len: int = 4, verbose: bool = False) -> bool:
    """Method for running liner ''paperlinter'

    Args:
        filename (str): name of the file
        verbose (bool, optional): prints additional information. Defaults to False.

    Returns:
        bool: valid or invalid file name
    """

    try:
        run_linter_once(filename)
    except Exception:
        print(f"Filename: {filename}; exception: {traceback.format_exc()}")
        return False

    return True


def main(argv: Sequence[str] | None = None) -> int:

    parser = argparse.ArgumentParser(prog="run-linter-paper-linter", description=__description__)
    parser.add_argument(
        "filenames",
        nargs="*",
        help="Filenames to process.",
    )
    parser.add_argument(
        "--verbose",
        default=False,
        type=bool,
        help="Prints additional information.",
    )

    args = parser.parse_args(argv)

    results = [not run_linter(filename, args.verbose) for filename in args.filenames]
    return int(any(results))


if __name__ == "__main__":
    sys.exit(main())
