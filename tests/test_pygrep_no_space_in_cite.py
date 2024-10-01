import re

# TODO: copy manually the regex to the hook as "entry" with "pygrep" as language
no_cite_pattern = r"\\cite\{([^\}]*\s)+[^\}]*\}"
no_citep_pattern = r"\\citep\{([^\}]*\s)+[^\}]*\}"


def test_no_space_in_cite():
    # Test that the hook matches when there is whitespace in the \cite command

    assert re.search(no_cite_pattern, r"\cite{ foo }")  # Expected to match
    # Test that the hook does not match when there is no whitespace in the \cite command
    assert not re.search(no_cite_pattern, r"\cite{foo}")  # Not expected to match


def test_no_space_in_cite_edge_cases():
    # Test edge cases, such as empty input or no \cite command
    assert not re.search(no_cite_pattern, "")  # Empty input
    assert not re.search(no_cite_pattern, "Hello world")  # No \cite command


def test_no_space_in_citep():
    # Test that the hook matches when there is whitespace in the \citep command

    assert re.search(no_citep_pattern, r"\citep{ foo }")  # Expected to match
    # Test that the hook does not match when there is no whitespace in the \citep command
    assert not re.search(no_citep_pattern, r"\citep{foo}")  # Not expected to match


def test_no_space_in_citep_edge_cases():
    # Test edge cases, such as empty input or no \citep command
    assert not re.search(no_citep_pattern, "")  # Empty input
    assert not re.search(no_citep_pattern, "Hello world")  # No \citep command
