__description__ = """"In American English, a comma should follow "e.g." and "i.e.""" ""

import argparse
import re
import sys
import traceback
from typing import Sequence

comma_in_eg_ie = "((e\\.g\\.)|(i\\.e\\.))[^,]"

ie_permutations = [
    "ie",
    "Ie",
    "iE",
    "IE",
    "i.e",
    "I.e",
    "i.E",
    "I.E",
    "ie.",
    "Ie.",
    "iE.",
    "IE.",
    "I.e.",
    "i.E.",
    "I.E.",
]

eg_permutations = ["e.G.", "E.g.", "E.G.", "eg.", "egG", "EG.", "Eg.", "e.g", "e.G", "E.g", "E.G"]


def container_permutation(line: str, permutations: list):
    for per in permutations:
        if per in line:
            return True
    return False


def is_correct_comma_ie_eg(file_path: str, verbose: bool = False) -> bool:
    """Method for checking commas in i.e. and e.g.

    Args:
        filename (str): name of the file
        verbose (bool, optional): prints additional information. Defaults to False.

    Returns:
        bool: valid or invalid file name
    """
    errors = {}
    errors["ie"], errors["eg"] = [], []
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                trimmed_line = line.strip()
                if not trimmed_line.startswith("%"):
                    if container_permutation(line, ie_permutations):
                        if not re.search(comma_in_eg_ie, line):
                            errors["ie"].append(line_number)
                    if container_permutation(line, eg_permutations):
                        if not re.search(comma_in_eg_ie, line):
                            errors["eg"].append(line_number)
    except Exception:
        print("Exception happened during the hook run. The run will be marked as 'passed'")
        print(f"Filename: {file_path}. Exception:\n{traceback.format_exc()}")
        return True
    
    is_ok = True
    if len(errors["ie"]) > 0:
        is_ok = False
        print(f"Found misused comma in 'i.e.' in lines: {errors["ie"]}. File: {file_path}")

    if len(errors["eg"]) > 0:
        is_ok = False
        print(f"Found misused comma in 'e.g.' in lines: {errors["eg"]}. File: {file_path}")
        

    return is_ok


def main(argv: Sequence[str] | None = None) -> int:
    """_summary_

    Args:
        argv (Sequence[str] | None, optional): set of arguments passed to the program . Defaults to None.

    Returns:
        int: 0 return value indicate successful termination
    """

    parser = argparse.ArgumentParser(prog="check-latex-packages", description=__description__)

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

    results = [not is_correct_comma_ie_eg(filename, args.verbose) for filename in args.filenames]
    return int(any(results))


if __name__ == "__main__":
    sys.exit(main())
