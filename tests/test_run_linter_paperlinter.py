import os

import pytest

from latexgithooks.run_linter_paperlinter import run_linter


# Test cases - linter "paperlinter"
def test_valid_linter_paperlinter(tex_file_path):
    all_tex_files = [f for f in tex_file_path if "tex" in f]

    for filename in all_tex_files:
        result = run_linter(filename)
        assert result, f"File {filename} should be valid"
