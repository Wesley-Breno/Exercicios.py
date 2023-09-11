"""
Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não
bissexto.
"""

ano = int(input('\nInforme o ano atual e informarei se ele é um ano bissexto\nAno atual: '))

if ano % 4 == 0:  # Se o ano for bissexto
    print(f'\n\n\t\t{ano} é \033[;32mbissexto\033[m')

else:
    print(f'\n\n\t\t{ano} \033[;31mnão\033[m é bissexto')
