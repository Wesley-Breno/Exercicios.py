"""
Crie um módulo chamado moeda.py que tenha as funções incorporadas
aumentar(), diminuir(), dobro() e metade(). Faça também um programa
que importe esse módulo e use algumas dessas funções.
"""

import ex107  # Importando o modulo

valor = float(input('Digite o preco: R\033[;32m$\033[m '))

metade = ex107.metade(valor)  # Pegando a metade do valor
dobro = ex107.dobro(valor)  # Pegando o dobro
aumento = ex107.aumentar(valor, 10)  # Fazendo um aumento de 10% no valor
diminuir = ex107.diminuir(valor, 10)  # Fazendo uma diminuicao de 10% no valor

# Mostrando o resultado
print('\n\n\t\t\033[;1mResultado\033[m\n\n'
      f'|> A metade de R\033[;32m$\033[m {valor:.2f} é R\033[;32m$\033[m {metade:.2f}\n'
      f'|> O dobro de R\033[;32m$\033[m {valor:.2f} é R\033[;32m$\033[m {dobro:.2f}\n'
      f'|> Um aumento de {aumento[1]}% de R\033[;32m$\033[m {valor:.2f} é R\033[;32m$\033[m {aumento[0]:.2f}\n'
      f'|> Uma diminuicao de {diminuir[1]}% de R\033[;32m$\033[m {valor:.2f} é R\033[;32m$\033[m {diminuir[0]:.2f}')
