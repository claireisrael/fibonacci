# CLAIRE and MELISSA
#These are serires of numbers where by each number is the sum of the two proceeding numbers
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, and so on
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
    


def fibonacci(n):
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

