"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados
aleatórios. Guarde esses resultados em um dicionário em Python. No final,
coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior
número no dado.
"""

from random import randint

jogadores = {  # Dicionario com os jogadores e seus valores tirados
    'jogador1': randint(1, 9),
    'jogador2': randint(1, 9),
    'jogador3': randint(1, 9),
    'jogador4': randint(1, 9)
}

# Mostrando os valores tirados dos jogadores na tela
print('\n\t\tValores sorteados;\n')
for chave, valor in jogadores.items():
    print(f'\t{chave} tirou {valor} no dado.')

valores_ordenados = sorted(jogadores.values(), reverse=True)  # Lista com os valores ordenados de forma descrecente
jogadores_ordenados = dict()  # Novo dicionario onde ficara os jogadores ordenados como pedido na descricao do exercicio

cont = 0  # Contador para trocar de valor se o valor da vez ja foi adicionado no novo dicionario
while cont != len(jogadores):
    for chave, valor in jogadores.items():
        if valor == valores_ordenados[cont]:
            jogadores_ordenados[chave] = valor

    cont += 1

print()
print('-=-' * 15)
print('\n\t\t- Ranking -\n')

cont = 1  # Contador para informar a colocao dos ganhadores
for chave, valor in jogadores_ordenados.items():
    print(f'\t{cont}º lugar: {chave} com {valor}')
    cont += 1
