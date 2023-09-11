"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
"""

numeros = []
numeros_pares = []
numeros_impares = []

while True:  # Enquanto o usuario nao informar os 20 valores.
    try:
        for c in range(20):
            numeros.append(int(input(f'\nAdicione o {c + 1}º valor\nValor: ')))

    except ValueError:  # Se o usuario informou um valor errado.
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, insira os valores corretamente.\n\n')
        numeros = []

    else:  # Se o usuario informou os 20 valores corretamente.
        break

for numero in numeros:  # Verificando cada numero e verificando se ele é par ou impar
    if numero % 2 == 0:  # Se o numero for par.
        numeros_pares.append(numero)
    else:  # Se o numero for impar.
        numeros_impares.append(numero)

print('\n\n\t\tResultado\n\n'
      f'Numeros informados: {numeros}\n'
      f'Numeros pares informados: {numeros_pares}\n'
      f'Numeros impares informados: {numeros_impares}')
