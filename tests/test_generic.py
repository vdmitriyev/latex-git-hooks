#!/usr/bin/env python

"""Tests for `latexgithooks` package."""

import pytest

import latexgithooks as latexgithooks


@pytest.fixture
def response_fix():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    pass


def test_license(response_fix):
    assert latexgithooks.__license__ == "MIT"
