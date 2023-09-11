# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:

# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

from functions import press_enter, erro, pular, programa_encerrado    # Funcoes que criei.

print(f'\n\n\033[;1m{"_- Loja do Jaozinho -_":^45}')
print(f'{"(Area de pagamento)":^45}\033[m')

while True:    # Enquanto o usuario nao digitar zero.
    try:    # Pegando o tipo de pagamento que sera feito.
        print(f'\n\n\n\033[1;31m{"Menu de escolha":^45}\033[m')
        tipo_de_pagamento = int(input('''
1 \033[1;31m➤\033[m à vista dinheiro/cheque.
2 \033[1;31m➤\033[m à vista no cartão.
3 \033[1;31m➤\033[m 2x no cartão.
4 \033[1;31m➤\033[m 3x ou mais no cartão.

0 \033[1;31m➤\033[m Encerrar programa.


escolha: '''))
    except:
        erro('Por favor\nVerifique a escolha feita.')
        pular(5)
    else:
        if tipo_de_pagamento == 0:    # Se o usuario digitar zero, o programa encerra.
            break

        try:    # pegando o preco do produto.
            preco = float(input('\n\nInforme o preco do produto: R\033[1;32m$\033[m '))
        except:
            erro('Por favor\nVerifique o preco informado.')
            pular(5)
        else:
            if tipo_de_pagamento == 1:    # Se o usuario escolher pagar à vista em dinheiro/cheque, faz 10% de desconto.
                preco_10_de_desconto = preco - (preco * 10 / 100)    # Variavel com o preco com 10% de desconto.

                pular(3)
                print('__' * 23)
                print(f'''Pagamento feito à vista dinheiro/cheque.
Total a pagar com 10% de desconto: R\033[1;32m$\033[m {preco_10_de_desconto:.2f}''')
                print('__' * 23)
                pular()
                press_enter('para voltar ao menu.')

            elif tipo_de_pagamento == 2:    # Se o usuario escolher pagar à vista no cartão, faz 5% de desconto.
                preco_5_de_desconto = preco - (preco * 5 / 100)    # Variavel com o preco com 5% de desconto.

                pular(3)
                print('__' * 23)
                print(f'''Pagamento feito à vista no cartão.
Total a pagar com 5% de desconto: R\033[1;32m$\033[m {preco_5_de_desconto:.2f}''')
                print('__' * 23)
                pular()
                press_enter('para voltar ao menu.')

            elif tipo_de_pagamento == 3:    # Se o usuario escolher pagar em 2x no cartao, faz com preco formal.
                preco_em_2x = preco / 2    # Preco do produto dividido em 2x.

                pular(3)
                print('__' * 23)
                print(f'''Pagamento feito em 2x no cartão
Total a pagar em 2x: R\033[1;32m$\033[m {preco_em_2x:.2f}''')
                print('__' * 23)
                pular()
                press_enter('para voltar ao menu.')

            elif tipo_de_pagamento == 4:  # Se o usuario escolher dividir em 3x ou mais no cartao, faz com 20% de juros.
                try:    # Perguntando quantas vezes o usuario quer fazer.
                    x = int(input('Quantas vezes no cartão? '))
                except:
                    erro('Por favor\nDigite um valor valido.')
                else:
                    if x >= 3:    # Se o usuario quer fazer em 3x ou mais.
                        preco_em_x_vezes = preco / x    # Preco dividido nas vezes que o usuario colocou.
                        preco_com_20_de_juros = preco_em_x_vezes + (preco_em_x_vezes * 20 / 100)    # Colocando os 20% de juros.

                        pular(3)
                        print('__' * 24)
                        print(f'''Pagamento feito em {x}x no cartão: R\033[1;32m$\033[m {preco_com_20_de_juros:.2f}
Total a pagar em {x}x com 20% de juros: R\033[1;32m$\033[m {preco + (preco * 20 / 100):.2f}''')
                        print('__' * 24)
                        pular()
                        press_enter('para voltar ao menu.')

                    else:
                        erro('Por favor\nDigite quantas vezes no cartão.')
                        pular(5)

            else:    # Se o usuario fez uma escolha onde nao é encontrada no menu.
                erro('Por favor\nVerifique a escolha feita.')
                pular(5)

            pular(5)

programa_encerrado()    # Mensagem de despedida para o usuario.
