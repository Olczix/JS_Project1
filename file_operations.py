import os


file_name = "generated_data.txt"
path = os.path.join(os.getcwd(), file_name)


def save_list_to_file(data_list) -> None:
    """
    Save data list to file
    :param data_list: list with values
    :return None
    """
    f = open(path, "w")
    for value in data_list:
        f.write(f'{value}\n')
    f.close()


def write_to_file(value) -> None:
    f = open(path, "w")
    f.write(f'{number}')
    f.close()


def read_from_file():
    f = open(path, "r")
    file_content = []
    for line in f:
        file_content.append(line)
    return file_content
