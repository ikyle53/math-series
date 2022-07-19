def factorial(num):
    if num <= 1:
        return 1

    if num > 1:
        return num * (factorial(num - 1))

    if __name__ == "__main__":
        x = input("Enter number > 1")
        result = factorial(int(x))
        print(f"factorial of {x} is {result}")
