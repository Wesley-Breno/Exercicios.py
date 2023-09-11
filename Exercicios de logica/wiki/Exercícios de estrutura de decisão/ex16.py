"""
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

* Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os
demais valores, sendo encerrado;
* Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
* Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
* Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""

from math import sqrt  # Funcao que sera responsavel por fazer o calculo da raiz quadrada.

valor_a = int(input('Informe o valor de A: '))

if valor_a == 0:
    print('\nCom base no valor informado, esta nao sera uma equacao do segundo grau.\n'
          '(So calculamos equacao do segundo grau)')

else:
    valor_b = int(input('Informe o valor de B: '))
    valor_c = int(input('Informe o valor de C: '))

    delta = valor_b ** 2 - 4 * valor_a * valor_c  # Pegando o valor do delta

    try:
        x1 = (-valor_b + sqrt(delta)) / (2 * valor_a)  # Pegando o valor do primeiro X
        x2 = (-valor_b - sqrt(delta)) / (2 * valor_a)  # Pegando o valor do segundo X
    except:  # Se o valor do delta for menor que zero.
        x1 = '[Vazio]'
        x2 = '[Vazio]'

    if delta < 0:
        print('\nA equacao nao possui raizes reais.')

    elif delta == 0:
        print('\nA equacao possui apenas uma raiz real.')

    else:
        print('\nA equacao possui duas raizes reais.')

    print(f'''
Valor do primeiro X: {x1}
Valor do segundo X: {x2}
Valor do delta: {delta}''')
