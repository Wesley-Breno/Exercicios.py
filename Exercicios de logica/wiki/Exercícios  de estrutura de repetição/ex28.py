"""
Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em
cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
"""

while True:  # Enquanto o usuario nao informar a quantidade de CDs
    try:
        quantidade_de_cds = int(input('\n\nInforme a quantidade de CDs que voce possui\nQuantidade: '))

    except:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Informe a quantidade de CDs novamente.\n\n')

    else:
        break

cds = {}
cont = 1

while quantidade_de_cds != 0:  # Enquanto o usuario nao informar o valor de cada CD
    try:
        valor_cd = float(input(f'Informe o valor do {cont}º CD\nValor: '))

    except:
        print(f'\n\n\t\t[\033[;31mERRO\033[m]: Informe o valor do {cont}º CD novamente.\n\n')

    else:
        cds[f'CD {cont}'] = valor_cd
        cont += 1
        quantidade_de_cds -= 1

investido = sum(cds.values())  # Valor total investido
media_gasta = sum(cds.values()) / len(cds.keys())  # Valor medio gasto em cada CD

print('\n\n\t\tResultado\n\n'
      f'Valor total investido: R${investido:.2f}\n'
      f'Valor medio investido em cada CD: R${media_gasta:.2f}\n')
