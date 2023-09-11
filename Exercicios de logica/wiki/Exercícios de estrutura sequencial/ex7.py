"""
Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

area == lado²
"""

while True:
    try:
        lado_do_quadrado = float(input('\nInforme um lado do quadrado para fazer o calculo.\n'
                                       'lado do quadrado: '))
    except:
        print('\n\n\t\t\033[;31mDIGITE UM VALOR NUMERICO\033[m\n')

    else:
        break

area_do_quadrado = lado_do_quadrado ** 2
print('\n\n\t\tResultado\n\n'
      f'| Lado do quadrado: {lado_do_quadrado:.1f}cm²\n'
      f'| Area do quadrado: {area_do_quadrado:.1f}cm²\n'
      f'| O dobro da area: {area_do_quadrado * 2:.1f}cm²\n')
