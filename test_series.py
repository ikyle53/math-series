from modules.series import factorial
def test_factorial_1():
    actual = factorial(1)
    expected = 1
    assert actual == expected
