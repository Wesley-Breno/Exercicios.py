"""
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
"""

vetor = []

while True:  # Enquanto o usuario nao informar os 5 valores do vetor.
    try:
        for c in range(5):
            vetor.append(int(input(f'\nInforme o {c + 1}º valor do vetor\nValor: ')))

    except ValueError:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, informe os valores corretamente\n\n')

    else:
        break

print()
print('--' * 10)
print('Valores do vetor\n'
      f'{vetor}')
