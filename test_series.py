from modules.series import fibonacci
from modules.series import lucas


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


def test_lucas_0():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_lucas_1():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_lucas_any():
    actual = lucas(6)
    expected = 18
    assert actual == expected


def sum_func():
    actual = sum_series()