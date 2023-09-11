"""
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""
matriz = [], [], []  # Lista que corresponde a matriz

for lista in range(3):  # Para cada linha da matriz
    for unidade in range(3):  # Para cada elemento da matriz
        matriz[lista].append(int(input(f'Digite o {unidade + 1}º valor da {lista + 1}º linha > ')))

soma_dos_pares = 0
maior_valor_segunda_linha = max(matriz[1])  # Pegando o maior valor da segunda linha da matriz
soma_terceira_coluna = matriz[0][2] + matriz[1][2] + matriz[2][2]  # Somando os valores da terceira coluna

for index, linha in enumerate(matriz):
    for valor in linha:  # Para cada valor em cada linha da matriz
        if valor % 2 == 0:  # Se o valor for par
            soma_dos_pares += valor

print('\n\n\t\tMatriz\n')

for linha in matriz:
    print()
    for valor in linha:
        print(f'[ {valor} ]\t', end='')

print(f'\n\nA soma dos valores pares digitados: {soma_dos_pares}\n'
      f'A soma dos valores da terceira coluna: {soma_terceira_coluna}\n'
      f'O maior valor da segunda linha: {maior_valor_segunda_linha}\n')
