"""
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de
valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da
compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para
então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar
a próxima compra. A saída deve ser conforme o exemplo abaixo:
Lojas Tabajara
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
...
"""

while True:  # Loop infinito
    contar_compras = 1  # Contador para saber quantos produtos estao sendo comprados
    produtos = []  # Lista onde ficara o preco dos produtos

    print('--' * 30)
    print('\t\tLojas Tabajara\n\t'
          '\033[;37mDigite [ 0 ] para finalizar a compra\033[m\n\n')

    while True:  # Enquanto o usuario nao digitar [ 0 ]
        try:
            valor_produto = float(input(f'Produto {contar_compras}: R\033[;32m$\033[m '))
        except:
            print('\n\n\t\t[\033[;31mERRO\033[m]: Informe o preço do produto corretamente.\n\n')
        else:
            if valor_produto == 0:
                break

            produtos.append(valor_produto)
            contar_compras += 1

    if sum(produtos) == 0:  # Se o usuario nao informou o valor dos produtos
        print('\n\n\t\tVoce nao ira pagar nada pelos produtos informados\n\n')

    else:
        print(f'\n\n\t\tTotal a pagar: R\033[;32m$\033[m {sum(produtos):.2f}\n\n')

        while True:  # Enquanto o usuario nao informar o valor que ele ira usar para pagar
            try:
                dinheiro = float(input('Dinheiro: R\033[;32m$\033[m '))
            except:
                print('\n\n\t\t[\033[;31mERRO\033[m]: Informe o valor que voce ira usar para pagar.\n\n')
            else:
                break

        troco = dinheiro - sum(produtos)

        if troco < 0:  # Se o usuario nao tiver dinheiro suficiente
            print('\n\n\t\tVoce \033[;31mNAO\033[m tem dinheiro suficiente para fazer esta compra\n\n')

        elif troco == 0:  # Se o usuario tiver o valor exato para realizar a compra
            print('\n\n\t\tCompra realizada com \033[;32mSUCESSO\033[m\n\n')

        else:
            print('\n\n\t\tCompra realizada com \033[;32mSUCESSO\033[m\n'
                  f'Total de troco: R\033[;32m$\033[m {troco:.2f}')
