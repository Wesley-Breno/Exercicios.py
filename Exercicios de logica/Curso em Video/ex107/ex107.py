"""
Crie um módulo chamado moeda.py que tenha as funções incorporadas
aumentar(), diminuir(), dobro() e metade(). Faça também um programa
que importe esse módulo e use algumas dessas funções.
"""


def aumentar(valor, porcentagem):
    """
    Funcao que recebe um valor e uma porcentagem e faz um aumento com a porcentagem.
    :param valor: Valor que sera aumentado
    :param porcentagem: Valor que sera usado como porcentagem para fazer o aumento
    :return: Retorna uma lista com o valor aumentado e o valor da porcentagem
    """
    return [valor + (valor * porcentagem / 100), porcentagem]


def diminuir(valor, porcentagem):
    """
    Funcao que recebe um valor e uma porcentagem e faz uma diminuicao com a porcentagem.
    :param valor: Valor que sera diminuido
    :param porcentagem: Valor que sera usado como porcentagem para fazer a diminuicao
    :return: Retorna uma lista com o valor diminuido e o valor da porcentagem
    """
    return [valor - (valor * porcentagem / 100), porcentagem]


def dobro(valor):
    """
    Funcao que recebe um valor e retorna o dobro do valor
    :param valor: Valor que sera dobrado
    :return: Retorna o valor dobrado
    """
    return valor * 2


def metade(valor):
    """
    Funcao que recebe um valor e retorna a metade do valor
    :param valor: Valor que sera diminuido pela metade
    :return: Retorna o valor pela metade
    """
    return valor / 2
