"""
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.
"""

produtos = []

while True:  # Enquanto o usuario nao digitar o preco corretamente
    try:
        for c in range(3):
            produtos.append({'nome': str(input(f'Informe o nome do {c + 1}º produto: ')),
                             'preco': float(input('Informe o preco do produto: R$ '))})
            print()

    except:
        print('\n\n\t\t\033[;31mDIGITE OS VALORES CORRETAMENTE.\033[m\n')
        produtos = []

    else:
        break

precos = []  # Lista onde ficara somente os precos dos produtos
for produto in produtos:
    precos.append(produto['preco'])

valor_mais_barato = min(precos)  # Pegando o valor mais barato.

print('\n\n\t\tResultado\n\n'
      'Os produtos mais baratos sao:')

for produto in produtos:
    if produto['preco'] == valor_mais_barato:  # Se o preco do produto for igual ao menor preco encontrado.
        print(f'{produto["nome"]}: R$ {produto["preco"]:.2f}')
