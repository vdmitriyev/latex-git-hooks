__description__ = "Checks usage of a single TeX command per line"

import argparse
import re
import sys
import traceback
from typing import Sequence

commands_main = ["\\section", "\\begin", "\\end", "\\chapter", "\\footnote"]
commands_custom = ["\\rewrite", "\\info", "\\improvetext"]

RE_LEFT_CURLY_BRACE = r"\}"
PATTERN_SYMBOLS_AFTER_LEFT_CURLY_BRACES = r"\}[^}]"


def remove_after_symbol(string: str, symbol: str) -> str:
    """Removes everything after the first occurrence of a given symbol in a string.

    Args:
        string: The input string.
        symbol: The symbol to search for.

    Returns:
        The modified string with everything after the symbol removed.
    """

    index = string.find(symbol)
    if index != -1:
        return string[:index]
    else:
        return string


def any_symbols_after_left_curly_braces(input: str) -> bool:
    if not re.search(RE_LEFT_CURLY_BRACE, input):
        return False
    input = remove_after_symbol(input, "%")
    input = input.strip()
    index = input.rfind("}")
    if index != len(input) - 1:
        return True
    return False


def is_single_command_per_line(file_path: str, verbose: bool = False) -> bool:
    """Method for usage of a single TeX command per line.

    Args:
        filename (str): name of the file
        verbose (bool, optional): prints additional information. Defaults to False.

    Returns:
        bool: valid or invalid file name
    """
    commands = commands_main + commands_custom
    try:
        incorrect_lines = []
        with open(file_path, mode="r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                clean_line = line.strip()
                if not clean_line.startswith("%"):
                    for command in commands:
                        if clean_line.startswith(command):
                            if any_symbols_after_left_curly_braces(clean_line):
                                incorrect_lines.append(line_number)

        if len(incorrect_lines) > 0:
            print(f"Found incorrect usage of TeX commands in file '{file_path}' in lines: {incorrect_lines}")
            return False

    except Exception:
        print("Exception happened during the hook run. The run will be marked as 'passed'")
        print(f"Filename: {file_path}. Exception:\n{traceback.format_exc()}")
        return True

    return True


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

    results = [not is_single_command_per_line(filename, args.verbose) for filename in args.filenames]
    return int(any(results))


if __name__ == "__main__":
    sys.exit(main())
