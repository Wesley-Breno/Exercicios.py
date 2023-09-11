"""
Modifique as funções que foram criadas no desafio 107 para que
elas aceitem um parâmetro a mais, informando se o valor retornado
por elas vai ser ou não formatado pela função moeda(),
desenvolvida no desafio 108.
"""


def aumentar(valor, porcentagem, formatar=True):
    """
    Funcao que recebe um valor e uma porcentagem e faz um aumento com a porcentagem.
    :param valor: Valor que sera aumentado
    :param porcentagem: Valor que sera usado como porcentagem para fazer o aumento
    :param formatar: Recebe True para deixar o valor formatado de forma monetaria
    :return: Retorna uma lista com o valor aumentado e o valor da porcentagem
    """
    if formatar:
        valor_formatado = moeda(valor + (valor * porcentagem / 100))
        return [valor_formatado, porcentagem]

    else:
        return [valor + (valor * porcentagem / 100), porcentagem]


def diminuir(valor, porcentagem, formatar=True):
    """
    Funcao que recebe um valor e uma porcentagem e faz uma diminuicao com a porcentagem.
    :param valor: Valor que sera diminuido
    :param porcentagem: Valor que sera usado como porcentagem para fazer a diminuicao
    :param formatar: Recebe True para deixar o valor formatado de forma monetaria
    :return: Retorna uma lista com o valor diminuido e o valor da porcentagem
    """
    if formatar:
        valor_formatado = moeda(valor - (valor * porcentagem / 100))
        return [valor_formatado, porcentagem]

    else:
        return [valor - (valor * porcentagem / 100), porcentagem]


def dobro(valor, formatar=True):
    """
    Funcao que recebe um valor e retorna o dobro do valor
    :param valor: Valor que sera dobrado
    :param formatar: Recebe True para deixar o valor formatado de forma monetaria
    :return: Retorna o valor dobrado
    """
    if formatar:
        return moeda(valor * 2)

    else:
        return valor * 2


def metade(valor, formatar=True):
    """
    Funcao que recebe um valor e retorna a metade do valor
    :param valor: Valor que sera diminuido pela metade
    :param formatar: Recebe True para deixar o valor formatado de forma monetaria
    :return: Retorna o valor pela metade
    """
    if formatar:
        return moeda(valor / 2)

    else:
        return valor / 2


def moeda(valor, tipo_moeda='R\033[;32m$\033[m'):
    """
    Funcao que recebe um valor e o tipo de moeda, formata o valor
    retornando uma string com o valor monetario formatado.
    :param valor: Valor que sera formatado
    :param tipo_moeda: Tipo de moeda que aparecera
    :return: Retorna o valor formatado
    """
    return f'{tipo_moeda} {float(valor):.2f}'.replace('.', ',')
