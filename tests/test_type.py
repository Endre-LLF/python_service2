from type_test import add


def test_add():
    assert add(5, 3) == 8
    assert add("Hello, ", "World!") == "Hello, World!"
