"""
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares
e a quantidade de números impares.
"""

while True:  # Enquanto o usuario nao informar os 10 valores
    numeros = []

    try:
        for c in range(10):
            numeros.append(int(input(f'Informe o {c + 1}° numero: ')))

    except:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, insira os valores corretamente.\n\n')

    else:
        break

quantidade_pares = 0
quantidade_impares = 0

for numero in numeros:  # Vendo quantos pares e impares foram informados
    if numero % 2 == 0:
        quantidade_pares += 1

    else:
        quantidade_impares += 1

print('\n\n\t\tResultado\n\n'
      f'Numeros informados: {numeros}\n'
      f'Total numeros pares: {quantidade_pares}\n'
      f'Total numeros impares: {quantidade_impares}\n\n')
