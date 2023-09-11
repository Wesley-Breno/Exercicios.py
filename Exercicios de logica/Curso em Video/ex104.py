"""
Crie um programa que tenha a função leiaInt(), que vai funcionar
de forma semelhante 'a função input() do Python, só que fazendo
a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')
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


n = leiaint('Digite um numero: ')  # Variavel que vai executar a funcao e receber o numero retornado.
print(f'\n\n\t\tVoce digitou o numero {n}\n\n')
