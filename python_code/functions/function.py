"""
Functions used in my first project from course
"Script languages and their usage"
"""

def factorial_function(arg: int) -> int:
    """
    Function for calculating a factorial of given arg
    :param arg: given number (only natural numbers)
    :return: calculated factorial of given number
    """
    if type(arg) is not int or arg < 0:
        raise ValueError

    result = 1
    for i in range(2, arg + 1, 1):
        result *= i

    return result
