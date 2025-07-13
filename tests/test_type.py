"""This file is part of a Python service project."""

from type_test import add


def test_add():
    """Test the add function."""
    assert add(5, 3) == 8
    assert add("Hello, ", "World!") == "Hello, World!"
