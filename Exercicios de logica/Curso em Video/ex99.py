"""
Faça um programa que tenha uma função chamada maior(), que receba vários
parâmetros com valores inteiros. Seu programa tem que analisar todos os
valores e dizer qual deles é o maior.
"""


def maior(*args):
    print('-=-' * 20)
    print('Analisando os valores passados...')

    for numero in args:
        print(numero, end=' ')

    print(f'Foram informados {len(args)} valores ao todo.\n'
          f'O maior valor informado foi {max(args)}.')
    print('-=-' * 20)


if __name__ == '__main__':
    maior(4, 2, 8, 5, 2, 4, 8)
