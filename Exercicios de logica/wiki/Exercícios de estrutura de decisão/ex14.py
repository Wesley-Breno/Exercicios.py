"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a
sua média. A atribuição de conceitos obedece à tabela abaixo:

  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for
A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""

notas = []
while True:  # Enquanto o usuario nao digitar as duas notas corretamente.
    try:
        for c in range(2):
            notas.append(float(input(f'Digite a {c + 1}º nota do semestre: ')))

    except:
        print('\n\n\t\t\033[;31mDIGITE AS NOTAS CORRETAMENTE\033[m\n')
        notas = []

    else:
        break

media = sum(notas) / len(notas)

if media <= 4:
    conceito = 'E'

elif media <= 6:
    conceito = 'D'

elif media <= 7.5:
    conceito = 'C'

elif media <= 9:
    conceito = 'B'

else:
    conceito = 'A'

print('\n\n\t\tResultado\n\n'
      f'Notas do aluno: {notas}\n'
      f'Media: {media}\n'
      f'Conceito: {conceito}')

print('Situacao: ', end='')
if conceito == 'A' or conceito == 'B' or conceito == 'C':
    print('\033[;32maprovado\033[m')

else:
    print('\033[;31mreprovado\033[m')
