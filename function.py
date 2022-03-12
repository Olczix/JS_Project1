import math


def factorial_function(arg) -> int:
    # TODO: add function docstring
    if type(arg) is not int or arg < 0:
        raise ValueError

    result = 1
    for i in range(2, arg + 1, 1):
        result *= i

    return result
