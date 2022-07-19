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

    if __name__ == "__main__":
        x = input("Enter number > 1")
        result = fibonacci(int(x))
        print(f"factorial of {x} is {result}")
