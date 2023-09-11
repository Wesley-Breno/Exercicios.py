"""
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor.
Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar
numeros aleatórios, simulando os lançamentos dos dados.
"""

from random import randint  # Funcao que sera responsavel por gerar os numeros aleatorios


def lancador_de_dado():  # Funcao que ira gerar um numero aleatorio entre 1 e 6
    return randint(1, 6)


quantidade_cada_valor_jogado = [0] * 6

# Jogando o dado 100x e somando +1 para cada valor repetido
for c in range(100):
    valor_do_dado = lancador_de_dado()
    quantidade_cada_valor_jogado[valor_do_dado - 1] += 1

# Mostrando quantas vezes o valor se repetiu nas 100 jogadas de dado que foram feitas
print('\nQuantidade de vezes que o valor do dado foi gerado;\n')
for index, quantidade in enumerate(quantidade_cada_valor_jogado):
    print(f'\tValor {index + 1} foi gerado: {quantidade}x')
