# Estudando Dictionary Comprehension

# Exemplo 1: Transformando uma lista em dicionario

lista = [
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
    ('chave3', 'valor3')
]

dicionario_exemplo = {x: y for x, y in lista}

# Exemplo 2: Multiplicando valores de um dicionario

dicionario_exemplo2 = {x: y * 2 for x, y in lista}

# Exemplo 3: Deixando valores/chaves em maiusculo

dicionario_exemplo3 = {x.upper(): y.upper() for x, y in lista}

# Exemplo 4: Criando chaves com sequencia e colocando os valores elevados a 2

dicionario_exemplo4 = {f'Key{x}': x**2 for x in range(5)}
