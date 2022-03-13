import math
from python_code.functions.function import factorial_function
from python_code.utils.file_operations import read_from_file, save_list_to_file, files_contents_equal


def check_my_implementation():
    data = read_from_file(file_name="generated_data.txt")
    results_array = []
    for number in data:
        results_array.append(factorial_function(number))
    save_list_to_file(results_array, file_name="python_results_my_function.txt")


def check_py_library_implementation():
    data = read_from_file(file_name="generated_data.txt")
    results_array = []
    for number in data:
        results_array.append(math.factorial(number))
    save_list_to_file(results_array, file_name="python_results_library_function.txt")


check_my_implementation()
check_py_library_implementation()
