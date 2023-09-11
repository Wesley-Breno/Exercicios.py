"""
Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""

numeros = []
while True:  # Enquanto o usuario nao digitar os numeros corretamente.
    try:
        for c in range(3):
            numeros.append(int(input(f'Digite o {c + 1}º numero: ')))

    except:
        print('\n\t\t\033[;31mDIGITE OS NUMEROS CORRETAMENTE.\033[m\n')
        numeros = []

    else:
        break


print('\n\nNumeros digitados em ordem decrescente;\n', sorted(numeros, reverse=True))
