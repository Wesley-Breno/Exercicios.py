"""
Faça um programa que leia 5 números e informe o maior número.
"""

valores = []  # Lista onde ficara os 5 valores numericos
contador = 1  # Contador para informar qual valor esta sendo informado

while len(valores) != 5:  # Enquanto o usuario nao informar os 5 valores corretamente
    try:
        valores.append(int(input(f'Informe o {contador}º valor: ')))
    except:  # Se o usuario informou o valor incorretamente
        print('\n\n\t\t[\033[;31mERRO\033[m]: Informe os 5 valores numericos corretamente.\n\n')
        valores = []
        contador = 1
    else:
        contador += 1

print(f'\n\n\t\tO maior valor informado foi [{max(valores)}]\n\n')
