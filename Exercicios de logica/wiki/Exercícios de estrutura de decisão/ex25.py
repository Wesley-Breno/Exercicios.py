"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""

respostas = []  # Lista onde ficara todas as respostas do usuario
perguntas = ["Telefonou para a vítima?",
             "Esteve no local do crime?",
             "Mora perto da vítima?",
             "Devia para a vítima?",
             "Já trabalhou com a vítima?"]  # Lista com todas as perguntas que serao feitas

while len(respostas) != 5:  # Enquanto o usuario nao responder todas as perguntas
    try:
        for pergunta in perguntas:
            print()
            print('--' * 22)
            resposta = int(input('Digite o numero conforme a resposta desejada\n\n'
                                 f'\033[;1m{pergunta}\033[m\n\n'
                                 f'[ 1 ] - Sim\n'
                                 f'[ 0 ] - Nao\n\n'
                                 f'Resposta: '))

            if resposta == 1 or resposta == 0:  # Se a resposta estiver entre 'sim' e 'nao'
                respostas.append(resposta)

            else:
                print('\n\n\t\t\033[;31mERRO\033[m\n'
                      '\t\tDigite [ 1 ] para "Sim" e [ 0 ] para "Nao"')
                respostas = []
                break

    except:
        print('\n\n\t\t\033[;31mERRO\033[m\n'
              '\t\tDigite [ 1 ] para "Sim" e [ 0 ] para "Nao"')
        respostas = []

print(f'\n\n\t\tVoce esta classificado como: ', end='')

if sum(respostas) == 2:
    print('Suspeito')

elif sum(respostas) == 3 or sum(respostas) == 4:
    print('Cumplice')

elif sum(respostas) == 5:
    print('Assasino')

else:
    print('Inocente')
