# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

from functions import press_enter    # Funcoes que criei.
from time import sleep    # Funcao para fazer o programa "dormir".

print()
print('--' * 22)
print(f'\033[;1m{"Numero pares de 1 a 50.":^45}\033[m')
print('--' * 22)
press_enter('para mostrar.')

print()
for c in range(1, 51):    # Fazendo a contagem de 1 a 50.
    if c == 50:    # Se chegar no final da contagem, tira o ', ' do end=''.
        print(f'\033[;32m{c}\033[m', end='')
    else:
        if c % 2 == 0:    # Se o numero for par.
            print(f'\033[;32m{c}\033[m', end=', ')
            sleep(0.4)    # Fazendo o programa "dormir", para demorar 0.4secs para fazer o proximo passo.
        else:
            print(f'{c}', end=', ')
            sleep(0.4)
