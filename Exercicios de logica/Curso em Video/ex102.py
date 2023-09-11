"""
Crie um programa que tenha uma função fatorial()
que receba dois parâmetros: o primeiro que indique
o número a calcular e outro chamado show, que será
um valor lógico (opcional) indicando se será mostrado
ou não na tela o processo de cálculo do fatorial.
"""
from math import factorial  # Importando funcao para fazer o calcula da fatorial


def fatorial(value, show=False):
    """
    Funcao para mostrar o resultado da fatorial de um numero.
    :param value: Parametro que recebe o valor que vai ser calculado.
    :param show: Parametro para mostrar ou nao o calculo ou so mostrar o resultado.
    :return: None
    """
    valor_fatorial = factorial(value)  # Resultado da fatorial
    if show:  # Se decidiu mostrar o calculo
        print(f'{value}', end=' x ')
        for c in range(value):  # Fazendo contagem da fatorial para mostrar cada valor

            if (value - 1) != 0:  # Se for o ultimo valor.
                if (value - 1) == 1:  # Se for o valor 1 (ultimo valor)
                    print(value - 1, end=' = ')
                    value -= 1

                else:  # Se nao for o ultimo valor
                    print(value - 1, end=' x ')
                    value -= 1

    print(f'{valor_fatorial}')  # Mostrando o resultado da fatorial


fatorial(3, True)
