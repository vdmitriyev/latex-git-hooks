import os

import pytest


# Fixtures
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
