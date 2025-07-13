"""This file is part of a Python service project."""


def add(a, b):
    """Add two values together."""
    return a + b


if __name__ == "__main__":
    x = 5  # pylint: disable=invalid-name
    y = 10  # pylint: disable=invalid-name
    result = add(x, y)  # pylint: disable=invalid-name
    print(f"{x} + {y} = {result}")
