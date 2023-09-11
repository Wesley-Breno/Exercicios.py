"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18
litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;

misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os
valores para cima, isto é, considere latas cheias.

1 lata de tinta 18l == 108m² == R$80
1 lata de tinta 3,6l == 21,6m² == R$25

"""

while True:  # Enquanto o usuario nao informar os metros quadrados
    try:
        metros = float(input('Informe quantos metros quadrados é a parede: '))

    except:
        print('\n\n\t\t\033[;31mDIGITE O VALOR CORRETAMENTE.\033[m\n\n')

    else:
        break

print('\n\n\t\tResultado\n\n'
      'Voce precisara de: ')

if metros < 108:  # Se precisar so das latas de 3,6l
    quantidade_de_latas_de_25_reais = int(metros / 21.6) if metros % 21.6 == 0 else int((metros / 21.6) + 1)
    print(f'{quantidade_de_latas_de_25_reais} latas de 3,6l\n\n'
          f'Total a pagar: R${quantidade_de_latas_de_25_reais * 25:.2f}')

else:
    if metros % 108 == 0:  # Se precisar so de latas de 18l
        quantidade_de_latas_de_80_reais = metros / 108
        print(f'{quantidade_de_latas_de_80_reais} latas de 18l\n\n'
              f'Total a pagar: R${quantidade_de_latas_de_80_reais * 80:.2f}')

    else:  # Se precisar de latas de 18l e latas de 3,6l
        quantidade_de_latas_de_80_reais = int(metros / 108)
        quantidade_de_latas_de_25_reais = int((metros - (108 * quantidade_de_latas_de_80_reais)) / 21.6) if metros % 21.6 == 0 else int(((metros - (108 * quantidade_de_latas_de_80_reais)) / 21.6) + 1)

        print(f'{quantidade_de_latas_de_80_reais} latas de 18l\n'
              f'{quantidade_de_latas_de_25_reais} latas de 3,6l\n\n'
              f'Total a pagar: R${(quantidade_de_latas_de_80_reais * 80) + (quantidade_de_latas_de_25_reais * 25):.2f}')
