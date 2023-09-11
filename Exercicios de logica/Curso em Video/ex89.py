"""
Crie um programa que leia nome e duas notas de vários alunos
e guarde tudo em uma lista composta. No final, mostre um boletim
contendo a média de cada um e permita que o usuário possa mostrar
as notas de cada aluno individualmente.
"""

alunos = {}  # Dicionario onde ficara o ID, nome e notas de cada aluno informado
cont = 0  # Contador que recebe +1 para ser o ID de cada aluno

print('\n\n\t\t\033[;37mDigite [ 0 ] no nome do aluno para ver tabela\033[m\n\n')

while True:  # Enquanto o usuario nao digitar 0 no nome do aluno, para ver a tabela de alunos
    cont += 1
    notas = []

    print()
    print('__' * 12)
    nome = str(input('Nome do aluno: '))

    if nome == '0':
        break

    if len(nome) > 1:  # Se for um nome com pelo menos 2 caracteres
        while len(notas) != 2:
            for c in range(2):  # Pegando as duas notas do aluno
                try:
                    nota = float(input(f'Digite a {c + 1}º nota de {nome}: '))

                except:  # Se o usuario nao informou as notas corretamente, esvazia a lista de notas e adiciona de novo
                    print('\n\n\t\t[\033[;31mERRO\033[m: Digite a nota do aluno corretamente.\n\n')
                    notas = []
                    break

                else:
                    notas.append(nota)

        alunos.update({f'{cont}': {'nome': nome, 'notas': notas}})  # Adicionando aluno no dicionario de alunos

    else:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Digite um nome mais comprido\n\n')
        cont -= 1

if len(alunos) >= 1:  # Se o usuario informou pelo menos 1 aluno
    print()
    print('--' * 20)
    print('ID\t\tNome\t\tMedia')
    print('--' * 20)

    for chave, valor in alunos.items():  # Mostrando ID, nome e media
        print(chave, '\t\t', valor['nome'], '\t\t', ((valor['notas'][0] + valor['notas'][1]) / len(valor['notas'])))

    print('--' * 20)

    print('\n\n\t\t\033[;37mDigite [ 0 ] para encerrar programa\033[m\n\n')

    while True:  # Enquanto o usuario nao digitar 0 para encerrar o programa
        ver = str(input('\nDigite o ID do aluno para ver suas notas...\nID aluno: '))

        if ver == '0':
            break

        if ver.isdigit():
            if ver in alunos:  # Se o ID digitado tiver em um dos alunos
                print(f'\n\n\tO aluno {alunos[ver]["nome"]} tirou as seguintes notas: {alunos[ver]["notas"]}\n\n')

            else:
                print('\n\n\t\t[\033[;31mERRO\033[m]: Indice do aluno nao encontrado.\n\n')

        else:
            print('\n\n\t\t[\033[;31mERRO\033[m]: Digite o indice do aluno desejado.\n\n')

else:
    print('\n\n\t\tVoce nao informou nenhum aluno\n\n')

print('\n\n\t\tPrograma encerrado... ate logo :)\n\n')
