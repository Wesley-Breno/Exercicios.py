from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'C'},
    {'nome': 'Anderson', 'nota': 'B'},
]

alunos.sort(key=lambda chave: chave['nota'])
agrupados = groupby(alunos, key=lambda chave: chave['nota'])  # Agrupando valores da lista condiserando a chave ['nota']

for grupo, valor in agrupados:
    print(f'\nAlunos que tiraram {grupo}')
    for aluno in valor:
        print(f'\t{aluno}')
