"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear
6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""

from random import randint  # Importando metodo do modulo random para gerar numeros aleatorios

while True:
    quantidade = str(input('Quantos palpites da mega sena deseja ver?\nPalpites: '))

    if quantidade.isdigit():  # Se o valor digitado for um numero
        quantidade = int(quantidade)

        print(f'\n\n\t\t{quantidade} Palpites da mega sena\n')

        for c in range(0, quantidade):  # Mostrando o total de palpites pedidos
            print(f'\n{c + 1}º Palpite: ', end='')
            for n in range(6):  # Gerando 6 numeros aleatorios
                print(f'\033[;1m{randint(1, 60)}\033[m', end=' ')

        break  # Encerrando programa depois de mostrar os palpites

    else:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Informe a quantidade de palpites desejada.\n\n')
