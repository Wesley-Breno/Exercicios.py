"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma
tupla. Depois disso, mostre a listagem de números gerados e também
indique o menor e o maior valor que estão na tupla.
"""

from random import randint  # Importando o modulo random com a funcao randint para gerar numeros inteiros aleatorios

tupla = tuple(randint(1, 99) for x in range(5))  # Criando uma tupla com 5 numeros aleatorios

print('\n\n\t\tListagem de numeros aleatorios criados\n')

print('--' * 13)
for index, numero in enumerate(tupla):  # Mostrando cada numero da tupla
    print(f'{index + 1}º > {numero}')

print('--' * 13)
print(f'Maior numero: {max(tupla)}\nMenor numero: {min(tupla)}')  # Mostrando o maior e menor valor que tem na tupla
print('--' * 13)
