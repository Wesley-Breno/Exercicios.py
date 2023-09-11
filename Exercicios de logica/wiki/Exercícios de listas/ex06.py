"""
Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o
número de alunos com média maior ou igual a 7.0.
"""

alunos = []
notas = []
alunos_na_media = []

while True:  # Enquanto o usuario nao informar as 4 notas dos 10 alunos.
    try:
        for aluno in range(10):  # Fazendo contagem dos alunos.
            print()
            for nota in range(4):  # Pegando as 4 notas do aluno da vez.
                notas.append(float(input(f'Informe a {nota + 1}º nota do {aluno + 1}º aluno\nNota: ')))
            alunos.append(notas)
            notas = []
    except ValueError:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, informe os dados corretamente.\n\n')
        notas = []
        alunos = []
    else:
        break

for index, aluno in enumerate(alunos):  # Adicionando em uma lista os alunos que tiverem media maior ou igual a 7
    if sum(aluno) / len(aluno) >= 7:
        alunos_na_media.append([index + 1, aluno, {sum(aluno) / len(aluno)}])

if len(alunos_na_media) > 0:  # Se tiver alunos com media maior ou igual a 7
    print('\n\t\tAlunos com media maior ou igual a 7\n')
    for aluno in alunos_na_media:
        print(f"""
{aluno[0]}º aluno:
Notas: {aluno[1]}
Media: {aluno[2]}""")

else:
    print('\n\t\tNenhum aluno tirou nota maior ou igual a 7\n')
