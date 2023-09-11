"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:

Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro

Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
(codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o
preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

gasolina - 2,50
alcool - 1,90
"""

while True:  # Enquanto o usuario nao informar o tipo de combustivel
    print('--' * 24)
    tipo_combustivel = str(input('\t\tInforme o tipo de combustivel\n\n'
                                 'G - Gasolina\n'
                                 'A - Alcool\n\n'
                                 'Tipo do combustivel: ')).upper()

    if tipo_combustivel == 'G' or tipo_combustivel == 'A':
        break

    else:
        print('\n\n\033[;31mERRO\033[m\nInforme o tipo de combustivel\n'
              'G para Gasolina\n'
              'A para Alcool\n\n')

while True:  # Enquanto o usuario nao informar a quantidade de litros que foram vendidos
    print()
    print('--' * 28)
    try:
        litros_vendidos = float(input('\t\tInforme a quantidade de litros vendidos\n\n'
                                      'Quantidade de litros: '))

    except:
        print('\n\n\033[;31mERRO\033[m\nInforme a quantidade de litros vendidos\n')

    else:
        break

if tipo_combustivel == 'G':  # Se for gasolina
    total_a_pagar = litros_vendidos * 2.5

    if litros_vendidos <= 20:  # Desconto de 4%
        total_a_pagar_com_desconto = total_a_pagar - (total_a_pagar * 4 / 100)
        desconto = '4%'

    else:  # Desconto de 6%
        total_a_pagar_com_desconto = total_a_pagar - (total_a_pagar * 6 / 100)
        desconto = '6%'

else:
    total_a_pagar = litros_vendidos * 1.9

    if litros_vendidos <= 20:  # Desconto de 3%
        total_a_pagar_com_desconto = total_a_pagar - (total_a_pagar * 3 / 100)
        desconto = '3%'

    else:  # Desconto de 5%
        total_a_pagar_com_desconto = total_a_pagar - (total_a_pagar * 5 / 100)
        desconto = '5%'

print('\n\n\t\tResultado\n'
      f'Tipo de combustivel: {tipo_combustivel}\n'
      f'Total de litros vendidos: {litros_vendidos:.1f}\n'
      f'Total a pagar com desconto de {desconto}: R\033[;32m$\033[m{total_a_pagar_com_desconto:.2f}')
