"""
Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade
de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
"""

turmas = {}  # Dicionario que ira conter o nome de cada turma e o total de alunos

while True:  # Enquanto o usuario nao informar a quantidade de turmas
    try:
        quantidade_de_turmas = int(input('\nInforme a quantidade de turmas\n'
                                         'Quantidade de turmas: '))

    except:
        print(f'\n\n\t\t[\033[;31mERRO\033[m]: Digite a quantidade de turmas\n\n')

    else:
        break

cont = 1  # Contador que ira servir para colocar numeração na turma. Ex: Turma 1, Turma 2...
while quantidade_de_turmas != 0:  # Enquanto o usuario nao informar a quantidade de alunos de cada turma
    try:
        quantidade_de_alunos = int(input(f'\nInforme a quantidade de alunos da {cont}º turma: '))

    except:
        print(f'\n\n\t\t[\033[;31mERRO\033[m]: Digite a quantidade de alunos da {cont}º turma corretamente.\n\n')

    else:
        if quantidade_de_alunos > 39:  # Se alguma turma ultrapassar a quantidade de 40 alunos
            print(f'\n\n\t\t[\033[;31mERRO\033[m]: Uma turma nao pode ultrapassar de 40 alunos.\n\n')

        else:
            turmas[f'Turma {cont}'] = quantidade_de_alunos
            cont += 1
            quantidade_de_turmas -= 1

print('\n\n\t\tResultado\n\n'
      f'Media de alunos por turma: {int(sum(turmas.values()) / len(turmas.keys()))}')

for key, value in turmas.items():
    print(f'[ {key} ] = {value} alunos')
