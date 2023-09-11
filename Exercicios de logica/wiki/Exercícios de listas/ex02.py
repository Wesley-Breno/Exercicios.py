"""
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""

vetor = []

while True:  # Enquanto o usuario nao informar os valores do vetor.
    try:
        for c in range(10):
            vetor.append(float(input(f'Informe o valor do {c + 1}º numero real do vetor\nValor: ')))

    except ValueError:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, informe o valor do vetor corretamente.\n\n')
        vetor = []

    else:
        break

print('\n\nResultado:')
for c in range(len(vetor) - 1, -1, -1):  # Fazendo uma contagem inversa com base na quantidade de valores no vetor
    if c == 0:
        print(vetor[c])  # Usando a contagem para mostrar o vetor na ordem inversa.
    else:
        print(vetor[c], end=', ')
