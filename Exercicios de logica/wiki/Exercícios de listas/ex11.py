"""
Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
"""

vetor = []  # Lista que ira conter os valores intercalados
vetor1 = []
vetor2 = []
vetor3 = []

while True:  # Enquanto o usuario nao informar os 10 valores de cada vetor
    try:
        for c in range(3):
            print()
            print('--' * 20)
            for n in range(10):  # Adicionando os 10 valores do vetor da vez
                vetor.append(int(input(f'Informe o valor do {n + 1}º valor do {c + 1}º vetor\nValor: ')))

            if c == 0:  # Se for para o primeiro vetor
                vetor1 = vetor[:]
                vetor = []
            elif c == 1:  # Se for para o segundo vetor
                vetor2 = vetor[:]
                vetor = []
            else:  # Se for para o terceiro vetor
                vetor3 = vetor[:]
                vetor = []

    except ValueError:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, insira corretamente os valores dos vetores.\n\n')
        vetor1 = []
        vetor2 = []
        vetor3 = []
        vetor = []

    else:
        break

for index, n in enumerate(vetor1):  # Adicionando os valores intercalados no terceiro vetor
    vetor.append(n)
    vetor.append(vetor2[index])
    vetor.append(vetor3[index])

print(f'\n\n\t\tResultado do 4º vetor com os elementos intercalados\n\n{vetor}')
