from modules.series import factorial


def test_factorial_1():
    actual = factorial(1)
    expected = 1
    assert actual == expected


def test_factorial_2():
    actual = factorial(2)
    expected = 2
    assert actual == expected


def test_factorial_any():
    actual = factorial(4)
    expected = 24
    assert actual == expected
