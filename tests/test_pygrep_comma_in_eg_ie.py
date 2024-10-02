import re

from latexgithooks.check_comma_ie_eg import (
    comma_in_eg,
    comma_in_ie,
    is_correct_comma_ie_eg,
)


def test_comma_in_eg_positive():
    """Tests the regex for correct matching of 'e.g.' or 'i.e.' followed by a non-comma character."""

    # Positive test cases
    positive_cases_eg = [
        "e.g. hello",
        "e.g.123",
        "e.g.!",
    ]

    for case in positive_cases_eg:
        assert re.search(comma_in_eg, case)


def test_comma_in_ie_positive():
    """Tests the regex for correct matching of 'e.g.' or 'i.e.' followed by a non-comma character."""

    # Positive test cases
    positive_cases_ei = [
        "i.e. world",
        "i.e. abc",
        "i.e.?",
    ]

    for case in positive_cases_ei:
        assert re.search(comma_in_ie, case)


def test_comma_in_eg_negative():
    """Tests the regex for incorrect matching of 'e.g.' or 'i.e.' followed by a non-comma character."""

    # Test cases with expected no matches
    test_cases_no_match_01 = [
        "e.g",
        "eg.,",
        "eg,",
        "eg..,",
        "e.g,",
        "this is a test",
        "this is another test",
        "hello world",
    ]

    for case in test_cases_no_match_01:
        assert not re.search(comma_in_eg, case)


def test_comma_in_ie_negative():
    """Tests the regex for incorrect matching of 'e.g.' or 'i.e.' followed by a non-comma character."""

    # Test cases with expected no matches
    test_cases_no_match_01 = [
        "i.e",
        "ie.,",
        "ie,",
        "ie..,",
        "this is a test",
        "this is another test",
        "hello world",
    ]

    for case in test_cases_no_match_01:
        assert not re.search(comma_in_ie, case)


def test_comma_in_eg():
    """Tests the regex for finding "e.g." or "i.e." followed by a non-comma character."""

    # Test cases with expected matches
    test_cases_match = [
        "e.g. this is a test",
        "e.g. this is a test, but this is not",
        "using data (e.g., data , etc.).",
    ]
    for test_case in test_cases_match:
        assert re.search(comma_in_eg, test_case)


def test_comma_in_ie():
    """Tests the regex for finding "e.g." or "i.e." followed by a non-comma character."""

    # Test cases with expected matches
    test_cases_match = [
        "i.e. this is another test",
        "i.e. this is another test, but this is not",
    ]
    for test_case in test_cases_match:
        assert re.search(comma_in_ie, test_case)


#
# Test cases - comma_ie_eg
#
def test_correct_comma_ie_eg(tex_file_path):
    valid_tex_files = [f for f in tex_file_path if "correct" in f and "comma_ie_eg" in f]

    for filename in valid_tex_files:
        result = is_correct_comma_ie_eg(filename)
        assert result, f"File {filename} should be valid"


def test_wrong_comma_ie_eg(tex_file_path):

    invalid_tex_files = [f for f in tex_file_path if "wrong" in f and "comma_ie_eg" in f]

    for filename in invalid_tex_files:
        result = is_correct_comma_ie_eg(filename)
        assert not result, f"File {filename} should be invalid"
