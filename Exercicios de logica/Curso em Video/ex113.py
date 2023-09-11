"""
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora
a possibilidade da digitação de um número de tipo inválido. Aproveite e
crie também uma função leiaFloat() com a mesma funcionalidade.
"""


def leiaint(mensagem):
    """
    Funcao que recebe um valor que so pode ser um numero inteiro e o retorna.
    :param mensagem: Mensagem que aparecera para o usuario digitar o numero.
    :return: Retorna o numero inteiro que foi digitado.
    """
    while True:  # Enquanto o usuario nao digitar um numero inteiro.
        print('__' * 12)
        try:
            num = int(input(mensagem))

        except:
            print('\n\n\t\t[\033[;31mERRO\033[m]: Digite um numero inteiro.\n\n')

        else:
            return num


def leiafloat(mensagem):
    """
    Funcao que recebe um valor que so pode ser um numero Float e o retorna.
    :param mensagem: Mensagem que aparecera para o usuario digitar o numero.
    :return: Retorna o numero Float que foi digitado.
    """
    while True:  # Enquanto o usuario nao digitar um numero tipo Float.
        print('__' * 12)
        try:
            num = float(input(mensagem))

        except:
            print('\n\n\t\t[\033[;31mERRO\033[m]: Digite um numero inteiro.\n\n')

        else:
            return num
