"""
Adicione o módulo moeda.py criado nos desafios anteriores, uma
função chamada resumo(), que mostre na tela algumas informações
geradas pelas funções que já temos no módulo criado até aqui.
"""

import ex110  # Importando o modulo

valor = float(input('Digite o preco: R\033[;32m$\033[m '))
ex110.resumo(valor, 10, 10)  # Chamando a funcao resumo() e adicionando as porcentagens
