import math
from random import randint, uniform
from python_code.utils.file_operations import save_list_to_file


LIMIT = 9223372036854775807  # Max value on __int64 type in Cpp
AMOUNT_OF_NUMBERS = 1000000


def factorial_below_integer_limit():
    result = 0
    for i in range(0, LIMIT):
        if math.factorial(i) <= LIMIT:
            result = i
        else:
            break
    return result


integer_limit = factorial_below_integer_limit()
test_data_list = []


def get_random_natural_number():
    return randint(0, integer_limit)

def get_random_negative_number():
    return randint(-2**64, 0)

def get_random_float():
    return uniform(-integer_limit, integer_limit)

def get_natural_numbers(amount):
    for _ in range(amount):
        test_data_list.append(get_random_natural_number())

def get_unique_natural_numbers():
    for _ in range(integer_limit+1):
        value = get_random_natural_number()
        while value in test_data_list:
            value = get_random_natural_number()
        test_data_list.append(value)

def get_random_negative_numbers():
    # Randomize negative values
    for _ in range(AMOUNT_OF_NUMBERS):
        value = get_random_negative_number()
        while value in test_data_list:
            value = get_random_negative_number()
        test_data_list.append(value)

def get_random_float_numbers():
    # Randomize floats
    for _ in range(AMOUNT_OF_NUMBERS):
        value = get_random_float()
        while value in test_data_list:
            value = get_random_float()
        test_data_list.append(value)


def data_generator():
    get_unique_natural_numbers()
    # get_natural_numbers(100000)
    save_list_to_file(test_data_list, file_name="generated_data.txt")


data_generator()
