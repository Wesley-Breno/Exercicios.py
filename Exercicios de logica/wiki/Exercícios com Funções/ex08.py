"""
Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
"""


def contagem_de_digitos(num: int) -> int:
    """
    Funca que recebe um valor numerico e retorna
    a quantidade de caracteres que o este numero tem.
    :param num: Numero que sera feito a contagem de caracteres
    :return: Retorna a quantidade de caracteres que o valor do parametro tem.
    """

    # Transformando o valor numerico em uma string e usando a funcao len() para fazer a contagem dos caracteres
    return len(str(num))


if __name__ == "__main__":
    quantidade_caracteres = contagem_de_digitos(123)
    print(quantidade_caracteres)
