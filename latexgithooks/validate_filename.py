__description__ = "Tool for validating TeX filenames meet certain requirements"

import argparse
import re
import traceback
from pathlib import Path
from typing import Sequence


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


def is_valid_filename(filename: str, min_len: int = 4, verbose: bool = False) -> bool:
    """Method for validating TeX filename meet certain requirements.

    Args:
        filename (str): name of the file
        min_len (int): min lne
        verbose (bool, optional): prints additional information. Defaults to False.

    Returns:
        bool: valid or invalid file name
    """

    TEX_FILENAME_REGEX = re.compile("^[a-zA-Z0-9_.-]+$")

    try:
        name = Path(filename).stem
        if verbose:
            print(f"Processing filename: {filename}")

        if len(name) < min_len:
            print(f"Name too short ({min_len=}): {filename}")
            return False

        if not TEX_FILENAME_REGEX.match(name):
            print(f"TeX filename is not valid: {filename}")
            return False

        if has_mixed_case(filename[1:]):
            print(f"TeX filename should not contain mixed cases: {filename}")
            return False

    except Exception:
        # if verbose:
        print(f"Filename: {filename}; exception: {traceback.format_exc()}")
        return False

    return True


def main(argv: Sequence[str] | None = None) -> int:

    parser = argparse.ArgumentParser(prog="validate-filename", description=__description__)
    parser.add_argument(
        "filenames",
        nargs="*",
        help="Filenames to process.",
    )
    parser.add_argument(
        "--min-len",
        default=4,
        type=int,
        help="Minimum length for a filename.",
    )

    parser.add_argument(
        "--verbose",
        default=False,
        type=bool,
        help="Prints additional information.",
    )

    args = parser.parse_args(argv)

    results = [not is_valid_filename(filename, args.min_len, args.verbose) for filename in args.filenames]
    return int(any(results))
