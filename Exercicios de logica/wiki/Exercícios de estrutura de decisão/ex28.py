"""
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há
limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um
desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de
pagamento, valor do desconto e valor a pagar.

* Apenas um tipo de carne por usuario
* Nao ha limites na quantidade da carne escolhida
* Se a compra for feita no cartao da loja, o usuario recebe 5% de desconto no total da compra
* Peça o tipo e a quantidade da carne comprada e gere um cupom fiscal
* O cupom fiscal deve ter:
    - Tipo da carne
    - Quantidade da carne
    - Preco total
    - Tipo de pagamento
    - Valor do desconto recebido
    - Valor total a pagar
"""
from time import sleep  # Funcao para fazer o programa demorar um pouco para prosseguir.

preco_das_carnes_menos_de_5kgs = [4.90, 5.90, 6.90]
preco_das_carnes_mais_de_5kgs = [5.80, 6.80, 7.80]
nome_das_carnes = ['File duplo', 'Alcatra', 'Picanha']
nome_dos_pagamentos = ['A vista', 'Cartao da loja']


while True:  # Enquanto o usuario nao informar o tipo de carne do menu.
    print('--' * 30)
    try:
        tipo_de_carne = int(input('\n\t\tMENU\n'
                                  '\033[;37m[Escolha o tipo de carne com base no numero de identificação]\033[m\n\n'
                                  '[ 1 ] - File duplo\n'
                                  '[ 2 ] - Alcatra\n'
                                  '[ 3 ] - Picanha\n\n'
                                  'Carne escolhida: '))

    except:
        print('\n\n\t[\033[;31mERRO\033[m]: Por favor tente novamente e verifique os dados informados.')
        sleep(2)

    else:
        if tipo_de_carne == 1 or tipo_de_carne == 2 or tipo_de_carne == 3:  # Se escolheu uma das carnes do menu
            break

        else:
            print(f'\n\n\t[\033[;31mERRO\033[m]: Nao foi encontrado nenhuma carne com identificador [{tipo_de_carne}].')
            sleep(2)

while True:  # Enquanto o usuario nao informar a quantidade em KGs da carne escolhida
    print('--' * 30)
    try:
        quantidade_da_carne = float(input('\n\t\tQUANTIDADE\n\n'
                                          'Informe a quantidade da carne em KGs\nQuantidade da carne: '))

    except:
        print('\n\n\t[\033[;31mERRO\033[m]: Por favor tente novamente e verifique os dados informados.')
        sleep(2)

    else:
        break

while True:  # Enquanto o usuario nao informar o tipo de pagamento
    print('--' * 30)
    try:
        tipo_de_pagamento = int(input('\n\t\tFORMA DE PAGAMENTO\n\n'
                                      '[ 1 ] - A vista\n'
                                      '[ 2 ] - Cartao da loja\n\n'
                                      'Tipo de pagamento: '))

    except:
        print('\n\n\t[\033[;31mERRO\033[m]: Por favor tente novamente e verifique os dados informados.')
        sleep(2)

    else:
        if tipo_de_pagamento == 1 or tipo_de_pagamento == 2:  # Se escolheu um dos pagamentos disponiveis
            break

        else:
            print(f'\n\n\t[\033[;31mERRO\033[m]: Nao foi encontrado nenhum tipo de pagamento com identificador '
                  f'[{tipo_de_pagamento}].')
            sleep(2)

valor_do_desconto = 0  # Variavel que ira somar descontos

if quantidade_da_carne <= 5:  # Se o peso da carne for menor ou igual a 5
    total = preco_das_carnes_menos_de_5kgs[tipo_de_carne - 1] * quantidade_da_carne
    valor_do_desconto = 1.8
else:
    total = preco_das_carnes_mais_de_5kgs[tipo_de_carne - 1] * quantidade_da_carne

if tipo_de_pagamento == 2:  # Se o tipo de pagamento for com o cartao da loja
    valor_do_desconto += total * 5 / 100

print('--' * 30)
print('\n\t\tCUPOM FISCAL\n\n'
      f'Tipo de carne: [{nome_das_carnes[tipo_de_carne - 1]}]\n'
      f'Quantidade da carne: [{quantidade_da_carne:.1f}Kgs]\n'
      f'Tipo de pagamento: [{nome_dos_pagamentos[tipo_de_pagamento - 1]}]\n'
      f'Desconto recebido: R${valor_do_desconto:.2f}\n'
      f'Valor total a pagar: R${total - valor_do_desconto:.2f}')
