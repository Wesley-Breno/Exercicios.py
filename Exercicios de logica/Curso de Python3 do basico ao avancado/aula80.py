pessoas = [
    {'pessoa': 'werli', 'idade': 18, 'salario': 700},
    {'pessoa': 'lia', 'idade': 20, 'salario': 650},
    {'pessoa': 'marisa', 'idade': 19, 'salario': 900},
    {'pessoa': 'lucas', 'idade': 28, 'salario': 1200},
]

produtos = [
    {'produto': 'product1', 'preco': 15},
    {'produto': 'product2', 'preco': 20},
    {'produto': 'product3', 'preco': 31},
    {'produto': 'product4', 'preco': 54}
]

numeros = [1, 2, 3, 4, 5]


def aumenta_salario(dic):
    """
    Vai pegar os valores da chave ['salario'] do dicionario 'pessoas'

    :param dic: dicionario pessoas
    :return: retorna um novo dicionario com o aumento de 20% no salario.
    """
    dic['salario'] = round(dic['salario'] * 1.20, 2)
    return dic


def aumenta_preco(dic):
    """
    Vai pegar os valores da chave ['preco'] do dicionario 'produtos'

    :param dic: Dicionario produtos
    :return: Retorna um novo dicionario com o preco dos produtos com um aumento de 5%
    """
    dic['preco'] = round(dic['preco'] * 1.05, 2)
    return dic


def nova_idade(dic):
    """
    Vai pegar os valores da chave ['idade'] do dicionario 'pessoas'

    :param dic: Dicionario pessoas
    :return: Retorna um novo dicionario somando 1 para cada idade
    """
    dic['idade'] += 1
    return dic


salarios_aumentados = map(aumenta_salario, pessoas)  # Novo dicionario com os salarios aumentados
numeros_duplicados = map(lambda n: n * 2, numeros)  # Multiplicando cada numero por 2
precos_aumentados = map(aumenta_preco, produtos)  # Novo dicionario com os precos aumentados
nomes = map(lambda nome: nome['pessoa'], pessoas)  # Pegando somente os nomes das pessoas
novas_idades = map(nova_idade, pessoas)  # Novo dicionario somando 1 para cada idade
