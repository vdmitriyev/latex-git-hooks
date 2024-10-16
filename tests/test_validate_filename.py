import os

import pytest

from latexgithooks.validate_filename import has_mixed_case, is_valid_filename, main


#
# Test has_mixed_case function
#
def test_has_mixed_case_true():
    assert has_mixed_case("Hello, World!") == True


def test_has_mixed_case_false_uppercase_only():
    assert has_mixed_case("HELLO") == False


def test_has_mixed_case_false_lowercase_only():
    assert has_mixed_case("hello") == False


def test_has_mixed_case_false_empty_string():
    assert has_mixed_case("") == False


def test_has_mixed_case_false_special_characters():
    assert has_mixed_case("!@#$%^&*()") == False


#
# Test cases for `is_valid_filename` function
#
def test_is_valid_filename_valid():
    assert is_valid_filename("valid_filename.tex", 3)


def test_is_valid_filename_too_short():
    assert not is_valid_filename("a.tex", 3)


def test_is_valid_filename_invalid_characters():
    assert not is_valid_filename("invalid_filename#$.tex", 3)


def test_is_valid_filename_mixed_case():
    assert not is_valid_filename("MixedCaseFilename.tex", 3)


def test_is_valid_filename_verbose_mode():
    assert not is_valid_filename("MixedCaseFilename.tex", 3, verbose=True)


#
# Test cases for `main` function
#
def test_main_valid_filenames():
    assert main(["valid_filename.tex", "another_valid_filename.tex"]) == 0


def test_main_invalid_filenames():
    assert main(["invalid_filename&.tex", "tex"]) == 1
