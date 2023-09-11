"""
Reverso do número.
Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
"""


def reverso_do_inteiro(num: int) -> int:
    """
    Funcao que recebe um valor inteiro e retorna o reverso desse numero.
    Por exemplo: 127 -> 721
    :param num: Valor numerico inteiro que sera revertido.
    :return: Retornar o numero inteiro revertido.
    """
    valor_string = str(num)
    valor_invertido = ''

    # Fazendo uma contagem do ultimo caractere ate o primeiro, e colocando cada caractere na variavel valor_invertido.
    for caractere in range(len(str(valor_string)) - 1, -1, -1):
        valor_invertido += valor_string[caractere]

    return int(valor_invertido)  # Retornando valor invertido


if __name__ == '__main__':
    inverte_123 = reverso_do_inteiro(123)
    print(inverte_123)
    