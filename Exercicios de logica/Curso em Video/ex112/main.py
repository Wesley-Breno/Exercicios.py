"""
Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(),
mas com uma validação de dados para aceitar apenas valores que seja monetários.
"""

from utilidadesCeV import moeda  # Importando 'moeda' para fazer o calculo do valor e a formatacao
from utilidadesCeV import dado  # Importando 'dado' para fazer o tratamento de erros

valor = dado.leiadinheiro('Digite o preco: R\033[;32m$\033[m ')  # Usando a funcao presente em 'dado'
moeda.resumo(valor, 10, 10)  # Chamando a funcao resumo() e adicionando as porcentagens
