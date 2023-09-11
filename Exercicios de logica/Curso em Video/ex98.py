"""
Faça um programa que tenha uma função chamada contador(), que receba
três parâmetros: início, fim e passo. Seu programa tem que realizar
três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""

from time import sleep


def contador():

    # De 1 ate 10, de 1 em 1
    inicio = 1
    fim = 10
    passo = 1
    print('Contagem de 1 ate 10 de 1 em 1:')
    for c in range(inicio, fim + 1, passo):
        print(c, end=' ')
        sleep(0.5)
    print('Fim!')

    # De 10 ate 0, de 2 em 2
    inicio = 10
    fim = 0
    passo = -2
    print('\nContagem de 10 ate 0 de 2 em 2:')
    for c in range(inicio, fim - 1, passo):
        print(c, end=' ')
        sleep(0.5)
    print('Fim!')

    # Contagem personalizada
    print('\nAgora é sua vez de personalizar a contagem!')
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))

    print(f'\nContagem de {inicio} ate {fim} de {passo} em {passo}:')
    for c in range(inicio, fim - 1, passo):
        print(c, end=' ')
        sleep(0.5)
    print('Fim!')


contador()
