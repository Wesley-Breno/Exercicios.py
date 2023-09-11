"""
Jogo de Craps. Faça um programa de implemente um jogo de Craps.
O jogador lança um par de dados, obtendo um valor entre 2 e 12.
Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou.
Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu.
Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto".
Seu objetivo agora é continuar jogando os dados até tirar este número novamente.
Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
"""

from random import randint


def craps() -> bool:
    """
    Funcao que simula o jogo de dados Craps. A funcao joga dois dados e analisa
    os valores, com base nisso ela aplica a regra do Craps e retorna True se o
    usuario ganhou, ou retorna False se caso o usuario tenha perdido.
    :return: Retorna True se o usuario ganhou, False se o usuario perdeu
    """

    valor1 = randint(1, 6)  # Valor do primeiro dado
    valor2 = randint(1, 6)  # Valor do segundo dado
    valores_total = valor1 + valor2

    # Se o usuario tirar 7 ou 11 de primeira, ele ganha.
    if valores_total == 7 or valores_total == 11:
        return True

    # Se o usuario tirar 2, 3 ou 12 de primeira, ele perde.
    elif valores_total == 2 or valores_total == 3 or valores_total == 12:
        return False

    # Se usuario tirou 4, 5, 6, 8, 9 ou 10, ira ficar jogando ate tirar esse valor de novo, caso ele tire 7, ele perde.
    else:
        ponto = valores_total  # Guardando valor que ele tirou
        while True:  # Enquanto o usuario nao tirar o valor da variavel 'ponto' ou tirar 7.
            valor1 = randint(1, 6)
            valor2 = randint(1, 6)
            valores_total = valor1 + valor2

            if valores_total == ponto:  # Se o usuario conseguiu tirar o valor novamente
                return True

            elif valores_total == 7:  # Se o usuario tirou 7
                return False
