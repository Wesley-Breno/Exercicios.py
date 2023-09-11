"""
Faça um programa que leia nome e peso de várias pessoas, guardando
tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""

lista_pessoas = []  # Lista de todas as pessoas cadastradas

print('\n\n\t\t\033[;37mDigite 0 pra parar de adicionar\033[m\n\n')

cont = 0
while True:  # Enquanto o usuario nao digitar 0 para encerrar
    cont += 1  # Mostrando se é a 1º pessoa a ser adicionada, 2º, 3º e etc.

    print('\n')
    print('__' * 14)
    nome = str(input(f'Nome da {cont}º pessoa: '))

    if nome == '0':  # Se o usuario quiser encerrar
        break

    peso = int(input('Peso: '))

    if peso == 0:  # Se o usuario quiser encerrar
        break

    lista_pessoas.append([nome, peso])  # Adicionando na lista de pessoas

if len(lista_pessoas) > 0:  # Se o usuario adicionou pelo menos uma pessoa
    pesos = []  # Lista com os pesos de todas as pessoas

    for nome, peso in lista_pessoas:
        pesos.append(peso)  # Adicionando os pesos

    mais_pesados = max(pesos)  # Pegando o maior valor dos pesos
    menos_pesados = min(pesos)  # Pegando o menor valor dos pesos
    pessoas_pesadas = []
    pessoas_leves = []

    for pessoa in lista_pessoas:

        if pessoa[1] == mais_pesados:  # Se a pessoa tiver o maior peso
            pessoas_pesadas.append(pessoa)

        if pessoa[1] == menos_pesados:  # Se a pessoa tiver o menor peso
            pessoas_leves.append(pessoa)

    print('\n\n\t\tResultado\n'
          f'\nTotal de pessoas cadastradas: {len(lista_pessoas)}\n'
          f'As pessoas mais leves: ', *pessoas_leves,
          f'\nAs pessoas mais pesadas: ', *pessoas_pesadas)

else:
    print('\n\n\t\tVoce nao digitou nenhuma pessoa\n\n')
