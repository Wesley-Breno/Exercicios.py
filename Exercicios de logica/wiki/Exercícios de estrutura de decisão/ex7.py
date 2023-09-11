"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""

numeros = []

print()
while True:  # Enquanto o usuario nao informar os numeros corretamente.
    try:  # Tentando pegar os 3 valores.
        for c in range(3):
            numeros.append(int(input(f'Digite o {c + 1}º numero: ')))

    except:  # Mostrando um erro na tela e esvaziando a lista para pegar os valores novamente.
        print('\n\t\tDIGITE OS NUMEROS CORRETAMENTE.\n')
        numeros = []

    else:  # Se o usuario informou os valores corretamente.
        break

print('\n\n\t\tResultado\n\n'
      f'Numeros informados: {numeros}\n'
      f'Maior numero informado: {max(numeros)}\n'
      f'Menor numero informado: {min(numeros)}\n')
