"""
Useful functions enabling easy file I/O management
"""
import os
from typing import List


data_folder_path = os.path.join(os.getcwd(), "data")


def save_list_to_file(data_list: List[int], file_name: str) -> None:
    """
    Save data list to file
    :param data_list: list with values
    :param file_name: name of I/O file
    :return None
    """
    f = open(os.path.join(data_folder_path, file_name), "w")
    for value in data_list:
        f.write(f'{value}\n')
    f.close()


def write_to_file(value: int, file_name: str) -> None:
    """
    Write value to file
    :param value: integer value
    :param file_name: name of I/O file
    :return None
    """
    f = open(os.path.join(data_folder_path, file_name), "w")
    f.write(f'{value}')
    f.close()


def read_from_file(file_name: str) -> List[int]:
    """
    Read all lines from file
    :param file_name: name of I/O file
    :return: list of values from file as integers
    """
    f = open(os.path.join(data_folder_path, file_name), "r")
    file_content = []
    for line in f:
        file_content.append(int(line))
    return file_content


def files_contents_equal(file_name1: str, file_name2: str) -> bool:
    """
    Returns information if files contents are the same (equal)
    :param file_name1: name of the first file
    :param file_name2: name of the second file
    :return: True - if files content is the same, False - otherwise
    """
    return True if read_from_file(file_name1) == read_from_file(file_name2) else False
