"""
Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos
juros, quantidade de parcelas e valor da parcela.

Os juros e a quantidade de parcelas seguem a tabela abaixo:

Quantidade de Parcelas | % de Juros sobre o valor inicial da dívida
1                               0
3                               10
6                               15
9                               20
12                              25

Exemplo de saída do programa:
Valor da Dívida | Valor dos Juros | Quantidade de Parcelas | Valor da Parcela
R$ 1.000,00         0               1                       R$  1.000,00
R$ 1.100,00         100             3                       R$    366,00
R$ 1.150,00         150             6                       R$    191,67
"""
juros, valor_parcela = 0, 0
qtd_parcelas = 1

while True:
    try:
        divida = float(input('\nInforme o valor da divida: R$ '))
        parcelas = int(input('\nDigite o valor que se refere a quantidade de parcelas\n'
                             '[ 1 ] - 1 parcela\n'
                             '[ 2 ] - 3 parcelas\n'
                             '[ 3 ] - 6 parcelas\n'
                             '[ 4 ] - 9 parcelas\n'
                             '[ 5 ] - 12 parcelas\n\n'
                             'Parcela: '))

    except ValueError:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Informe um valor valido!\n\n')

    else:
        if parcelas == 1:
            juros = 0
            qtd_parcelas = 1
            valor_parcela = divida

        elif parcelas == 2:
            juros = divida * 10 / 100
            qtd_parcelas = 3

        elif parcelas == 3:
            juros = divida * 15 / 100
            qtd_parcelas = 6

        elif parcelas == 4:
            juros = divida * 20 / 100
            qtd_parcelas = 9

        elif parcelas == 5:
            juros = divida * 25 / 100
            qtd_parcelas = 12

        else:
            print('\n\n\t\t[\033[;31mERRO\033[m]: Informe um valor valido!\n\n')

        valor_parcela = (divida + juros) / qtd_parcelas
        break

print(f"""
        Resultado

Valor da divida: R\033[;32m$\033[m{divida:.2f}
Valor dos juros: R\033[;32m$\033[m{juros:.2f}
Qtd. de parcelas: {qtd_parcelas}
Valor da parcela: R\033[;32m$\033[m{valor_parcela:.2f}""")
