"""
Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos
possuem altura inferior à média de altura desses alunos.
"""

# Idade e altura de 30 alunos
idades_alturas = [
    [10, 1.40], [11, 1.45], [12, 1.50], [13, 1.55], [14, 1.60], [15, 1.65], [16, 1.70], [17, 1.75], [18, 1.80],
    [19, 1.85], [20, 1.90], [21, 1.95], [22, 2.00], [23, 2.10], [24, 2.15], [25, 2.20], [26, 2.25], [27, 2.30],
    [28, 2.35], [29, 2.40], [30, 2.45], [31, 2.50], [32, 2.55], [33, 2.60], [34, 2.65], [35, 2.70], [36, 2.75],
    [37, 2.80], [38, 2.85], [39, 2.90]
]

media_altura = 0
quantidade_alunos = 0  # Quantidade de alunos que tem mais de 13 anos e possuem altura inferior à média de altura

for aluno in idades_alturas:
    media_altura += aluno[1]

media_altura = media_altura / len(idades_alturas)  # Descobrindo a media de altura dos alunos

for aluno in idades_alturas:
    if aluno[0] > 13 and aluno[1] < media_altura:  # Contando alunos que tem mais de 13 anos e altura menor que a media
        quantidade_alunos += 1

print(f'Quantidade de alunos com mais de 13 anos que possuem altura inferior à média de altura\nQuantidade de alunos: '
      f'{quantidade_alunos}')
