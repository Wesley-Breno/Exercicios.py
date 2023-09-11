lista_de_compras = [
    {'produto 1': 25},
    {'produto 2': 25},
    {'produto 3': 50}
]

print('--' * 25)

valores_produtos = sum([float(valor) for dicionario in lista_de_compras for chave, valor in dicionario.items()])  # Pegando cada preço

exibir = [print(k, f'-> R\033[;32m$\033[m{v:.2f}') for t in lista_de_compras for k, v in t.items()]  # Mostrando produtos e seus preçoes
print(f'\ntotal a pagar: R\033[;32m$\033[m{valores_produtos:.2f}')

print('--' * 25)
