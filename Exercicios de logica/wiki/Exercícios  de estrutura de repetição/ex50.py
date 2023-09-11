"""
Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.
"""

while True:  # Enquanto o usuario nao informar a quantidade de termos
    try:
        termos = int(input('\nInforme a quantidade de termos...\nTermos: '))

    except ValueError:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Por favor, informe a quantidade de termos.\n\n')

    else:
        break

soma = 1

print('h = 1 + ', end='')
for c in range(1, termos + 1):
    soma += 1/c  # Fazendo a soma do termo da vez
    if c == termos:  # Se for o ultimo termo
        print(f'1/{c} = ', end='')
    else:
        print(f'1/{c} + ', end='')

print(soma)
