"""
Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor
da função2 executada.
"""


def mostrar(arg):  # Função mestre que vai retorna a função2 executada.
    return arg()


def falar():  # Função2, retornando uma string.
    return 'Ola mundo!'


escrever = mostrar(falar)  # Função mestre recebendo a função2 como parametro.
print(escrever)  # Imprimindo na tela, o conteudo da função mestre, usando a função2 como parametro.
