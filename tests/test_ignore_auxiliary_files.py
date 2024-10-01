import os
import tempfile

import pytest

from latexgithooks.ignore_auxiliary_files import auxiliary_extensions, is_auxiliary_file

allowed_extensions = [".tex", ".pdf", ".bib"]


@pytest.fixture
def create_and_remove_empty_files():
    """
    Creates empty files with specified extensions in a temporary directory and removes them after the test finishes.

    Args:
        auxiliary_extensions (list): List of file extensions.

    Yields:
        None
    """

    target_extensions = auxiliary_extensions
    with tempfile.TemporaryDirectory() as tmpdir:
        print(f"Using temp dir for tests: {tmpdir}")
        for extension in target_extensions:
            if len(extension) == 0:
                continue
            filename = os.path.join(tmpdir, f"test{extension}")
            with open(filename, "w"):
                pass
        yield

    # # Remove temporary files after the test finishes
    # for extension in target_extensions:
    #     filename = os.path.join(tmpdir, f"test{extension}")
    #     os.remove(filename)


def test_is_auxiliary_file(create_and_remove_empty_files):
    with tempfile.TemporaryDirectory() as tmpdir:
        for extension in auxiliary_extensions:
            filename = os.path.join(tmpdir, f"test{extension}")
            with open(filename, "w"):
                pass
            assert not is_auxiliary_file(filename)
