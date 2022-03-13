from python_code.utils.file_operations import files_contents_equal

if_python_files_equal = files_contents_equal(
    file_name1="python_results_my_function.txt", 
    file_name2="python_results_library_function.txt")
print(f'Are Python files contents equal?\n\t{if_python_files_equal}')

if_cpp_files_equal = files_contents_equal(
    file_name1="cpp_results_my_function.txt", 
    file_name2="python_results_library_function.txt")
print(f'Are cpp and python files contents equal?\n\t{if_cpp_files_equal}')
