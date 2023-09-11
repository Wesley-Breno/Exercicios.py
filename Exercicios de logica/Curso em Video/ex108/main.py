"""
Adapte o código do desafio #107, criando uma função adicional
chamada moeda() que consiga mostrar os números como um valor
monetário formatado.
"""

import ex108  # Importando o modulo

valor = float(input('Digite o preco: R\033[;32m$\033[m '))

metade = ex108.metade(valor)  # Pegando a metade do valor
dobro = ex108.dobro(valor)  # Pegando o dobro
aumento = ex108.aumentar(valor, 10)  # Fazendo um aumento de 10% no valor
diminuir = ex108.diminuir(valor, 10)  # Fazendo uma diminuicao de 10% no valor

# Mostrando o resultado
print('\n\n\t\t\033[;1mResultado\033[m\n\n'
      f'|> A metade de {ex108.moeda(valor)} é {ex108.moeda(metade)}\n'
      f'|> O dobro de {ex108.moeda(valor)} é {ex108.moeda(dobro)}\n'
      f'|> Um aumento de {aumento[1]}% de {ex108.moeda(valor)} é {ex108.moeda(aumento[0])}\n'
      f'|> Uma diminuicao de {diminuir[1]}% de {ex108.moeda(valor)} é {ex108.moeda(diminuir[0])}')
