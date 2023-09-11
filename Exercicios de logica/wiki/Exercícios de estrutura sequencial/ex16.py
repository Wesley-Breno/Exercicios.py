"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18
litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""

while True:  # Enquanto o usuario nao digitar os metros quadrados
    try:
        metros = float(input('\nInforme quantos metros quadrados é a parede: '))

    except:
        print('\n\n\t\t\033[;31mINFORME UM VALOR NUMERICO VALIDO.\033[m')

    else:
        break

quantidade_latas_de_tinta = int(metros / 54) if metros % 54 == 0 else int((metros / 54) + 1)
total_a_pagar = quantidade_latas_de_tinta * 80

print(f'\n\n\t\tResultado\n\nCom uma parede de {int(metros)}²m voce precisara de:\n'
      f'{quantidade_latas_de_tinta}x Latas de tinta\n'
      f'Total a pagar: R\033[;32m$\033[m{total_a_pagar:.2f}')
