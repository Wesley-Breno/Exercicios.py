# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

from functions import *
from math import sqrt

while True:
    titulo('_- Hipotenusa -_')
    try:
        cateto_oposto = float(input('\nInforme o comprimento do cateto oposto: '))
        cateto_adjacente = float(input('\nInforme o comprimento do cateto adjacente: '))
    except:
        erro('Informe um dado valido.')
    else:
        hipotenusa = (cateto_oposto * cateto_oposto) + (cateto_adjacente * cateto_adjacente)
        hipotenusa = sqrt(hipotenusa)
        pular(2)
        print('__' * 15)
        print(f'O valor da hipotenusa é \033[;1m{hipotenusa:.2f}\033[m')
        print('__' * 15)
        press_enter()
        stop = encerrar()
        if stop == 1:
            break

pular(5)
print(f'{"Programa encerrado":^45}')
print(f'{"Ate logo :D":^45}')
