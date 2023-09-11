"""
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os
dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
"""

pessoas = []  # Lista onde ficara as pessoas
cont = 1  # Contador para saber qual pessoa esta adicionando

while True:  # Enquanto o usuario nao digitar 0
    print(f'\n\t\tInforme os dados da {cont}º pessoa')
    print('\t\t  Digite [ 0 ] para encerrar\n')

    nome = str(input('\n‣Nome: '))

    if nome == '0':
        break

    if len(nome) > 1:
        try:
            sexo = str(input('‣Sexo [F ou M]: ').upper())[0]

        except IndexError:
            print('\n\n\t\t[\033[;31mERRO\033[m]: Informe o sexo com F ou M\n\n')

        else:

            if sexo == '0':
                break

            if sexo == 'F' or sexo == 'M' and sexo != '':

                try:
                    idade = int(input('‣Idade: '))
                    if idade == 0:
                        break

                except:
                    print('\n\n\t\t[\033[;31mERRO\033[m]: Informe um valor numerico como idade\n\n')

                else:
                    print(nome.title(), '\033[;32madicionado\033[m na lista.')
                    pessoa = {'nome': nome, 'idade': idade, 'sexo': sexo}  # Adicionando os dados em um dicionario
                    pessoas.append(pessoa)  # Adicionando o dicionario criado na lista
                    cont += 1  # Aumentando +1 para mostrar que esta adicionando a 2º pessoa, 3º, 4º e etc

            else:
                print('\n\n\t\t[\033[;31mERRO\033[m]: Informe o sexo com F ou M\n\n')

    else:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Informe o nome completo\n\n')

if len(pessoas) > 0:  # Se o usuario digitou pelo menos 1 pessoa
    media_idade = []  # Lista que ira conter todas as idades
    mulheres = []

    for pessoa in pessoas:
        media_idade.append(pessoa['idade'])

        if pessoa['sexo'] == 'F':
            mulheres.append(pessoa)

    media_idade = sum(media_idade) / len(media_idade)  # Transformando a lista na media de idades

    acima_da_media = []  # Lista onde ficara as pessoas acima da media
    for pessoa in pessoas:
        if pessoa['idade'] > media_idade:
            acima_da_media.append(pessoa)

    print(f'''\n\n\t\tResultado

- Total de pessoas cadastradas: {len(pessoas)}
- Media de idade: {int(media_idade)}''')
    print(f'- Pessoas com idade acima da media: ', end='')

    for indice, pessoa in enumerate(acima_da_media):
        if indice == len(acima_da_media) - 1:  # Se for a ultima pessoa
            print(f'{pessoa["nome"].title()}:{pessoa["idade"]}')
        else:
            print(f'{pessoa["nome"].title()}:{pessoa["idade"]}', end=', ')

    print('- Mulheres cadastradas: ', end='')

    for indice, pessoa in enumerate(mulheres):
        if indice == len(mulheres) - 1:
            print(pessoa['nome'].title())
        else:
            print(pessoa['nome'].title(), end=', ')

else:
    print('\n\n\t\t[\033[;31mERRO\033[m]: Voce nao adicionou pessoas suficiente\n\n')
