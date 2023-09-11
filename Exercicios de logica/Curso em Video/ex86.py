"""
Crie um programa que declare uma matriz de dimensão 3x3
e preencha com valores lidos pelo teclado. No final,
mostre a matriz na tela, com a formatação correta.
"""

matriz = [[], [], []], [[], [], []], [[], [], []]  # Lista que corresponde a matriz

for lista in range(3):  # Para cada linha da matriz
    for unidade in range(3):  # Para cada elemento da matriz
        matriz[lista][unidade].append(str(input('Digite o valor para a matriz> ')))

print('\n\n\t\tMatriz\n')

for linha in matriz:
    print(*linha)
