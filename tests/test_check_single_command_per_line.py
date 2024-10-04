import re
from typing import Literal, LiteralString

import pytest

from latexgithooks.check_single_command_per_line import (
    PATTERN_SQUARE_BRACES,
    any_symbols_after_left_curly_braces,
    is_single_command_per_line,
    remove_after_symbol,
)


#
# Test cases - remove_after_symbol
#
@pytest.mark.single_command_per_line
def test_remove_after_symbol():
    # Test cases where the symbol is present
    assert remove_after_symbol("hello, world!", ",") == "hello"
    assert remove_after_symbol("hello world,", ",") == "hello world"
    assert remove_after_symbol(",hello world", ",") == ""

    # Test cases where the symbol is not present
    assert remove_after_symbol("hello world", ",") == "hello world"
    assert remove_after_symbol("", ",") == ""

    # Additional test cases with '%' as the symbol
    assert remove_after_symbol("\\begin{document} %here is the comment", "%") == "\\begin{document} "
    assert remove_after_symbol("hello%world", "%") == "hello"
    assert remove_after_symbol("hello%world%", "%") == "hello"


@pytest.mark.single_command_per_line
def test_check_symbols_after_left_curly_braces():
    """Tests the check_symbols_after_left_curly_braces function."""

    # Test case with symbols after closing curly brace
    text_with_symbols = "This is {a sample text} with some symbols after!@"
    assert any_symbols_after_left_curly_braces(text_with_symbols)

    # Test case with only whitespaces after closing curly brace
    text_with_whitespaces = "This is {a sample text} with whitespaces after  "
    assert any_symbols_after_left_curly_braces(text_with_whitespaces)

    # Test case without closing curly brace
    text_no_brace = "This is a simple text with no curly braces"
    assert not any_symbols_after_left_curly_braces(text_no_brace)

    # Test case with closing curly brace
    text_no_brace = "This is a simple text with no curly braces}"
    assert not any_symbols_after_left_curly_braces(text_no_brace)

    # Test case with closing curly brace and whitespaces
    text_no_brace = "This is a simple text with no curly braces}     "
    assert not any_symbols_after_left_curly_braces(text_no_brace)

    # Test case with closing curly brace and whitespaces
    text_no_brace = "This is a simple text with no curly braces}     "
    assert not any_symbols_after_left_curly_braces(text_no_brace)


@pytest.mark.single_command_per_line
def test_remove_content_between_brackets():

    input_string = "\\begin{figure}[h!]"
    expected_output = "\\begin{figure}"

    result_string = re.sub(PATTERN_SQUARE_BRACES, "", input_string)
    assert result_string == expected_output, f"Expected string: '{expected_output}'"


@pytest.mark.single_command_per_line
def test_check_symbols_after_left_curly_braces_many():
    """Tests the check_symbols_after_left_curly_braces function."""

    cases_left_curly_braces = [
        "\\section{Math references}",
        "\\begin{equation}",
        "\\end{equation}",
        "\\section{Last section}",
        "\\end{document}",
        "\\begin{figure}[h!]",
        "\\begin{table}[h!]",
    ]
    for item in cases_left_curly_braces:
        assert not any_symbols_after_left_curly_braces(item)


@pytest.mark.single_command_per_line
def test_correct_single_command_per_line(tex_file_path: list[str]):

    invalid_tex_files = [f for f in tex_file_path if "correct" in f and "command_per_file_" in f]
    assert len(invalid_tex_files) != 0, "Files with test data were not found"

    for filename in invalid_tex_files:
        result = is_single_command_per_line(filename)
        assert result, f"File {filename} should be correct"


@pytest.mark.single_command_per_line
def test_wrong_single_command_per_line(tex_file_path: list[str]):

    invalid_tex_files = [f for f in tex_file_path if "wrong" in f and "command_per_file_" in f]

    for filename in invalid_tex_files:
        result = is_single_command_per_line(filename)
        assert not result, f"File {filename} should be wrong"
