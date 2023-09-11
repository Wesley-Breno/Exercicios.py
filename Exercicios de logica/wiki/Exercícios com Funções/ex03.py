"""
Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
"""


def soma_tres_valores(num1: float, num2: float, num3: float):
    """
    Funcao que recebe tres parametros com valores numericos e retorna a soma deles.
    :param num1:  Primeiro valor numerico
    :param num2:  Segundo valor numerico
    :param num3:  Terceiro valor numerico
    :return: Soma dos tres parametros
    """
    return num1 + num2 + num3  # Retornando a soma dos tres parametros


if __name__ == "__main__":
    total = soma_tres_valores(1, 1.3, 3)  # Chamando funcao e fornecendo os tres parametros numericos
    print(total)  # Mostrando na tela a soma dos tres parametros que foram fornecidos
