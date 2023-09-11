"""
O cardápio de uma lanchonete é o seguinte:

Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00

Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por
item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser
encerrado.
"""

codigo_produtos = {'Cachorro Quente': {'codigo': 100, 'preco': 1.20},
                   'Bauru Simples': {'codigo': 101, 'preco': 1.30},
                   'Bauru com ovo': {'codigo': 102, 'preco': 1.50},
                   'Hambúrguer': {'codigo': 103, 'preco': 1.20},
                   'Cheeseburguer': {'codigo': 104, 'preco': 1.30},
                   'Refrigerante': {'codigo': 105, 'preco': 1}}

pedidos = dict()  # Dicionario onde irao ficar os pedidos
ok = False  # Se o codigo que o usuario informou pertence a algum codigo de produto

while True:  # Enquanto o usuario nao informar um valor negativo
    print('\n\n\t\t\033[;37m[ Digite um valor negativo para encerrar ]\033[m')
    print()
    print('--' * 18)

    try:
        produto = int(input("""\t\t\tProdutos

N. do produto | Código | Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00

| Informe o codigo do produto: """))

    except ValueError:
        print('\n\n\t\t[\033[;31mERRO\033[m]: Informe o código do produto que deseja comprar.\n'
              '\t\t\t\t\tPressione ENTER para continuar\n')
        input()

    else:
        if produto < 0:
            break

        # Verificando se o usuario informou o codigo de algum produto
        for nome_produto, codigo_preco in codigo_produtos.items():
            if produto == codigo_preco['codigo']:
                ok = True

        if ok:  # Se o usuario informou o codigo de algum produto
            try:
                quantidade = int(input('| Informe a quantidade que deseja: '))

            except ValueError:
                print('\n\n\t\t[\033[;31mERRO\033[m]: Informe a quantidade que deseja do produto.\n'
                      '\t\t\t\t\tPressione ENTER para continuar\n')
                input()

            else:
                if quantidade < 0:
                    break

                # Adicionando o produto, preco e a quantidade no dicionario de pedidos
                for nome_produto, codigo_preco in codigo_produtos.items():
                    if codigo_preco['codigo'] == produto:  # Se for o produto que o usuario pediu
                        pedidos[nome_produto] = {'preco': codigo_preco['preco'], 'quantidade': quantidade}
                        input(f'\n\n\t\t{quantidade}x {nome_produto} \033[;32madicionado\033[m no pedido\n'
                              f'\t\t\tPressione ENTER para continuar')
                        quantidade = 0

        else:
            print('\n\n\t\t[\033[;31mERRO\033[m]: Informe o código do produto que deseja comprar.\n'
                  '\t\t\t\t\tPressione ENTER para continuar\n')
            input()

total = 0  # Total que o usuario ira pagar

print('\n\n\t\tResumo da compra\n')
print('--' * 15)
for nome, preco_quantidade in pedidos.items():  # Mostrando cada pedido, o seu preco e a quantidade
    print(f'Produto: {nome}\n'
          f'Preco: {preco_quantidade["preco"]:.2f}\n'
          f'Quantidade: {preco_quantidade["quantidade"]}')
    print('--' * 15)
    total += preco_quantidade['preco'] * preco_quantidade['quantidade']  # Fazendo a soma de todos os pedidos

print(f'\n\t\tTotal a pagar: R$ {total:.2f}\n')
