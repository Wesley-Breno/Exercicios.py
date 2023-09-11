"""
Faça um Programa que converta metros para centímetros.
"""

while True:  # Enquanto o usuario nao digitar um valor numerico
    try:
        metros = float(input('\nDigite os metros para converter em centimetros\n'
                             'Metros: '))

    except:  # Se o usuario nao digitou um valor numerico.
        print('\n\t\t\033[;31mDigite um valor numerico\033[m')

    else:  # Se o usuario digitou um valor numerico.
        break

print(f'\n\n\t\t{metros:.1f}m convertidos para CMs equivale a {metros * 100:.1f}cm\n\n')
