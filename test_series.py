from modules.series import fibonacci


def test_fib_1():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fib_2():
    actual = fibonacci(2)
    expected = 3
    assert actual == expected


def test_fib_any():
    actual = fibonacci(4)
    expected = 10
    assert actual == expected
