import os
import time
from function import factorial_function
from file_operations import read_from_file


def main():
    data = read_from_file()
    amount = len(data)

    start_empty_loop = time.time()
    for number in data:
        pass
    end_empty_loop = time.time()

    empty_loop_duration = end_empty_loop - start_empty_loop

    start_loop = time.time()
    for number in data:
        factorial_function(int(number))
    end_loop = time.time()

    loop_duration = end_loop - start_loop

    print(loop_duration-empty_loop_duration)

main()
