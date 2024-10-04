__description__ = """"In American English, a comma should follow "e.g." and "i.e.""" ""

import argparse
import re
import sys
import traceback
from typing import Sequence

comma_in_ie = "(i\\.e\\.)"
comma_in_eg = "(e\\.g\\.)"

ie_base_permutations = [
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

eg_base_permutations = [
    "eg",
    "Eg",
    "eG",
    "EG",
    "e.g",
    "E.g",
    "e.G",
    "E.G",
    "eg.",
    "Eg.",
    "eG.",
    "EG.",
    "E.g.",
    "e.G.",
    "E.G."
]

def add_symbols_to_permutations(permutations:list) -> list:
    """Adds symbols to each item in the given list.

    Args:   
        permutations (list): a list of strings.

    Returns:
        list:  a new list with symbols added to each item.
    """    
    symbols = ["#", "'", "\"", "(", ")"]
    new_permutations = []
    new_permutations += [item + " " for item in permutations]
    new_permutations += [" " + item for item in permutations]

    for permutation in permutations:
        for symbol in symbols:
            new_permutations.append(permutation + symbol)
            new_permutations.append(symbol + permutation)

    return new_permutations


def contains_permutation(line: str, permutations: list) -> bool:
    """Checks if any of the given permutations is contained within the line.
       If a letter ig given before item from a permutations, will be marked as "no-permutation found"

    Args:
        line (str): The input string to be checked.
        permutations (list): A list of strings representing the permutations to search for.

    Returns:
        bool: True if any of the permutations is found in the line, False otherwise.
    """

    for item in permutations:
        if item in line:
            index = line.find(item)
            if index > 0:
                if line[index-1].isalpha():
                    return False
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
    
    ie_extended_permutations = add_symbols_to_permutations(ie_base_permutations)
    eg_extended_permutations = add_symbols_to_permutations(eg_base_permutations)

    errors = {}
    errors["ie"], errors["eg"] = [], []
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                trimmed_line = line.strip()
                if not trimmed_line.startswith("%"):
                    if contains_permutation(line, ie_extended_permutations):
                        if not re.search(comma_in_ie, line):
                            errors["ie"].append(line_number)
                    if contains_permutation(line, eg_extended_permutations):
                        if not re.search(comma_in_eg, line):
                            errors["eg"].append(line_number)
    except Exception:
        print("Exception happened during the hook run. The run will be marked as 'passed'")
        print(f"Filename: {file_path}. Exception:\n{traceback.format_exc()}")
        return True
    
    check_verdict = True
    if len(errors["ie"]) > 0:
        check_verdict = False
        print(f"Found misused comma in 'i.e.' in lines: {errors["ie"]}. File: {file_path}")

    if len(errors["eg"]) > 0:
        check_verdict = False
        print(f"Found misused comma in 'e.g.' in lines: {errors["eg"]}. File: {file_path}")
    
    return check_verdict


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
