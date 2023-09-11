"""
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto
e o número do aluno mais baixo, junto com suas alturas.
"""

alunos = dict()

while len(alunos) < 10:
    try:
        print()
        print('--' * 30)
        numero_aluno = int(input('Informe um numero inteiro para representar o ID do aluno\nNumero inteiro: '))
        altura_aluno = int(input('---\nInforme a altura do aluno em centimetros\nAltura do aluno: '))
    except:
        print('\n\n\t\t[ERRO]: Informe os dados corretamente.\n\n')
    else:
        alunos[numero_aluno] = altura_aluno

alturas = []
for v in alunos.values():
    alturas.append(v)

aluno_mais_alto = 0
aluno_mais_baixo = 0

for k, v in alunos.items():
    if v == max(alturas):
        aluno_mais_alto = k, v

    if v == min(alturas):
        aluno_mais_baixo = k, v

print('\n\n\t\tResultado\n\n'
      'Alunos mais alto\n'
      f'[ID] - {aluno_mais_alto[0]}\n'
      f'[Altura] - {aluno_mais_alto[1]}cms\n\n'
      f'Aluno mais baixo\n'
      f'[ID] - {aluno_mais_baixo[0]}\n'
      f'[Altura] - {aluno_mais_baixo[1]}cms')
