"""
Crie um programa que tenha uma tupla única com nomes de produtos e seus
respectivos preços, na sequência. No final, mostre uma listagem de preços,
organizando os dados em forma tabular.
"""

produtos = ('Macarrao', 6,  # Produtos e precos
            'Guarana', 7,
            'Monster', 9,
            'Cigarrin', 6)

print('\n\n\t\t\033[;1mListagem de produtos e seus precos\033[m\n\n')
print('--' * 20)

for indice, produto in enumerate(produtos):
    if indice % 2 == 0:  # Se o indice do valor da tupla for par, é o nome do produto
        print(produto, end='.............R\033[;32m$\033[m ')  # Produto
        print(float(produtos[indice + 1]))  # Preco do produto

print('--' * 20)
