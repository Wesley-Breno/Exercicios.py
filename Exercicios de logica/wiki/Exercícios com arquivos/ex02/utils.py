"""
Funcoes que serao usadas no programa
"""


def converte_bytes_pra_megabytes(valor_bytes: int) -> float:
    """
    Funcao que recebe um valor em bytes e o retorna em megabytes.
    :param valor_bytes: Valor bytes que sera convertido em megabytes.
    :return: Retorna o valor do parametro em megabytes.
    """
    return float(valor_bytes / 1048576)


def pega_porcentagem_de_uso_do_usuario(lista_com_bytes: list, bytes_do_usuario: float):
    """
    Funcao que recebe uma lista com bytes usados de cada usuario, tambem recebe o byte usado pelo usuario e faz o
    calculo para saber quantos porcentos o usuario usa comparado aos outros usuarios.
    :param lista_com_bytes: Lista com os bytes usados de cada usuario
    :param bytes_do_usuario: Bytes usados do usuario em especifico para saber a porcentagem de uso
    :return: Retorna a porcentagem de uso do usuario
    """
    return (bytes_do_usuario / sum(lista_com_bytes)) * 100
