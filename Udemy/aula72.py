# Faca um algoritmo que mostre o valor total a se pagar por uma compra
# usando list comprehension.

carrinho = [('Farofa yoki', 7), ('Vinho', 12), ('Regata', 109)]

# Usando o list comprehension para pegar cada valor e soma-los
# A variavel 'n' é o nome do produto, 'v' é o valor.
# Transformando o valor em um numero flutuante e depois colocando tudo dentro de um sum() para finalmente somar tudo.
total = sum([float(v) for n, v in carrinho])
preco = (v for p, v in carrinho)    # Um gerador com o valor dos produtos.
produtos = (p for p, v in carrinho)    # Um gerador com o nome dos produtos.

print(f'\n\n\033[;1m{"Produtos comprados":^45}\033[m\n')
print('__' * 10)
while True:    # Vai ficar escrevendo ate nao haver mais nenhum produto a ser mostrado e depois ira parar o loop.
    try:
        print(next(produtos), '> R\033[1;32m$\033[m', next(preco))  # Escrevendo o produto e em seguida o preco 1 por 1.
    except:
        break
print('__' * 10)
print(f'\nO total da sua compra foi R\033[1;32m$\033[m{total}\n')
