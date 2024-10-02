import re

from latexgithooks.check_comma_ie_eg import comma_in_eg_ie, is_correct_comma_ie_eg


def test_comma_in_eg_ie_positive():
    """Tests the regex for correct matching of 'e.g.' or 'i.e.' followed by a non-comma character."""

    # Positive test cases
    positive_cases = [
        "e.g. hello",
        "i.e. world",
        "e.g.123",
        "i.e. abc",
        "e.g.!",
        "i.e.?",
    ]

    for case in positive_cases:
        assert re.search(comma_in_eg_ie, case)


def test_comma_in_eg_ie_negative():
    """Tests the regex for correct matching of 'e.g.' or 'i.e.' followed by a non-comma character."""

    # Negative test cases
    negative_cases = [
        "e.g",
        "eg.,",
        "eg,",
        "eg..,",
        "i.e",
        "ie.,",
        "ie,",
        "ie..,",
        "hello world",
    ]

    for case in negative_cases:
        assert not re.search(comma_in_eg_ie, case)


def test_comma_in_eg_ie():
    """Tests the regex for finding "e.g." or "i.e." followed by a non-comma character."""

    # Test cases with expected matches
    test_cases_match = [
        "e.g. this is a test",
        "i.e. this is another test",
        "e.g. this is a test, but this is not",
        "i.e. this is another test, but this is not",
    ]
    for test_case in test_cases_match:
        assert re.search(comma_in_eg_ie, test_case)

    # Test cases with expected no matches
    test_cases_no_match = ["e.g,", "i.e,", "this is a test", "this is another test"]
    for test_case in test_cases_no_match:
        assert not re.search(comma_in_eg_ie, test_case)


# Test cases - comm_ie_eg
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
