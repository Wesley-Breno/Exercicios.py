"""
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
"""

while True:  # Enquanto o usuario nao digitar um valor valido
    try:
        graus_celsius = float(input('Digite os graus Celsius: '))

    except:
        print('\n\n\t\t\033[;31mDIGITE OS VALORES CORRETAMENTE.\033[m')

    else:
        break

graus_fahrenheit = (graus_celsius * (9/5)) + 32  # Convertendo graus Celsius para Fahrenheit

print(f'\n\n\t\t{graus_celsius:.1f}ºC convertido para Fahrenheit equivale a {graus_fahrenheit:.1f}ºF')
