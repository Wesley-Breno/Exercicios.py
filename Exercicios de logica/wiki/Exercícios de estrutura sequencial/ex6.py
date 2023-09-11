"""
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

area == pi * raio²
"""

while True:
    try:
        raio = float(input('\nDigite o raio de um circulo em cm: '))
    except:
        print('\n\n\t\t\033[;31mDIGITE UM VALOR NUMERICO\033[m')
    else:
        break

area = 3.14 * (raio ** 2)
print(f'\n\n\t\tA area de um circulo com o raio de {raio:.1f}cm, equivale a uma area de {area:.1f}cm².')
