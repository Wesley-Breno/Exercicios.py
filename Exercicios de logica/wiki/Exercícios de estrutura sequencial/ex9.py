"""
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""

while True:  # Enquanto o usuario nao digitar um valor valido
    try:
        graus_fahrenheit = float(input('Digite os graus Fahrenheit: '))

    except:
        print('\n\n\t\t\033[;31mDIGITE OS VALORES CORRETAMENTE.\033[m')

    else:
        break

graus_celsius = (graus_fahrenheit - 32) * (5/9)  # Convertendo graus Fahrenheit em Celsius

print(f'\n\n\t\t{graus_fahrenheit:.1f}ºF convertido para Celsius equivale a {graus_celsius:.1f}ºC')
