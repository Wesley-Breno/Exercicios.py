"""
Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores
deverão ser compostos pelos elementos intercalados dos dois outros vetores.
"""

vetor = []  # Lista que ira conter os valores intercalados
vetor1 = []
vetor2 = []

while True:  # Enquanto o usuario nao informar os 10 valores de cada vetor
    try:
        for c in range(2):
            print()
            print('--' * 20)
            for n in range(10):  # Adicionando os 10 valores do vetor da vez
                vetor.append(int(input(f'Informe o valor do {n + 1}º valor do {c + 1}º vetor\nValor: ')))

            if c == 0:  # Se for para o primeiro vetor
                vetor1 = vetor[:]
                vetor = []
            else:
                vetor2 = vetor[:]
                vetor = []

    except ValueError:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, insira corretamente os valores dos vetores.\n\n')
        vetor1 = []
        vetor2 = []
        vetor = []

    else:
        break

for index, n in enumerate(vetor1):  # Adicionando os valores intercalados no terceiro vetor
    vetor.append(n)
    vetor.append(vetor2[index])

print(f'\n\n\t\tResultado do terceiro vetor com os elementos intercalados\n\n{vetor}')
