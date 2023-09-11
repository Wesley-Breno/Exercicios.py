"""
Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
"""

from time import sleep

print('\n\n\t\tNumeros impares entre 1 e 50\n')
for c in range(1, 51):
    if c % 2 != 0:
        sleep(0.3)
        print(c, end=' ')
