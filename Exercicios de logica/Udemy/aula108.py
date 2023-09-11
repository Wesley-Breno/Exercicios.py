class CarroDeCompra:  # Obejto que sera como se fosse  um carrinho de compras
    def __init__(self):
        self.produtos = []  # Lista onde ficara todos os produtos

    def inserir_produtos(self, produtos):  # Inserindo produtos no carrinho de compras
        self.produtos.append(produtos)

    def listar_produtos(self):  # Mostrando cada produto e seu preco
        for produto in self.produtos:
            print(produto.nome, 'R\033[;32m$\033[m', produto.valor)

    def total_produtos(self):  # Retornando o valor total a pagar por todos os produtos
        total = 0
        for valor in self.produtos:
            total += valor.valor
        return total


class Produto:  # Objeto que sera o produto
    def __init__(self, nome, valor):  # So ira receber o nome e seu valor
        self.nome = nome
        self.valor = valor


# Produtos
produto1 = Produto('Cigarro', 6)
produto2 = Produto('Camisa', 40)
produto3 = Produto('Sushi', 50)

carrinho = CarroDeCompra()  # Variavel onde ficara todos os produtos
# Inserindo produtos no carrinho de compras
carrinho.inserir_produtos(produto2)
carrinho.inserir_produtos(produto1)
carrinho.inserir_produtos(produto3)

carrinho.listar_produtos()  # Mostrando todos os produtos
print('__' * 15)
print('Total a pagar R\033[;32m$\033[m', carrinho.total_produtos())  # Mostrando o total a se pagar.
