import os

import pytest

from latexgithooks.check_latex_packages import (
    is_correct_packages_import,
    remove_package_args,
)


# Test cases - regex
def test_remove_package_args_empty_string():
    """Test that an empty string is returned when input is empty."""
    assert remove_package_args("") == ""


def test_remove_package_args_no_match():
    """Test that the original string is returned when there's no match."""
    assert remove_package_args("\\usepackage{foo}") == "\\usepackage{foo}"


def test_remove_package_args_with_args():
    """Test that the original string is returned when there's no match."""
    assert remove_package_args("\\usepackage[dsadsadsa]{foo}") == "\\usepackage{foo}"


# Test cases - packages
def test_valid_package_imports(tex_file_path):
    """
    Test a valid .tex file with correct package imports.
    """

    valid_tex_files = [f for f in tex_file_path if "correct" in f and "packages" in f]

    for filename in valid_tex_files:
        result = is_correct_packages_import(filename)
        assert result, f"File {filename} should be valid"


def test_invalid_package_imports(tex_file_path):
    """
    Test a .tex file with wrong package imports.
    """

    invalid_tex_files = [f for f in tex_file_path if "wrong" in f and "packages" in f]

    for filename in invalid_tex_files:
        result = is_correct_packages_import(filename)
        assert not result, f"File {filename} should be invalid"
