"""
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
-> Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
-> entre 3 e 4 como "Cúmplice"
-> e 5 como "Assassino".
-> Caso contrário, ele será classificado como "Inocente".
"""

perguntas = ['Telefonou para a vítima?', 'Esteve no local do crime?', 'Mora perto da vítima?', 'Devia para a vítima?',
             'Já trabalhou com a vítima?']
respostas = []  # Lista onde ficara as respostas do usuario
zeros = 0  # Quantidade de "Sim" que o usuario informou digitando o numero zero.

while True:  # Enquanto o usuario nao informar as 5 respostas para as 5 perguntas
    try:
        for pergunta in perguntas:
            print()
            print('--' * 14)
            resposta = int(input(f"""{pergunta}
[ 0 ] - Sim
[ 1 ] - Nao
Resposta: """))

            if resposta == 0 or resposta == 1:  # Se o usuario informou "Sim" ou "Nao"
                respostas.append(resposta)

            else:
                print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, digite [ 0 ] para sim ou [ 1 ] para nao.\n\n')
                respostas = []
                break

    except ValueError:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, digite [ 0 ] para sim ou [ 1 ] para nao.\n\n')
        respostas = []

    else:
        if len(respostas) == 5:  # Se o usuario informou as 5 respostas
            break

for res in respostas:  # Contando quantos "Sim" o usuario informou
    if res == 0:
        zeros += 1

print('\n\n\t\tVoce foi considerado um ', end='')

if zeros == 2:
    print('suspeito')
elif zeros == 3 or zeros == 4:
    print('cumplice')
elif zeros == 5:
    print('assassino')
else:
    print('inocente')
