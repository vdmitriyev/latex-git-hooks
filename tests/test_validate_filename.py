import os
from typing import Any

import pytest
from typer.testing import CliRunner

import latexgithooks as latexgithooks
import latexgithooks.validate_filename as validate_filename
from latexgithooks.validate_filename import app

runner = CliRunner()


def test_has_mixed_case_true():
    assert validate_filename.has_mixed_case("Hello, World!") == True


def test_has_mixed_case_false_uppercase_only():
    assert validate_filename.has_mixed_case("HELLO") == False


def test_has_mixed_case_false_lowercase_only():
    assert validate_filename.has_mixed_case("hello") == False


def test_has_mixed_case_false_empty_string():
    assert validate_filename.has_mixed_case("") == False


def test_has_mixed_case_false_special_characters():
    assert validate_filename.has_mixed_case("!@#$%^&*()") == False


@pytest.fixture
def tex_file_path(folder_name="data", file_pattern=".tex"):
    """
    Fixture to get the path to files in a given folder.

    Args:
        folder_name (str): The name of the folder containing the files.
        file_pattern (str, optional): The pattern to match file names (e.g., ".txt").

    Returns:
        list: A list of file paths matching the pattern within the specified folder.
    """

    test_file_dir = os.path.dirname(__file__)
    folder_path = os.path.join(test_file_dir, folder_name)
    file_paths = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(file_pattern)]
    if not file_paths:
        pytest.fail(f"No files matching pattern '{file_pattern}' found in folder '{folder_name}'.")

    return file_paths


def test_cli_invoke_validate_filenames(tex_file_path):

    tex_files = tex_file_path
    cli_params = []
    for file in tex_files:
        cli_params.append("--filenames")
        cli_params.append(file)
    result = runner.invoke(app, cli_params)
    assert result.exit_code == 0
