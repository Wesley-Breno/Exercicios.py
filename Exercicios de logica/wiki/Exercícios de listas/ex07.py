"""
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""

vetor = []

while True:  # Enquanto o usuario nao informar corretamente os 5 valores do vetor.
    try:
        for c in range(5):
            vetor.append(int(input(f'\nInforme o valor do {c + 1}º numero\nValor: ')))

    except ValueError:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, informe corretamente os valores do vetor.\n\n')
        vetor = []

    else:
        break

multi = 1  # Variavel que ira conter a multiplicacao de todos os valores informados
for c in vetor:
    multi *= c

print('\n\t\tResultado\n'
      f'Soma dos valores informados: {sum(vetor)}\n'
      f'Multiplicação dos valores informados: {multi}\n'
      f'Valores que foram informados: {vetor}')
