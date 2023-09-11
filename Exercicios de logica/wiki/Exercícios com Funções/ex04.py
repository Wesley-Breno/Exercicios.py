"""
Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu
argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
"""


def retorna_p_se_negativo_ou_positivo(valor: int):
    """
    Funcao que recebe um valor numerico como parametro e retorna P ou N
    caso o numero seja positivo (P) ou negativo (N). Caso o numero seja igual a
    zero o programa ira retornar o N.
    :param valor: Valor numerico como parametro
    :return: Retorna (P) Caso o numero seja positivo, ou (N), caso o numero seja igual ou menor que zero.
    """
    if valor > 0:
        return 'P'

    return 'N'


if __name__ == "__main__":
    valor_positivo = retorna_p_se_negativo_ou_positivo(1)
    valor_zero = retorna_p_se_negativo_ou_positivo(0)
    valor_negativo = retorna_p_se_negativo_ou_positivo(-1)

    print(valor_positivo)
    print(valor_zero)
    print(valor_negativo)
