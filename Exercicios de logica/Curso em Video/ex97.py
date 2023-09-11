"""
Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma mensagem
com tamanho adaptável.
"""


def escreva(msg: str):
    """
    Função que recebe uma string para escrever uma linha de '='
    ajustavel com o tamanho da string.
    :param msg: Recebe a string
    :return: None
    """
    print('=' * len(msg))  # Escrevendo o caractere '=', com base na quantidade de caracteres da string
    print(msg)
    print('=' * len(msg))


escreva('Valquiria')
