"""
Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e
mantenha tudo funcionando.
"""

from utilidadesCeV import moeda  # Importando o modulo

valor = float(input('Digite o preco: R\033[;32m$\033[m '))
moeda.resumo(valor, 10, 10)  # Chamando a funcao resumo() e adicionando as porcentagens
