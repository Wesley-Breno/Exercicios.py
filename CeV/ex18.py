# Faça um programa que leia um ângulo qualquer e mostre na tela
# o valor do seno, cosseno e tangente desse ângulo.

# Importando as funcoes que criei e a biblioteca math para fazer
# o calculo do seno, cosseno e tangente.
from functions import *
from math import cos, sin, tan

stop = 0
while stop != 1:
    titulo('Valores de um ângulo')
    try:
        angulo = float(input('\nDigite o valor do ângulo: '))
    except:
        erro('Digite um valor valido.')
    else:
        if type(angulo) == float:
            pular(2)
            print('__' * 14)
            print(f'Valores do ângulo {int(angulo)}')
            print('__' * 14)
            print(f"""Valor do seno: {sin(angulo):.2f}
-
Valor do cosseno: {cos(angulo):.2f}
-
Valor da tangente: {tan(angulo):.2f}""")
            print('__' * 14)
            press_enter()
            stop = encerrar('calculo')
        else:
            erro('Digite um valor valido.')

pular(5)
print(f'{"Programa encerrado com sucesso!":^45}')
print(f'{"Ate logo :D":^45}')
