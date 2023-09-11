"""
Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do
vetor.
"""

vetor_A = []
soma_dos_quadrados = 0

while True:  # Enquanto o usuario nao informar corretamente os valores do vetor.
    try:
        for c in range(10):
            print()
            print('--' * 15)
            vetor_A.append(int(input(f'Digite o {c + 1}º valor do vetor A\nValor: ')))

    except ValueError:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, informe corretamente os valores do vetor.\n\n')
        vetor_A = []

    else:
        break

# Fazendo a soma dos quadrados de cada elemento
soma_dos_quadrados = sum([soma_dos_quadrados + n ** 2 for n in vetor_A])

print('\n\n\t\tResultado\n\n'
      f'Soma dos quadrados dos valores do vetor A\n'
      f'Soma dos quadrados: {soma_dos_quadrados}')
