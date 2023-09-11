"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto
de 10% sobre este total.

Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças
adquiridas e escreva o valor a ser pago pelo cliente.
"""

while True:  # Enquanto o usuario nao digitar a quantidade em KGs de cada fruta.
    try:
        kgs_morango = float(input('Informe a quantidade de KGs de morango: '))
        kgs_maca = float(input('Informe a quantidade de KGs de maçãs: '))

    except:
        print('\n\n\033[;31mERRO\033[m\nInforme a quantidade em KGs de cada fruta\n\n')

    else:
        break

# Verificando se as frutas ultrapassam os 5kgs
if kgs_morango <= 5:
    total_a_pagar_morango = kgs_morango * 2.50

else:
    total_a_pagar_morango = kgs_morango * 2.20

if kgs_maca <= 5:
    total_a_pagar_maca = kgs_maca * 1.80

else:
    total_a_pagar_maca = kgs_maca * 1.50

if (kgs_maca + kgs_morango) > 8 or (total_a_pagar_maca + total_a_pagar_morango) > 25:  # Recebendo desconto de 10%
    total_a_pagar = total_a_pagar_maca + total_a_pagar_morango
    total_a_pagar = total_a_pagar - (total_a_pagar * 10 / 100)
    print('\n\n\t\tResultado\n\n'
          f'Total a pagar com 10% de desconto: R\033[;32m$\033[m{total_a_pagar:.2f}')

else:
    total_a_pagar = total_a_pagar_maca + total_a_pagar_morango
    print('\n\n\t\tResultado\n\n'
          f'Total a pagar: R\033[;32m$\033[m{total_a_pagar:.2f}')
