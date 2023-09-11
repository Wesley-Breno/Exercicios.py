"""
Modifique as funções que foram criadas no desafio 107 para que
elas aceitem um parâmetro a mais, informando se o valor retornado
por elas vai ser ou não formatado pela função moeda(),
desenvolvida no desafio 108.
"""

import ex109  # Importando o modulo

valor = float(input('Digite o preco: R\033[;32m$\033[m '))

metade = ex109.metade(valor)  # Pegando a metade do valor
dobro = ex109.dobro(valor)  # Pegando o dobro
aumento = ex109.aumentar(valor, 10)  # Fazendo um aumento de 10% no valor
diminuir = ex109.diminuir(valor, 10)  # Fazendo uma diminuicao de 10% no valor

# Mostrando o resultado
print('\n\n\t\t\033[;1mResultado\033[m\n\n'
      f'|> A metade de {ex109.moeda(valor)} é {metade}\n'
      f'|> O dobro de {ex109.moeda(valor)} é {dobro}\n'
      f'|> Um aumento de {aumento[1]}% de {ex109.moeda(valor)} é {aumento[0]}\n'
      f'|> Uma diminuicao de {diminuir[1]}% de {ex109.moeda(valor)} é {diminuir[0]}')
