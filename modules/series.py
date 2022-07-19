def fibonacci(n):
    """
    Fibonacci is a function which takes an integer in
    and adds it together with the next number in the
    sequence until it reaches that integer.
    """

    if n <= 1:
        return 1

    if n > 1:
        return n + (fibonacci(n - 1))


def lucas(n):
    """
    Lucas is the same as Fibonacci, but the starting integers are
    always 2 and 1
    """
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n - 1) + lucas(n - 2)
