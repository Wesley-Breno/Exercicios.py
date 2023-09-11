"""
Faça um Programa que peça dois números e imprima a soma.
"""

num = []  # Lista onde ficara os valores
for c in range(2):  # Usando o FOR para pegar os dois valores.
    num.append(int(input(f'Digite o {c + 1}º numero: ')))

print(f'\nA soma entre {num[0]} e {num[1]} equivale a {sum(num)}')  # Mostrando cada valor e sua soma.
