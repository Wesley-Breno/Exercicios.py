"""
Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e
mantenha tudo funcionando.
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


def resumo(valor, aumento_porcentagem, diminuicao_porcentagem, formatar=True):
    """
    Funcao que mostra um resumo do valor onde é mostrado a
    metade, dobro, aumento percentual, diminuicao percentual do valor.
    Mostrando o valor com formatacao monetaria ou nao.
    :param valor: Valor que sera mostrado
    :param aumento_porcentagem: Valor percentual que sera adicionado no valor
    :param diminuicao_porcentagem: Valor percentual que sera diminuido do valor
    :param formatar: Recebe True para deixar o valor com formatacao monetaria, ou False para nao formatar
    :return: None
    """

    if formatar:
        metade_valor = metade(valor)  # Pegando a metade do valor
        dobro_valor = dobro(valor)  # Pegando o dobro
        aumento_valor = aumentar(valor, aumento_porcentagem)  # Fazendo um aumento de 10% no valor
        diminuir_valor = diminuir(valor, diminuicao_porcentagem)  # Fazendo uma diminuicao de 10% no valor

        # Mostrando o resultado
        print('\n\n\t\t\033[;1mResultado\033[m\n\n'
              f'|> A metade de {moeda(valor)} é {metade_valor}\n'
              f'|> O dobro de {moeda(valor)} é {dobro_valor}\n'
              f'|> Um aumento de {aumento_valor[1]}% de {moeda(valor)} é {aumento_valor[0]}\n'
              f'|> Uma diminuicao de {diminuir_valor[1]}% de {moeda(valor)} é {diminuir_valor[0]}')

    else:
        metade_valor = metade(valor, False)
        dobro_valor = dobro(valor, False)
        aumento_valor = aumentar(valor, aumento_porcentagem, False)
        diminuir_valor = diminuir(valor, diminuicao_porcentagem, False)

        print('\n\n\t\t\033[;1mResultado\033[m\n\n'
              f'|> A metade de {valor} é {metade_valor}\n'
              f'|> O dobro de {valor} é {dobro_valor}\n'
              f'|> Um aumento de {aumento_valor[1]}% de {valor} é {aumento_valor[0]}\n'
              f'|> Uma diminuicao de {diminuir_valor[1]}% de {valor} é {diminuir_valor[0]}')
