# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
# que o carro custa R$60 por dia e R$0,15 por Km rodado.

from functions import *

encerrar = ''
while encerrar != 'S':
    titulo('Devolução de carros alugados')
    try:
        km = float(input('\nInforme os Kms que foram rodados...\nKms: '))
        dias = int(input('\nQuantos dias voce passou com ele?\nTotal de dias -> '))
    except:
        erro()
    else:
        if type(km) == float and type(dias) == int:
            total = (dias * 60) + (km * 0.15)
            print()
            print('__' * 22)
            print(f'Voce ira pagar o total de R\033[1;32m$\033[m{total:.2f} no carro.')
            print('__' * 22)
            while True:
                try:
                    encerrar = str(input('\n\nDeseja encerrar o programa? [S]/[N] -> ')).upper()[0]
                except:
                    erro()
                else:
                    if encerrar == 'S' or encerrar == 'N':
                        break
                    else:
                        erro('Reveja os dados inseridos.')

print(f'\n\n{"Ate logo :)":^45}')
