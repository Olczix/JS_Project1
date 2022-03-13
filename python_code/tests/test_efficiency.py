import time
import math
from python_code.utils.file_operations import read_from_file
from python_code.functions.function import factorial_function


n_my_function = 14000000
n_python_library = 100000000


def test_my_implementation():
    print(f"\n\nCUSTOM FACTORIAL FUNCTION IMPLEMENTATION IN PYTHON ({n_my_function} times)\n")
    data = read_from_file(file_name="generated_data.txt")

    start_empty_loop = time.time()
    for _ in range(n_my_function):
        for number in data:
            pass
    end_empty_loop = time.time()
    empty_loop_duration = end_empty_loop - start_empty_loop

    start_loop = time.time()
    for _ in range(n_my_function):
        for number in data:
            factorial_function(number)
    end_loop = time.time()
    loop_duration = end_loop - start_loop

    print(f"empty loop duration is \t\t{empty_loop_duration} [s] ")
    print(f"loop with calculations is \t{loop_duration} [s]")
    print(f"actual calculations time is \t{loop_duration - empty_loop_duration} [s]")


def test_py_library_implementation():
    print(f"\n\nPYTHON LIBRARY FACTORIAL FUNCTION IMPLEMENTATION ({n_python_library} times)\n")
    data = read_from_file(file_name="generated_data.txt")

    start_empty_loop = time.time()
    for _ in range(n_python_library):
        for number in data:
            pass
    end_empty_loop = time.time()
    empty_loop_duration = end_empty_loop - start_empty_loop

    start_loop = time.time()
    for _ in range(n_python_library):
        for number in data:
            math.factorial(number)
    end_loop = time.time()
    loop_duration = end_loop - start_loop

    print(f"empty loop duration is \t\t{empty_loop_duration} [s] ")
    print(f"loop with calculations is \t{loop_duration} [s]")
    print(f"actual calculations time \t{loop_duration - empty_loop_duration} [s]")


test_my_implementation()
test_py_library_implementation()
