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


def sum_series(num, opt1=0, opt2=1):
    if num == 0:
        return opt1
    if num == 1:
        return opt2
    return sum_series(num - 1, opt1, opt2) + sum_series(num - 2, opt1, opt2)
    # one parameter required, two optional
    # required parameter - determines which element in the series to print
    # optionals will be 0 and 1 and determine the first 2 values for the series to be produced
    # Calling the function with no optional parameters will produce number from the fibonacci series
    # Calling it with the optional arguments of 2 and 1 will produce values from the lucas series
print(sum_series(7))
