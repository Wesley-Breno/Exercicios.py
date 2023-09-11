"""
Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:

A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

notas = []
while True:  # Enquanto o usuario nao digitar as duas notas corretamente.
    try:
        for c in range(2):
            notas.append(float(input(f'Digite a {c + 1}º nota do aluno: ')))

    except:
        print('\n\t\t\033[;31mINFORME A NOTA DO ALUNO CORRETAMENTE.\033[m\n')
        notas = []  # Esvaziando lista das notas para pegar os valores de novo.

    else:
        break

media = sum(notas) / len(notas)  # Pegando a media do aluno.

if media == 10:
    print('\n\n\t\tAluno \033[;32maprovado\033[m com distinção\n')

elif media >= 7:
    print('\n\n\t\tAluno \033[;32maprovado\033[m\n')

else:
    print('\n\n\t\tAluno \033[;31mreprovado\033[m\n')
