__description__ = "Checks usage of LaTeX packages"

import argparse
import re
import sys
import traceback
from typing import Sequence


def remove_package_args(input_str: str) -> str:
    """Removes everything between '\\usepackage' and the first '{'

    Args:
        input_str (str): The string to modify

    Returns:
        str: The modified string
    """
    pattern = re.compile(r"\\usepackage\[(.*?)\]\{(.*?\})")
    # Use the compiled pattern to find and replace the string
    return re.sub(pattern, lambda x: "\\usepackage{" + x.group(2), input_str)


def find_duplicates(input_list: dict) -> list:
    """Find duplicates

    Args:
        input_list (dict): input dict with elements

    Returns:
        list: line numbers with package duplicates
    """

    seen, duplicates = set(), set()

    for item in input_list.values():
        if item["line"] in seen:
            duplicates.add(item["number"])
        seen.add(item["line"])

    return list(duplicates)


def is_correct_packages_import(file_path: str, verbose: bool = False) -> bool:
    """Method for checking LaTeX package imports.

    Args:
        filename (str): name of the file
        verbose (bool, optional): prints additional information. Defaults to False.

    Returns:
        bool: valid or invalid file name
    """

    try:
        packages_lines = {}
        after_document_tag = False

        with open(file_path, mode="r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                trimmed_line = line.strip()
                if not trimmed_line.startswith("%"):
                    if trimmed_line.startswith("\\begin{document}"):
                        after_document_tag = True
                    if trimmed_line.startswith("\\usepackage"):
                        if after_document_tag:
                            print(
                                f"Found '\\usepackage' usage after '\\begin{{document}}' in file '{file_path}' on line: {line_number}"
                            )
                            return False
                        packages_lines[line_number] = {
                            "number": line_number,
                            "line": remove_package_args(trimmed_line),
                            "after": after_document_tag,
                        }

        duplicates = find_duplicates(packages_lines)

        if len(duplicates) > 0:
            print(f"Found '\\usepackage' duplicates in file '{file_path}' in lines: {duplicates}")
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

    results = [not is_correct_packages_import(filename, args.verbose) for filename in args.filenames]
    return int(any(results))


if __name__ == "__main__":
    sys.exit(main())
