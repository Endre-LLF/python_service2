"""This file is part of a Python service project."""


def add(a, b):
    """Add two values together."""
    return a + b


if __name__ == "__main__":
    x = 5
    y = 10
    result = add(x, y)
    print(f"{x} + {y} = {result}")
