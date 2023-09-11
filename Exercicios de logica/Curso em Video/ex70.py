"""
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não.
No final, mostre:

A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
"""

produtos = []  # Lista onde vai ficar os produtos informados
mais_de_1000, total, menor_preco, cont = 0, 0, 0, 0

print('\n\n\t\033[;37mDigite [ 0 ] no nome do produto para encerrar o programa.\033[m\n\n')
while True:  # Enquanto o usuario nao digitar [ 0 ].
    print()
    print('__' * 12)

    try:
        nome = str(input('Nome do produto: ')).title()
        if nome == '0':  # Encerrando o programa se o usuario digitar [ 0 ].
            break

        preco = int(input('Preco: R\033[;32m$\033[m '))

    except:
        print('\n\n\t[\033[;31mERRO\033[m]: Por favor, insira o nome e o valor em numero inteiro.\n\n')

    else:
        if nome == '':  # Se o usuario nao digitou o nome do produto.
            print('\n\n\t[\033[;31mERRO\033[m]: Por favor, insira o nome corretamente.\n\n')

        else:
            produtos.append([nome, preco])  # Adicionando o nome e o preco do produto.

            for produto in produtos:  # Comparando os valores e descobrindo o produto de menor valor.
                if cont == 0:  # Se for a primeira vez comparando.
                    menor_preco = produto[0], produto[1]
                    cont += 1
                else:
                    if produto[1] < menor_preco[1]:  # Se o preco for menor que o menor preco de antes.
                        menor_preco = produto[0], produto[1]

            total += preco  # Total a se pagar pelos produtos.
            if preco > 1000:  # Contando os produtos que sao maiores de 1000.
                mais_de_1000 += 1

if len(produtos) == 0:  # Se o usuario nao adicionou nenhum produto.
    print('\n\n\tNenhum produto adicionado :(\n\n')

else:
    print('\n' * 4)
    print('--' * 20)
    print(f"""
        Informaçoes da compra

> Total gasto na compra: R\033[;32m$\033[m{total}
> Produtos que custam mais de R\033[;32m$\033[m1000: {mais_de_1000}
> Produto mais barato: {menor_preco[0]} - R\033[;32m$\033[m{menor_preco[1]}
""")
    print('--' * 20)

    print('\n\n\tPrograma encerrado com sucesso.\n\n')
