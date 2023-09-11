from tabulate import tabulate


def read_file(file_name: str) -> list:
    """
    Funcao que le o arquivo informado do projeto e retorna uma lista contendo
    o nome e total de bytes usado por cada usuario.
    :param file_name:  Nome do arquivo a ser lido
    :return: Retorna uma lista contendo o nome e total de bytes de cada usuario
    """
    with open(file_name, 'r') as file:
        data_unformated = file.read().split('\n')
        data_formated = [[data.split(' ')[0], data.split(' ')[-1]] for data in data_unformated]
    return data_formated


def convert_bytes_for_megabytes(total_bytes: int) -> float:
    return round(total_bytes / 1048576, 2)


def percentage_calculation(total: float, my_usage: float) -> float:
    return round((my_usage / total) * 100, 2)


def show_table(*args) -> str:
    ...
