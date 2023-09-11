"""
Faça um Programa que leia três números e mostre o maior deles.
"""

tres_numeros = []

while True:  # Enquanto o usuario nao digitar os tres numeros corretamente.
    try:
        for c in range(3):
            tres_numeros.append(int(input(f'Informe o {c + 1}º numero: ')))

    except:
        print('\n\n\t\t\033[;31mINFORME OS NUMEROS CORRETAMENTE.\033[m\n')
        tres_numeros = []

    else:
        break

print(f'\n\n\t\tO maior numero entre {tres_numeros} é {max(tres_numeros)}\n')
