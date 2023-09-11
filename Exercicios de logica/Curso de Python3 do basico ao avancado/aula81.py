pessoas = [
    {'pessoa': 'werli', 'idade': 18, 'salario': 700},
    {'pessoa': 'lia', 'idade': 20, 'salario': 650},
    {'pessoa': 'marisa', 'idade': 19, 'salario': 900},
    {'pessoa': 'lucas', 'idade': 28, 'salario': 1200},
]

produtos = [
    {'produto': 'product1', 'preco': 15},
    {'produto': 'product2', 'preco': 50},
    {'produto': 'product3', 'preco': 31},
    {'produto': 'product4', 'preco': 54}
]

pessoas_menores_de19 = filter(lambda idade: idade['idade'] <= 19, pessoas)  # Pessoas menores ou iguais a 19 anos.
produtos_maiores_de50 = filter(lambda produto: produto['preco'] >= 50, produtos)  # Produtos valem mais ou iguais a 50.
